# Задание №1 по варианту : `Множество`

Студент ИТМО, Останин Андрей Сергеевич 466977

## Вариант 17

## Задание

Реализуйте множество с операциями «добавление ключа», «удаление ключа»,
«проверка существования ключа».

– A x – добавить элемент x в множество. Если элемент уже есть в множестве, то ничего делать не надо.

– D x – удалить элемент x. Если элемента x нет, то ничего делать не
надо.

– ? x – если ключ x есть в множестве, выведите «Y», если нет, то выведите
«N».

## Input / Output

| Input | Output |
|-------|--------|
| 8     | Y      | 
| A 2   | N      |
| A 5   | N      |
| A 3   |        |
| ? 2   |        |
| ? 4   |        |
| A 2   |        |
| D 2   |        |
| ? 2   |        |

## Ограничения по времени и памяти

- Ограничение по времени. 2 сек.
- Ограничение по памяти. 256 мб.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/vzhuhfaka/AlgoritmLAB1.git
   ```
2. Перейдите в папку с проектом:
   ```bash
   cd AlgoritmLAB1/lab6
   ```
3. Запустите программу:
   ```bash
   python task1/src/task1.py
   ```
4. Запуск тестов:
   ```bash
   pytest
   ```
