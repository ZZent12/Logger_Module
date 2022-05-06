from time import perf_counter
from Random_Base64 import get_rand_str
import numpy as np


class Timer():
    
    def __init__(self):
        self.Timer_Start = "Not Initlized"
        self.Timer_Stop = "Not Initlized"
        self.Timer_Eleasped = "Not Initlized"
        self.Timer_ID = "Not Initlized"
        self.Timer_Started_Message = "Not Initlized"
        self.Timer_Finished_Message = "Not Initlized"
        self.Timer_Array = np.array([])

    def Timeit_Start(self, op_name="none"):
        
        self.Timer_Start = perf_counter()
        if op_name == "none":
            self.Timer_ID = get_rand_str()
            while self.Timer_ID in self.Timer_Array:
                self.Timer_ID = get_rand_str()
        else:
            self.Timer_ID = op_name
        self.Timer_Array = np.append(self.Timer_Array, self.Timer_ID)
        self.Timer_Started_Message = f"Operation {self.Timer_ID} has been started"
        
    def Timeit_Stop(self):
        self.Timer_Stop = perf_counter()
        self.Timer_Eleasped = round((self.Timer_Stop - self.Timer_Start)*100, 3)
        self.Timer_Finished_Message = f"Operation {self.Timer_ID} took {self.Timer_Eleasped} miliseconds to compleate"
            
    def Get_Finished_Message(self):
        return self.Timer_Finished_Message
        
    def Get_Started_Message(self):
        return self.Timer_Started_Message
        
    def Get_Used_IDs(self):
        return self.Timer_Array
    
    def Get_Current_ID(self):
        return self.Timer_ID
    
    def Get_Last_Time(self):
        return self.Timer_Eleasped