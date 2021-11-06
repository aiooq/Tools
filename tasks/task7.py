'''7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
    При вызове функции должен создаваться объект-генератор. 
    Функция должна вызываться следующим образом: for el in fact(n). 
    Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
    Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.'''

from itertools import count
class Main:
    def __call__(self):
        config = (({"in":"Введите целое число n, чтобы получить факториал n: ", "def":self.FuncMain, "type":int}))
        return config

    def fact(self, n):
        result=1
        for i in range(1,n+1):
            result*=i
            yield result

    def FuncMain(self, value, out):
        c = count(1)
        for el in self.fact(value):
            print("{0}! = {1}".format(next(c),el))