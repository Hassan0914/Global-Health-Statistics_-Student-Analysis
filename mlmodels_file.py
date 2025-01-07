import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb
from sklearn.impute import SimpleImputer

def preprocess_data(file_path, features, target):
    df = pd.read_csv(file_path)
    imputer = SimpleImputer(strategy='mean')
    df[features] = imputer.fit_transform(df[features])
    
    df = df.dropna(subset=[target])
    df = pd.get_dummies(df, columns=['Age Group', 'Gender', 'Treatment Type', 'Country', 'Disease Name'], drop_first=True)
    
    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test


def scale_features(X_train, X_test):

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled

def train_model(model, X_train, y_train):
 
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    
    predictions = model.predict(X_test)
    metrics = {
        "MAE": mean_absolute_error(y_test, predictions),
        "MSE": mean_squared_error(y_test, predictions),
        "R2": r2_score(y_test, predictions)
    }
    return metrics