class Main:
    def __call__(self):

        config = (  ({"in":"Введите значение числителя: ", "def":self.FuncSetX, "type": {int,float}}),
                    ({"in":"Введите значение знаменателя: ", "out":"Результат = {0}", "def":self.FuncSetY, "type": {int,float}}))
        return config

    def FuncArgs(self, x,y):
        return x/y

    def FuncSetX(self, value, out):
        self.x = value

    def FuncSetY(self, value, out):
        if value==0:
            raise Exception("ValueIsNull")
        self.y = value
        return out.format(self.FuncArgs(self.x,self.y))
