import win32api     
import win32con      
key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE,  
"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",0 ,win32con.KEY_ALL_ACCESS)  
try:
    win32api.RegQueryValueEx(key, "EnableLinkedConnections")
except Exception as e:
    print(e[2])
    if(e[0] == 2):
        win32api.RegSetValueEx(key, "EnableLinkedConnections", 0, win32con.REG_DWORD, 1)
win32api.RegCloseKey(key)  