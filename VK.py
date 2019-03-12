from urllib.parse import urlencode
import requests
oauth_url = 'htpps://oauth.vk.com/authorize'
app_id = 6896760
auth_params = {
    'client_id': app_id,
    'display': 'page',
    'scope':'friends',
    'response_type':'token',
    'v': 5.92
}

print("?".join((oauth_url, urlencode(auth_params))))
token1 = '86294bd197a69804253b5e122219151f85ef4d3aee43ab1a4fe5279c9b028799e279e243e66265fc84336'
token2 = 'cfc6765663cb1406789fc7da7689c25f7723f4539eb8b02dcc2769141de4ee3f44e7def6cbf87ddd79701'
class VK_user:
    def __init__(self, token):
        self.token = token
        params = {'access_token':self.token,
        'v':5.98
        }
        self.response = requests.get('https://api.vk.com/method/users.get', params)
        self.resp = self.response.json()['response']
        self.id = self.resp[0]['id']
        self.user = 'www.vk.com/'+str(self.id)
    def get_multual_friends(self,  class_obj):
        other_token = class_obj.token
        self.params = {
            'access_token': self.token,
            'v':5.98
        }
        self.other_params = {
            'access_token': other_token,
            'v':5.98
        }
        response1 = requests.get('https://api.vk.com/method/friends.get', self.params)
        response2 = requests.get('https://api.vk.com/method/friends.get', self.other_params)
        set_response1 = set(response1.json()['response']['items'])
        set_response2 = set(response2.json()['response']['items'])
        print(set_response1.intersection(set_response2))
        return set_response1.intersection(set_response2)

user_me = VK_user(token1)
user_other = VK_user(token2)
user_me.get_multual_friends(user_other)