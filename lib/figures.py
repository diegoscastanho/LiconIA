"""
@author: Diego Solak Castanho
https://github.com/diegoscastanho
"""
import matplotlib.pyplot as plt
import numpy as np

class PlotGraphics:
    """
    Plot graphics
    """
    def __init__(self, obj):
        self.database = obj.database_radiobutton.isChecked()
        self.real_prediction_test = obj.rxp_test_radiobutton.isChecked()
        self.real_prediction_training = obj.rxp_training_radiobutton.isChecked()
        self.global_best_fit_evolution = obj.gb_fitness_radiobutton.isChecked()
        self.global_best_cost_evolution = obj.gb_cost_radiobutton.isChecked()
        self.boxplot_fitness = obj.boxplot_fitness_radiobutton.isChecked()
        self.boxplot_cost = obj.boxplot_cost_radiobutton.isChecked()

        self.data = obj.json_data

    def run(self):
        """
        Generate graphics
        """
        if self.database:
            self.generate_database()
            # self.generate_test_figure()
        if self.real_prediction_test:
            self.generate_test_figure()
        if self.real_prediction_training:
            self.generate_training_figure()
        if self.global_best_fit_evolution:
            self.generate_global_best_fit_evolution()
        if self.global_best_cost_evolution:
            self.generate_global_best_cost_evolution()
        if self.boxplot_fitness:
            self.generate_boxplot_fitness()
        if self.boxplot_cost:
            self.generate_boxplot_cost()

    def generate_database(self):
        """
        Generate database
        """
        
        real = self.data[0]["obj"].hospit

        # title = "PSO_training_hospitalizations_delay " + str(delay_day)
        plt.plot(real, 'black', label='observado')
        plt.ylabel('Número de Hospitalizações')
        plt.xlabel('Dias')
        plt.grid(True)
        # plt.legend()
        plt.show()


    def generate_test_figure(self):
        """
        Generate the training figure
        """
        prediction = self.data[0]['best'].test_prediction
        real = self.data[0]["obj"].hospit_test

        plt.plot(real, 'r', label='observado')
        plt.plot(prediction, 'b', label='simulado')
        plt.ylabel('Número de hospitalizações')
        plt.xlabel('Dias')
        plt.grid(True)
        plt.legend()
        # plt.savefig('/home/diego/Desktop/ae_de/real_prediction_test.png', dpi=150) 
        plt.show()

    def generate_training_figure(self):
        """
        Generate the training figure
        """
        prediction = self.data[0]['best'].train_prediction
        real = self.data[0]["obj"].hospit_train

        plt.plot(real, 'r', label='observado')
        plt.plot(prediction, 'b', label='simulado')
        plt.ylabel('Número de hospitalizações')
        plt.xlabel('Dias')
        plt.grid(True)
        plt.legend()
        # plt.savefig('/home/diego/Desktop/mse_pso_real_prediction_trainning.png', dpi=150) 
        plt.show()

    def generate_global_best_fit_evolution(self):
        """
        Generate global_best_fit_evolution
        """
        fit_evolution = self.data[0]['best'].fit_evolution

        plt.plot(fit_evolution)
        plt.ylabel('Evolução do fitness')
        plt.xlabel('Iterações')
        plt.grid(True)
        plt.legend()
        # plt.savefig('/home/diego/Desktop/ae_de/global_best_fit_evolution.png', dpi=150) 
        plt.show()

    def generate_global_best_cost_evolution(self):
        """
        Generate global_best_cost_evolution
        """
        cost_evolution = self.data[0]['best'].cost_evolution

        cost_type = ""
        if self.data[0]['obj'].type_ae_cost:
            cost_type = "Erro Absoluto (AE)"
        if self.data[0]['obj'].type_mse_cost:
            cost_type = "Erro Quadrático Médio - MSE "

        plt.plot(cost_evolution)
        plt.ylabel(cost_type)
        plt.xlabel('Iterações')
        plt.grid(True)
        plt.legend()
        # plt.savefig('/home/diego/Desktop/ae_de/global_best_cost_evolution.png', dpi=150) 
        plt.show()

    def generate_boxplot_fitness(self):
        """
        Generate Boxplot fitness
        """
        fit_lits, plot_labels = list(), list()
        for lag in self.data:
            fit_list = list()
            for part in lag['best_particles']:
                fit_list.append(part.fit)
            fit_lits.append(fit_list)
            aux = "lag_" + str(lag['obj'].day_lag)
            plot_labels.append(aux)

        # title = "Box Plot Fitness - " + lag['obj'].algorithm 
        _, ax = plt.subplots()
        # ax.set_title(title)
        ax.boxplot(fit_lits, labels = plot_labels)
        ax.set_ylabel('Fitness')
        # plt.savefig('/home/diego/Desktop/mse_pso_boxplot_fitness.png', dpi=150) 
        plt.show()

    def generate_boxplot_cost(self):
        """
        Generate boxplot_cost
        """
        cost_lits, plot_labels = list(), list()
        for lag in self.data:
            cost_lit = list()
            for part in lag['best_particles']:
                cost_lit.append(part.cost)
            cost_lits.append(cost_lit)
            aux = "lag_" + str(lag['obj'].day_lag)
            plot_labels.append(aux)

        cost_type = ""
        if self.data[0]['obj'].type_ae_cost:
            cost_type = "Erro Absoluto (AE)"
        if self.data[0]['obj'].type_mse_cost:
            cost_type = "Erro Quadrático Médio - MSE "

        # title = "Box Plot Cost - " + lag['obj'].algorithm 
        _, ax = plt.subplots()
        # ax.set_title(title)
        ax.boxplot(cost_lits, labels = plot_labels)
        ax.set_ylabel(cost_type)
        # plt.savefig('/home/diego/Desktop/ae_de/boxplot_cost.png', dpi=150) 
        plt.show()
