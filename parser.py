from bs4 import BeautifulSoup
import requests
import re

url = "https://istihi.ru"

name_author = input('Введите автора: ')
verse_name = input('Введите название стиха: ')


def get_catalog(tag, url, key): # Получение каталога html страницы
	request = requests.get(url)
	soup = BeautifulSoup(request.content, 'lxml')
  
	if tag == 'h3': # каталог автора
		ctl = soup.find('div', text=re.compile(key)).find_parent('a')
		ctl = ctl.get('href')
    
	if tag == 'a': # каталог стихов
		ctl = soup.find(tag, text=re.compile(key))
		ctl = ctl.get('href')
    
	if tag == 'div': # стих
		ctl = soup.find('div', class_=key).next
	return ctl


def main():  # Парсинг

  author = get_catalog('h3', url + '/authors', name_author)
	verse = get_catalog('a', url + author, verse_name)
	div =  get_catalog('div', url + verse, "poem-text")
	print(div)
	input("Нажмите Enter чтобы выйти")
  
if __name__ == '__main__':
	main()
