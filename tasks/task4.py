'''4. Представлен список чисел. 
    Определить элементы списка, не имеющие повторений. 
    Сформировать итоговый массив чисел, соответствующих требованию. 
    Элементы вывести в порядке их следования в исходном списке. 
    Для выполнения задания обязательно использовать генератор.
    Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
    Результат: [23, 1, 3, 10, 4, 11]'''
class Main:
    def __call__(self):
        config = (
            ({"in":"Введите действительное положительное число x: ", "def":self.FuncSetX, "type":(float,int)}),
            ({"in":"Введите целое отрицательное число y: ", "def":self.FuncSetY, "type":int}),
            ({"out":"Первый способ результат = {0}", "def":self.FuncGetFirst}),
            ({"out":"Второй способ результат = {0}", "def":self.FuncGetSecond}))
        return config

    def FuncSetX(self, value, out):
        if value<=0:
            raise Exception("PositiveNumber")
        self.x = value

    def FuncSetY(self, value, out):
        if value>=0:
            raise Exception("NegativeNumber")
        self.y = value

    def FuncGetFirst(self, value, out):
        return self.FuncFirst(self.x, self.y)

    def FuncGetSecond(self, value, out):
        return self.FuncSecond(self.x, self.y)           

    def FuncFirst(self, x, y):
        return x ** y

    def FuncSecond(self, x, y):
        result = x
        i = abs(y)
        while i > 1:
            result*=x
            i-=1
        if y<0:
            return 1/result
        else:
            return result
