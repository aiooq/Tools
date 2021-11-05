'''3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
    Необходимо решить задание в одну строку.
    Подсказка: использовать функцию range() и генератор.'''
class Main:
    def __call__(self):
        config = (({"out":"Результат = {0}", "def":self.FuncOut}))
        return config

    def FuncOut(self, value, out):
        return out.format([i for i in range(20,240,1) if i % 20 == 0 or i % 21 == 0])