# -*- coding: utf-8 -*-"

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"
file = "D:\\data\\Orthodontics.cszx"
file_type = "orth"

def main():
    source(findFile("scripts", "common.py"))    
    startApplication(APPNAME)
    snooze(1)
    #Click ok button on the warn message which says it's an internal version
    skipInternalVersionDlg()
    
    recoverDataDlg()#recover dialog is in front of sign in dialog
    userLogin("andy.qin@carestream.com","kdis7")
    
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
    
    
