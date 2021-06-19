"""
@author: Diego Solak Castanho
https://github.com/diegoscastanho
"""
import logging
from typing import List
import numpy as np
from copy import deepcopy
import random as rand
import operator
from lib.error_metrics import (
    calc_prediction, calc_error, destandardization, calc_mse, calc_mae, calc_mape, index_agreement, calc_arv)
from lib.txt_logs import GA_PlotLogResults
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
                self.cromo: list with the position of the individuals
                self.penal: used in NICHING
                self.sum_fit: din mutation
                self.fit: standardized forecast
                self.cost: fitness
                self.prediction: cost function (mse)
        """
        self.cromo = [0]*coefficients
        self.penal = 1 
        self.sum_fit = 0
        self.fit = 0
        self.cost = 0
        self.prediction = list()

class GeneticAlgorithm:
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
        logging.info("Initializing the GA")
        self.population_size = int(interface.ga_population_field.text())
        self.num_generations = int(interface.ga_gerations_field.text())
        self.num_executions = int(interface.ga_executions_field.text())
        # Type of Selection
        self.roulette_tournament = interface.roulette_radiobutton.isChecked()
        self.roulette_sus_tournament = interface.roulette_sus_radiobutton.isChecked()
        self.single_tournament = interface.single_tournament_radiobutton.isChecked()
        self.death_tournament = interface.death_tournament_radiobutton.isChecked()
        self.niching_tournament = interface.niching_tournament_radiobutton.isChecked()
        self.local_seach = interface.local_search_scrollbar.value()
        # Type of Crossover
        self.point_crossover = interface.point_radiobutton.isChecked()
        self.arithmetic_crossover = interface.arithmetic_radiobutton.isChecked()
        self.sbx_crossover = interface.sbx_radiobutton.isChecked()
        self.m_sbx_value = interface.sbx_ScrollBar.value()
        self.crossover_rate = float(interface.crossover_rate_spinbox.text().replace(',' , '.')) 

        # Type of Mutation
        self.fixed_mutation = interface.fixed_mutation_radiobutton.isChecked()
        self.dyn_mutation = interface.dyn_mutation_radiobutton.isChecked()
        self.mutation_rate = float(interface.mutation_rate_SpinBox.text().replace(',' , '.')) 
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
            local_search = 0
            for iteration in range(self.num_generations):
                pop = self.calc_crossover(pop)
                pop = self.calc_mutation(pop)
                pop, best = self.calc_fitness(pop, best)
                pop = self.selection(pop)

                if local_search == self.local_seach-1:
                    best = self.calc_local_search(best)
                    local_search = 0
                local_search += 1

                if self.dyn_mutation:
                    mean_fit = best.sum_fit/self.population_size
                    self.mutation_rate = 30*(1-((1-mean_fit)/1))

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

        # Final resultsf
        best_individual = max(self.best_individuals, key=operator.attrgetter('fit'))
        logging.info("GA delay %d, Best particule fitness: %.8f" % (self.delay_day, best_individual.fit))
        best_individual.delay_day = self.delay_day


        # pred_aux = destandardization(
        #     best.prediction, self.obj.averages, self.obj.variances, self.obj.months_train)
        # generate_trainning_figure(pred_aux, self.obj.hospit_train, self.delay_day)

        logs = GA_PlotLogResults(self.obj, self, self.best_individuals, best_individual)
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
            best.sum_fit += individual.fit  # mut din

            # update o best
            if individual.fit > best.fit:
                best = deepcopy(individual)
        return pop, best

    def calc_mutation(self, pop):
        """
        Calculates the speed of all individuals in the pop
            INPUTS:
                pop: list with all individuals
                best: best individual
        """
        for individual in pop:
            if rand.random() <= self.mutation_rate:
                x = rand.uniform(-1, 1)
                y = rand.randint(0, self.coefficients-1)
                individual.cromo[y] = x
        return pop

    def calc_crossover(self, pop):
        """
        Calculates the position of all individuals in the pop
            INPUTS:
                pop: list with all individuals
        """
        # POINT CROSSOVER 
        if self.point_crossover:
            for i in range(self.population_size//2):
                if rand.random() <= self.crossover_rate:
                    indPai1 = rand.randint(0, len(pop)-1)
                    pai1 = pop[indPai1].cromo
                    indPai2 = rand.randint(0, len(pop)-1)
                    pai2 = pop[indPai2].cromo
                    ponto = rand.randint(0, self.coefficients-1)

                    filho1 = Individual(self.coefficients)
                    filho1.cromo = pai1[0:ponto]+pai2[ponto:self.coefficients]
                    pop.append(filho1)

                    filho2 = Individual(self.coefficients)
                    filho2.cromo = pai2[0:ponto]+pai1[ponto:self.coefficients]
                    pop.append(filho2)
                else:
                    filho1 = Individual(self.coefficients)
                    pop.append(filho1)

                    filho2 = Individual(self.coefficients)
                    pop.append(filho2)

        # arithmetic crossover
        elif self.arithmetic_crossover:
            for i in range(self.population_size//2):
                if rand.random() <= self.crossover_rate:
                    indPai1 = rand.randint(0, len(pop)-1)
                    pai1 = pop[indPai1].cromo
                    indPai2 = rand.randint(0, len(pop)-1)
                    pai2 = pop[indPai2].cromo

                    ponto = rand.randint(0, self.coefficients-1)
                    beta = rand.random()
                    mbeta = 1-beta

                    filho1 = Individual(self.coefficients)
                    filho2 = Individual(self.coefficients)
                    filho1.cromo = pai1[0:ponto]+pai2[ponto:self.coefficients]
                    filho2.cromo = pai2[0:ponto]+pai1[ponto:self.coefficients]

                    for i in range(self.coefficients):
                        if i <= ponto:
                            filho1.cromo[i] = filho1.cromo[i]*beta
                            filho2.cromo[i] = filho2.cromo[i]*beta

                        else:
                            filho1.cromo[i] = filho1.cromo[i]*mbeta
                            filho2.cromo[i] = filho2.cromo[i]*mbeta

                    pop.append(filho1)
                    pop.append(filho2)
                else:
                    filho1 = Individual(self.coefficients)
                    pop.append(filho1)

                    filho2 = Individual(self.coefficients)
                    pop.append(filho2)

        # sbx_crossover
        elif self.sbx_crossover:
            for i in range(self.population_size//2):
                if rand.random() <= self.crossover_rate:
                    indPai1 = rand.randint(0, len(pop)-1)
                    pai1 = pop[indPai1].cromo
                    indPai2 = rand.randint(0, len(pop)-1)
                    pai2 = pop[indPai2].cromo

                    u = rand.random()
                    if u < 0.5:
                        beta = (2*u)**(1/self.m_sbx_value+1)
                    else:
                        beta = (0.5/(1-u))**(1/self.m_sbx_value+1)

                    filho1 = Individual(self.coefficients)
                    filho2 = Individual(self.coefficients)

                    for i in range(self.coefficients):
                        filho1.cromo[i] = 0.5 * \
                            (pai1[i]+pai2[i])-0.5*beta*(pai1[i]-pai2[i])
                        filho2.cromo[i] = 0.5 * \
                            (pai1[i]+pai2[i])+0.5*beta*(pai1[i]-pai2[i])
                    pop.append(filho1)
                    pop.append(filho2)

                else:
                    filho1 = Individual(self.coefficients)
                    pop.append(filho1)

                    filho2 = Individual(self.coefficients)
                    pop.append(filho2)
        return pop

    def selection(self, pop):
        """
        Calculates the position of all individuals in the pop
            INPUTS:
                pop: list with all individuals
        """
        new_pop = list()
        # single_tournament
        if self.single_tournament:
            for i in range(self.population_size):
                ind_compet1 = rand.randint(0, self.population_size-1)
                ind_compet2 = rand.randint(0, self.population_size-1)
                if pop[ind_compet1].fit > pop[ind_compet2].fit:
                    new_pop.append(pop[ind_compet1])
                else:
                    new_pop.append(pop[ind_compet2])

        # roulette_tournament
        elif self.roulette_tournament:
            sum_fit = 0
            for i in range(self.population_size):
                sum_fit = sum_fit + pop[i].fit
            for _ in range(self.population_size):
                S = 0
                r = rand.uniform(0, sum_fit)
                for j in range(self.population_size):
                    S = S + pop[j].fit
                    if S > r:
                        new_pop.append(pop[j])
                        break

        # Roleta espacamentos iguais #Roleta com Stochastic Universal Sampling
        elif self.roulette_sus_tournament:
            sum_fit = 0
            for i in range(self.population_size):
                sum_fit = sum_fit + pop[i].fit
            media = sum_fit/self.population_size

            for _ in range(self.population_size):
                S = 0
                r = rand.uniform(0, sum_fit)
                for j in range(self.population_size):
                    S = S + media
                    if S > r:
                        new_pop.append(pop[j])
                        break

        # death_tournament
        elif self.death_tournament:
            for i in range(self.population_size):
                ind_compet1 = i
                ind_compet2 = (len(pop)-1)-i
                if pop[ind_compet1].fit > pop[ind_compet2].fit:
                    new_pop.append(pop[ind_compet1])
                else:
                    new_pop.append(pop[ind_compet2])

        # Sinple tournament with niching_tournament
        elif self.niching_tournament:
            for i in range(self.population_size):
                ind_compet1 = rand.randint(0, self.population_size-1)
                ind_compet2 = rand.randint(0, self.population_size-1)

                if pop[ind_compet1].fit >= pop[ind_compet2].fit:
                    new_pop.append(pop[ind_compet1])
                    if pop[ind_compet1].fit == pop[ind_compet2].fit:
                        # diminui o fit pela metade
                        pop[ind_compet2].penal = pop[ind_compet2].penal + 2
                else:
                    new_pop.append(pop[ind_compet2])
                    if pop[ind_compet1].fit == pop[ind_compet2].fit:
                        # diminui o fit pela metade
                        pop[ind_compet2].penal = pop[ind_compet2].penal + 2

        return new_pop

    def calc_local_fitness(self, new):
        """
        performs the fitness calculation
            INPUTS:
                pop: list with all individuals
                best: individual that presented greater fitness
        """
        new.prediction = calc_prediction(new.cromo, self.obj.data_train)
        if self.obj.type_ae_cost:
            new.cost = calc_error(new.prediction, self.obj.hospit_train_standard)
        else:
            new.cost = calc_mse(new.prediction, self.obj.hospit_train_standard)
        new.fit = 1/(1+new.cost)
        return new

    def calc_local_search(self, best):
        """
        Calculates the position of all individuals in the pop
            INPUTS:
                best: best individual in optimization
        """
        trial_new_best = Individual(self.coefficients)
        trial_new_best.cromo = best.cromo
        for i in range(self.coefficients):
            # subindo e descendo
            b1 = rand.random()
            k = 0
            while k == 0:
                trial_new_best.cromo[i] = best.cromo[i]+b1  # sobe
                trial_new_best = self.calc_local_fitness(trial_new_best)
                if trial_new_best.fit > best.fit:  # melhorou
                    best = deepcopy(trial_new_best)
                else:
                    k = 1

            k = 0
            while k == 0:
                trial_new_best.cromo[i] = best.cromo[i]-b1  # desce
                trial_new_best =self.calc_local_fitness(trial_new_best)
                if trial_new_best.fit > best.fit:  # melhorou
                    best = deepcopy(trial_new_best)
                else:
                    k = 1

        return best
    