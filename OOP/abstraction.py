# hiding the internal funtionality from user
from abc import ABC,abstractmethod
class webpage(ABC):
    def dashboard(self):
        print("welcome to dashboard")
    def userprofile(self):
        print("welcome to profile page")
    @abstractmethod
    def login(self,user,password):
        pass
class user(webpage):
    def login(self,user,password):
        print("hello")
obj=user()
obj.dashboard() 