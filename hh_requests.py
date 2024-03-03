import requests
from pprint import pprint
from def_hh import vac
from json import dump as jdump

DOMAIN = 'https://api.hh.ru/'

url = f'{DOMAIN}vacancies'

data = []



params = {'text': 'python developer AND Москва AND python AND django',
            'page': '1'
            }
results = requests.get(url, params=params).json()
# pprint(results)
# print(results['found'])
found_p_j = results['found']
msc_sal_have = []
sal_from = []
sal_to = []
count_1 = vac(results)
# print(count_1)

params = {'text': 'python developer AND Москва AND python AND django AND flask',
            'page': '1'
            }
results = requests.get(url, params=params).json()
# print(results['found'])
found_p_j_f = results['found']
count_2 = vac(results)
# print(count_2)

params = {'text': 'python developer AND Москва AND python AND sqlalchemy',
            'page': '1'
            }
results = requests.get(url, params=params).json()
# print(results['found'])
found_p_s = results['found']
count_3 = vac(results)
# print(count_3)

python_vac = found_p_j + found_p_j_f + found_p_s
django_vac = found_p_j + found_p_j_f
sqla_vac = found_p_s
found_all_develop = python_vac + django_vac + sqla_vac
data.append(f'all vacancy: {python_vac} vacancy')

python_vac_percent = (python_vac / found_all_develop) * 100
data.append(f'pyton: {python_vac} vacancy,{python_vac_percent} %')

django_vac_percent = (django_vac / found_all_develop) * 100
data.append(f'django: {django_vac} vacancy,{django_vac_percent} %')

sqla_vac_percent = (sqla_vac / found_all_develop) * 100
data.append(f'sqlalchemy: {sqla_vac} vacancy,{sqla_vac_percent} %')

average_salary = (count_1 + count_2 + count_3) / 3
data.append(f'average salary: {average_salary} RUR')
pprint(data)
with open('data.json', mode = 'w') as f:
    jdump([data],f)
