class Main:
    def __call__(self, tasks):
        self.IsStopped = False
        # Основной цикл
        while not self.IsStopped:
            # Основная функция
            self.main(tasks)

            if self.IsStopped:
                break

            value = input("Введите 'yes' или 'y', чтобы повторить программу, а для выхода нажмите Enter: ")
            if value != 'y' and value != 'yes':
                break

        print("Завершение программы")

    def main(self, tuple):
        i=0
        while len(tuple)>i and not self.IsStopped:
            if not isinstance(tuple[i], dict):
                self.main(tuple[i])
                i+=1
                continue

            out = None
            value = None
            if "in" in tuple[i]:  
                if "out" in tuple[i]:
                    out = tuple[i]["out"]

                value = input(tuple[i]["in"])

                if "type" in tuple[i]:
                    try:
                        type_value=tuple[i]["type"]
                        if type(type_value)==type:
                            type_value={type_value}
                        
                        result = False
                        for item in type_value:
                            try:
                                if item == str:
                                    try:
                                        float(value)
                                        continue
                                    except ValueError:
                                        if value.isnumeric():
                                            continue

                                elif item == int:
                                    if not value.isnumeric():
                                        continue
                                value=item(value)
                                result = True
                                break
                            except:
                                continue

                        if not result:
                            raise Exception()
                    except:
                        print("Некорректное значение, ожидается {0}, пожалуйста повторите ввод!".format(tuple[i]["type"]))
                        continue
            elif "out" in tuple[i]:
                value = tuple[i]["out"]

            try:
                if "def" in tuple[i]:
                    value = tuple[i]["def"](value,out)
                if value != None:
                    print(value)
            except Exception as e:
                if e.args[0]=="PositiveNumber":
                    i-=1
                    print("Некорректное значение, ожидается положительное число, пожалуйста повторите ввод!")
                elif e.args[0]=="StrIsNotNumeric":
                    i-=1
                    print("Некорректное значение, ожидается число, пожалуйста повторите ввод!")
                elif e.args[0]=="StrFormatIsNotValid":
                    i-=1
                    print("Некорректный формат, пожалуйста смотрите пример и повторите ввод!")
                elif e.args[0]=="ValueOutOfRange":
                    i-=1
                    print("Значение вне диапазона, пожалуйста повторите ввод!") 
                elif e.args[0]=="ValueIsNull":
                    i-=1
                    print("Некорректное значение, оно не должно быть равно нулю, пожалуйста повторите ввод!") 
                elif e.args[0]=="ProgramStop":
                    self.IsStopped=True
                else:
                    print("Ошибка в конфигурации: "+e)               
                continue
            finally:
                i+=1        