import os
import time

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    
    export_CSZX("D:\\data\\Orthodontics.cszx", "orth", "D:\\data\\Export")
    export_CSZX("D:\\data\\Restore_Postscan.cszx", "restore", "D:\\data\\Export")
    export_CSZX("D:\\data\\Implant.cszx", "implant", "D:\\data\\Export")
    

def export_CSZX(file, type, path):
    snooze(3)
    startApplication(APPNAME)
    clickButton(waitForObject(names.btn_box_OK_QPushButton)) 
    #Import data
    importData(file, type, "normal")
    
    now = time.strftime("%Y-%m-%d %H-%M-%S_", time.localtime())
    name = now + type + '.cszx'
    snooze(1)
    exportToCSZ(path, name)
    
    #Close scanflow
    snooze(2)
    os.system("taskkill /f /im cs_scanflow.exe")