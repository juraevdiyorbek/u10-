class Countries:
    def __init__(self,name,capital,population,square) -> None:
        self.name = name
        self.capital = capital
        self.population = population
        self.square = square

    def get_info(self):
        return f"""Nmae: {self.name}
Capital: {self.capital}
Population : {self.population}
Square : {self.square}"""
    def set_info(self,name,capital,population,square):
        self.n= name
        self.c = capital
        self.p = population
        self.s = square
        return self.n,self.c,self.p,self.s
    
country = Countries("Uzbekistan","Tashkent","36mln","448.9.kv.km")

my_dict = dict()
lst = list()
for i in range(10):
    name = input("Name : ")
    capital = input("Capital : ")
    population = input("Population : ")
    square = input("Square : ")
    my_dict[i] = country.set_info(name,capital,population,square)
    lst.append(my_dict[i])

lst.sort(key=lambda x : x[0])

print(lst)