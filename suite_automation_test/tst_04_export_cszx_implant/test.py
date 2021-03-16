# -*- coding: utf-8 -*-"

import time

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"
file = "D:\\data\\Implant.cszx"
file_type = "implant"
path = "D:\\data\\Export"

def main():
    source(findFile("scripts", "common.py"))
    
    startApplication(APPNAME)
    #Click ok button on the warn message which says it's an internal version
    skipInternalVersionDlg()
    #Import data
    importData(file, file_type, "normal")
    
    now = time.strftime("%Y-%m-%d %H-%M-%S_", time.localtime())
    name = now + file_type + '.cszx'
    snooze(1)
    exportToCSZ(path, name)
