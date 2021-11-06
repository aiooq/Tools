'''1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. 
    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.'''

from sys import argv
from include.main import Main as main
class Main:
    def __call__(self):

        config = (
            ({"out":"(выработка в часах * ставка в час) + премия, Результат = {0}", "def":self.FuncArgs}))
        return config

    def FuncArgs(self, value, out):
        try:
            hours=main.GetValueByType(argv[1], {int})
            if hours==None:
                raise Exception("Первая переменная (выработка в часах) не корректна, ожидается {0}".format({int}))

            bid_by_hour=main.GetValueByType(argv[2], {float,int})
            if bid_by_hour==None:
                raise Exception("Вторая переменная (ставка в час) не корректна, ожидается {0}".format({float,int}))

            prize=main.GetValueByType(argv[3], {float,int})
            if prize==None:
                raise Exception("Третья переменная (премия) не корректна, ожидается {0}".format({float,int}))                            

            result=hours*bid_by_hour+prize
        except Exception as error:
            print("Ошибка в инициализации: "+str(error))
            raise Exception("ProgramStop")  
        return out.format(result)
