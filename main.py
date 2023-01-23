from user_agent import generate_user_agent
from telebot import types
import telebot
import requests
import random
import os
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)
token = os.environ.get("TOKEN")
bot = telebot.TeleBot(token)


dev = int(os.environ.get("ID"))
username = os.environ.get("USERNAME")


def check(username):
    url = "https://t.me/"+str(username)
    headers = {
        "User-Agent": generate_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

    response = requests.get(url, headers=headers)
    if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
        return "av"
    else:
        return "not"


def delete_text(file_name, text_to_delete):
    with open(file_name, 'r') as f:
        old_text = f.read()
        old_text = old_text.split(" ")
    with open(file_name, 'w') as f:
        new_text = ""
        old_text.remove(text_to_delete)
        new_text = " ".join(old_text)
        f.write(new_text)


@bot.message_handler(commands=['start'])
def start(message):
    with open("users.txt", "r") as f:
        users = str(f.read())
    if str(message.from_user.id) in users:
        mas = types.InlineKeyboardMarkup(row_width=2)
        A = types.InlineKeyboardButton(text="BFLLL", callback_data="F1")
        B = types.InlineKeyboardButton(
            text="BFFF2", callback_data="F2")
        C = types.InlineKeyboardButton(text="BF1BOT", callback_data="F3")
        D = types.InlineKeyboardButton(text="BBLLL", callback_data="F4")
        E = types.InlineKeyboardButton(text="B_F_L", callback_data="F5")
        F = types.InlineKeyboardButton(text="BFLLL", callback_data="F6")
        Dev = types.InlineKeyboardButton('Dev', url='https://t.me/dar4k')

        mas.add(A, B, C, D, E, F, Dev)

        bot.send_message(message.chat.id, f'''
    𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗼𝘁
        𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝘂𝘀𝗲𝗿 𝗰𝗵𝗲𝗰𝗸𝗲𝗿
        𝘽𝙮 : @dar4k
        ''', reply_markup=mas)
    elif message.from_user.id == dev:
        bot.send_message(message.chat.id, '''
هلا بلمطور
اذا تريد تضيف عضو ارسل : 
/add ايدي العضو
اذا تريد تحذف عضو ارسل : 
/remove ايدي العضو
ارسل /id علمود تاخذ ايديك
ارسل /users علمود تشوف الاعضاء الي ضايفهم
''')
        mas = types.InlineKeyboardMarkup(row_width=2)
        A = types.InlineKeyboardButton(text="BFLLL", callback_data="F1")
        B = types.InlineKeyboardButton(
            text="BFFF2", callback_data="F2")
        C = types.InlineKeyboardButton(text="BF1BOT", callback_data="F3")
        D = types.InlineKeyboardButton(text="BBLLL", callback_data="F4")
        E = types.InlineKeyboardButton(text="B_F_L", callback_data="F5")
        F = types.InlineKeyboardButton(text="BFLLL", callback_data="F6")
        Dev = types.InlineKeyboardButton('Dev', url='https://t.me/dar4k')

        mas.add(A, B, C, D, E, F, Dev)

        bot.send_message(message.chat.id, f'''
    𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗯𝗼𝘁
        𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝘂𝘀𝗲𝗿 𝗰𝗵𝗲𝗰𝗸𝗲𝗿
        𝘽𝙮 : @dar4k
        ''', reply_markup=mas)
    else:
        bot.send_message(
            message.chat.id, f"حبيبي انت ممشترك بلبوت , روح للمطور {username}")


@bot.message_handler(commands=['add'])
def add(message):
    if message.from_user.id == dev:
        user_id = message.text.replace("/add ", "")
        if user_id == '/add':
            bot.send_message(
                message.chat.id, "حبيبي ضيف عدل , مثال : \n /add 1403347605")
        else:
            with open("users.txt", "a") as f:
                f.write(f" {user_id}")
            bot.send_message(
                message.chat.id, "تم اضافة العضو بنجاح")
    else:
        bot.send_message(message.chat.id, "ولك دي انت مو المطور")


@bot.message_handler(commands=['users'])
def users(message):
    if message.from_user.id == dev:
        with open("users.txt", "r") as f:
            users = f.read()
        bot.send_message(
            message.chat.id, f"الاعضاء : \n {users}")
    else:
        bot.send_message(message.chat.id, "ولك دي انت مو المطور")


@bot.message_handler(commands=['remove'])
def remove(message):
    if message.from_user.id == dev:
        try:
            user_id = message.text.replace("/remove ", "")
            if user_id == '/reomve':
                bot.send_message(
                    message.chat.id, "حبيبي احذف عدل , مثال : \n /remove 1403347605")
            else:
                delete_text("users.txt", user_id)
                bot.send_message(
                    message.chat.id, "تم حذف العضو بنجاح")
        except:
            bot.send_message(
                message.chat.id, "خطأ")
    else:
        bot.send_message(message.chat.id, "ولك دي انت مو المطور")


@bot.message_handler(commands=['id'])
def id(message):
    bot.send_message(
        message.chat.id, f"ايديك : `{message.from_user.id}`", parse_mode="MARKDOWN")


@bot.callback_query_handler(func=lambda call: True)
def main(call):

    if call.data == "F1":
        xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xm = "0987654321MNBVCXZLKJHGFDSAPOIUYTREWQ"
        ok = 0
        cp = 0
        sk = 0
        for i in range(400):
            letter1 = str(''.join(random.choice(xu)for i in range(1)))
            letter2 = str(''.join(random.choice(xn)for i in range(1)))
            letter3 = str(''.join(random.choice(xa)for i in range(1)))
            num1 = str(''.join(random.choice(xm)for i in range(1)))
            username = ""
            username = letter1+num1+letter2+letter2+letter2
            isav = async_result = pool.apply_async(check, (username,))
            isav = async_result.get()
            if 'av' in isav:
                ok += 1
                sk += 1
                bot.send_message(call.message.chat.id, f'''
	𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 :
		@{username}
 Click to copy : `{username}`
 𝘽𝙔 : @dar4k
				''', parse_mode="markdown")
            else:
                cp += 1
                sk += 1
                mas = types.InlineKeyboardMarkup(row_width=2)
                A = types.InlineKeyboardButton(
                    f'GOOD : {ok}', callback_data="1x")
                E = types.InlineKeyboardButton(
                    f'EROR : {cp}', callback_data="1x")
                B = types.InlineKeyboardButton(
                    f'{username}', callback_data="1x")
                R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
                M = types.InlineKeyboardButton(
                    'المطور', url='https://t.me/dar4k')
                mas.add(A, E, B, R, M)
                bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id, text="ok start", reply_markup=mas)
        bot.send_message(call.message.chat.id, f'''𝗕𝗼𝘁 𝘀𝘁𝗼𝗽𝗲𝗱
	𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗮𝗴𝗮𝗶𝗻 𝘁𝘆𝗽𝗲 /start''')

    if call.data == "F2":
        xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xm = "0987654321MNBVCXZLKJHGFDSAPOIUYTREWQ"
        ok = 0
        cp = 0
        sk = 0
        for i in range(400):
            letter1 = str(''.join(random.choice(xu)for i in range(1)))
            letter2 = str(''.join(random.choice(xn)for i in range(1)))
            letter3 = str(''.join(random.choice(xa)for i in range(1)))
            num1 = str(''.join(random.choice(xm)for i in range(1)))
            username = ""
            username = letter1+letter2+letter2+letter2+num1
            async_result = pool.apply_async(check, (username,))
            isav = async_result.get()
            if 'av' in isav:
                ok += 1
                sk += 1
                bot.send_message(call.message.chat.id, f'''
	𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 :
		@{username}
 Click to copy : `{username}`
 𝘽𝙔 : @dar4k
				''', parse_mode="markdown")
            else:
                cp += 1
                sk += 1
                mas = types.InlineKeyboardMarkup(row_width=2)
                A = types.InlineKeyboardButton(
                    f'GOOD : {ok}', callback_data="1x")
                E = types.InlineKeyboardButton(
                    f'EROR : {cp}', callback_data="1x")
                B = types.InlineKeyboardButton(
                    f'{username}', callback_data="1x")
                R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
                M = types.InlineKeyboardButton(
                    'المطور', url='https://t.me/dar4k')
                mas.add(A, E, B, R, M)
                bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id, text="ok start", reply_markup=mas)
        bot.send_message(call.message.chat.id, f'''𝗕𝗼𝘁 𝘀𝘁𝗼𝗽𝗲𝗱
	𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗮𝗴𝗮𝗶𝗻 𝘁𝘆𝗽𝗲 /start''')

    if call.data == "F3":
        xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xm = "0987654321MNBVCXZLKJHGFDSAPOIUYTREWQ"
        ok = 0
        cp = 0
        sk = 0
        for i in range(400):
            letter1 = str(''.join(random.choice(xu)for i in range(1)))
            letter2 = str(''.join(random.choice(xn)for i in range(1)))
            letter3 = str(''.join(random.choice(xa)for i in range(1)))
            num1 = str(''.join(random.choice(xm)for i in range(1)))
            num2 = str(''.join(random.choice(xm)for i in range(1)))
            username = ""
            username = letter1+num1+num2+"BOT"
            async_result = pool.apply_async(check, (username,))
            isav = async_result.get()
            if 'av' in isav:
                ok += 1
                sk += 1
                bot.send_message(call.message.chat.id, f'''
	𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 :
		@{username}
 Click to copy : `{username}`
 𝘽𝙔 : @dar4k
				''', parse_mode="markdown")
            else:
                cp += 1
                sk += 1
                mas = types.InlineKeyboardMarkup(row_width=2)
                A = types.InlineKeyboardButton(
                    f'GOOD : {ok}', callback_data="1x")
                E = types.InlineKeyboardButton(
                    f'EROR : {cp}', callback_data="1x")
                B = types.InlineKeyboardButton(
                    f'{username}', callback_data="1x")
                R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
                M = types.InlineKeyboardButton(
                    'المطور', url='https://t.me/dar4k')
                mas.add(A, E, B, R, M)
                bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id, text="ok start", reply_markup=mas)
        bot.send_message(call.message.chat.id, f'''𝗕𝗼𝘁 𝘀𝘁𝗼𝗽𝗲𝗱
	𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗮𝗴𝗮𝗶𝗻 𝘁𝘆𝗽𝗲 /start''')

    if call.data == "F4":
        xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xm = "0987654321MNBVCXZLKJHGFDSAPOIUYTREWQ"
        ok = 0
        cp = 0
        sk = 0
        for i in range(400):
            letter1 = str(''.join(random.choice(xu)for i in range(1)))
            letter2 = str(''.join(random.choice(xn)for i in range(1)))
            letter3 = str(''.join(random.choice(xa)for i in range(1)))
            num1 = str(''.join(random.choice(xm)for i in range(1)))
            num2 = str(''.join(random.choice(xm)for i in range(1)))
            username = ""
            username = letter1+letter1+num1+num1+num1
            async_result = pool.apply_async(check, (username,))
            isav = async_result.get()
            if 'av' in isav:
                ok += 1
                sk += 1
                bot.send_message(call.message.chat.id, f'''
	𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 :
		@{username}
 Click to copy : `{username}`
 𝘽𝙔 : @dar4k
				''', parse_mode="markdown")
            else:
                cp += 1
                sk += 1
                mas = types.InlineKeyboardMarkup(row_width=2)
                A = types.InlineKeyboardButton(
                    f'GOOD : {ok}', callback_data="1x")
                E = types.InlineKeyboardButton(
                    f'EROR : {cp}', callback_data="1x")
                B = types.InlineKeyboardButton(
                    f'{username}', callback_data="1x")
                R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
                M = types.InlineKeyboardButton(
                    'المطور', url='https://t.me/dar4k')
                mas.add(A, E, B, R, M)
                bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id, text="ok start", reply_markup=mas)
        # Bot stop msg
        bot.send_message(call.message.chat.id, f'''𝗕𝗼𝘁 𝘀𝘁𝗼𝗽𝗲𝗱
	𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗮𝗴𝗮𝗶𝗻 𝘁𝘆𝗽𝗲 /start''')

    if call.data == "F5":
        xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xm = "0987654321MNBVCXZLKJHGFDSAPOIUYTREWQ"
        ok = 0
        cp = 0
        sk = 0
        for i in range(400):
            letter1 = str(''.join(random.choice(xu)for i in range(1)))
            letter2 = str(''.join(random.choice(xn)for i in range(1)))
            letter3 = str(''.join(random.choice(xa)for i in range(1)))
            num1 = str(''.join(random.choice(xm)for i in range(1)))
            username = ""
            username = letter1+"_"+letter2+"_"+letter3
            async_result = pool.apply_async(check, (username,))
            isav = async_result.get()
            if 'av' in isav:
                ok += 1
                sk += 1
                bot.send_message(call.message.chat.id, f'''
	𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 :
		@{username} 
 Click to copy : `{username}`
 𝘽𝙔 : @dar4k
				''', parse_mode="markdown")
            else:
                cp += 1
                sk += 1
                mas = types.InlineKeyboardMarkup(row_width=2)
                A = types.InlineKeyboardButton(
                    f'GOOD : {ok}', callback_data="1x")
                E = types.InlineKeyboardButton(
                    f'EROR : {cp}', callback_data="1x")
                B = types.InlineKeyboardButton(
                    f'{username}', callback_data="1x")
                R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
                M = types.InlineKeyboardButton(
                    'المطور', url='https://t.me/dar4k')
                mas.add(A, E, B, R, M)
                bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id, text="ok start", reply_markup=mas)
        bot.send_message(call.message.chat.id, f'''𝗕𝗼𝘁 𝘀𝘁𝗼𝗽𝗲𝗱  
	𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗮𝗴𝗮𝗶𝗻 𝘁𝘆𝗽𝗲 /start''')

    if call.data == "F6":
        xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
        xm = "0987654321MNBVCXZLKJHGFDSAPOIUYTREWQ"
        ok = 0
        cp = 0
        sk = 0
        for i in range(400):
            letter1 = str(''.join(random.choice(xu)for i in range(1)))
            letter2 = str(''.join(random.choice(xn)for i in range(1)))
            letter3 = str(''.join(random.choice(xa)for i in range(1)))
            num1 = str(''.join(random.choice(xm)for i in range(1)))
            num2 = str(''.join(random.choice(xm)for i in range(1)))
            username = ""
            f = [letter1, letter2, num1, num1, num1]
            random.shuffle(f)
            username = "".join(f)
            async_result = pool.apply_async(check, (username,))
            isav = async_result.get()
            if 'av' in isav:
                ok += 1
                sk += 1
                bot.send_message(call.message.chat.id, f'''
	𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 :
		@{username} 
 Click to copy : `{username}`
 𝘽𝙔 : @dar4k
				''', parse_mode="markdown")
            else:
                cp += 1
                sk += 1
                mas = types.InlineKeyboardMarkup(row_width=2)
                A = types.InlineKeyboardButton(
                    f'GOOD : {ok}', callback_data="1x")
                E = types.InlineKeyboardButton(
                    f'EROR : {cp}', callback_data="1x")
                B = types.InlineKeyboardButton(
                    f'{username}', callback_data="1x")
                R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
                M = types.InlineKeyboardButton(
                    'المطور', url='https://t.me/dar4k')
                mas.add(A, E, B, R, M)
                bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id, text="ok start", reply_markup=mas)
        bot.send_message(call.message.chat.id, f'''𝗕𝗼𝘁 𝘀𝘁𝗼𝗽𝗲𝗱  
	𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗮𝗴𝗮𝗶𝗻 𝘁𝘆𝗽𝗲 /start''')


bot.infinity_polling()
