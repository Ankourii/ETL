from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def extract_moon_phases():
    months=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    years=[i for i in range(1994,2004)]
    driver = webdriver.Chrome()

    phases_data=[]

    url = f'https://mooncalendar.astro-seek.com/moon-phases-calendar-january-1994'
    driver.get(url)
    driver.find_element(By.XPATH, '/html/body/div[1]/a[2]').click()


    
    for year in years:
        for month in months:
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
                print(f'{month} completed succesfully')
            except:
                print(f'error with {month}, {year}')




    driver.quit()
    return phases_data

