class ParentClass:
    def call_me(self):
        print("I am parent class")


class ChildClass(ParentClass):
    def call_me(self):
        print("I am child class")

        # If we do not want that the child class override the parent class 
        # we add the next line of code
        # super().call_me()

pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me() # override the parent method