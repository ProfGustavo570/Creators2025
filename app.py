import logging
import random
import string
import os
import time

import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


logging.basicConfig(
    handlers=[logging.FileHandler('app.log'), logging.StreamHandler()],
    encoding='utf-8',
    format='%(asctime)s [%(levelname)s: %(filename)s (line %(lineno)d)] %(message)s',
    datefmt='%d/%m/%Y - %H:%M:%S',
    level=logging.INFO
)

Creators = {
    'hainerd': {
        'INSTAGRAM': 'hain.nerd',
        'TIKTOK': '_hainerd_',
        'YOUTUBE': 'haiinerd'
    },
    'danguizos': {
        'INSTAGRAM': 'daneosguizos',
        'TIKTOK': 'dan.e.os.guizos',
        'YOUTUBE': 'Daneosguizos'
    },
    'aff': {
        'INSTAGRAM': 'affgirls',
        'TIKTOK': 'affcast',
        'YOUTUBE': ''
    },
    'tocomfome': {
        'INSTAGRAM': '_tocomfome_sp',
        'TIKTOK': 'to.com.fomr.sp',
        'YOUTUBE': ''
    },
    'dizcordia': {
        'INSTAGRAM': 'dizcordia.pura',
        'TIKTOK': 'diz_cordia',
        'YOUTUBE': 'UCMOlw3yMWN7rDCdh86uZ0cQ'
    },
    'twins': {
        'INSTAGRAM': 'diariode_Twins',
        'TIKTOK': 'diario.de.twins',
        'YOUTUBE': 'diariodeTwins'
    },
    'minecraft': {
        'INSTAGRAM': '',
        'TIKTOK': '',
        'YOUTUBE': ''
    },
}


def init_driver():
    try:
        if os.path.exists('/usr/bin/firefox'):
            options = FirefoxOptions()
            options.add_argument('-headless')
            driver = webdriver.Firefox(options=options)
            driver.implicitly_wait(10)
        else:
            options = ChromeOptions()
            options.binary_location = '/usr/bin/chromium-browser'
            options.add_argument('-headless')
            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(10)

        return driver
    
    except Exception as error:
        logging.critical(error)


def get_screenshots():
    try:
        from datetime import datetime

        date = datetime.now()

        driver = init_driver()

        for creator, redes in Creators.items():
            os.makedirs(f'./screenshots/{creator}', exist_ok=True)
            
            for rede, user in redes.items():
                if user:
                    if rede == 'INSTAGRAM':
                        driver.get(f'https://instagram.com/{user}')
                    elif rede == 'TIKTOK':
                        driver.get(f'https://tiktok.com/@{user}')
                    else:
                        driver.get(f'https://youtube.com/@{user}')
                    time.sleep(5)

                    driver.save_screenshot(f'./screenshots/{creator}/{rede}-{date}.png')

            logging.info(f'{creator} - OK')

    except Exception as error:
        logging.critical(error)

    driver.quit()

get_screenshots()