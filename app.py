import logging
import os
import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        'YOUTUBE': 'tocomfomesp'
    },
    'dizcordia': {
        'INSTAGRAM': 'dizcordia.pura',
        'TIKTOK': 'diz_cordia',
        'YOUTUBE': 'Diz_cordia'
    },
    'twins': {
        'INSTAGRAM': 'diariode_Twins',
        'TIKTOK': 'diario.de.twins',
        'YOUTUBE': 'diariodeTwins'
    },
    'chefs': {
        'INSTAGRAM': 'chefsdelacoss',
        'TIKTOK': 'chefsde_lacos',
        'YOUTUBE': 'chefsdelaco'
    },
    'minecraft': {
        'INSTAGRAM': '',
        'TIKTOK': '',
        'YOUTUBE': ''
    },
    'tralalelo': {
        'INSTAGRAM': '',
        'TIKTOK': '',
        'YOUTUBE': ''
    },
}


def init_driver():
    try:
        driver = uc.Chrome(headless=True, use_subprocess=False,)
        driver.implicitly_wait(10)

        return driver

    except Exception as error:
        logging.critical(error)


def cycle_pages(driver):
    driver.get(f'https://instagram.com/virginia')

    try:
        # Espera até o botão de aceitar cookies aparecer
        botao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(., 'Permitir todos os cookies')]"))
        )
        botao.click()
    except:
        print("Nenhum modal de cookies detectado")

    driver.get(f'https://tiktok.com/@virginiafonseca')

    try:
        # Espera até o botão de aceitar cookies aparecer
        botao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(., 'Permitir todos')]"))
        )
        botao.click()
    except:
        print("Nenhum modal de cookies detectado")

    driver.get(f'https://www.youtube.com/channel/UCsaB2VrLZrtGbum6Eo0ClbA')

    try:
        # Espera até o botão de aceitar cookies aparecer
        botao = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(., 'Aceitar tudo')]"))
        )
        botao.click()
    except:
        print("Nenhum modal de cookies detectado")


def get_screenshots():
    try:
        from datetime import datetime

        date = datetime.now()

        driver = init_driver()
        cycle_pages(driver)

        for creator, redes in Creators.items():
            os.makedirs(f'./screenshots/{creator}', exist_ok=True)

            for rede, user in redes.items():
                if user:
                    if rede == 'INSTAGRAM':
                        driver.get(f'https://instagram.com/{user}')
                    else:
                        driver.get(f'https://{rede.lower()}.com/@{user}')
                    time.sleep(10)

                    driver.save_screenshot(
                        f'./screenshots/{creator}/{rede}-{date}.png')

            logging.info(f'{creator} - OK')

    except Exception as error:
        logging.critical(error)

    driver.quit()


get_screenshots()
