# 1. Checking String is containing the Digits, Uppercase , lower case, Alpha Numeric , Alphabets
data = 'aA'
upper_status = any(char.isupper() for char in data)  # False if data.islower() else True
lower_status = any(char.islower() for char in data)  # False if data.isupper() else True
digits_status = any(char.isdigit() for char in data)
alphabet_status = True if upper_status or lower_status else False
alpha_numeric_status = True if alphabet_status and digits_status else False
print("Uppercase status: ", upper_status)
print("Lowercase status: ", lower_status)
print("Digits Status: ", digits_status)
print("Alpha Numeric Status: ", alpha_numeric_status)
print("Alphabet Status: ", alphabet_status)


# 2. Number Division
num1 = int(input())
num2 = int(input())

try:
    result = num1//num2
    print('Result: ', result)
except ZeroDivisionError as ex:
    print("Zero Division Error", ex)

# 3. Complex Number Operations


class ComplexNumber:
    def __init__(self, real, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def addition(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def subtraction(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def multiplication(self, other):
        return ComplexNumber(self.real*other.real - self.imaginary*other.imaginary, self.imaginary*other.real + self.real*other.imaginary)

    def display(self):
        return '(%g, %g)' % (self.real, self.imaginary)

    def division(self, other):
        num1_real, num1_img, num2_real, num2_img = self.real, self.imaginary, other.real, other.imaginary
        r = float(num2_real**2 + num2_img**2)
        return ComplexNumber((num1_real*num2_real+num1_img*num2_img)/r, (num1_img*num2_real-num1_real*num2_img)/r)


print('Started')
obj1 = ComplexNumber(3, 5)
obj2 = ComplexNumber(2, 4)
obj3 = obj1.multiplication(obj2)
print(obj3.display())
