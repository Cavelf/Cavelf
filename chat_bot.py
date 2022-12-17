import random
import config
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

#token = input('Token: ')
token = config #token_user

#vk = vk_api.VkApi(token=config)
vk = vk_api.VkApi(token=config.token_user)
longpoll = VkLongPoll(vk)

def write_msg(user_id, message):
#    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': randrange(10 ** 7),})
    vk.method('messages.send', {'chat_id': user_id, 'message': message,  'random_id': random.randint(0, 2048)})
#    vk.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, друг!', 'random_id': random.randint(0, 2048)})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text.lower()
            user_id = event.chat_id
            if request == 'привет':
                write_msg(user_id, 'Привет, друг!')
                write_msg(user_id, f'Хай, {user_id}')
            elif request == 'пока':
                write_msg(user_id, 'Пока((')
            else:
                write_msg(user_id, "Не поняла вашего ответа...")
        print('Текст сообщения: ' + str(request))
        print(user_id)

