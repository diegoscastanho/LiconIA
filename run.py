"""
@author: Diego Solak Castanho
https://github.com/diegoscastanho
"""
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from gui_tcc import Ui_MainWindow
import multiprocessing
from lib.create_process import OtimizationProcess
# from lib.create_process import LoadWorksheetProcess
import logging
from lib.communicator import Communicator
from lib.load_excel import LoadExcelFile
import pickle
from lib.figures import PlotGraphics
from lib.communicator import PlotLogs
from os import walk
import pandas as pd

# from lib.optimization import SerialExecution

# General procedures to show the log
logging.basicConfig(
    format=(
        '%(asctime)s - %(levelname)s: ' +
        '(%(filename)s:%(funcName)s at %(lineno)d): %(message)s'),
    datefmt='%b %d %H:%M:%S', level=logging.INFO)


class App(QtWidgets.QMainWindow, Ui_MainWindow):
    '''
    Ui class
    '''
    def __init__(self, parent=None):
        '''
        init class
        '''
        super(App, self).__init__(parent)
        self.setupUi(self)

        # set develop (True) or use method (False)
        if self.exec_method_radiobutton.isChecked():
            self.debug_method = False
            logging.info("Execution method type: Execution")
        if self.debug_method_radiobutton.isChecked():
            self.debug_method = True
            logging.info("Execution method type: Debug")

        # controller start stop process
        self.process_pso = 8*[0]
        self.process_ga = 8*[0]
        self.process_de = 8*[0]
        self.cont_process = 1

        # Open
        self.open_button.clicked.connect(self.handle_button)

        # Start / STOP buttons
        self.start_pso_0.clicked.connect(lambda:self.start_algorithm(0, "PSO"))
        self.start_pso_1.clicked.connect(lambda:self.start_algorithm(1, "PSO"))
        self.start_pso_2.clicked.connect(lambda:self.start_algorithm(2, "PSO"))
        self.start_pso_3.clicked.connect(lambda:self.start_algorithm(3, "PSO"))
        self.start_pso_4.clicked.connect(lambda:self.start_algorithm(4, "PSO"))
        self.start_pso_5.clicked.connect(lambda:self.start_algorithm(5, "PSO"))
        self.start_pso_6.clicked.connect(lambda:self.start_algorithm(6, "PSO"))
        self.start_pso_7.clicked.connect(lambda:self.start_algorithm(7, "PSO"))

        self.stop_pso_0.clicked.connect(lambda:self.stop_algorithm(0, "PSO"))
        self.stop_pso_1.clicked.connect(lambda:self.stop_algorithm(1, "PSO"))
        self.stop_pso_2.clicked.connect(lambda:self.stop_algorithm(2, "PSO"))
        self.stop_pso_3.clicked.connect(lambda:self.stop_algorithm(3, "PSO"))
        self.stop_pso_4.clicked.connect(lambda:self.stop_algorithm(4, "PSO"))
        self.stop_pso_5.clicked.connect(lambda:self.stop_algorithm(5, "PSO"))
        self.stop_pso_6.clicked.connect(lambda:self.stop_algorithm(6, "PSO"))
        self.stop_pso_7.clicked.connect(lambda:self.stop_algorithm(7, "PSO"))

        self.start_ga_0.clicked.connect(lambda:self.start_algorithm(0, "GA"))
        self.start_ga_1.clicked.connect(lambda:self.start_algorithm(1, "GA"))
        self.start_ga_2.clicked.connect(lambda:self.start_algorithm(2, "GA"))
        self.start_ga_3.clicked.connect(lambda:self.start_algorithm(3, "GA"))
        self.start_ga_4.clicked.connect(lambda:self.start_algorithm(4, "GA"))
        self.start_ga_5.clicked.connect(lambda:self.start_algorithm(5, "GA"))
        self.start_ga_6.clicked.connect(lambda:self.start_algorithm(6, "GA"))
        self.start_ga_7.clicked.connect(lambda:self.start_algorithm(7, "GA"))

        self.stop_ga_0.clicked.connect(lambda:self.stop_algorithm(0, "GA"))
        self.stop_ga_1.clicked.connect(lambda:self.stop_algorithm(1, "GA"))
        self.stop_ga_2.clicked.connect(lambda:self.stop_algorithm(2, "GA"))
        self.stop_ga_3.clicked.connect(lambda:self.stop_algorithm(3, "GA"))
        self.stop_ga_4.clicked.connect(lambda:self.stop_algorithm(4, "GA"))
        self.stop_ga_5.clicked.connect(lambda:self.stop_algorithm(5, "GA"))
        self.stop_ga_6.clicked.connect(lambda:self.stop_algorithm(6, "GA"))
        self.stop_ga_7.clicked.connect(lambda:self.stop_algorithm(7, "GA"))

        self.start_de_0.clicked.connect(lambda:self.start_algorithm(0, "DE"))
        self.start_de_1.clicked.connect(lambda:self.start_algorithm(1, "DE"))
        self.start_de_2.clicked.connect(lambda:self.start_algorithm(2, "DE"))
        self.start_de_3.clicked.connect(lambda:self.start_algorithm(3, "DE"))
        self.start_de_4.clicked.connect(lambda:self.start_algorithm(4, "DE"))
        self.start_de_5.clicked.connect(lambda:self.start_algorithm(5, "DE"))
        self.start_de_6.clicked.connect(lambda:self.start_algorithm(6, "DE"))
        self.start_de_7.clicked.connect(lambda:self.start_algorithm(7, "DE"))

        self.stop_de_0.clicked.connect(lambda:self.stop_algorithm(0, "DE"))
        self.stop_de_1.clicked.connect(lambda:self.stop_algorithm(1, "DE"))
        self.stop_de_2.clicked.connect(lambda:self.stop_algorithm(2, "DE"))
        self.stop_de_3.clicked.connect(lambda:self.stop_algorithm(3, "DE"))
        self.stop_de_4.clicked.connect(lambda:self.stop_algorithm(4, "DE"))
        self.stop_de_5.clicked.connect(lambda:self.stop_algorithm(5, "DE"))
        self.stop_de_6.clicked.connect(lambda:self.stop_algorithm(6, "DE"))
        self.stop_de_7.clicked.connect(lambda:self.stop_algorithm(7, "DE"))

        # Results
        self.process_open_button.clicked.connect(self.handle_button_results)
        self.plot_graph_button.clicked.connect(lambda:self.plot_graphics())
        self.copy_lag0_pushbutton.clicked.connect(lambda:self.copy_text(0))
        self.copy_lag1_pushbutton.clicked.connect(lambda:self.copy_text(1))
        self.copy_lag2_pushbutton.clicked.connect(lambda:self.copy_text(2))
        self.copy_lag3_pushbutton.clicked.connect(lambda:self.copy_text(3))
        self.copy_lag4_pushbutton.clicked.connect(lambda:self.copy_text(4))
        self.copy_lag5_pushbutton.clicked.connect(lambda:self.copy_text(5))
        self.copy_lag6_pushbutton.clicked.connect(lambda:self.copy_text(6))
        self.copy_lag7_pushbutton.clicked.connect(lambda:self.copy_text(7))


    def handle_button(self):
        '''
        Open button optimizations algoritms
        '''
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Single File', QtCore.QDir.rootPath(), '*.xlsx')
        self.open_file_field.setText(fileName)
        self.load_worksheet()

    def load_worksheet(self):
        '''
        Load worksheet
        '''
        self.label_pso_0.setText("Loading worksheet...")
        # parent_conn, child_conn = multiprocessing.Pipe()
        # process = LoadWorksheetProcess(
        #     str(0), child_conn, self)
        # process.start()
        # process.join()
        # self.data = process.recv()
        # file_path = self.object.open_file_field.text()
        self.type_method()
        file_path = self.open_file_field.text()
        load = LoadExcelFile(file_path, self.debug_method)
        self.data = load.run()


    def start_algorithm(self, day_lag, method):
        '''
        Button that starts simulation
        '''
        self.type_method()
        parent_conn, child_conn = multiprocessing.Pipe()
        # pso1_label = Communicator(self.pso1_label)
        process = OtimizationProcess(
            self.cont_process, child_conn, self, day_lag, method)
        process.start()
        self.cont_process += 1

        # self.label_pso_0.setText(parent_conn.recv())

        if method == "PSO":
            self.process_pso[day_lag] = process
        elif method == "DE":
            self.process_de[day_lag] = process
        elif method == "GA":
            self.process_ga[day_lag] = process

        logging.info("Start %s -> lag %d " % (method, day_lag))

    def stop_algorithm(self, day_lag, method):
        '''
        Button that stop simulation
        '''
        # pso1_label = Communicator(self.pso1_label)
        if method == "PSO":
            self.process_pso[day_lag].terminate()
        elif method == "DE":
            self.process_de[day_lag].terminate()
        elif method == "GA":
            self.process_ga[day_lag].terminate()       
        logging.info("Stop %s -> lag %d " % (method, day_lag))

    def handle_button_results(self):
        '''
        Open button result
        '''
        logging.info("Loading json file...")
        # file_path, test = QtWidgets.QFileDialog.getOpenFileName(
        #     self, 'Single File', QtCore.QDir.rootPath(), '*.txt')
        mypath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        _, _, filenames = next(walk(mypath))
        self.graph_file_field.setText(mypath)

        self.json_data = list() 
        for file_ in filenames:
            aux_path = mypath + "/" + file_
            with open(aux_path, 'rb') as handler:
                aux_data = pickle.loads(handler.read())
                self.json_data.append(aux_data)
        self.json_data.sort(key=lambda x: x["obj"].day_lag, reverse=False)
        logging.info("Json file load")

        self.results_logs()

    def results_logs(self):
        '''
        Creates the results log in the interface
        '''
        logging.info("Logging the interface")
        my_logs = PlotLogs(self)
        my_logs.run()


    def plot_graphics(self):
        '''
        Button that plots Graphics
        '''
        logging.info("Plotting Graphics")
        graphics = PlotGraphics(self)
        graphics.run()

    def copy_text(self, lag):
        '''
        copies the generated text to the cliboards
        '''
        ae = self.json_data[lag]['best'].ae
        mse = self.json_data[lag]['best'].mse
        mape = self.json_data[lag]['best'].mape
        arv = self.json_data[lag]['best'].arv
        ia = self.json_data[lag]['best'].ia
        mae = self.json_data[lag]['best'].mae
        rmse = self.json_data[lag]['best'].rmse
        mean = self.json_data[lag]['best'].mean
        ranking = self.json_data[lag]['best'].ranking
        df=pd.DataFrame(columns = [ ae, mse, mape, arv, ia, mae, rmse, mean, ranking])
        df.to_clipboard(index=False)

    def type_method(self):
        '''
        type exec method
        '''
        if self.exec_method_radiobutton.isChecked():
            self.debug_method = False
            logging.info("Exec method Type: Execution")
        if self.debug_method_radiobutton.isChecked():
            self.debug_method = True
            logging.info("Exec method Type: Debug")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.exit(app.exec_())
