"""
@author: Diego Solak Castanho
https://github.com/diegoscastanho
"""


class Communicator():
    '''
    test
    '''
    def __init__(self, label1_=None):
        self.label1 = label1_
        self.label1.setText("Iniciando o processamento ...")
        print()

    def log_update(
            self, execution, num_executions, iteration, best_cost,
            num_iterations):
        if self.label1:
            texto = (
                "Training Progress: " + str(execution) + "/" +
                str(num_executions) + "\n" + "Interation: " +
                str(iteration) + "/" + str(num_iterations) +
                "\n" + "Best Int. MSE: " + str(best_cost))
            self.label1.setText(texto)

class PlotLogs():
    '''
    Creates the results log in the interface
    '''
    def __init__(self, obj):
        '''
        init method
        '''
        self.lag_0 = obj.lag0_label
        self.lag_1 = obj.lag1_label
        self.lag_2 = obj.lag2_label
        self.lag_3 = obj.lag3_label
        self.lag_4 = obj.lag4_label
        self.lag_5 = obj.lag5_label
        self.lag_6 = obj.lag6_label
        self.lag_7 = obj.lag7_label
        self.data = obj.json_data
    
    def run(self):
        '''
        run method
        '''

        texts = list()
        for lag in self.data:
            ae = round(lag['best'].ae, 2)
            mse = round(lag['best'].mse, 2)
            mape = round(lag['best'].mape, 2)
            arv = round(lag['best'].arv, 2)
            ia = round(lag['best'].ia, 2)
            mae = round(lag['best'].mae, 2)
            rmse = round(lag['best'].rmse, 2)
            mean = round(lag['best'].mean, 2)
            ranking = round(lag['best'].ranking, 2)
            text = (
                "AE: " + str(ae) +
                " MSE: " + str(mse) +
                " MAPE: " + str(mape) +
                " ARV: " + str(arv) +
                " IA: " + str(ia) +
                " MAE: " + str(mae) +
                " RMSE: " + str(rmse) +
                " Mean: " + str(mean) +
                " Ranking: " + str(ranking)
            )
            texts.append(text)

        self.lag_0.setText(texts[0])
        self.lag_1.setText(texts[1])
        self.lag_2.setText(texts[2])
        self.lag_3.setText(texts[3])
        self.lag_4.setText(texts[4])
        self.lag_5.setText(texts[5])
        self.lag_6.setText(texts[6])
        self.lag_7.setText(texts[7])
