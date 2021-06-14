import redis
print('Задание 18.5.4')
red = redis.Redis (
    host='redis-10199.c244.us-east-1-2.ec2.cloud.redislabs.com',
    port=10199,
    password='DtUlgltLQWkzQa8LhUKkw5V0VZUZLMG1'
)
contact = True

while contact:
    action = input ('action: wwrite/rread/ddelete/sshow/eexit(click here):\t')
    if action == 'll':

       print(red.keys())

    if action == 'ww':
        name = input ('name:\t')
        phone = input ('phone:\t')
        red.set (name, phone)
        # red.hmset('red', name)
    elif action == 'rr':
        name = input ('name:\t')
        phone = red.get (name)
        if phone:
            print (f'{name}\'s phone is {str (phone)}')
    elif action == 'dd':
        name = input ('name:\t')
        phone = red.delete (name)
        if phone:
            print (f"{name}'s phone is deleted")
        else:
            print (f"Not found {name}")
    elif action == 'ee':
        break