"""
@author: Diego Solak Castanho
https://github.com/diegoscastanho
"""
import logging
import multiprocessing
from lib.optimization import SerialExecution
# from lib.load_excel import LoadExcelFile

# General procedures to show the log
logging.basicConfig(
    format=(
        '%(asctime)s - %(levelname)s: ' +
        '(%(filename)s:%(funcName)s at %(lineno)d): %(message)s'),
    datefmt='%b %d %H:%M:%S', level=logging.INFO)


# class LoadWorksheetProcess(multiprocessing.Process):
#     ''' Classe que auxila na parelização do roteamento ponto a ponto'''

#     def __init__(self, process_number, child_conn, object_):
#         ''' Método de instanciamento da classe'''
#         multiprocessing.Process.__init__(self)
#         self.process_number = process_number
#         self.child_conn = child_conn
#         self.object = object_

#     def run(self):
#         ''' método de execução da classe '''
#         file_path = self.object.open_file_field.text()
#         load = LoadExcelFile(file_path, self.object.debug_method)
#         data = load.run()
#         self.child_conn.send(data)
#         self.child_conn.close()


class OtimizationProcess(multiprocessing.Process):
    ''' Classe que auxila na parelização do roteamento ponto a ponto'''

    def __init__(self, process_number, child_conn, object_, day_lag, method):
        ''' Método de instanciamento da classe'''
        multiprocessing.Process.__init__(self)
        self.process_number = process_number
        self.child_conn = child_conn
        self.object = object_
        self.day_lag = day_lag
        self.method = method

    def run(self):
        ''' método de execução da classe '''
        logging.info("Starting the Process %s ... lag-> %d" % (self.process_number, self.day_lag))
        self.process_start()
        logging.info("End of Process %s" % (self.process_number))

    def process_start(self):
        ''' 
        Método que realiza a chamada das funções de otimização
        '''
        algorithm = SerialExecution(
            self.object, self.child_conn, self.day_lag, self.method)
        algorithm.run()
        self.child_conn.close()
