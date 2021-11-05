'''5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
    В список должны войти четные числа от 100 до 1000 (включая границы). 
    Необходимо получить результат вычисления произведения всех элементов списка.
    Подсказка: использовать функцию reduce().'''

from functools import reduce    
class Main:

    def __init__(self):
        self.list_gen=[i for i in range(100,1001,2)]

    def __call__(self):
        config = (({"out":"Результат = {0}", "def":self.FuncMain}))
        return config

    def FuncMul(self, x, y):
        return x*y

    def FuncMain(self, value, out):
        return out.format(reduce(self.FuncMul,self.list_gen))