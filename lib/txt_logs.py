"""
@author: Diego Solak Castanho
https://github.com/diegoscastanho
"""
import os
import pickle
import logging
from copy import deepcopy 

# General procedures to show the log
logging.basicConfig(
    format=(
        '%(asctime)s - %(levelname)s: ' +
        '(%(filename)s:%(funcName)s at %(lineno)d): %(message)s'),
    datefmt='%b %d %H:%M:%S', level=logging.INFO)

class PSO_PlotLogResults(object):
    """
    Class responsible for generating the log files
    """
    def __init__(self, obj, configs, best_particles, best):
        """
        Variable mapping
        """
        self.obj = obj
        self.configs = configs
        self.best_particles = best_particles  #best of all executions
        self.best = best  # list with the best of each execution
        self.file_name = deepcopy(obj.interface.open_file_field.text())

        del(obj.child_conn)
        del(obj.interface)
        self.data = {}
        self.data['obj'] = obj 
        self.data["configs"] = configs
        self.data["best_particles"] = best_particles
        self.data["best"] = best

    def create_log(self):
        """
        Creates the log for the PSO
        """
        # json log
        newpath = "results/pso/json_logs"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        file_path = "results/pso/json_logs/pso_day_delay_" + str(self.best.delay_day) + ".txt"
        with open(file_path, 'wb') as handle:
            pickle.dump(self.data, handle)

        # txt log
        newpath = "results/pso/txt_logs"
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        file_name = "results/pso/txt_logs/pso_day_delay_" + str(self.best.delay_day) + ".txt"
        self.basic_config(file_name)
        self.executions_log(file_name)
        self.execution_log(file_name)

    def basic_config(self, file_name):
        """
        Basic simulation settings for PSO
        """

        file = open(file_name, 'w')
        file.write("----------------GLM-PSO------------------------\n")
        file.write("GLM PSO - Settings: Delay " + str(self.configs.delay_day) + "\n")
        file.write("File Name: " + str(self.file_name) + "\n")
        file.write("Particle number:" + str(self.configs.num_particles) + "\n")
        file.write("Number of iterations:" + str(self.configs.num_iterations) + "\n")
        file.write("Number od executions:" + str(self.configs.num_executions) + "\n")
        file.write("Day index:" + str(self.configs.delay_day) + "\n")
        file.write("Prediction index:" + str(self.obj.real_internation_index) + "\n")
        file.write("Day of the week index:" + str(self.obj.index_day_week) + "\n")
        file.write("Number of test samples:" + str(self.obj.len_test) + "\n")
        file.write("Number of trainning samples:" + str(self.obj.len_train) + "\n")

        if self.configs.classic_vel:
            file.write("Type of velocity: Classic\n")
        if self.configs.canonica_vel:
            file.write("Type of velocity: Canonica\n")

        if self.obj.type_mse_cost:
            file.write("Type of cost: MSE (mean square error)\n")
        if self.obj.type_ae_cost:
            file.write("Type of cost: AE (absolute error)\n")

        if self.configs.inertial_constant:
            file.write("Inertial Type: Constant\n")
            file.write("Inercia Weight (W):" + str(self.configs.inertia_weight) + "\n")
        if self.configs.inertial_fall:
            file.write("Inertial Type: Linear Fall\n")
            file.write("W lower:" + str(self.configs.w_inf) + "\n")
            file.write("w upper:" + str(self.configs.w_sup) + "\n")
        if self.configs.inertial_rise:
            file.write("Inertial Type: Linear Rise\n")
            file.write("W lower:" + str(self.configs.w_inf) + "\n")
            file.write("w upper:" + str(self.configs.w_sup) + "\n")

        if self.configs.constant_normal:
            file.write("Type of Constants: Normal\n")
            file.write("Cognite Constant(C1):" + str(self.configs.cognat_const) + "\n")
            file.write("Social Constant(C2):" + str(self.configs.social_const) + "\n\n")
        if self.configs.constant_dynamic:
            file.write("Type of Constants: Dynamic\n")
            file.write("C1 lower:" + str(self.configs.c1_inf) + "\n")
            file.write("C2 lower:" + str(self.configs.c2_inf) + "\n")
            file.write("k value:" + str(self.configs.k_value) + "\n")
            file.write("fi:" + str(self.configs.val_fi) + "\n\n")
        file.close()

    def executions_log(self, file_name):
        """
        Results by execution for PSO
        """
        file = open(file_name, 'a')
        file.write("-----------------Results by Execution-----------------------\n")
        for num, exec_ in enumerate(self.best_particles):
            file.write("Execution nº:" + str(num) + "\n")
            file.write("convergence generation:" + str(exec_.convergence_generation) + "\n")
            file.write("position:" + str(exec_.pos) + "\n")
            file.write("velocity:" + str(exec_.vel) + "\n")
            file.write("cost:" + str(exec_.cost) + "\n")
            file.write("fitness:" + str(exec_.fit) + "\n")
            file.write("local best fitness:" + str(exec_.lb_fit) + "\n")
            file.write("local best position:" + str(exec_.lb_pos) + "\n")
            file.write("AE (Absolute Error):" + str(exec_.ae) + "\n")
            file.write("MSE (Mean Square Error):" + str(exec_.mse) + "\n")
            file.write("MAPE (Mean Absolute Percentage Error):" + str(exec_.mape) + "\n")
            file.write("ARV (Average Relative Variance):" + str(exec_.arv) + "\n")
            file.write("IA (Index of Agreement):" + str(exec_.ia) + "\n")
            file.write("MAE (Mean Absolute Error):" + str(exec_.mae) + "\n")
            file.write("RMSE (Root Mean Squared Error):" + str(exec_.rmse) + "\n")
            file.write("Mean:" + str(exec_.mean) + "\n")
            file.write("Ranking:" + str(exec_.ranking) + "\n")
            file.write("training prediction:" + str(exec_.prediction) + "\n")
            file.write("test prediction:" + str(exec_.test_prediction) + "\n\n\n")
        file.close()

    def execution_log(self, file_name):
        """
        Best execution results for PSO
        """
        file = open(file_name, 'a')
        file.write("-----------------Best execution results-----------------------\n")
        file.write("convergence generation:" + str(self.best.convergence_generation) + "\n")
        file.write("position:" + str(self.best.pos) + "\n")
        file.write("velocity:" + str(self.best.vel) + "\n")
        file.write("cost:" + str(self.best.cost) + "\n")
        file.write("fitness:" + str(self.best.fit) + "\n")
        file.write("local best fitness:" + str(self.best.lb_fit) + "\n")
        file.write("local best position:" + str(self.best.lb_pos) + "\n")
        file.write("AE (Absolute Error):" + str(self.best.ae) + "\n")
        file.write("MSE (Mean Square Error):" + str(self.best.mse) + "\n")
        file.write("MAPE (Mean Absolute Percentage Error):" + str(self.best.mape) + "\n")
        file.write("ARV (Average Relative Variance):" + str(self.best.arv) + "\n")
        file.write("IA (Index of Agreement):" + str(self.best.ia) + "\n")
        file.write("MAE (Mean Absolute Error):" + str(self.best.mae) + "\n")
        file.write("RMSE (Root Mean Squared Error):" + str(self.best.rmse) + "\n")
        file.write("Mean:" + str(self.best.mean) + "\n")
        file.write("Ranking:" + str(self.best.ranking) + "\n")
        file.write("training prediction:" + str(self.best.prediction) + "\n")
        file.write("test prediction:" + str(self.best.test_prediction) + "\n\n\n")
        file.close()

