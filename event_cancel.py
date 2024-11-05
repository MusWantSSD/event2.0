import requests
from utils.init_headers import init_headers
from event_history import get_history

his_list = get_history()


def cancel(id):
    headers = init_headers()

    data = {
        'id' : id
    }

    response = requests.post('https://nxdyjs.nuist.edu.cn/gmis5/student/yggl/kwhdbm_del',
                             headers=headers,
                             data=data).json()
    print('id:{} 已取消'.format(id))
    
    return response

if __name__ == '__main__':
    ls = []
    for i in ls:
        cancel(i)