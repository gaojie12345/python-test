# 01-25


import redis

client = redis.Redis(host='xxxxxx', port=6379, password='xxxxxxx')

client.set("qifei", 'amin')
client.hset("qifei1", 'amin', '111')

print(client.get('qifei'))