'''3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
    Необходимо решить задание в одну строку.
    Подсказка: использовать функцию range() и генератор.'''
class Main:
    def __call__(self):
        config = (({"out":"Сумма двух наибольших аргументов = {0}", "def":self.FuncOut}))
        return config

    def FuncOut(self, value, out):
        return out.format(self.my_func(*[7,5,9]))

    def my_func(self, *args):
        return sum(sorted(args, reverse=True)[0:2])
