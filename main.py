from  event_history import get_history
from event_register import register
from event_list import event_list
"""
Ciallo ~(∠・ωく)⌒☆
"""


history = get_history()
ev_list = event_list()

id1 = history[-1]['hdid'] if history else 0
id2 = ev_list[0]['id'] if ev_list else 0

start = id1 if id1 >= id2 else id2
id = start
ls = {}

while 1:
    response = register(id)
    zt = response['zt']
    if zt == '1':
        ls[str(id)] = {}
        print('hdid:{} 已成功报名'.format(id))
        id += 1
    else:
        msg = response['msg']
        if msg == '未发布活动':
            break
        else:
            id += 1
# print(ls)

history = get_history()
for i in range(len(ls)):
    event = history[-i-1]
    e_hdid = event['hdid']
    e_id = event['id']
    e_name = event['hdmc']
    ls[str(e_hdid)]['name'] = e_name
    ls[str(e_hdid)]['id'] = e_id

print('\n已成功报名下列活动:')
for k,v in ls.items():
    print('hdid: {} 活动名称: {}'.format(k,v['name']))

print('\n活动hdid与id列表如下，请转到event_cancel对不需要的活动进行取消')
print([int(i) for i in ls.keys()])
print([int(i['id']) for i in ls.values()])





