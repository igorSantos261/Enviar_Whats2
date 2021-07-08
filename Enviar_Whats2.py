import pandas as pd

contatos_df = pd.read_excel("Enviar.xlsx")
print(contatos_df)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#Biblioteca em Python para codificar texto em url(url Code).Codificar texto para links de url, ler.
import urllib

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)
    
#Ja estamos com login realizado nos whatsapp
for i, mensagem in enumerate(contatos_df["Mensagem"]):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Numero"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
        

