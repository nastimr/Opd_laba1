from bs4 import BeautifulSoup
from openpyxl import load_workbook
from fake_useragent import UserAgent
import requests

def parse():
    UserAgent().chrome #маскируемся под пользователя
    url = 'https://omsk.hh.ru/search/vacancy?text=Python&area=68'  #передаём необходимый URL адресс
    page = requests.get(url, headers={'User-Agent': UserAgent().chrome})  #отправляем запрос методом Get на данный адресс
    print(page.status_code)  #получаем код запроса
    soup = BeautifulSoup(page.text, "html.parser")  #передаём страницу в bs4
    items = soup.findAll('a', class_='serp-item__title')  #находим контейнер с нужным классом
    vacancy = []  #создаём пустой список вакансий
    for name in items:
        vacancy.append(name.text)  #добавляем вакансии в список
        print(name)
    file = 'SpisokVacancy.xlsx' #создаём файловую переменную
    wb = load_workbook(file) #создаём переменную, которая будет загружать файл SpisokVacancy.xlsx
    ws = wb['list1']  #создаём переменную, указывающую на лист, с которым будем работать
    for element in vacancy:
        text = element  #создаём строковую переменную
        ws.append([text])  #заносим строковую переменную в файл(на указанный лист)
    wb.save(file)  #сохраняем изменения
    wb.close()  # закрываем файл