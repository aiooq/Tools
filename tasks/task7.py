'''7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
    При вызове функции должен создаваться объект-генератор. 
    Функция должна вызываться следующим образом: for el in fact(n). 
    Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
    Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.'''
class Main:
    def __call__(self):
        config = (({"in":"Введите слова из маленьких латинских букв, разделенных пробелом: ","out":"Результат = {0}", "def":self.FuncResult}))
        return config 

    # Используем стандартную функцию для установки заглавной буквы в слове
    def int_func_first(self, text):
        return text.capitalize()

    # Используем собственную реализацию для установки заглавной буквы в слове
    def int_func_second(self, text):
        length = len(text)
        if length<=0 or not text[0:1].isalpha():
            return text
        return text[0:1].upper()+text[1:length]

    # Используем стандартную функцию для установки заглавной буквы во всех словах в переданной строке (по сути почти вся наша программа)
    def int_func_third(self, text):
        return text.title()

    def FuncResult(self, value, out):
        words = value.split(" ")
        result = ""
        for word in words:
            result += self.int_func_first(word) + " "
        return out.format(result)
