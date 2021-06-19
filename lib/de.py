"""
@author: Diego Solak Castanho
https://github.com/diegoscastanho
"""
import logging
import numpy as np
from copy import deepcopy
import random as rand
import operator
from lib.error_metrics import (
    calc_prediction, calc_error, destandardization, calc_mse, calc_mae, calc_mape, index_agreement, calc_arv)
from lib.txt_logs import DE_PlotLogResults

# General procedures to show the log
logging.basicConfig(
    format=(
        '%(asctime)s - %(levelname)s: ' +
        '(%(filename)s:%(funcName)s at %(lineno)d): %(message)s'),
    datefmt='%b %d %H:%M:%S', level=logging.INFO)


class Individual(object):
    """
    Creates an object for each individual
    """
    def __init__(self, coefficients):
        """
        Initializes the variables of each individual
            INPUTS:
                coefficients: number of free coefficients
            OUTPUTS:
                self.pos: list with the position of the individuals
                self.lb_pos: better individual position during optimization
                self.vel: individual speed
                self.prediction: standardized forecast
                self.fit: fitness
                self.cost: cost function (mse)
                self.lb_fit: best fitness that the individual has ever had
        """
        self.cromo = np.random.uniform(-1, 1, coefficients) # targetVector
        self.donor = np.zeros(coefficients)  # donorVector
        self.trial = np.zeros(coefficients) # trialVector
        self.fit = 0
        self.fitt = 0
        self.cost = 0
        self.prediction = list()

