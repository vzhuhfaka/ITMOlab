import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.insert(0, parent_dir)

from lab7.utils import read_data, write_data


def money_exchange(money: int, coins: list):
    """
    :param money: сумма, которую нужно набрать
    :param coins: список доступных номиналов монет
    :return: Минимальное количество монет, необходимое для набора суммы money
    """
    MinNumCoins = [0] + [float('inf')] * money  # массив для хранения минимального количества монет для каждой суммы

    for m in range(1, money + 1):
        for coin in coins:  # проверяем каждую монету
            if m >= coin:  # если текущая сумма больше или равна номиналу монеты
                NumCoins = MinNumCoins[m - coin] + 1
                MinNumCoins[m] = min(NumCoins, MinNumCoins[m])

    return MinNumCoins[money]


def task1():
    PATH_INPUT = 'lab7/task1/txtf/input.txt'
    PATH_OUTPUT = 'lab7/task1/txtf/output.txt'

    origin_input = read_data(PATH_INPUT)

    data = read_data(PATH_INPUT)
    money_ = int(data[0].split()[0])
    coins_ = [int(i) for i in data[1].split()]

    result = money_exchange(money_, coins_)

    write_data(PATH_OUTPUT, str(result))
    print(origin_input)
    print(result)


if __name__ == "__main__":
    task1()
