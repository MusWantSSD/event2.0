import time
import requests
from vertify import base64_api
import execjs
from pprint import pprint
from bs4 import BeautifulSoup


def get_cookie():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    }

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    data = {
        "username": "xxxxxxx",
        "password": "xxxxx",
        "captcha": "",
        "rememberMe": "true",
        "_eventId": "submit",
        "cllt": "userNameLogin",
        "dllt": "generalLogin",
        "lt": "",
    }
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    
    session = requests.Session()
    session.headers.update(headers)

    # get salt and execution
    url = "https://authserver.nuist.edu.cn/authserver/login?service=https://nxdyjs.nuist.edu.cn/gmis5/oauthLogin/njxxgcdx"
    response = session.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    salt = soup.find(id="pwdEncryptSalt").get("value")
    execution = soup.find(id="execution")["value"]

    # get vertify img code
    img_url = "https://authserver.nuist.edu.cn/authserver/getCaptcha.htl?"
    time_now = str(int(time.time() * 1000))
    img_url += time_now

    img = session.get(img_url).content
    with open("ver_img.jpg", "wb") as file:
        file.write(img)

    ver_code = base64_api(uname="hylin", pwd="Ll123qwe", img="ver_img.jpg", typeid=3)
    data["captcha"] = ver_code

    # encrypt pwd
    js_file = open("utils/encrypt.js", encoding="utf-8").read()
    js_code = execjs.compile(js_file)
    encry_pwd = js_code.call("encryptPassword", data["password"], salt)

    data["password"] = encry_pwd
    data["execution"] = execution


    # grade_url = "https://nxdyjs.nuist.edu.cn/gmis5/student/pygl/xscjpm_list"
    # res = session.post(grade_url,data=data)
    # print(res.text)


    # login
    login_url = "https://authserver.nuist.edu.cn/authserver/login?service=https%3A%2F%2Fnxdyjs.nuist.edu.cn%2Fgmis5%2FoauthLogin%2Fnjxxgcdx"
    response = session.post(login_url, data=data)
    # print(response.text)

    cookies = session.cookies.get_dict()
    # pprint(cookies)

    cookie_str = ""
    for k, v in cookies.items():
        cookie_str += k + "=" + v + ";"

    with open('cookie.txt', 'w', encoding='utf-8') as f:
        f.write(cookie_str)

    # # grades rank
    # grade_url = 'https://nxdyjs.nuist.edu.cn/gmis5/student/pygl/xscjpm_list'
    # params = {
    #     'sort1': 'zkcjqcj'
    # }
    # rank = session.post(grade_url,data=params).text
    # pprint(rank)

        
    return cookie_str


if __name__ == "__main__":
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    }
    cookie = get_cookie()
    grade_url = "https://nxdyjs.nuist.edu.cn/gmis5/student/pygl/xscjpm_list"
    params = {"sort1": "zkcjqcj"}
    headers["Cookie"] = cookie
    rank = requests.post(grade_url, data=params, headers=headers).json()
    pprint(rank['rows'][0])

# print(cookie_str)



# # grades rank
# grade_url = 'https://nxdyjs.nuist.edu.cn/gmis5/student/pygl/xscjpm_list'
# params = {
#     'sort1': 'zkcjqcj'
# }
# headers['Cookie'] = cookie_str
# rank = requests.post(grade_url,data=params,headers=headers).text
# pprint(rank)
