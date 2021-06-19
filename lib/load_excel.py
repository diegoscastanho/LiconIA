"""
@author: Diego Solak Castanho
https://github.com/diegoscastanho
"""
import pandas as pd
import logging
import pickle

# General procedures to show the log
logging.basicConfig(
    format=(
        '%(asctime)s - %(levelname)s: ' +
        '(%(filename)s:%(funcName)s at %(lineno)d): %(message)s'),
    datefmt='%b %d %H:%M:%S', level=logging.INFO)


class LoadExcelFile:
    """
    Is responsible for loading the spreadsheet, transforming it into an nparray
    """
    def __init__(self, file_path, debug_method):
        '''
        Initializes the class
        INPUTS:
            - file_path: path to spreadsheet
            - debug_method: True or False
        OUTPUTS:
        '''
        self.file_path = file_path
        self.debug_method = debug_method
        self.data = list()

    def run(self):
        """
        This function can be performed in debug mode or in normal mode,
        depending on the requested configuration.
        INPUTS:
            - self
        OUTPUTS:
            - data: [day0, day1, day2, ..., day7] -> entries made available
            for the simulation
        """
        logging.info("Loading the spreadsheet...")
        if self.debug_method:
            logging.info("Debug method detected")
            try:
                with open("input_files/spreadsheet.txt", 'rb') as handler:
                    self.data = pickle.loads(handler.read())
            except Exception:
                logging.info('Loading spreadsheet, txt not found...')
                self.load_spreadsheet()
                with open('input_files/spreadsheet.txt', 'wb') as handle:
                    pickle.dump(self.data, handle)
        else:
            self.load_spreadsheet()
        logging.info("Spreadsheet upload completed successfully!")
        return self.data

    def load_spreadsheet(self):
        '''
        This function loads all spreadsheet tabs into an np.array list
        INPUTS:
            - self
        OUTPUTS:
            - self.data: [day0, day1, day2, ..., day7]
            day0 is a tab with the entries with the respective delay days
        '''
        spreadsheet = pd.ExcelFile(self.file_path)
        for num, name in enumerate(spreadsheet.sheet_names):
            logging.info("Loading the spreadsheet -> lag %d " % (num))
            df = pd.read_excel(self.file_path, sheet_name=name)
            self.data.append(df.to_numpy(na_value=0))
