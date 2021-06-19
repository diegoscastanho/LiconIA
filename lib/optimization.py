"""
@author: Diego Solak Castanho
https://github.com/diegoscastanho
"""
from copy import deepcopy
import logging
import numpy as np
from lib.pso import ParticleSwarmOptimization
from lib.de import DifferentialEvolution
from lib.ga import GeneticAlgorithm
from lib.communicator import Communicator


# General procedures to show the log
logging.basicConfig(
    format=(
        '%(asctime)s - %(levelname)s: ' +
        '(%(filename)s:%(funcName)s at %(lineno)d): %(message)s'),
    datefmt='%b %d %H:%M:%S', level=logging.INFO)


class SerialExecution(object):
    '''
    This class is responsible for all the optimizations
    '''

    def __init__(self, object, child_conn, day_lag, method):
        ''' Constructor. '''
        self.debug_method = object.debug_method
        self.child_conn = child_conn  # connection parallel execution
        self.day_lag = day_lag
        self.data = object.data

        # Global Variables
        self.index_timestamp = int(object.dayindex_field.text())
        self.real_internation_index = int(object.prediction_field.text())
        self.index_day_week = int(object.dayoftheweek_field.text())

        if(method =="GA"):
            logging.info("Optimization algorithm: GA")
            self.algorithm = "GA"
            self.type_mse_cost = object.ga_mse_radiobutton.isChecked()
            self.type_ae_cost = object.ga_ae_radiobutton.isChecked()

        elif(method =="DE"):
            logging.info("Optimization algorithm: DE")
            self.algorithm = "DE"
            self.type_mse_cost = object.de_mse_radiobutton.isChecked()
            self.type_ae_cost = object.de_ae_radiobutton.isChecked()
        
        elif(method =="PSO"):
            logging.info("Optimization algorithm: PSO")
            self.algorithm = "PSO"
            self.type_mse_cost = object.pso_mse_radiobutton.isChecked()
            self.type_ae_cost = object.pso_ae_radiobutton.isChecked()

        logging.info("Load variables")
        self.interface = object

        # init variables
        self.dimensions = None
        self.coefficients = None
        self.hospit = None  # number days of hospitalizations
        self.len_train = None  # 85% for training
        self.len_test = int(object.number_test_samples_field.text())   # 15% for testing
        self.hospit_test = None  # number of days of testing hospitalizations
        self.hospit_train = None  # number of days of training hospitalizations
        self.months = None  # Array with the monthss from 1 to 12
        self.months_test = None  # Array with the monthss from 1 to 12
        self.months_train = None  # Array with the monthss from 1 to 12
        self.hospit_train = None
        self.hospit_train_standard = None
        self.hospit_test_standard = None
        self.averages = None
        self.variances = None
        self.data_train = None
        self.data_test = None

    def run(self):
        '''
        Main optimization class
        '''

        self.data_format(self.data , delay_day=self.day_lag)

        if self.algorithm == "GA":
            logging.info("Starting GA execution")
            # self.pso1_label.log_update(0, 0, 0, 0, 0)
            ga = GeneticAlgorithm(
                self, self.interface, self.debug_method, delay_day=self.day_lag)
            best_particles, best_particle = ga.run()

        elif self.algorithm == "DE":
            logging.info("Starting DE execution")
            # self.pso1_label.log_update(0, 0, 0, 0, 0)
            de = DifferentialEvolution(
                self, self.interface, self.debug_method, delay_day=self.day_lag)
            best_particles, best_particle = de.run()

        elif self.algorithm == "PSO":
            logging.info("Starting PSO execution")
            # self.pso1_label.log_update(0, 0, 0, 0, 0)
            pso = ParticleSwarmOptimization(
                self, self.interface, self.debug_method, delay_day=self.day_lag)
            best_particles, best_particle = pso.run()

    def data_format(self, data, delay_day):
        '''
        Formats the data
        '''
        self.input_data = self.convert_date_to_month(
            data[delay_day], self.index_timestamp)
        self.input_data = self.convert_day_week_binary(
            data[delay_day], self.index_day_week)

        # len trainning and testing data
        self.len_train = int(self.input_data.shape[0] - self.len_test)

        # training and testing data
        self.data_train = deepcopy(
            self.input_data[
                0:self.len_train][:][:, self.real_internation_index+1:])
        self.data_test = deepcopy(
            self.input_data[
                self.len_train:][:][:, self.real_internation_index+1:])

        # months data
        self.months = deepcopy(self.input_data[:][:, 0])
        self.months_train = deepcopy(self.months[0:self.len_train])
        self.months_test = deepcopy(self.months[self.len_train:])

        # hospitalization data
        self.hospit = deepcopy(
            self.input_data[:][:, self.real_internation_index])
        self.hospit_train = deepcopy(self.hospit[0:self.len_train])
        self.hospit_test = deepcopy(self.hospit[self.len_train:])

        self.dimensions = self.data_train.shape[1]
        self.coefficients = self.dimensions + 1

        self.averages, self.variances = self.calc_averages_variances(
            self.hospit, self.months)

        self.hospit_train_standard = self.standardize_data(
            self.hospit_train, self.months, self.averages, self.variances)

        self.hospit_test_standard = self.standardize_data(
            self.hospit_test, self.months, self.averages, self.variances)

    def convert_date_to_month(self, data, index_timestamp):
        """
        Convert date to month
            INPUTS:
                data: matrix with all input data
                index_timestamp: index where the data position is located
            OUTPUTS:
                data: formatted column from 1 to 12
        """
        for date in data:
            date[index_timestamp] = date[index_timestamp].month
        return data

    def convert_day_week_binary(self, data, index_day_week):
        """
        Convert date to month
            INPUTS:
                data: matrix with all input data
                index_day_week: index where the column of the day is located
            OUTPUTS:
                new_data_: binary formatted days of the week
        """
        new_data = list()
        for num, date in enumerate(data):
            aux = []
            for day in range(7):
                if date[index_day_week] == day:
                    aux.append(1)
                else:
                    aux.append(0)
            date_aux = np.append(date, aux)
            new_data.append(date_aux)
        np.delete(new_data, index_day_week, axis=1)
        new_data_ = np.array(new_data)
        return new_data_

    def calc_averages_variances(self, hospitalizations, months):
        """
        Performs the calculation of means and variances
            INPUTS:
                hospitalizations: list with number of hospitalizations
                months: list with months of the year
            OUTPUTS:
                averages: list with 12 average hospitalizations of the year
                variances: list with 12 variances hospitalizations of the year
        """
        averages = np.zeros((12, 1), dtype=np.float64)
        amount = np.zeros((12, 1), dtype=np.float64)
        variances = np.zeros((12, 1), dtype=np.float64)

        # Calculation of averages
        for num, hospit in enumerate(hospitalizations):
            month = months[num] - 1
            averages[month] += hospit
            amount[month] += 1
        for i in range(len(averages)):
            averages[i] /= amount[i]

        # Calculation of variance
        for num, hospit in enumerate(hospitalizations):
            month = months[num] - 1
            variances[month] += (hospit - averages[month])**2
        for i in range(len(variances)):
            variances[i] = np.sqrt(variances[i] / amount[i])
        return averages, variances

    def standardize_data(self, hospitalizations, months, averages, variances):
        """
        Performs data standardization
            INPUTS:
                hospitalizations: list with hospitalizations
                months: list with months of the year formatted from 1 to 12
                averages: list with 12 average hospitalizations of the year
                variances: list with 12 variances hospitalizations of the year
            OUTPUTS:
                    standardized_hospitalizations: list of standardized number
                        of hospitalizations
        """
        standardized_hospitalizations = deepcopy(hospitalizations)
        for num, hospit in enumerate(standardized_hospitalizations):
            month = months[num] - 1
            standardized_hospitalizations[num] = (
                hospit - averages[month][0]) / variances[month][0]
        return standardized_hospitalizations
