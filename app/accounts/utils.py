import requests

#TODO: добавить соощение об ошибке
def get_data_about_company_from_dadata(tax_code):
    '''Полуение данных о компании по её ИНН/ОГРН

    Больше информации о использовании API dadata https://dadata.ru/api/find-party
    '''
    url = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party'
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Authorization': 'Token 77e78f4862b3d616275575a90de5689862fac8d8'}
    data = '{"query": "value"}'.replace("value", str(tax_code))
    response = requests.post(url, headers=headers, data=data)
    return response.json()