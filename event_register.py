import requests
from utils.init_headers import init_headers


def register(id):
    headers = init_headers()

    data = {
        'id' : id
    }

    response = requests.post('https://nxdyjs.nuist.edu.cn/gmis5/student/yggl/kwhdbm_bm',
                                headers=headers,
                                data=data).json()

    return response
    


if __name__  == '__main__':
    print(register(121))


