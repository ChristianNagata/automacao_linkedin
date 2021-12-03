from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def process(link_modal):
    # Abre o modal da formação
    w.get(link_modal)

    # Clica no botão de adicionar mídia
    element1 = w.find_element(By.ID, 'ember160')  # (same)
    element1.click()
    time.sleep(1)
    element1.send_keys(Keys.TAB)

    # Clica no botão de adicionar link
    element2 = w.find_element(
        By.XPATH, '/html/body/div[3]/div/div/div[2]/div[3]/div[2]/div[3]/div/div/div/ul/li/div[1]')  # (same)
    element2.click()

    # Cola e envia o link selecionado
    element3 = w.find_element(
        By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/div/input')  # (same)
    element3.send_keys(Keys.CONTROL, 'v')
    element3.send_keys(Keys.ENTER)

    time.sleep(8)

    # Clica em 'apply'
    element4 = w.find_element(
        By.XPATH, '/html/body/div[3]/div/div/div[3]/button')
    element4.click()

    # Clica em 'save'
    element5 = w.find_element(
        By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
    element5.click()

    time.sleep(2)


options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:\\Users\\ACER\\AppData\\Local\\Google\\Chrome\\User Data")
w = webdriver.Chrome(
    executable_path="C:\\Users\\ACER\\Documents\\VSCodeProjects\RPA\\chromedriver.exe", chrome_options=options)
w.get('https://cursos.alura.com.br/user/christiannagata')

for n in range(1, 39):
    w.find_element(By.XPATH,
                   '/html/body/main/section[6]/div[2]/button').click()
    w.find_element(By.XPATH,
                   f'/html/body/main/section[6]/div[1]/ul/li[{n}]/div/div[3]/a').click()  # Cerificado

    certificado = w.find_element(By.XPATH, '//*[@id="url"]')
    certificado.click()

    title = w.find_element(By.TAG_NAME, 'h5').text
    list_exception = []

    if 'DJANGO' in title:
        if 'API' in title:
            process('https://www.linkedin.com/in/christiannagata/edit/forms/education/763542341/?profileFormEntryPoint=PROFILE_SECTION')
        else:
            process('https://www.linkedin.com/in/christiannagata/edit/forms/education/763536997/?profileFormEntryPoint=PROFILE_SECTION')
    elif 'PYTHON' in title:
        process('https://www.linkedin.com/in/christiannagata/edit/forms/education/748847180/?profileFormEntryPoint=PROFILE_SECTION')
    elif 'POSTGRESQL' in title:
        process('https://www.linkedin.com/in/christiannagata/edit/forms/education/763540624/?profileFormEntryPoint=PROFILE_SECTION')
    else:
        list_exception.append(title)
        print(title)

    w.get('https://cursos.alura.com.br/user/christiannagata')
    time.sleep(1)


w.close()

if list_exception:
    for n in list_exception:
        print(f'\033[1m{n}')
