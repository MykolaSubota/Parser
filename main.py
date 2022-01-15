import requests
from bs4 import BeautifulSoup

abs_url = 'https://www.ivi.ru'


def get_hrefs(url=abs_url):
    if not ('ivi' in url):
        url = f'{abs_url}{url}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.findAll('a')


write_file, file, ok = '', None, False
while not ok:
    write_file = input('Y - Save links to file. \nn - Write in the terminal. \nEnter (Y/n)?').strip().lower()
    if write_file == 'y' or write_file == 'n':
        if write_file == 'y':
            file = open('links_ivi_ru.txt', 'w')
        ok = True
if file is not None:
    print('Writing to file has started.')
for p_link in get_hrefs():
    if write_file == 'n':
        print(p_link.get('href'))
    else:
        file.write(f'{p_link.get("href")}\n')
    for link in get_hrefs(p_link.get('href')):
        if write_file == 'n':
            print(f'   {link.get("href")}')
        else:
            file.write(f'   {link.get("href")}\n')
if file is not None:
    file.close()
    print('Writing to file is over.')
