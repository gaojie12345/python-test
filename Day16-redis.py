# 01-25


import redis

client = redis.Redis(host='10.0.220.30', port=6379, password='wj@2022')

client.set("qifei", 'amin')
client.hset("qifei1", 'amin', '111')

print(client.get('qifei'))