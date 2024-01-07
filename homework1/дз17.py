# задание 1
class Car:
    def __init__(self):
        self.model = ""
        self.year = 0
        self.manufacturer = ""
        self.engine_capacity = 0.0
        self.color = ""
        self.price = 0.0

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price
    
    def print_data(self):
        print("модель:", self.model)
        print("год выпуска:", self.year)
        print("производитель:", self.manufacturer)
        print("ёмкость двигателя:", self.engine_capacity)
        print("цвет:", self.color)
        print("цена:", self.price)

car = Car()

car.set_model("Audi r8")
car.set_year(2021)
car.set_manufacturer("Audi")
car.set_engine_capacity(4.2)
car.set_color("чёрный")
car.set_price(11000000)

car.print_data()





# задание 2
class Book:
    def __init__(self):
        self.name = ""
        self.year = 0
        self.publisher = ""
        self.genre = ""
        self.author = ""
        self.price = 0

    def set_name(self, name):
        self.name = name

    def set_year(self, year):
        self.year = year

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_genre(self, genre):
        self.genre = genre

    def set_author(self, author):
        self.author = author

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price
    
    def print_data(self):
        print("название:", self.name)
        print("год выпуска:", self.year)
        print("издатель:", self.publisher)
        print("жанр:", self.genre)
        print("автор:", self.author)
        print("цена:", self.price)

book = Book()
book.set_name("Гарри Поттер")
book.set_year(2000)
book.set_publisher("хз")
book.set_genre("фэнтези")
book.set_author("Джоан  Роулинг")
book.set_price(1100)


book.print_data()







# задание 3
class Stadium:
    def __init__(self):
        self.name = ""
        self.year = 0
        self.country = ""
        self.city = ""
        self.capacity = ""

    def set_name(self, name):
        self.name = name

    def set_year(self, year):
        self.year = year

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def print_data(self):
        print("название:", self.name)
        print("год постройки:", self.year)
        print("страна:", self.country)
        print("город:", self.city)
        print("вместимость:", self.capacity)

stadium = Stadium()
stadium.set_name("Ростех Арена")
stadium.set_year(2018)
stadium.set_country("Россия")
stadium.set_city("Калининград")
stadium.set_capacity("")


stadium.print_data()



