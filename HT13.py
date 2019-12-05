import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType



def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-РєР»СЋС‡ СЃРѕР·РґР°РЅРЅС‹Р№ СЂР°РЅРµРµ
token = "e32d195135a7e4029798e1b35453eaa3264a4a4419eb79a96508b820c3782923c281e50439d1967552d63"

# РђРІС‚РѕСЂРёР·СѓРµРјСЃСЏ РєР°Рє СЃРѕРѕР±С‰РµСЃС‚РІРѕ
vk = vk_api.VkApi(token=token)

# Р Р°Р±РѕС‚Р° СЃ СЃРѕРѕР±С‰РµРЅРёСЏРјРё
longpoll = VkLongPoll(vk)

# Commander
#commander = Commander()

print("Р‘РѕС‚ Р·Р°РїСѓС‰РµРЅ")
# РћСЃРЅРѕРІРЅРѕР№ С†РёРєР»
for event in longpoll.listen():

    # Р•СЃР»Рё РїСЂРёС€Р»Рѕ РЅРѕРІРѕРµ СЃРѕРѕР±С‰РµРЅРёРµ
    if event.type == VkEventType.MESSAGE_NEW:

        # Р•СЃР»Рё РѕРЅРѕ РёРјРµРµС‚ РјРµС‚РєСѓ РґР»СЏ РјРµРЅСЏ( С‚Рѕ РµСЃС‚СЊ Р±РѕС‚Р°)
        if event.to_me:

            # РЎРѕРѕР±С‰РµРЅРёРµ РѕС‚ РїРѕР»СЊР·РѕРІР°С‚РµР»СЏ
            request = event.text

            # РљР°РјРµРЅРЅР°СЏ Р»РѕРіРёРєР° РѕС‚РІРµС‚Р°
            if request == "РїСЂРёРІРµС‚":
                write_msg(event.user_id, "РҐР°Р№")
            elif request == "РїРѕРєР°":
                write_msg(event.user_id, "РџРѕРєР°((")
            else:
                write_msg(event.user_id, "РќРµ РїРѕРЅСЏР»Р° РІР°С€РµРіРѕ РѕС‚РІРµС‚Р°...")