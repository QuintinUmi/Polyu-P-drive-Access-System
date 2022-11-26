

import win32api     
import win32con    

class register_UAC:

    def __init__(self):
        self.status = 5
        self.status_output = "None"

        self.status = self.register_init()

    def register_init(self):
        try:  
            key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, 
                    "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System",0 ,win32con.KEY_ALL_ACCESS)  
        except Exception as admin_authority:
            self.status = admin_authority.args[0]
            self.status_output = admin_authority.args[2]
            return 5

        try:
            win32api.RegQueryValueEx(key, "EnableLinkedConnections")
        except Exception as e:
            print(e[2])
            if(e[0] == 2):
                win32api.RegSetValueEx(key, "EnableLinkedConnections", 0, win32con.REG_DWORD, 1)

        win32api.RegCloseKey(key)  
        return 0

if __name__ == '__main__':
    register_UAC()