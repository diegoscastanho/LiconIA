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
from lib.txt_logs import PSO_PlotLogResults
# General procedures to show the log
logging.basicConfig(
    format=(
        '%(asctime)s - %(levelname)s: ' +
        '(%(filename)s:%(funcName)s at %(lineno)d): %(message)s'),
    datefmt='%b %d %H:%M:%S', level=logging.INFO)


class Particle(object):
    """
    Creates an object for each particle
    """
    def __init__(self, coefficients):
        """
        Initializes the variables of each particle
            INPUTS:
                coefficients: number of free coefficients
            OUTPUTS:
                self.pos: list with the position of the particles
                self.lb_pos: better particle position during optimization
                self.vel: particle speed
                self.prediction: standardized forecast
                self.fit: fitness
                self.cost: cost function (mse)
                self.lb_fit: best fitness that the particle has ever had
        """
        self.pos = np.random.uniform(-2, 2, coefficients)
        self.lb_pos = [0]*coefficients  # local best position
        self.vel = [0]*coefficients
        self.prediction = list()
        self.fit = 0
        self.cost = 0  # mse
        self.lb_fit = 0  # local best fitness


class ParticleSwarmOptimization:
    '''
    PSO class
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
        logging.info("Initializing the PSO")
        self.num_particles = int(interface.pso_particle_field.text())
        self.num_iterations = int(interface.pso_iteration_field.text())
        self.num_executions = int(interface.pso_executions_field.text())
        # Type of Velocity
        self.classic_vel = interface.pso_classic_radiobutton.isChecked()
        self.canonica_vel = interface.pso_canonica_radiobutton.isChecked()
        # Inertial Type
        self.inertial_constant = interface.constant_radiobutton.isChecked()
        self.inertial_fall = interface.linear_fall_radiobutton.isChecked()
        self.inertial_rise = interface.linear_rise_radiobutton.isChecked()
        self.inertia_weight = float(interface.w_field.text())  # w
        # Type of Constants
        self.constant_normal = interface.normal_radiobutton.isChecked()
        self.constant_dynamic = interface.dynamic_mutation_radiobutton.isChecked()
        self.cognat_const = float(interface.c1_field.text())  # c1
        self.social_const = float(interface.c2_field.text())  # c2
        # Input Data
        self.obj = obj

        self.w_inf = 0.2
        self.w_sup = 0.9
        self.c1_inf = 0.1
        self.c2_inf = 2.5
        self.k_value = 1
        self.val_fi = 10
        # List with the best particles
        self.best_particles = list()

        # Debug method
        if debug_method:
            self.num_particles = 5
            self.num_iterations = 10
            self.num_executions = 2

        self.delay_day = delay_day

    def run(self):
        """
        Main PSO class
            OUTPUTS:
                self.best_particles: list with the best particles of each iteration
                best_particle: particular that presented greater fitness
        """
        for execution in range(self.num_executions):
            logging.info("Running %d/%d" % (execution+1, self.num_executions))
            cont_converg, convergence_generation, best_fit, swarm, fit_evolution, cost_evolution =0, 0, 0, list(), list(), list()
            for _ in range(self.num_particles):
                swarm.append(Particle(self.obj.coefficients))
            best = Particle(self.obj.coefficients)
            swarm, best = self.calc_fitness(swarm, best)
            for iteration in range(self.num_iterations):
                swarm = self.calc_velocity(swarm, best)
                swarm = self.calc_position(swarm)
                swarm, best = self.calc_fitness(swarm, best)
                if best.fit > best_fit:
                    best_fit = best.fit
                    convergence_generation = iteration
                    cont_converg = 0
                else:
                    cont_converg += 1
                    if cont_converg == 150:
                        break

                if self.inertial_fall:
                    self.inertia_weight = self.w_sup - ((self.w_inf - self.w_sup)/self.num_iterations)*iteration
                elif self.inertial_rise:
                    self.inertia_weight = self.w_inf + ((self.w_sup - self.w_inf)/self.num_iterations)*iteration

                if self.constant_dynamic:
                    self.cognat_const = self.cognat_const + ((self.c1_inf-self.cognat_const)/self.num_iterations)*iteration
                    self.social_const = self.social_const + ((self.c2_inf-self.social_const)/self.num_iterations)*iteration

                # Evolution fit and cost
                fit_evolution.append(best.fit)
                cost_evolution.append(best.cost)
                # self.obj.Communicator.log_update(
                #     execution + 1, self.num_executions, iteration, best.cost, self.num_iterations)
                logging.info("Execution %d/%d - Iteration %d/%d - fitness: %.10f" % (
                    execution+1, self.num_executions, iteration+1, self.num_iterations, best.fit))

            # Final results of execution
            logging.info("Algorithm converged in generation %d - fitness: %.8f" % (convergence_generation, best.fit))
            best.fit_evolution = fit_evolution
            best.cost_evolution = cost_evolution
            best.convergence_generation = convergence_generation
            self.best_particles.append(best)

            # Testing data gives optimization
            # Obtaining the number of standardized hospitalizations
            standardized_test_prediction = calc_prediction(best.pos, self.obj.data_test)
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
        best_particle = max(self.best_particles, key=operator.attrgetter('fit'))
        logging.info("PSO delay %d, Best particule fitness: %.8f" % (self.delay_day, best_particle.fit))
        best_particle.delay_day = self.delay_day


        # pred_aux = destandardization(
        #     best.prediction, self.obj.averages, self.obj.variances, self.obj.months_train)
        # generate_trainning_figure(pred_aux, self.obj.hospit_train, self.delay_day)

        logs = PSO_PlotLogResults(self.obj, self, self.best_particles, best_particle)
        logs.create_log()
        return self.best_particles, best_particle

    def calc_fitness(self, swarm, best):
        """
        performs the fitness calculation
            INPUTS:
                swarm: list with all particles
                best: particle that presented greater fitness
        """
        for particle in swarm:
            particle.prediction = calc_prediction(particle.pos, self.obj.data_train)
            if self.obj.type_ae_cost:
                particle.cost = calc_error(particle.prediction, self.obj.hospit_train_standard)
            else:
                particle.cost = calc_mse(particle.prediction, self.obj.hospit_train_standard)
            particle.fit = 1/(1+particle.cost)

            # update o best
            if particle.fit > best.fit:
                best = deepcopy(particle)

            # update o l_best
            if particle.fit > particle.lb_fit:  # atualiza local best
                particle.lb_fit = particle.fit  # atualiza o melhor fit da particula
                particle.lb_pos = particle.pos  # atualiza melhor posicao obtida da part
        return swarm, best

    def calc_velocity(self, swarm, best):
        """
        Calculates the speed of all particles in the swarm
            INPUTS:
                swarm: list with all particles
                best: particle that presented greater fitness
        """
        for particle in swarm:
            r1, r2 = rand.random(), rand.random()

            # classic speed
            if self.classic_vel:
                for num, vel in enumerate(particle.vel):
                    aux1 = self.inertia_weight*vel + self.cognat_const*r1
                    aux2 = particle.lb_pos[num] - particle.pos[num]
                    aux3 = self.social_const*r2*(best.pos[num] - particle.pos[num])
                    particle.vel[num] = aux1 * aux2 + aux3

            # canonical speed
            elif self.canonica_vel:
                X = (2*self.k_value)/np.abs(2-self.val_fi - (self.val_fi*2 - 4*self.val_fi)**0.5)
                for num, vel in enumerate(particle.vel):
                    aux1 = self.inertia_weight*vel + self.cognat_const*r1
                    aux2 = particle.lb_pos[num] - particle.pos[num]
                    aux3 = self.social_const*r2*(best.pos[num] - particle.pos[num])
                    particle.vel[num] = X * (aux1 * aux2 + aux3)
        return swarm

    def calc_position(self, swarm):
        """
        Calculates the position of all particles in the swarm
            INPUTS:
                swarm: list with all particles
        """
        for particle in swarm:
            for num, pos in enumerate(particle.pos):
                particle.pos[num] = pos + particle.vel[num]
        return swarm
