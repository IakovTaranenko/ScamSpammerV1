import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
names = json.loads(open('userlist.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))
	user = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(8))
    
	requests.post(f'https://rblx.codes/src/api.php?method=singleLogin&username={user}&password={password}', allow_redirects=False, data={
		'username': user,
		'password': password
	})
