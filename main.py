
from bfs import bfs
from util import Queue, Stack
import requests

url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/'

status_url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/status/'

headers = {'Authorization': 'Token 3547480e7afe9c21b68f3bad7e9d76ada756baf8'}

# r = requests.get(url, headers=headers)

status = requests.post(status_url, headers=headers)

# print(r.text)

print(f"\nstatus : {status.text}\n")

## keep track of traversed rooms
traversal_path = []

## keep track of which rooms have been
## visited and their edges
visited = {}

# initialized visited as the starting room
visited[0] = {'n': '?', 's': '?', 'e': '?', 'n': '?'}

# initialize bfs
bfs = bfs(0)
bfs.honk()

# put initial room in stack
s = Stack()






## make call to api

## receive back info
## that info is room info

## now we know what room we are in!

## we need to see if there are any unexplored rooms

exits = received_object['exits'] # {'n': 124, 's': '?'}

