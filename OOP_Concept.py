class Country:    
    def __init__(self, cname, population):
        self.name = cname
        self.population = population
    
    def __del__(self):
        print("DELETED : ", self.cname)

    def display_country(self):
        print("\nCOUNTRY NAME : ", self.name)
        print("POPULATION : ", self.population)

class State (Country):
    def __init__(self, cname, sname, population, capital):
        super().__init__(cname, population)        # Calling parent class' constructor
        self.sname = sname
        self.capital = capital

    def __del__(self):
        print("\nDELETED OBJECT : ", self.sname)

    def display_state(self):
        print("\nSTATE NAME : ", self.sname)
        print("CAPITAL : ", self.capital)
        Country.display_country(self)        # Accessing parent class' method

kerala = State("INDIA", "KERALA", "1.4 BILLION", "TRIVANDRUM")
kerala.display_state()
# kerala.display_country()

perth = State("WESTERN AUSTRALIA", "PERTH", "25 MILLION", "PERTH")
perth.display_state()
# perth.display_country()
