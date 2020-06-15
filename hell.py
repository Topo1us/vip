import vk_api
import os
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from random import randint
import time
os.system('ifconfig >>io.txt')
i=open('io.txt')
IP=i.read()
def bot_vk():
    x=128711
    def categories():
        y=716237
        def lol(user_id,message):
            vk.method('messages.send',{'user_id': user_id, 'message': message,'random_id':y})
        token='35a0b1e44117b4857a36a347b3b1c948b260b314bf7edb44494165442202ea6ff5049d5ea3225d8c90199'
        vk=vk_api.VkApi(token=token)
        longpoll=VkLongPoll(vk)
#        lol(event.user_id,'Termux_Cod/Menu/Cotigories\n\nвыход - exit\n\n')
        for event in longpoll.listen():
            if event.type==VkEventType.MESSAGE_NEW:
                y+=1
                if event.to_me:
                    msg=event.text
                    id_lol='https://m.vk.com/id'+str(event.user_id)+''
                    print(event.user_id,msg,id_lol)
                    if msg=='Показ' or msg=='top':
                        lol(event.user_id,'Termux_Cod/Menu/Cotigories\n\nвыход - exit\n\n')
                    if msg=='exit' or 'e':
                        bot_vk()
                    else:
                        lol(event.user_id,'не понимаю')

    def y(user_id,message):
    
        vk.method('messages.send',{'user_id': user_id, 'message': message,'random_id':x})

    token='35a0b1e44117b4857a36a347b3b1c948b260b314bf7edb44494165442202ea6ff5049d5ea3225d8c90199'
    vk=vk_api.VkApi(token=token)
    longpoll=VkLongPoll(vk)
    for event in longpoll.listen():
        if event.type==VkEventType.MESSAGE_NEW:
            x+=1
            if event.to_me:
                r=event.text
                id_lol='https://m.vk.com/id'+str(event.user_id)+''
                print(r,id_lol)
                if r=='ip' or r=='1':
                    y(event.user_id,IP)
#ПРИВЕТСТВИЕ
                if r=='Привет' or r=='привет' or r=='Хай' or r=='хай':
                    y(event.user_id,'Привет, я бот Termux Cod.\n \nНапиши menu.')

                
#МЕНЮ
                if r=='Menu' or r=='menu' or r=='Меню' or r=='меню' or r=='Termux_Cod/Menu':
                    y(event.user_id,'Termux_Cod/Menu\n\n1. Категории.\n2. Правила.\n3. Информация.\n4. Помощь администрации.')

#КАТЕГОРИИ
                if r=='1' or r=='Категории' or r=='категории' or r=='Termux_Cod/Menu/Cotigories':
#                    categories()
                    y(event.user_id,'Жмякай показ')
                    categories()
#                if r=='fish' or r=='Fish':
#                    y(event.user_id,'лол типо статья о фишинге')
#                if r=='exploit' or r=='Exploit':
#                    y(event.user_id,'а это об уязвимостях')
#ПРАВИЛА
                if r=='2' or r=='Правила' or r=='правила' or r=='Termux_Cod/Menu/Cotigories':
                    y(event.user_id,'Termux_Cod/Menu/Rules\n\nПравила пока не зарегистрированы.')
#ИНФОРМАЦИЯ
                if r=='3' or r=='Информация'or r=='информация' or r=='Termux_Cod/Menu/Info':
                    y(event.user_id,'Termux_Cod/Menu/Info\n\nBot Termux Cod создан для автоматизации сообщества.\n\nВесь ресурс подготовлен и изложен для изучения в области IT.\n\nЗа ваши провокационные поступки, ответственности не несем!')
#ПОМОЩЬ АДМИНИСТРАЦИИ
                if r=='4' or r=='Помощь администрации' or r=='помощь администрации' or r=='помощь' or r=='Termux_Cod/Menu/Help_Adm':
                    y(event.user_id,'Termux_Cod/Menu/Help_Adm\n\nКаждый ваш лайк помогает нам быть лучше.')
                if r=='Проблема' or r=='проблема' or r=='Проблемс' or r=='Ошибка':
                    y(event.user_id,'Если есть проблемы то обратитесь в тех.поддержу.\nhttps://m.vk.com/id437306907\nhttps://m.vk.com/id596372809')
                if r=='ошибка' or r=='sss':
                    p9p()
                    
                if r=='Кто я?' or r=='кто я?' or r=='Кто я' or r=='кто я':
                    if event.user_id==437306907 or event.user_id==596372809:
                        y(event.user_id,'Вы администратор группы.')
                    else:
                        y(event.user_id,'Вы не идентифицированы.')


                
                if r=='Пока' or r=='пока':
                    y(event.user_id,'Да и хуй с тобой\n\n(:позже изменю:)')
                if r=='my id':
                    y(event.user_id,id_lol)

                
                if r=='lol6cod':
                    break
bot_vk()