class DE_PlotLogResults(object):
    """
    Class responsible for generating the log files
    """
    def __init__(self, obj, configs, best_particles, best):
        """
        Variable mapping
        """
        self.obj = obj
        self.configs = configs
        self.best_particles = best_particles  #best of all executions
        self.best = best  # list with the best of each execution
        self.file_name = deepcopy(obj.interface.open_file_field.text())

        del(obj.child_conn)
        del(obj.interface)
        self.data = {}
        self.data['obj'] = obj 
        self.data["configs"] = configs
        self.data["best_particles"] = best_particles
        self.data["best"] = best

    def create_log(self):
        """
        Creates the log for the DE
        """
        # json log
        newpath = "results/de/json_logs"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        file_path = "results/de/json_logs/de_day_delay_" + str(self.best.delay_day) + ".txt"
        with open(file_path, 'wb') as handle:
            pickle.dump(self.data, handle)

        # txt log
        newpath = "results/de/txt_logs"
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        file_name = "results/de/txt_logs/de_day_delay_" + str(self.best.delay_day) + ".txt"
        self.basic_config(file_name)
        self.executions_log(file_name)
        self.execution_log(file_name)

    def basic_config(self, file_name):
        """
        Basic simulation settings for DE
        """

        file = open(file_name, 'w')
        file.write("----------------GLM-DE------------------------\n")
        file.write("GLM DE - Settings: Delay " + str(self.configs.delay_day) + "\n")
        file.write("File Name: " + str(self.file_name) + "\n")
        file.write("Population size:" + str(self.configs.population_size) + "\n")
        file.write("Number of generations:" + str(self.configs.num_generations) + "\n")
        file.write("Number od executions:" + str(self.configs.num_executions) + "\n")
        file.write("Day index:" + str(self.configs.delay_day) + "\n")
        file.write("Prediction index:" + str(self.obj.real_internation_index) + "\n")
        file.write("Day of the week index:" + str(self.obj.index_day_week) + "\n")
        file.write("Number of test samples:" + str(self.obj.len_test) + "\n")
        file.write("Number of trainning samples:" + str(self.obj.len_train) + "\n")

        if self.configs.exponential_crossover:
            file.write("Type of Crossover: Exponential\n")
        elif self.configs.binary_crossover:
            file.write("Type of Crossover: Binary\n")

        if self.obj.type_mse_cost:
            file.write("Type of cost: MSE (mean square error)\n")
        elif self.obj.type_ae_cost:
            file.write("Type of cost: AE (absolute error)\n")

        if self.configs.rand_mutation:
            file.write("Type of Mutation: Rand\n")
        elif self.configs.rand2dp_mutation:
            file.write("Type of Mutation: Rand2DB\n")
        elif self.configs.best_mutation:
            file.write("Type of Mutation: Best\n")
        elif self.configs.best2dp_mutation:
            file.write("Type of Mutation: Best2DP\n")
        elif self.configs.target_mutation:
            file.write("Type of Mutation: Target to Best\n")

        file.write("Social of F:" + str(self.configs.f_number) + "\n")
        file.write("Crossover rate:" + str(self.configs.crossover_rate) + "\n")
        file.write("Mutation rate:" + str(self.configs.mutation_rate) + "\n\n")
        file.close()

    def executions_log(self, file_name):
        """
        Results by execution for DE
        """
        file = open(file_name, 'a')
        file.write("-----------------Results by Execution-----------------------\n")
        for num, exec_ in enumerate(self.best_particles):
            file.write("Execution nº:" + str(num) + "\n")
            file.write("convergence generation:" + str(exec_.convergence_generation) + "\n")
            file.write("cromo:" + str(exec_.cromo) + "\n")
            file.write("cost:" + str(exec_.cost) + "\n")
            file.write("fitness:" + str(exec_.fit) + "\n")
            file.write("AE (Absolute Error):" + str(exec_.ae) + "\n")
            file.write("MSE (Mean Square Error):" + str(exec_.mse) + "\n")
            file.write("MAPE (Mean Absolute Percentage Error):" + str(exec_.mape) + "\n")
            file.write("ARV (Average Relative Variance):" + str(exec_.arv) + "\n")
            file.write("IA (Index of Agreement):" + str(exec_.ia) + "\n")
            file.write("MAE (Mean Absolute Error):" + str(exec_.mae) + "\n")
            file.write("RMSE (Root Mean Squared Error):" + str(exec_.rmse) + "\n")
            file.write("Mean:" + str(exec_.mean) + "\n")
            file.write("Ranking:" + str(exec_.ranking) + "\n")
            file.write("training prediction:" + str(exec_.prediction) + "\n")
            file.write("test prediction:" + str(exec_.test_prediction) + "\n\n\n")
        file.close()

    def execution_log(self, file_name):
        """
        Best execution results for DE
        """
        file = open(file_name, 'a')
        file.write("-----------------Best execution results-----------------------\n")
        file.write("convergence generation:" + str(self.best.convergence_generation) + "\n")
        file.write("cromo:" + str(self.best.cromo) + "\n")
        file.write("cost:" + str(self.best.cost) + "\n")
        file.write("fitness:" + str(self.best.fit) + "\n")
        file.write("AE (Absolute Error):" + str(self.best.ae) + "\n")
        file.write("MSE (Mean Square Error):" + str(self.best.mse) + "\n")
        file.write("MAPE (Mean Absolute Percentage Error):" + str(self.best.mape) + "\n")
        file.write("ARV (Average Relative Variance):" + str(self.best.arv) + "\n")
        file.write("IA (Index of Agreement):" + str(self.best.ia) + "\n")
        file.write("MAE (Mean Absolute Error):" + str(self.best.mae) + "\n")
        file.write("RMSE (Root Mean Squared Error):" + str(self.best.rmse) + "\n")
        file.write("Mean:" + str(self.best.mean) + "\n")
        file.write("Ranking:" + str(self.best.ranking) + "\n")
        file.write("training prediction:" + str(self.best.prediction) + "\n")
        file.write("test prediction:" + str(self.best.test_prediction) + "\n\n\n")
        file.close()

