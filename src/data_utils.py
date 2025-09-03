import pandas as pd
import numpy as np
import urllib.request
import zipfile
import os

def descargar_mhealth_dataset():
    """
    Descarga y prepara el dataset mHealth
    """
    url = "https://archive.ics.uci.edu/static/public/319/mhealth+dataset.zip"
    
    if not os.path.exists('data/raw'):
        os.makedirs('data/raw')
    
    # Descargar y extraer
    urllib.request.urlretrieve(url, 'data/raw/mhealth.zip')
    with zipfile.ZipFile('data/raw/mhealth.zip', 'r') as zip_ref:
        zip_ref.extractall('data/raw/')
    
    return True

def crear_muestra_dataset(filepath, output_path, sample_size=5000):
    """
    Crea una muestra pequeña para GitHub
    """
    df = pd.read_csv(filepath, sep='\t', nrows=sample_size)
    df.to_csv(output_path, index=False)
    return df