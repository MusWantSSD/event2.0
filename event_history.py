import requests
from utils.init_headers import init_headers
from pprint import pprint

def get_history():
    url = 'https://nxdyjs.nuist.edu.cn/gmis5/student/yggl/kwhdbm_sqlist'
    headers = init_headers()
    response = requests.get(url,headers=headers).json()
    history = response['rows']


    return history

if __name__ == '__main__':
    pprint(get_history())