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
token1 = '5e354313b78f73ef38950d096b4b462bdcd2847acfac2c4c8bd244c0d6609e48469871f1409b32bd14d6f'
token2 = '3082f37da725283f5e4c593ad93f3aab248d86fa7a79b93a597f6994923ba00046aee6e7d5c698646b0d3'
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
    def __str__(self):
        return self.user
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
    def __and__(self, class_obj):
        self.get_multual_friends(class_obj)

user_me = VK_user(token1)
user_other = VK_user(token2)
user_me&user_other
print(user_other)