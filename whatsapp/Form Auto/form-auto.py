#####  importações para para o arquivo Excell
import pandas as pd

##### Importações para automatizar navegador web

from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://google.com")


# 0- ler arquivo Excell - OK
# 1- Loopar o arquivo - loopar cada linha do arquivo - OK
#  preencher os  dados lidos para cada linha no navegador web#