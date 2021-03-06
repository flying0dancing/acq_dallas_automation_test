# -*- coding: utf-8 -*-"

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"
file = "D:\\data\\Orthodontics.cszx"
file_type = "orth"

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
#    export_STL_PLY("D:\\data\\Restore_Postscan.cszx", "restore", "D:\\data\\Export")
#    export_STL_PLY("D:\\data\\Implant.cszx", "implant", "D:\\data\\Export")
    

