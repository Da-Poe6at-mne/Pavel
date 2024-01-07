# задание 1
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"радиус окружности изменился на {self.radius}"
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __ge__(self, other):
        return self.radius >= other.radius
    
    def __le__(self, other):
        return self.radius <= other.radius
    
    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(new_radius)
    
    def __sub__(self, other):
        new_radius = self.radius - other.radius
        return Circle(new_radius)
    
    def __iadd__(self, other):
        self.radius += other.radius
        return self
    
    def __isub__(self, other):
        self.radius -= other.radius
        return self
circle1 = Circle(50)
circle2 = Circle(30)

print(circle1 == circle2)  
print(circle1 > circle2)   
print(circle1 + circle2)  
print(circle1 - circle2)   

circle1 += circle2
print(circle1.radius)    
    
# задание 2

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other):
        real = (self.real * other.real) - (self.imaginary * other.imaginary)
        imaginary = (self.real * other.imaginary) + (self.imaginary * other.real)
        return Complex(real, imaginary)
    
    def __truediv__(self, other):
        denominator = (other.real ** 2) + (other.imaginary ** 2)
        real = ((self.real * other.real) + (self.imaginary * other.imaginary)) / denominator
        imaginary = ((self.imaginary * other.real) - (self.real * other.imaginary)) / denominator
        return Complex(real, imaginary)

c1 = Complex(1, 2)
c2 = Complex(3, 4)

sum = c1 + c2
print(sum.real, '+', sum.imaginary, 'i')

diff = c1 - c2
print(diff.real, '+', diff.imaginary, 'i')

product = c1 * c2
print(product.real, '+', product.imaginary, 'i')

quotient = c1 / c2
print(quotient.real, '+', quotient.imaginary, 'i')

# задание 3
class Airplane:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.current_passengers = 0
        
    def __eq__(self, other):
        return isinstance(other, Airplane) and self.max_passengers == other.max_passengers
    
    def __add__(self, other):
        if isinstance(other, int):
            self.current_passengers += other
            if self.current_passengers > self.max_passengers:
                self.current_passengers = self.max_passengers
        return self
    
    def __sub__(self, other):
        if isinstance(other, int):
            self.current_passengers -= other
            if self.current_passengers < 0:
                self.current_passengers = 0
        return self
    
    def __iadd__(self, other):
        return self.__add__(other)
    
    def __isub__(self, other):
        return self.__sub__(other)
    
    def __gt__(self, other):
        return isinstance(other, Airplane) and self.max_passengers > other.max_passengers
    
    def __lt__(self, other):
        return isinstance(other, Airplane) and self.max_passengers < other.max_passengers
    
    def __le__(self, other):
        return isinstance(other, Airplane) and self.max_passengers <= other.max_passengers
    
    def __ge__(self, other):
        return isinstance(other, Airplane) and self.max_passengers >= other.max_passengers
airplane1 = Airplane(200)
airplane2 = Airplane(150)

print(airplane1 == airplane2)

airplane1 += 201
print(airplane1.current_passengers)

airplane2 -= 20
print(airplane2.current_passengers)

print(airplane1 > airplane2)
print(airplane1 <= airplane2)
'''
# задание 4
class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price
flat1 = Flat(70, 1000000)
flat2 = Flat(90, 1200000)

print(flat1 == flat2)  
print(flat1 != flat2)  
print(flat1 > flat2)   
print(flat1 < flat2)  
print(flat1 <= flat2) 
print(flat1 >= flat2)










