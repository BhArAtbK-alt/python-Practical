'''
General case represents that developer working on 
frontend cannot work backend development unless he/she is fullstack dev.

Write a method named verifier () that checks this condition.

The method should check that if frontend is True and backend is True,
the method returns Fullstack as string. If one of them is True, it should return
the respective desgination, and if none of them are true, it returns,
not a developer respetively.
'''

class Employee:
    def __init__ (
            self,
            designation : str = 'Developer',
            frontend : bool = False,
            backend : bool = False
    ):
        self.designation = designation
        self.frontend = frontend
        self.backend = backend

    def __repr__ (self):
        return '{}'.format (self.designation, self.frontend, self.backend)
    
    ### Write the your method over here.
    def verifier (self):
        
       if    self.frontend and self.backend:
              return "FULLSTACK USER DEVELOPER"
       elif  self.frontend:
              return "FRONTEND DEVELOPER"
       elif  self.backend:
              return "BACKEND DEVELOPER"
       else:
            return "NOT A DEVELOPER"
       
      #  pass

if __name__ == '__main__':

    userF = input("user work on fronted (Y/N) ")
    userB = input("user work on backend (Y/N) ")

    frontdev = userF == 'Y'
    backdev = userB == 'Y'  

    firstEmployee = Employee (frontend=frontdev,backend=backdev)
    
    print(firstEmployee.verifier())
    

    