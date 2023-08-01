import os
import sys
import dill   

import numpy as np
import pandas as pd
from src.logger import logging

from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_obj(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)   #dill help us to create pickle file

    except Exception as e:
        raise CustomException(e,sys)


def evaluate_models(X_train,y_train,X_test,y_test,models,param):
    try:
        report = {}
        
        for i in range(len(list(models))):   # list(models)==>converts the keys of the models dictionary into a list
            model = list(models.values())[i]   # extracting the model object from the dictionary models at a specific index i
            
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=2)
            gs.fit(X_train,y_train)

            
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            
            report[list(models.keys())[i]] = test_model_score  #the R2 score of a model is stored in the report dictionary with the corresponding model's name as the key.
            logging.info(report)
        return report

    except Exception as e:
        logging.info('Occured in utils')
        raise CustomException(e, sys)            