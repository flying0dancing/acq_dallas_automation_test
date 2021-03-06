# -*- coding: utf-8 -*-"

import time

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"
file = "D:\\data\\Orthodontics.cszx"
file_type = "orth"
path = "D:\\data\\Export"

def main():
    source(findFile("scripts", "common.py"))
    
    startApplication(APPNAME)
    #Click ok button on the warn message which says it's an internal version
    skipInternalVersionDlg()
    recoverDataDlg()#recover dialog is in front of sign in dialog
    userLogin("andy.qin@carestream.com","kdis7")
    #Import data
    importData(file, file_type, "normal")
    # check button status after import
    checkButtonState(file_type) 
    
    now = time.strftime("%Y-%m-%d %H-%M-%S_", time.localtime())
    name = now + file_type + '.cszx'
    snooze(1)
    exportToCSZ(path, name)
    
#    os.system("taskkill /f /im cs_scanflow.exe")