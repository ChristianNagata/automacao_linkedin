from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-data-dir=C:\\Users\\ACER\\AppData\\Local\\Google\\Chrome\\User Data")
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\ACER\\Documents\\VSCodeProjects\RPA\\chromedriver.exe", chrome_options=options)
    return driver


def process(link_modal):
    # Abre o modal da formação
    w.get(link_modal)

    # Clica no botão de adicionar mídia
    # O id pode mudar dependendo de algumas circunstâncias
    element1 = w.find_element(By.ID, 'ember160')
    element1.click()
    time.sleep(1)
    element1.send_keys(Keys.TAB)

    # Clica no botão de adicionar link
    element2 = w.find_element(
        By.XPATH, '/html/body/div[3]/div/div/div[2]/div[3]/div[2]/div[3]/div/div/div/ul/li/div[1]')
    element2.click()

    # Cola e envia o link selecionado
    element3 = w.find_element(
        By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/div/input')
    element3.send_keys(Keys.ENTER)

    time.sleep(9)

    # Clica em 'apply'
    element4 = w.find_element(
        By.XPATH, '/html/body/div[3]/div/div/div[3]/button')
    element4.click()

    # Clica em 'save'
    element5 = w.find_element(
        By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
    element5.click()

    time.sleep(2)


def open_course(title):
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
        print(f'\033[1m{title}\033[m [não adicionado]')


w = open_browser()
w.get('https://cursos.alura.com.br/user/christiannagata')

n = 0
while True:
    n += 1
    w.find_element(
        By.XPATH, '/html/body/main/section[6]/div[2]/button').click()
    try:
        w.find_element(
            By.XPATH, f'/html/body/main/section[6]/div[1]/ul/li[{n}]/div/div[3]/a').click()
    except:
        print(
            f'\033[1;91mErro ao encontrar o item de número {n} dentro da lista.\033[m')
        w.close()
        break

    try:
        certificado = w.find_element(By.XPATH, '//*[@id="url"]')
        certificado.click()
    except:
        print('\033[1;91mErro ao encontrar o elemento: Usuário não logado.\033[m')
        w.close()
        break

    title = w.find_element(By.TAG_NAME, 'h5').text

    open_course(title)

    w.get('https://cursos.alura.com.br/user/christiannagata')
    time.sleep(1)
