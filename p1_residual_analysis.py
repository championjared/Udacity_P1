# -*- coding: UTF-8 -*
# File:: Udacity_P1 - p1_residual_analysis.py
# Description::
#   
# | © Copyright 2015 Llama Logic | #
__copyright__ = '© 2015 Jared Champion'

__author__ = 'Jared Champion'
__buildCode__ = 'Udacity_P1.p1_residual_analysis.JC.2015.08.13.12'


#import required libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm




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
'''
def predictions(dataframe)