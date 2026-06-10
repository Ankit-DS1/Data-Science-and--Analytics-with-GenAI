                                # Constructor

# A constructor is a method that runs automatically whenever we call the class.
# The constructor will target the location of the object.

# self - the constructor will target the location of that object so we have to store the location somewhere to store the location we use self keyword.
# Then we take the specific parrameters for that for that object.

# Ex

class Factory:
    def __init__(self):
        print("Hello i will run no matter what")

Factory()

class Factory:
    def __init__(self,material,zips,pockets):
        print(self)
        self.material = material 
        self.zips = zips 
        self.pockets = pockets
    
    def showdetails(self):
        print(self.material,self.pockets,self.zips)



reebok = Factory("Leather",3,3)
campus = Factory("nylon",2,2)






    
