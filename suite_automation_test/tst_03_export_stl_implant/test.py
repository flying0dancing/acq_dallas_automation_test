# -*- coding: utf-8 -*-"

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"
file = "D:\\data\\Implant.cszx"
file_type = "implant"

def main():
    source(findFile("scripts", "common.py"))
    snooze(3)
    startApplication(APPNAME)
    #Click ok button on the warn message which says it's an internal version
    skipInternalVersionDlg()
    recoverDataDlg()#recover dialog is in front of sign in dialog
    userLogin("andy.qin@carestream.com","kdis7")
    #Import data
    importData(file, file_type, "normal")
    # check button status after import
    checkButtonState(file_type) 
    #Perform refinement
    refineMesh("standard")
    export_STL_PLY(file_type, "D:\\data\\Export")
    #export_STL_PLY(file_type, "D:\\Smoke test\\1.0.4_smoke")
