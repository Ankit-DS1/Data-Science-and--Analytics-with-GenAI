                                  # Object in class

# we use class blueprint to make an object.

class Factory:
    a = "hello I am an attribute"
    def hello(s):
        print("hello I am a method")
        
obj = Factory() #obj becomes an object who can access anythin inside the class till now
obj2 = Factory()

print(obj.a)
obj2.hello()