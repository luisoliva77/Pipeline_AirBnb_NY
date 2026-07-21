from src.Extract_data import extract
from src.Load_data import load_airbnb_data
from src.Transform_data import (
    Alterando_Tipo_Coluna_Last_Review,
    Preenchendo_Coluna_Host_Name,
    Preenchendo_Coluna_Reviews_Por_Month,
    Preenchendo_Nome_Imovel,
    Removendo_Linhas_Preco_0,
    Removendo_Linhas_Minimum_Nights_365
)

import traceback
import os
from pathlib import Path
from dotenv import load_dotenv

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

table_name = "ny_airbnb_2019"

def pipeline():
    try:
        logging.info("ETAPA 1: EXTRACT")
        df_raw = extract()

        logging.info("ETAPA 2: TRANSFORM")
        # Aplicando as tranformações sequencialmente no DataFrame
        df_transformed = df_raw.copy()
        df_transformed = Preenchendo_Nome_Imovel(df_transformed)
        df_transformed = Preenchendo_Coluna_Host_Name(df_transformed)
        df_transformed = Preenchendo_Coluna_Reviews_Por_Month(df_transformed)
        df_transformed = Alterando_Tipo_Coluna_Last_Review(df_transformed)
        df_transformed = Removendo_Linhas_Preco_0(df_transformed)
        df_transformed = Removendo_Linhas_Minimum_Nights_365(df_transformed)

        logging.info("ETAPA 3: LOAD")
        load_airbnb_data(table_name, df_transformed)

        print("\n" + "=" * 60)
        print("Pipeline completed successfully!")
        print("=" * 60)

    except Exception as e:
        logging.error(f" X ERRO no Pipeline: {e}")
        traceback.print_exc()  # Ajustado aqui

if __name__ == "__main__":
    pipeline()
