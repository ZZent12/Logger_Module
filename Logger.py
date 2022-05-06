from Timer import Timer
from datetime import datetime
import numpy as np
import os


class Logger():
    Common_Types = np.array(["Timing", "Debug", "Info", "Warning", "Error", "Critical Error"])
    Working_Loggers = set()
    Working_Modules = set()
    Number_of_Loggers = 0
    Number_of_Modules = 0
    Path = "Unknown"
    First_Init = True
    Mode = "Unknown"
    
    def __init__(self, Logger_Name="Unknown Logger", Module_Name="Unknown", Mode="Master Module Log"):
        self.Logger_Name = Logger_Name
        self.Module_Name = Module_Name
        self.Has_Timers = False
        t1 = len(Logger.Working_Modules)
        Logger.Working_Loggers.add(self.Logger_Name)
        Logger.Working_Modules.add(self.Module_Name)
        if len(Logger.Working_Modules) > t1:
            Logger.Number_of_Modules += 1
        Logger.Number_of_Loggers += 1

        cwd = os.getcwd()        
        if not os.path.exists(f'{cwd}\\Logs'):
            os.mkdir(f'{cwd}\\Logs')
        Logger.Path = f'{cwd}\\Logs'
        
        if Logger.First_Init == True:
            Logger.Mode = Mode
        
        Logger.First_Init == False
    
        if Logger.Mode == "Master Module Log":
            self.master_module_log_mode()
        elif Logger.Mode == "Module Log":
            self.module_log_mode()
        elif Logger.Mode == "Master Log":
            self.master_log_mode()
        elif Logger.Mode == "Master Instance Log":
            self.master_instance_log_mode()
        elif Logger.Mode == "Instance Log":
            self.instance_log_mode()


    def now():
        return datetime.now()

    def master_module_log_mode(self):
        Logger.Formatter = "--{Time} - {Logger_Name} - {Message_Type}--\n{Message_Content}"
        Logger.Master_Formatter = "--{Time} - {Logger_Name} - {Module_Name} - {Message_Type}--\n{Message_Content}"
        if not os.path.exists(f"{Logger.Path}\\Master.LOG"):
            open(f"{Logger.Path}\\Master.LOG", "x")
        self.Master_Path = f"{Logger.Path}\\Master.LOG"
        if not os.path.exists(f"{Logger.Path}\\{self.Module_Name}.LOG"):
            open(f"{Logger.Path}\\{self.Module_Name}.LOG", "x")
        self.Log_Path = f"{Logger.Path}\\{self.Module_Name}.LOG"

    def master_log_mode(self):
        Logger.Master_Formatter = "--{Time} - {Logger_Name} - {Module_Name} - {Message_Type}--\n{Message_Content}"
        if not os.path.exists(f"{Logger.Path}\\Master.LOG"):
            open(f"{Logger.Path}\\Master.LOG", "x")
        self.Master_Path = f"{Logger.Path}\\Master.LOG"

    def module_log_mode(self):
        Logger.Formatter = "--{Time} - {Logger_Name} - {Message_Type}--\n{Message_Content}"
        if not os.path.exists(f"{Logger.Path}\\{self.Module_Name}.LOG"):
            open(f"{Logger.Path}\\{self.Module_Name}.LOG", "x")
        self.Log_Path = f"{Logger.Path}\\{self.Module_Name}.LOG"
        
    def master_instance_log_mode(self):
        Logger.Formatter = "--{Time} - {Message_Type}--\n{Message_Content}"
        Logger.Master_Formatter = "--{Time} - {Logger_Name} - {Message_Type}--\n{Message_Content}"
        if not os.path.exists(f"{Logger.Path}\\Master.LOG"):
            open(f"{Logger.Path}\\Master.LOG", "x")
        self.Master_Path = f"{Logger.Path}\\Master.LOG"
        if not os.path.exists(f"{Logger.Path}\\{self.Logger_Name}.LOG"):
            open(f"{Logger.Path}\\{self.Module_Name}-{self.Logger_Name}.LOG", "x")
        self.Log_Path = f"{Logger.Path}\\{self.Module_Name}-{self.Logger_Name}.LOG"
        
    def instance_log_mode(self):
        Logger.Formatter = "--{Time} - {Message_Type}--\n{Message_Content}"
        if not os.path.exists(f"{Logger.Path}\\{self.Logger_Name}.LOG"):
            open(f"{Logger.Path}\\{self.Module_Name}-{self.Logger_Name}.LOG", "x")
        self.Log_Path = f"{Logger.Path}\\{self.Module_Name}-{self.Logger_Name}.LOG"

    def log(self, Type, Message):
        NOW = self.now()
        if Logger.Mode == "Master Module Log":
            with open(self.Master_Path, "a") as f:
                f.write(Logger.Formatter.format(Time = NOW, Logger_Name = self.Logger_Name, Module_Name = self.Module_Name, Message_Type = Type, Message_Content = Message))
            with open(self.Log_Path, "a") as f:
                f.write(Logger.Formatter.format(Time = NOW, Logger_Name = self.Logger_Name, Message_Type = Type, Message_Content = Message))
        elif Logger.Mode == "Module Log":
            with open(self.Log_Path, "a") as f:
                f.write(Logger.Formatter.format(Time = NOW, Logger_Name = self.Logger_Name, Message_Type = Type, Message_Content = Message))
        elif Logger.Mode == "Master Log":
            with open(self.Master_Path, "a") as f:
                f.write(Logger.Formatter.format(Time = NOW, Logger_Name = self.Logger_Name, Module_Name = self.Module_Name, Message_Type = Type, Message_Content = Message))
        elif Logger.Mode == "Master Instance Log":
            with open(self.Master_Path, "a") as f:
                f.write(Logger.Formatter.format(Time = NOW, Logger_Name = self.Logger_Name, Message_Type = Type, Message_Content = Message))
            with open(self.Log_Path, "a") as f:
                f.write(Logger.Formatter.format(Time = NOW, Message_Type = Type, Message_Content = Message))
        elif Logger.Mode == "Instance Log":
            with open(self.Log_Path, "a") as f:
                f.write(Logger.Formatter.format(Time = NOW, Message_Type = Type, Message_Content = Message))
    
    def Create_Timers(self, number=3, names=[]):
        if self.Has_Timers == False:
            if number > 1:                
                if names == []:
                    self.Has_Timers = True
                    self.Timers = {}
                    for i in range(number):
                        self.Timers[f"Timer-{i}"] = Timer()
                elif len(names) == number:
                    self.Has_Timers = True
                    self.Timers = {}
                    for i in names:
                        self.Timers[i] = Timer()

    def Creater_Timer(self):
        if self.Has_Timers == False:
            self.Has_Timers = True
            return Timer()
        
    @classmethod
    def Get_Number_Loggers(cls):
        return cls.Number_of_Loggers
    
    @classmethod
    def Get_Number_Modules(cls):
        return cls.Number_of_Modules