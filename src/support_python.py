#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
pd.set_option('display.max_columns', None)


import numpy as np

import warnings
warnings.filterwarnings('ignore')

import pylab as plt  # import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


def check_nan(df: pd.DataFrame) -> None:
    
    """
    Recibe un dataframe y enseña el % de nulos y lo grafica
    """
    
    nan_cols = df.isna().mean() * 100  # % de valores nulos
    
    nan_cols = nan_cols[nan_cols>0]
    
    display(f'N nan cols: {len(nan_cols)}')
    display(nan_cols)
    
    
    # grafico de nulos en el dataframe

    #inicializa la figura
    plt.figure(figsize=(10, 6))  # 100X60  pixeles


    sns.heatmap(df.isna(),       # datos
                yticklabels=False,  # quita las etiquetas del eje y
                cmap='viridis',      # mapa de color
                cbar=False           # sin barra lateral
               )

    plt.show();
    
    
import pandas as pd
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import sys

def extract_moon_phases():
    months=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    years=[i for i in range(1994,2004)]
    driver = webdriver.Chrome()

    phases_data=[]

    url = f'https://mooncalendar.astro-seek.com/moon-phases-calendar-january-1994'
    driver.get(url)
    driver.find_element(By.XPATH, '/html/body/div[1]/a[2]').click()
    for year in years:
        for month in months[1:]:
            url = f'https://mooncalendar.astro-seek.com/moon-phases-calendar-{month}-{year}'
            driver.get(url)

            time.sleep(1) 

            try:

                body = driver.find_element(By.CSS_SELECTOR, 'div > table > tbody')
                rows = body.find_elements(By.TAG_NAME, 'tr')
                for row in rows:
                    rows_cleaned = row.text.split('\n')
                    info = rows_cleaned[0]
                    phases_data.append([year,info])
                print(f"mes {month} completed succesfully")
            except:
                print(f'error with {month}, {year}')




    driver.quit()
    return phases_data