class DifferentialEvolution:
    '''
    DE class
    '''
    def __init__(self, obj, interface, debug_method, delay_day):
        '''
        Interface and interface for PSO
        INPUTS:
            obj: are all input data previously handled
            interface: data coming from the user interface
            debug_method: used to facilitate development
            delay_day: optimization delay day
        OUTPUTS:
        '''
        # mapping of interface variables
        logging.info("Initializing the DE")
        self.population_size = int(interface.de_population_field.text())
        self.num_generations = int(interface.de_gerations_field.text())
        self.num_executions = int(interface.de_executions_field.text())
        # Type of Selection
        self.type_of_selection = interface.greedy_radiobutton.isChecked()
        self.f_number = float(interface.number_f_spinbox.text().replace(',' , '.')) 
        # Type of Crossover
        self.exponential_crossover = interface.exponential_radiobutton.isChecked()
        self.binary_crossover = interface.binary_radiobutton.isChecked()
        self.crossover_rate = float(interface.crossover_rate_spinbox_2.text().replace(',' , '.')) 
        # Type of Mutation
        self.rand_mutation = interface.rand_radiobutton.isChecked()
        self.rand2dp_mutation = interface.rand2dp_radiobutton.isChecked()
        self.best_mutation = interface.best_radiobutton.isChecked()
        self.best2dp_mutation = interface.best2dp_radiobutton.isChecked()
        self.target_mutation = interface.target_to_best_radiobutton.isChecked()
        self.mutation_rate = float(interface.mutation_rate_spinbox.text().replace(',' , '.')) 
        # Input Data
        self.obj = obj
        # List with the best individuals
        self.best_individuals = list()
        self.coefficients = obj.coefficients

        # Debug method
        if debug_method:
            self.population_size = 5
            self.num_generations = 10
            self.num_executions = 2
            self.mutation_rate = 1
            self.crossover_rate = 1

        self.delay_day = delay_day

    def run(self):
        """
        Main DE class
            OUTPUTS:
                self.best_individuals: list with the best individuals of each iteration
                best_individual: particular that presented greater fitness
        """
        for execution in range(self.num_executions):
            logging.info("Running %d/%d" % (execution+1, self.num_executions))
            cont_converg, convergence_generation, best_fit, pop, fit_evolution, cost_evolution =0, 0, 0, list(), list(), list()
            for _ in range(self.population_size):
                pop.append(Individual(self.obj.coefficients))
            best = Individual(self.obj.coefficients)
            pop, best = self.calc_fitness(pop, best)
            for iteration in range(self.num_generations):
                pop = self.calc_mutation(pop, best)
                pop = self.calc_crossover(pop)
                pop, best = self.calc_fitness(pop, best)
                if best.fit > best_fit:
                    best_fit = best.fit
                    convergence_generation = iteration
                    cont_converg = 0
                else:
                    cont_converg += 1
                    if cont_converg == 150:
                        break

                # Evolution fit and cost
                fit_evolution.append(best.fit)
                cost_evolution.append(best.cost)
                # self.obj.Communicator.log_update(
                #     execution + 1, self.num_executions, iteration, best.cost, self.num_generations)
                logging.info("Execution %d/%d - Iteration %d/%d - fitness: %.10f" % (
                    execution+1, self.num_executions, iteration+1, self.num_generations, best.fit))

            # Final results of execution
            logging.info("Algorithm converged in generation %d - fitness: %.8f" % (convergence_generation, best.fit))
            best.fit_evolution = fit_evolution
            best.cost_evolution = cost_evolution
            best.convergence_generation = convergence_generation
            self.best_individuals.append(best)

            # Testing data gives optimization
            # Obtaining the number of standardized hospitalizations
            standardized_test_prediction = calc_prediction(best.cromo, self.obj.data_test)
            # Destandardization, get the real prediction
            best.test_prediction = destandardization(
                standardized_test_prediction, self.obj.averages, self.obj.variances, self.obj.months_test)
            best.train_prediction = destandardization(
                best.prediction, self.obj.averages, self.obj.variances, self.obj.months_train)

            # error metrics
            best.mse = calc_mse(best.test_prediction, self.obj.hospit_test)
            best.rmse = best.mse ** 0.5
            best.ia = index_agreement(best.test_prediction, self.obj.hospit_test)
            best.mean = sum(best.test_prediction) / self.obj.len_test
            best.ae = calc_error(best.test_prediction, self.obj.hospit_test)
            best.mae = calc_mae(best.test_prediction, self.obj.hospit_test)
            best.mape = calc_mape(best.test_prediction, self.obj.hospit_test)
            best.arv = calc_arv(best.test_prediction, self.obj.hospit_test)
            best.ranking = (best.mse + best.rmse + best.ia + best.mean + best.ae + best.mae + best.mape + best.arv) / 8

        # Final results
        best_individual = max(self.best_individuals, key=operator.attrgetter('fit'))
        logging.info("DE delay %d, Best particule fitness: %.8f" % (self.delay_day, best_individual.fit))
        best_individual.delay_day = self.delay_day


        # pred_aux = destandardization(
        #     best.prediction, self.obj.averages, self.obj.variances, self.obj.months_train)
        # generate_trainning_figure(pred_aux, self.obj.hospit_train, self.delay_day)

        logs = DE_PlotLogResults(self.obj, self, self.best_individuals, best_individual)
        logs.create_log()
        return self.best_individuals, best_individual

    def calc_fitness(self, pop, best):
        """
        performs the fitness calculation
            INPUTS:
                pop: list with all individuals
                best: individual that presented greater fitness
        """
        for individual in pop:
            individual.prediction = calc_prediction(individual.cromo, self.obj.data_train)
            if self.obj.type_ae_cost:
                individual.cost = calc_error(individual.prediction, self.obj.hospit_train_standard)
            else:
                individual.cost = calc_mse(individual.prediction, self.obj.hospit_train_standard)
            individual.fit = 1/(1+individual.cost)

            # update o best
            if individual.fit > best.fit:
                best = deepcopy(individual)
        return pop, best

    def calculafitt(self, individual):
        """
        performs the fitness calculation
            INPUTS:
                individual: performs de fitt
        """
        prediction = calc_prediction(individual.cromo, self.obj.data_train)
        if self.obj.type_ae_cost:
            cost = calc_error(prediction, self.obj.hospit_train_standard)
        else:
            cost = calc_mse(prediction, self.obj.hospit_train_standard)
        individual.fitt = 1/(1+cost)

        return individual

    def calc_mutation(self, pop, best):
        """
        Calculates the speed of all individuals in the pop
            INPUTS:
                pop: list with all individuals
                best: best individual
        """
        for individual in pop:
            # rand mutation
            if self.rand_mutation:
                if self.mutation_rate >= rand.uniform(0, 1):
                    t1 = rand.randint(0, self.population_size-1)
                    t2 = rand.randint(0, self.population_size-1)
                    t3 = rand.randint(0, self.population_size-1)

                    while (t1 == t2) or (t1 == t3):
                        t1 = rand.randint(0, self.population_size-1)
                    while (t2 == t1) or (t2 == t3):
                        t2 = rand.randint(0, self.population_size-1)

                    for i in range(self.coefficients):  # calcula donorVector
                        v = pop[t1].cromo[i] + self.f_number * (pop[t2].cromo[i]-pop[t3].cromo[i])
                        individual.donor[i] = v

            # rand2dp mutation
            elif self.rand2dp_mutation:
                t1 = rand.randint(0, self.population_size-1)
                t2 = rand.randint(0, self.population_size-1)
                t3 = rand.randint(0, self.population_size-1)
                t4 = rand.randint(0, self.population_size-1)
                t5 = rand.randint(0, self.population_size-1)

                while t1 == t2 or t1 == t3 or t1 == t4 or t1 == t5:
                    t1 = rand.randint(0, self.population_size-1)
                while t2 == t1 or t2 == t3 or t2 == t4 or t2 == t5:
                    t2 = rand.randint(0, self.population_size-1)
                while t3 == t1 or t3 == t2 or t3 == t4 or t3 == t5:
                    t3 = rand.randint(0, self.population_size-1)
                while t4 == t1 or t4 == t2 or t4 == t3 or t4 == t5:
                    t4 = rand.randint(0, self.population_size-1)

                for i in range(self.coefficients):  # calcula donorVector
                    v = pop[t1].cromo[i] + self.f_number*((pop[t2].cromo[i]-pop[t3].cromo[i])+(
                        pop[t4].cromo[i]-pop[t5].cromo[i]))
                    individual.donor[i] = v

            # best mutation
            elif self.best_mutation:
                t2 = rand.randint(0, self.population_size-1)
                t3 = rand.randint(0, self.population_size-1)
                while t2 == t3:
                    t2 = rand.randint(0, self.population_size-1)
                for i in range(self.coefficients):  # calcula donorVector
                    v = best.cromo[i]+self.f_number * \
                        (pop[t2].cromo[i]-pop[t3].cromo[i])
                    individual.donor[i] = v

            # best2dp mutation
            elif self.best2dp_mutation:
                t2 = rand.randint(0, self.population_size-1)
                t3 = rand.randint(0, self.population_size-1)
                t4 = rand.randint(0, self.population_size-1)
                t5 = rand.randint(0, self.population_size-1)

                while t2 == t3 or t2 == t4 or t2 == t5:
                    t2 = rand.randint(0, self.population_size-1)
                while t3 == t2 or t3 == t4 or t3 == t5:
                    t3 = rand.randint(0, self.population_size-1)
                while t4 == t2 or t4 == t3 or t4 == t5:
                    t4 = rand.randint(0, self.population_size-1)

                for i in range(self.coefficients):  # calcula donorVector
                    v = best.cromo[i]+self.f_number*((pop[t2].cromo[i]-pop[t3].cromo[i])+(
                        pop[t4].cromo[i]-pop[t5].cromo[i]))
                    individual.donor[i] = v

            # target mutation
            elif self.target_mutation:
                t1 = rand.randint(0, self.population_size-1)
                t3 = rand.randint(0, self.population_size-1)
                while (t1 == t3):
                    t1 = rand.randint(0, self.population_size-1)
                for i in range(self.coefficients):  # calcula donorVector
                    v = pop[t1].cromo[i]+self.f_number * \
                        (best.cromo[i]-pop[t3].cromo[i])
                    individual.donor[i] = v
        return pop

    def calc_crossover(self, pop):
        """
        Calculates the position of all individuals in the pop
            INPUTS:
                pop: list with all individuals
        """
        for individual in pop:
            # CROSSOVER BIN BERNOLLI EXPERIMENT
            if self.binary_crossover:
                for i in range(self.coefficients):
                    if self.crossover_rate >= rand.uniform(0, 1):
                        individual.trial[i] = individual.donor[i]
                    else:
                        individual.trial[i] = individual.cromo[i]
                individual = self.calculafitt(individual)

            # EXP CROSSOVER BERNOLLIE XPERIMENT
            elif self.exponential_crossover:
                ponto = rand.randint(0, self.coefficients-1)
                individual.trial = individual.cromo
                while ponto < self.coefficients:
                    if self.crossover_rate >= rand.uniform(0, 1):
                        individual.trial[ponto] = individual.donor[ponto]
                        ponto += 1
                    else:
                        break
                individual = self.calculafitt(individual)

            # greedy selection
            if individual.fitt > individual.fit:
                individual.cromo = individual.trial
        return pop
