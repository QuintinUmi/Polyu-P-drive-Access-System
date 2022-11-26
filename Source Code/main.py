

import os
import polyu_student_drive.register_UAC as reg
import polyu_student_drive.p_drive_access as pd

studentID = ""
pwd = ""

register = reg.register_UAC()
if(register.status == 5):
    print("{} Please Run with admin Authority!\n".format(register.status_output))
    os.system("PAUSE")
    exit(0)
p_drive = pd.p_drive(studentID, pwd)
p_drive.disconnect()