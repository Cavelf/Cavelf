import random
import config
#from config import token_user
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk = vk_api.VkApi(token=config.token_user)
#vk = vk_api.VkApi(token=token_user)
longpoll = VkLongPoll(vk)

print('работа бота')

def write_msg(user_id, message):
    vk.method('messages.send', {'chat_id': user_id, 'message': message, 'random_id': 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text.lower()
            user_id = event.chat_id
            if request == 'привет':
                write_msg(user_id, 'Привет, друг!')

###########