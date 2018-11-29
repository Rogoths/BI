import requests


def get_banks():
    r = requests.get("https://demo.biapi.pro/2.0/banks").json()
    banks = r['banks']
    for bank in banks:
        print (bank['name'],':', bank['id'])

def get_token():

    r = requests.post("https://demo.biapi.pro/2.0/auth/init").json()

    return(r['auth_token'])

def request_api(bank, log, password):
    token = str(get_token())
    payload = {'id_bank':bank, 'login':log, 'password':password,}
    headers = {'Authorization': 'Bearer '+token}
    s = requests.Session()
    s.get("https://demo.biapi.pro/2.0/banks?expand=fields", headers=headers)
    s.post('https://demo.biapi.pro/2.0/users/me/connections?expand=fields', data=payload, headers=headers)
    a = s.get('https://demo.biapi.pro/2.0/users/me/accounts', headers=headers).json()
    t = s.get('https://demo.biapi.pro/2.0/users/me/transactions', headers=headers).json()
    print(a)
    print(t)


"""
POST /users/me/connections
Authorization: Bearer <token>
-F login:
-F password:
-F id_bank:1152
"""

if __name__ == '__main__':
    pass