class GA_PlotLogResults(object):
    """
    Class responsible for generating the log files
    """
    def __init__(self, obj, configs, best_particles, best):
        """
        Variable mapping
        """
        self.obj = obj
        self.configs = configs
        self.best_particles = best_particles  #best of all executions
        self.best = best  # list with the best of each execution
        self.file_name = deepcopy(obj.interface.open_file_field.text())

        del(obj.child_conn)
        del(obj.interface)
        self.data = {}
        self.data['obj'] = obj 
        self.data["configs"] = configs
        self.data["best_particles"] = best_particles
        self.data["best"] = best

    def create_log(self):
        """
        Creates the log for the GA
        """
        # json log
        newpath = "results/ga/json_logs"
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        file_path = "results/ga/json_logs/ga_day_delay_" + str(self.best.delay_day) + ".txt"
        with open(file_path, 'wb') as handle:
            pickle.dump(self.data, handle)

        # txt log
        newpath = "results/ga/txt_logs"
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        file_name = "results/ga/txt_logs/ga_day_delay_" + str(self.best.delay_day) + ".txt"
        self.basic_config(file_name)
        self.executions_log(file_name)
        self.execution_log(file_name)

    def basic_config(self, file_name):
        """
        Basic simulation settings for GA
        """

        file = open(file_name, 'w')
        file.write("----------------GLM-GA------------------------\n")
        file.write("File Name: " + str(self.file_name) + "\n")
        file.write("GLM GA - Settings: Delay " + str(self.configs.delay_day) + "\n")
        file.write("Population size:" + str(self.configs.population_size) + "\n")
        file.write("Number of generations:" + str(self.configs.num_generations) + "\n")
        file.write("Number od executions:" + str(self.configs.num_executions) + "\n")
        file.write("Day index:" + str(self.configs.delay_day) + "\n")
        file.write("Prediction index:" + str(self.obj.real_internation_index) + "\n")
        file.write("Day of the week index:" + str(self.obj.index_day_week) + "\n")
        file.write("Number of test samples:" + str(self.obj.len_test) + "\n")
        file.write("Number of trainning samples:" + str(self.obj.len_train) + "\n")

        # Type of Selection
        if self.configs.roulette_tournament:
            file.write("Type of Selection: Roulette\n")
        elif self.configs.roulette_sus_tournament:
            file.write("Type of Selection: Roulette SUS - Stochastic Universal Sampling \n")
        elif self.configs.single_tournament:
            file.write("Type of Selection: Single Tournament\n")
        elif self.configs.death_tournament:
            file.write("Type of Selection: Death Tournament\n")
        elif self.configs.niching_tournament:
            file.write("Type of Selection: Niching Tournament\n")

        # Type of Crossover
        if self.configs.point_crossover:
            file.write("Type of Crossover: Point\n")
        elif self.configs.arithmetic_crossover:
            file.write("Type of Crossover: Arithmetic\n")
        elif self.configs.sbx_crossover:
            file.write("Type of Crossover: SBX\n")

        if self.obj.type_mse_cost:
            file.write("Type of cost: MSE (mean square error)\n")
        elif self.obj.type_ae_cost:
            file.write("Type of cost: AE (absolute error)\n")

        # Type of Mutation
        if self.configs.fixed_mutation:
            file.write("Type of Mutation: Fixed\n")
        elif self.configs.dyn_mutation:
            file.write("Type of Mutation: Dynamic\n")

        file.write("Local Search:" + str(self.configs.local_seach) + "\n")
        file.write("Crossover rate:" + str(self.configs.crossover_rate) + "\n")
        file.write("Mutation rate:" + str(self.configs.mutation_rate) + "\n\n")
        file.close()

    def executions_log(self, file_name):
        """
        Results by execution for GA
        """
        file = open(file_name, 'a')
        file.write("-----------------Results by Execution-----------------------\n")
        for num, exec_ in enumerate(self.best_particles):
            file.write("Execution nº:" + str(num) + "\n")
            file.write("convergence generation:" + str(exec_.convergence_generation) + "\n")
            file.write("cromo:" + str(exec_.cromo) + "\n")
            file.write("cost:" + str(exec_.cost) + "\n")
            file.write("fitness:" + str(exec_.fit) + "\n")
            file.write("AE (Absolute Error):" + str(exec_.ae) + "\n")
            file.write("MSE (Mean Square Error):" + str(exec_.mse) + "\n")
            file.write("MAPE (Mean Absolute Percentage Error):" + str(exec_.mape) + "\n")
            file.write("ARV (Average Relative Variance):" + str(exec_.arv) + "\n")
            file.write("IA (Index of Agreement):" + str(exec_.ia) + "\n")
            file.write("MAE (Mean Absolute Error):" + str(exec_.mae) + "\n")
            file.write("RMSE (Root Mean Squared Error):" + str(exec_.rmse) + "\n")
            file.write("Mean:" + str(exec_.mean) + "\n")
            file.write("Ranking:" + str(exec_.ranking) + "\n")
            file.write("training prediction:" + str(exec_.prediction) + "\n")
            file.write("test prediction:" + str(exec_.test_prediction) + "\n\n\n")
        file.close()

    def execution_log(self, file_name):
        """
        Best execution results for DE
        """
        file = open(file_name, 'a')
        file.write("-----------------Best execution results-----------------------\n")
        file.write("convergence generation:" + str(self.best.convergence_generation) + "\n")
        file.write("cromo:" + str(self.best.cromo) + "\n")
        file.write("cost:" + str(self.best.cost) + "\n")
        file.write("fitness:" + str(self.best.fit) + "\n")
        file.write("AE (Absolute Error):" + str(self.best.ae) + "\n")
        file.write("MSE (Mean Square Error):" + str(self.best.mse) + "\n")
        file.write("MAPE (Mean Absolute Percentage Error):" + str(self.best.mape) + "\n")
        file.write("ARV (Average Relative Variance):" + str(self.best.arv) + "\n")
        file.write("IA (Index of Agreement):" + str(self.best.ia) + "\n")
        file.write("MAE (Mean Absolute Error):" + str(self.best.mae) + "\n")
        file.write("RMSE (Root Mean Squared Error):" + str(self.best.rmse) + "\n")
        file.write("Mean:" + str(self.best.mean) + "\n")
        file.write("Ranking:" + str(self.best.ranking) + "\n")
        file.write("training prediction:" + str(self.best.prediction) + "\n")
        file.write("test prediction:" + str(self.best.test_prediction) + "\n\n\n")
        file.close()
