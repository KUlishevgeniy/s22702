import Bot
import Parser
import DBOperator


def main():
    answer = ""
    while (answer != "y") and (answer != "n"):
        answer = input("Do you want to parse data? (Y/N) \n").lower()
    if answer == "y":
        while answer != "0":
            answer = input("What do you want to parse? Games(G), Films(F), or exit(0) \n").lower()
            if answer == "g":
                data = Parser.kanobu_parse()
                DBOperator.insert_games(data)
            elif answer == "f":
                data = Parser.kinopoisk_parse()
                DBOperator.insert_films(data)
            else:
                pass

    Bot.load()


main()
