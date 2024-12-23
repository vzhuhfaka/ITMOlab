# Задание №1 по варианту : `Обмен монет`

Студент ИТМО, Останин Андрей Сергеевич 466977

## Вариант 17

## Задание

Как мы уже поняли из лекции, не всегда "жадное" решение задачи на обмен
монет работает корректно для разных наборов номиналов монет. Например, если
доступны номиналы 1, 3 и 4, жадный алгоритм поменяет 6 центов, используя
три монеты (4 + 1 + 1), в то время как его можно изменить, используя всего две
монеты (3 + 3). Теперь ваша цель - применить динамическое программирование
для решения задачи про обмен монет для разных номиналов.

## Input / Output

| Input | Output |
|-------|--------|
| 34 3  | 9      | 
| 1 3 4 |        |

## Ограничения по времени и памяти

- Ограничение по времени. 1 сек.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/vzhuhfaka/AlgoritmLAB1.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd AlgoritmLAB1/lab7
   ```
3. Запустите программу:
   ```bash
   python task1/src/task1.py
   ```
4. Запуск тестов:
   ```bash
   pytest
   ```