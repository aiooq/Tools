'''2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
    Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
    Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
    Результат: [12, 44, 4, 10, 78, 123].'''
class Main:
    def __init__(self):
        self.list_orig = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

    def __call__(self):
        config = (({"out":"Результат: {0}", "def":self.FuncMain}))
        return config

    def FuncGen(self):
        for i in range(1,len(self.list_orig),1):
            if self.list_orig[i-1]<self.list_orig[i]:
                yield self.list_orig[i]

    def FuncMain(self, value, out):
        list_new=list()
        for i in self.FuncGen():
            list_new.append(i)
        return out.format(list_new)
