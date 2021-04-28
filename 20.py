class Person:
    def __init__(self, i , n):
        self.ID = i
        self.name = n

class Student(Person):
    def __init__(self,i,n,c):
         super().__init__(i,n)
         self.classroom = c
    def prints(self):
        print(self.ID,self.name,self.classroom)
userID = int(input("enter ID->"))
userName = input("enter name->")
userClass = input("enter classroom->")
s = Student(userID,userName,userClass)
s.prints()        
