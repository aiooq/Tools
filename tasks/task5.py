'''5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
    В список должны войти четные числа от 100 до 1000 (включая границы). 
    Необходимо получить результат вычисления произведения всех элементов списка.
    Подсказка: использовать функцию reduce().'''
class Main:

    def __init__(self):
        self.sum=0

    def __call__(self):
        config = (({"in":"Введите строку чисел, разделенных пробелом (или все кроме числа для выхода): ","out":"Сумма чисел = {0}", "def":self.FuncSum}))
        return config 

    def FuncSum(self, value, out):
        values=value.split(" ")

        for number in values:
            if number=="":
                continue

            try:
                number=float(number)
                self.sum+=number
            except:
                print(out.format(self.sum))
                self.sum=0
                return#raise Exception("ProgramStop")

        print(out.format(self.sum))
        raise Exception("Repeat")
