# -*- coding: UTF-8 -*
# File:: Udacity_P1 - p1_residual_analysis.py
# Description::
#   
# | © Copyright 2015 Llama Logic | #
__copyright__ = '© 2015 Jared Champion'

__author__ = 'Jared Champion'
__buildCode__ = 'Udacity_P1.p1_residual_analysis.JC.2015.08.13.12'


#import required libraries
from scipy import stats
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as pp


'''
This function loads the data for analysis
@since 2015.08.24

@param csv_f_path :: string :: path to csv file
'''
def load_csv(csv_f_path):
    f = open(csv_f_path)
    csv_data = pd.read_csv(f)

    return csv_data

'''
This function performs the linear regression model on the data. It is used by predictions()

@since 2015.08.13

@param features :: array model | features :: These are the features used by the linear regression model
No default.
@param values :: pandas dataframe | values :: These are the data values in pandas dataframe format
No Default.
'''
def linear_regression(features, values):

    #Create an intercept from our features
    intercept = sm.add_constant(features)


    #Create model from Intercept and Values
    #OLS is our linear regression model (Ordinary Least Squares)
    #more info: http://statsmodels.sourceforge.net/devel/generated/statsmodels.regression.linear_model.OLS.html
    model = sm.OLS(values, intercept)


    #fit the results to our model
    results = model.fit()


    #store the results
    params = results.params

    #slice added intercept; store
    intercept = results.params[0]

    #slice params; store
    params = results.params[1:]

    return intercept, params




'''
This function performs the predictions on the data
This function is based on the Udacity Intro to Data Science Problem Set 3.5 Code

@since 2015.08.13

@param dataframe :: pandas dataframe | dataset :: This is the dataframe of the NYC Data

@return: predictions :: array (test for type)
'''
def predictions(dataframe):

    '''
    The below model was used in my P1 Submission, and will be left untouched.

    This re-implementation is to test the residuals as an assessment of the fit of linear regression on the data.
    '''

    features = dataframe[['rain', 'precipi', 'Hour', 'mintempi', 'maxtempi', 'meanwindspdi', 'meandewpti']]
    dummy_units = pd.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)

    # Values
    values = dataframe['ENTRIESn_hourly']

    # Perform linear regression
    intercept, params = linear_regression(features, values)

    predictions = intercept + np.dot(features, params)

    return predictions




def residual_analysis_cyclic(predictedData, actualData):
    '''
    This function displays a representation of the fit of the linear regression model on the data

    @since 2015.08.13
    @param predictedData: pandas dataframe :: This is the dataframe of the predicted data from predictions()
    @param actualData: pandas dataframe :: This is the dataframe of the actual data to compare to the predictions

    :return: Returns True at end of process
    '''
    plt = pp.plot(actualData - predictedData)
    plt.show()

    return True


def residual_analysis_QQ( predictedData ):

    x = predictedData #array of SD?

    res = stats.probplot(x, plot=pp)

    #Show Q-Q Plot
    res.show()


inputData = load_csv('p1-data.csv')