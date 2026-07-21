from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

def extract():
    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        "dgomonov/new-york-city-airbnb-open-data",
        path="data/raw",
        unzip=True
    )

    df = pd.read_csv("data/AB_NYC_2019.csv")
    return df