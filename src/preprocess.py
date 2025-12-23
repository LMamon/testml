import os
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

def preprocess_data(df, target_cols):
    os.makedirs("models", exist_ok=True)
    X = df.drop(columns=target_cols)

    numeric_features = X.select.dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object', 'category']).columns

    numerical_pipeline = SimpleImputer(strategy='median')
    categorical_pipeline = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', categorical_pipeline, categorical_features),
        ]
    )
    
    joblib.dump(preprocessor, "models/preprocessors.joblib")
    return preprocessor, X