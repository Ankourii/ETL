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

    

def cleaning_month_phases(x):
    
    if 'Jan' in x:
        return 1
    elif 'Feb' in x:
        return 2
    elif 'Mar' in x:
        return 3
    elif 'Apr' in x:
        return 4
    elif 'May' in x:
        return 5
    elif 'Jun' in x:
        return 6
    elif 'Jul' in x:
        return 7
    elif 'Aug' in x:
        return 8
    elif 'Sep' in x:
        return 9
    elif 'Oct' in x:
        return 10
    elif 'Nov' in x:
        return 11
    elif 'Dec' in x:
        return 12
    else:
        return x  


    
import re
def cleaning_day(x):    
    num = re.findall('\d+', x)
    
    
    if num:
        
        return int(num[0])
    
    else:
        
        return x

    
def cleaning_phase(x):
    if 'waning gibbous' in x.lower():
        return 'waning gibbous'
    elif 'last quarter' in x.lower():
        return 'last quarter'
    elif 'waning crescent' in x.lower():
        return 'waning crescent'
    elif 'new moon' in x.lower():
        return 'new moon'
    elif 'waxing crescent' in x.lower():
        return 'waxing crescent'
    elif 'first quarter' in x.lower():
        return 'first quarter'
    elif 'waxing gibbous' in x.lower():
        return 'waxing gibbous'
    elif 'full moon' in x.lower():
        return 'full moon'
    else:
        return x
    
import re    
def cleaning_year_ecl(x):
    num = re.findall('\d+', x)
    
    if num:
        
        return int(num[1])
    
    else:
        
        return x
    
import re
def cleaning_day_ecl(x):
    num = re.findall('\d+', x)
    
    if num:
        
        return int(num[0])
    
    else:
        
        return x

def cleaning_hol_year(x):
    return x.split('-')[0]

def cleaning_hol_month(x):
    return x.split('-')[1]


def cleaning_hol_day(x):
    return x.split('-')[2]

def cleaning_dow(x):
    if x==1:
        return 'Monday'
    elif x==2:
        return 'Tuesday'
    elif x==3:
        return 'Wednesday'
    elif x==4:
        return 'Thursday'
    elif x==5:
        return 'Friday'
    elif x==6:
        return 'Saturday'
    elif x==7:
        return 'Sunday'
    else:
        return x

def convert_object_to_category(df):
    for c in df.select_dtypes(include="object"):
        df[c] = df[c].astype("category")

def downcast_int(df):
    for c in df.select_dtypes(include="integer"):
        df[c] = pd.to_numeric(df[c], downcast="integer")

    
