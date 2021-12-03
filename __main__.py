from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:\\Users\\ACER\\AppData\\Local\\Google\\Chrome\\User Data")
w = webdriver.Chrome(
    executable_path="C:\\Users\\ACER\\Documents\\VSCodeProjects\RPA\\chromedriver.exe", chrome_options=options)
w.get('https://cursos.alura.com.br/user/christiannagata')

for n in range(1, 5):
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
            # Abre o modal da formação
            w.get('https://www.linkedin.com/in/christiannagata/edit/forms/education/763542341/?profileFormEntryPoint=PROFILE_SECTION')

            # Clica no botão de adicionar mídia
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
            element3.send_keys(Keys.CONTROL, 'v')
            element3.send_keys(Keys.ENTER)

            time.sleep(3)

            # Clica em 'apply'
            element4 = w.find_element(
                By.XPATH, '/html/body/div[3]/div/div/div[3]/button')
            element4.click()

            # Clica em 'save'
            element5 = w.find_element(
                By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')
            element5.click()

            time.sleep(5)

        else:
            w.get('https://www.linkedin.com/in/christiannagata/edit/forms/education/763536997/?profileFormEntryPoint=PROFILE_SECTION')
    elif 'PYTHON' in title:
        w.get('https://www.linkedin.com/in/christiannagata/edit/forms/education/748847180/?profileFormEntryPoint=PROFILE_SECTION')
    elif 'POSTGRESQL' in title:
        w.get('https://www.linkedin.com/in/christiannagata/edit/forms/education/763540624/?profileFormEntryPoint=PROFILE_SECTION')
    else:
        list_exception.append(title)

    w.get('https://cursos.alura.com.br/user/christiannagata')
    time.sleep(1)

w.close()
print(list_exception)
