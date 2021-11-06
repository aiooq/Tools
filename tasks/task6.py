'''6. Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее.
    Подсказка: использовать функцию count() и cycle() модуля itertools. 
    Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
    Необходимо предусмотреть условие его завершения.
    Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
    Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.'''
from itertools import count,cycle
class Main:
    def __call__(self):
        config = (
            ({"def":self.FuncA}),
            ({"def":self.FuncB}))
        return config 

    def FuncA(self, value, out):
        c = count(3)
        i = next(c)
        while i<10:
            print (i,end=" ")
            i = next(c)
        print ("end FuncA")
        '''for i in c1:
            if i>=10:
                break
            print (i)'''

    def FuncB(self, value, out):
        c = cycle([4,8,15,16,23,42])
        count=0
        for i in c:
            if count >= 12:
                break
            print (i,end=" ")
            count+=1
        print ("end FuncB")