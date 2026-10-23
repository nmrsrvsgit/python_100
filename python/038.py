class NormalRide:
    def __init__(self,custo_name,dist_travel):
        self.custo_name=custo_name
        self.dist_travel=dist_travel
    def calculate_fare(self):
        return self.dist_travel*12

class PremiumRide(NormalRide):
    def __init__(self, custo_name, dist_travel):
         super().__init__(custo_name, dist_travel)
    def calculate_fare(self):
        return self.dist_travel*12  +150

N1=NormalRide("Rahul",10)
p1=PremiumRide("priya",12)  
print("normal ride fare",N1.calculate_fare())
print("premium ride fare",p1.calculate_fare() ) 
          