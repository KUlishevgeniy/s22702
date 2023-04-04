# import bot telebot bot
import logging
import aiohttp
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command, Text, or_f
from aiogram.types import Message
import mariadb
import aiofiles
import sys
from bs4 import BeautifulSoup
try:
    conn = mariadb.connect(
        user="",
        password="",
        host="",
        port=3306,
        database="labs"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
cur = conn.cursor()

# Bot token can be obtained via https://t.me/BotFahter
TOKEN = ""
# https://t.me/wireguard_make_cfg_bot
# All handlers should be attached to the Router (or Dispatcher)
router = Router()


def pretty(res):
    return


async def req(session, url, img=False):
    async with session.get(url, allow_redirects=False) as response:
        if response.status != 200:
            return False
        if img:
            return await response.content.read()
        else:
            return await response.text()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Здарова, <b>{message.from_user.full_name}!</b>")


@router.message(Text(contains="."))
async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward received message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker and etc.)
    """
    uname = message.text.replace('.', '_')
    cur.execute(
        "SELECT * FROM telebot WHERE number=?",
        (uname,))
    res = [i for i in cur]
    if not res:
        async with aiohttp.ClientSession() as session:
            url = f'http://exir.ru/other/savelev/resh/{uname}.htm'
            r = await req(session, url)
            if not r:
                await message.reply('Задача не найдена!')
                return
            soup = BeautifulSoup(r, 'html.parser')
            # ищем элемент с классом "abltop" и берем его 5-й дочерний элемент
            usl = soup.find(class_='abltop').text.split('<<')[0]
            while '\n\n' in usl:
                usl = usl.replace('\n\n', '\n')
            img = soup.find('img')['src']
            cur.execute(
                "INSERT IGNORE INTO telebot (number,usl,img) VALUES (?,?,?)",
                (uname, usl, img))
            conn.commit()
    else:
        uname, usl, img = res[0]
    await message.reply_photo(photo=f'http://exir.ru/other/savelev/resh/{img}', caption=f'Задача № {uname.replace("_",".")}{usl}'[0:1023])


async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

conn.close()
