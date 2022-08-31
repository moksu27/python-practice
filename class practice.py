import math

class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        if self.img >=0:
            return '{} + {}j'.format(self.real, self.img)
        elif self.img <0:
            return '{} - {}j'.format(self.real, abs(self.img))

    def __add__(self,cn):
        return ComplexNumber(self.real+ cn.real, self.img + cn.img)

    def __sub__(self,cn):
        return ComplexNumber(self.real-cn.real, self.img - cn.img)

    def __mul__(self, cn):
        if type(cn) == int:
            return ComplexNumber(self.real*cn, self.img *cn)
        elif type(cn) == ComplexNumber:
            return ComplexNumber(self.real * cn.real - self.img * cn.img , self.real * cn.img + self.img *cn.real)
            #(a+bj) * (c+dj) = (ac-bd) + (ad+bc)j

    def __eq__(self, cn):
        return self.real == cn.real and self.img == cn.img

    def __ne__(self, cn):
        return not(self.real == cn.real and self.img == cn.img)

    def __abs__(self):
        return math.sqrt(self.real **2 + self.img **2)

    def __len__(self):
        return self.real**2 + self.img**2
a = ComplexNumber(1,2)
b = ComplexNumber(3,5)


print(a-b)
print(a+b)
print(a*b)
print(a==b)
print(len(a))