import telegrambot
import Parser
import Database

data = Parser.parse()
Database.insert(data)
telegrambot.create_bot()
