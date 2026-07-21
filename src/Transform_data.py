import pandas as pd

def Preenchendo_Nome_Imovel(df):
    """
    Preenche os valores nulos na coluna 'name' com o valor 'Sem Nome'.
    
    Parâmetros:
    df (DataFrame): O DataFrame que contém a coluna 'name'.
    
    Retorna:
    DataFrame: O DataFrame com os valores nulos preenchidos.
    """
    df['name'] = df['name'].fillna('Sem nome informado')
    return df

def Preenchendo_Coluna_Host_Name(df):
    """
    Preenche os valores nulos na coluna 'host_name' com o valor 'Sem Nome'.
    
    Parâmetros:
    df (DataFrame): O DataFrame que contém a coluna 'host_name'.
    
    Retorna:
    DataFrame: O DataFrame com os valores nulos preenchidos.
    """
    df['host_name'] = df['host_name'].fillna('Sem nome informado')
    return df

def Preenchendo_Coluna_Reviews_Por_Month(df):
    """
    Preenche os valores nulos na coluna 'reviews_per_month' com o valor 0.
    
    Parâmetros:
    df (DataFrame): O DataFrame que contém a coluna 'reviews_per_month'.
    
    Retorna:
    DataFrame: O DataFrame com os valores nulos preenchidos.
    """
    df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
    return df

def Alterando_Tipo_Coluna_Last_Review(df):
    """
    Converte a coluna 'last_review' para o tipo datetime.
    
    Parâmetros:
    df (DataFrame): O DataFrame que contém a coluna 'last_review'.
    
    Retorna:
    DataFrame: O DataFrame com a coluna 'last_review' convertida para datetime.
    """
    df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
    return df

def Removendo_Linhas_Preco_0(df):
    """
    Remove as linhas do DataFrame onde a coluna 'price' é igual a 0.
    
    Problema identificado:

    Foram encontrados 11 registros com preço igual a zero. Apesar de apresentarem informações completas de anúncio,
     um valor de diária igual a zero foi considerado inconsistente com a regra de negócio da plataforma.

    Tratamento aplicado:

    Os registros foram removidos para evitar impacto nas análises de precificação.

    """
    df = df[df['price'] != 0]
    return df

def Removendo_Linhas_Minimum_Nights_365(df):
    """
    Remove as linhas do DataFrame onde a coluna 'minimum_nights' é maior que 365.
    
    "Foram identificados valores extremos na variável minimum_nights, incluindo registros superiores a 365 dias. 
    Como o objetivo da análise é avaliar hospedagens de curta e média duração, esses registros foram removidos por 
    representarem um comportamento fora do escopo da análise."
    
    """
    df = df[df['minimum_nights'] <= 365]
    return df

