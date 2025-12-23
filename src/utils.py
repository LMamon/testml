import pandas as pd

def load_standard_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    allowed_columns = [
        'Attendence',
        'Midterm',
        'Final',
        'Projects',
        'Study_Hours'
    ]
    return df[allowed_columns]

def load_biased_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    biased_allowed_columns = [
        'Attendence',
        'Midterm',
        'Final',
        'Project',
        'Study_Hours',
        'Gender',
        'Parental_Level_of_Education',
        'Internet_Access'
    ]

    return df[biased_allowed_columns]