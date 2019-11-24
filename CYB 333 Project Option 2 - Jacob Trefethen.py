from winreg import *

print (r"Reading from SYSTEM\CurrentControlSet\Services\USBSTOR")

reg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

print (r" Writing to SYSTEM\CurrentControlSet\Services\USBSTOR")

key = OpenKey(reg, r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0, KEY_WRITE)

try:   
   SetValueEx(key,"Start",0, REG_DWORD, 4) 
except EnvironmentError:                                          
    print ("Encountered problems writing to Windows Registry")
    
CloseKey(key)

CloseKey(reg) 
