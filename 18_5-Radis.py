import redis  # импортируем библиотеку
print ('подключаемся к redis и записывам значения (на латинице)')
red = redis.Redis (
    host='redis-10199.c244.us-east-1-2.ec2.cloud.redislabs.com',
    # ваш хост, если вы поставили Redis к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
    port=10199,
    # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт всегд разный, по этому его надо копировать оттуда же, что и host.
    password='DtUlgltLQWkzQa8LhUKkw5V0VZUZLMG1'
    # для локальной машины пароль не требуется (если вы устанавливали Redis к себе на компьютер и не пользовались облачным сервисом из скринкаста выше). Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password.
)
red.set('var1', 'Write(latin) in cash value1') # записываем в кеш строку "value1"
# print(red.get()) # считываем из кэша данные

red = redis.Redis (
    host='redis-10199.c244.us-east-1-2.ec2.cloud.redislabs.com',
    port=10199,
    password='DtUlgltLQWkzQa8LhUKkw5V0VZUZLMG1'
)
print ('считываем из кэша данные')
print (red.get('var1'))


print ('Создаём словари с ключами и значениями')
import json  # Наш старый друг Джейсон заглянул на огонёк!
red = redis.Redis (
    host='redis-10199.c244.us-east-1-2.ec2.cloud.redislabs.com',
    port=10199,
    password='DtUlgltLQWkzQa8LhUKkw5V0VZUZLMG1'
)

dict1 = {'num1': 'value1_1', 'num2': 'value2_2'}  # создаём словарь для записи
red.set ('dict1', json.dumps (dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads (
    red.get ('dict1'))  # с помощью знакомой нам функции превращаем данные полученные из кэша обратно в словарь
print (red.get ('dict1'))
print (type (converted_dict))  # убеждаемся, что получили действительно словарь
print (converted_dict)  # ну и выводим его содержание

print ('Учимся удалять')
red = redis.Redis (
    host='redis-10199.c244.us-east-1-2.ec2.cloud.redislabs.com',
    port=10199,
    password='DtUlgltLQWkzQa8LhUKkw5V0VZUZLMG1'
)
red.delete('dict1') # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))

print('Задание 18.5.4')
red = redis.Redis (
    host='redis-10199.c244.us-east-1-2.ec2.cloud.redislabs.com',
    port=10199,
    password='DtUlgltLQWkzQa8LhUKkw5V0VZUZLMG1'
)
contact = True

while contact:
    action = input ('action: wwrite/rread/ddelete/llok/eexit(click here):\t')
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