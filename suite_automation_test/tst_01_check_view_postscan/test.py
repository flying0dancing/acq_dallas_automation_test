# -*- coding: utf-8 -*-"


APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"
file = "D:\\data\\Restore_Postscan.cszx"
file_type = "restore"

def main():
    source(findFile("scripts", "common.py"))

    startApplication(APPNAME)
    
    #Click ok button on the warn message which says it's an internal version
    skipInternalVersionDlg()
    
    mouseClick(UiTypes.ScreenPoint(410,950), Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    #Import Orth data and check buttons on scan view
    importData(file, file_type, "normal")   
    # check button status after import
    checkButtonState(file_type)  
    #Refine mesh
    refineMesh("low")
    #Check buttons after refinement
    checkAfterRefine(file_type)
    snooze(2)
    