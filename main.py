
import requests

url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/'

headers = {'Authorization': 'Token 3547480e7afe9c21b68f3bad7e9d76ada756baf8'}

r = requests.get(url, headers=headers)



print(r.text)