import requests
from utils.init_headers import init_headers
from pprint import pprint

def event_list():
    url = 'https://nxdyjs.nuist.edu.cn/gmis5/student/yggl/kwhdbm_list'
    headers = init_headers()

    response = requests.get(url,headers=headers)

    return response.json()['rows']

if __name__ == '__main__':
    pprint(event_list())
