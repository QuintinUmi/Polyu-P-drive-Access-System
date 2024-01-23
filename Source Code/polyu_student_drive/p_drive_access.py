

import os


class p_drive:
    
    def __init__(self, studentID, pwd):
        self.studentID = str(studentID)
        self.pwd = str(pwd)

    def connect(self):
        os.system("net use P: \\\\phdstud.polyu.edu.hk\\student\\{} /p:no {} /user:{}".format(self.studentID, self.pwd, "hh\\" + self.studentID))
        return 0

    def disconnect(self):
        os.system("net use P: /delete")
        return 0
