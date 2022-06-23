#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import pickle
def process_data(dependent_variable):
    # load the model from disk
    filename = 'Linear_Regression_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(dependent_variable)
    # result = loaded_model.score(X_test, Y_test)
    print(result)
    res = [[dependent_variable, result]]
    result_df = pd.DataFrame(res, columns = ['Height', 'Weight'])
    return result_df
def predict_and_return_data(dependent_variable):
 output = process_data(dependent_variable)
 return output

