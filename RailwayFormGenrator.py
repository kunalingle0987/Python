class formDetials:
    status1=" Status : ontime \n"

    def __init__(self,railNo,passengerName,Coach,time):
        self.railNo=railNo
        self.passengerName=passengerName
        self.coach=Coach
        self.time=time
        
        print(f"Railway number is: {railNo} \npassenger: {passengerName} \ncoach: {Coach} \n time: {time}")
      
    @classmethod
    def status(self):
       print(self.status1)
    
    @staticmethod
    def Railname():
        print("Mh_ExP")
    
ps1=formDetials(120,"Kunal","sl01","12-3 pm")
ps1.Railname()
ps1.status()

ps2=formDetials(120,"harsha","s102","1-4 pm")
ps2.Railname()
ps2.status()
