"""
@author: Diego Solak Castanho
https://github.com/diegoscastanho
"""
import numpy as np


def calc_prediction(pos, data_train):
    """
    Cost function
    Calculates the predictions
        INPUTS:
            pos: particle position in space
            data_train: training input data
        OUTPUTS:
            prediction: list of predictions
    """
    # beta 0 of the predictor formula
    beta_zero = np.full((data_train.shape[0], 1), pos[0])
    # other dimensions of the linear predictor
    aux_predictor = pos[1:] * data_train
    # join the two matrices
    linear_predictor = np.append(beta_zero, aux_predictor, axis=1)
    # sum the axes for detecting the forecast
    predictions = linear_predictor.sum(axis=1)
    return predictions


def calc_error(predictions, hospitalizations):
    """
    Calculates the absolute error.
        INPUTS:
            predictions: number of planned hospitalizations
            hospitalizations: number of real hospitalizations
        OUTPUTS:
        error: error of prediction
    """
    aux_error = (hospitalizations.T - predictions)  # error matrix
    aux_error_quadr = np.power(aux_error, 2)  # distance module
    error_mod = np.power(aux_error_quadr, 0.5)  # distance module
    error = error_mod.sum()  # here we have cost function the lower the better
    # ae = error/len(hospitalizations)
    return error


def calc_mse(predictions, hospitalizations):
    """
    Calculates the mean square error.
        INPUTS:
            predictions: number of planned hospitalizations
            hospitalizations: number of real hospitalizations
        OUTPUTS:
        error: error of prediction
    """
    aux_error = (hospitalizations.T - predictions)  # error matrix
    aux_error_quadr = np.power(aux_error, 2)  # distance module
    mse = aux_error_quadr.sum()/len(hospitalizations)
    return mse


def destandardization(standardized_test_prediction, averages, variances, months):
    """
    Get the real forecast of hospitalizations
        INPUTS:
            standardized_test_prediction: list with test standardized prediction
            averages: average hospitalizations per month
            variances: variances in hospitalizations per month
            months: months ordered from 1 to 12
        OUTPUTS:
            real_predictions: list with real predictions
    """
    real_predictions = list()
    for num, pred in enumerate(standardized_test_prediction):
        month = months[num] - 1
        real_prediction = int((standardized_test_prediction[num] * variances[month]) + averages[month])
        if real_prediction < 0:
            real_prediction = 0
        real_predictions.append(real_prediction)
    return real_predictions


def calc_mae(predictions, hospitalizations):
    """
    Calculates Mean absolute error
        INPUTS:
            predictions: number of planned hospitalizations
            hospitalizations: number of real hospitalizations
        OUTPUTS:
            MAE: Mean absolute error
    """
    error_sum = 0
    for num, hospit in enumerate(hospitalizations):
        error = np.abs(hospit - predictions[num])  # (dt-yt)^2
        error_sum += error
    mae = error_sum / len(hospitalizations)
    return mae


def calc_mape(predictions, hospitalizations):
    """
    Calculates Mean absolute percentage error
        INPUTS:
            predictions: number of planned hospitalizations
            hospitalizations: number of real hospitalizations
        OUTPUTS:
            MAPE: Mean absolute percentage error
    """
    error_sum = 0
    for num, hospit in enumerate(hospitalizations):
        if hospit > 0:
            error = np.abs(hospit - predictions[num] / hospit)
        error_sum += error
    mape = (error_sum / len(hospitalizations)) * 100
    return mape

def index_agreement(predictions, hospitalizations):
    """
    Calculates index of agreement
        INPUTS:
            predictions: number of planned hospitalizations
            hospitalizations: number of real hospitalizations
        OUTPUTS:
            IA: index of agreement
    """
    o = hospitalizations
    s = np.array(predictions)
    ia = 1 -(np.sum((o-s)**2))/(np.sum((np.abs(s-np.mean(o))+np.abs(o-np.mean(o)))**2))
    return ia

def calc_arv(predictions, hospitalizations):
    """
    Calculates Average Relative Variance
        INPUTS:
            predictions: number of planned hospitalizations
            hospitalizations: number of real hospitalizations
        OUTPUTS:
            ARV: average_relative_variance
    """
    y_true = np.asarray(hospitalizations).reshape(-1)
    y_pred = np.asarray(predictions).reshape(-1)
    mean = np.mean(y_true)

    error_sup = np.square(np.subtract(y_true, y_pred)).sum()
    error_inf = np.square(np.subtract(y_pred, mean)).sum()

    return error_sup / error_inf

# import scipy.stats as ss
# import numpy as np
# import itertools

# data = np.array([[ 8.82, 11.8 , 10.37], [ 8.92,  9.58, 10.59], [ 8.27, 11.46, 10.24],[ 8.83, 13.25,  8.33]])


# print(ss.friedmanchisquare(*data.T))
