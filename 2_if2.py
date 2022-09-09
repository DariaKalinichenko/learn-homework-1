"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def compare_string(first_string, second_string):
      if isinstance(first_string, str) == False or isinstance(second_string, str) == False:
            return 0
      if first_string == second_string:
            return 1
      elif len(first_string) > len(second_string):
            return 2
      elif first_string != second_string and second_string == 'learn':
            return 3

def main():
    print(compare_string(1, 'hello'))  #0
    print(compare_string('hello', 'hello'))  #1
    print(compare_string('hellooooo', 'hello'))  #2
    print(compare_string('hello', 'learn'))  #3

    
if __name__ == "__main__":
    main()
