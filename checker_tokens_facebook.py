import requests

def register(token):
    data = f'fb_access_token={token}&username=zyll&first_name=&enc_password=#PWD_INSTAGRAM_BROWSER:0:0:zyllishere'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": "missing",
    }
    url = 'https://www.instagram.com/fb/create/ajax/'
    resp = requests.post(url,headers=headers,data=data).text
    return resp

tokens = open('tokens.txt','r').read().splitlines()
work = 0
for token in tokens:
    resp = register(token)
    if 'username_is_taken' in resp:
        print(token)
        work += 1
        with open('tokens working.txt', 'a', encoding='utf-8', errors='ignore') as p:
            p.writelines(token + '\n')
    # else:
    #     print(resp)
print(f'Working : {str(work)}')
input('')
