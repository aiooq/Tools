'''2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
    Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
    Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
    Результат: [12, 44, 4, 10, 78, 123].'''
class Main:
    def __call__(self):
        config = (({"out":"Данных о пользователе:: имя: {0}, фамилия: {1}, год рождения: {2}, город проживания: {3}, email: {4}, телефон: {5}", "def":self.FuncUser}))
        return config

    def FuncUser(self, value, out):
        self.FuncSetUser(
            fisrt_name="Иван", 
            second_name="Иванович", 
            year_of_birth=2000,
            сity_of_residence="Москва", 
            email="name@gmail.com", 
            phone_number=89991234567)

        return out.format(
            self.fisrt_name,
            self.second_name, 
            self.year_of_birth,
            self.сity_of_residence, 
            self.email, 
            self.phone_number)

    def FuncSetUser(self, fisrt_name, second_name, year_of_birth, сity_of_residence, email, phone_number):
        self.fisrt_name=fisrt_name
        self.second_name=second_name
        self.year_of_birth=year_of_birth
        self.сity_of_residence=сity_of_residence
        self.email=email
        self.phone_number=phone_number
