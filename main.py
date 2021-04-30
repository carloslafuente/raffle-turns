import datetime
import random


devs_list = []
available_devs = []


def raffle_turns():
    init_date = datetime.datetime(2021, 5, 7)
    next_date = init_date
    result = ''
    weeks_to_raffle = round(52 / len(devs_list))
    for time in range(weeks_to_raffle):
        available_devs = list(devs_list)
        for raffle in range(len(available_devs)):
            dev = getRandomDev(available_devs)
            next_date = next_date + datetime.timedelta(days=7)
            result = result + f'{dev} -> {next_date.strftime("%d/%m/%Y")} \n'
    saveTurns(result)


def getRandomDev(temp_list):
    temp_dev = temp_list.pop(random.randrange(0, len(temp_list)))
    return temp_dev


def saveTurns(devs_turns):
    with open("turns.txt", "a+") as turns:
        turns.write(devs_turns)


def readDevs():
    with open('devs.txt', 'r') as devs_list_file:
        global devs_list
        devs_list = devs_list_file.read().splitlines()
        raffle_turns()


if(__name__ == '__main__'):
    readDevs()