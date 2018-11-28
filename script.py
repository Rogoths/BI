import requests

class Bi_connec:
    def __init__(self, log, password):

        self.token = get_token()
        self.log = log
        self.password = password

    pass

    def get_banks():
        r = requests.get("https://demo.biapi.pro/2.0/banks").json()
        banks = r['banks']
        for bank in banks:
            print (bank['name'],':', bank['id'])

    def get_token():

        r = requests.post("https://demo.biapi.pro/2.0/auth/init").json()

        return(r['auth_token'])

    def request_api(log, password):
        token = str(get_token())
        payload = {'id_bank':'1152', 'login':log, 'password':password,}
        headers = {'Authorization': 'Bearer '+token}

        r = requests.post('https://demo.biapi.pro/2.0/users/me/connections?expand=fields', data=payload, headers=headers).json()#data pour le POST et param pour le GET
        #r = requests.get('https://demo.biapi.pro/2.0/banks/1152?expand=fields', headers=headers).json()
        #print(s)
        return(r['id_user'])

    def update(id):
        token = str(get_token())
        headers = {'Authorization': 'Bearer '+token}
        r = requests.get("https://demo.biapi.pro/2.0//users/"+str(id)+"/connections?expand=accounts", headers=headers).json()
        print(r)
"""
POST /users/me/connections
Authorization: Bearer <token>
-F login:
-F password:
-F id_bank:1152
"""

if __name__ == '__main__':
    print(get_token())
    get_banks()
