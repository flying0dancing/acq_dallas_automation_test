# -*- coding: utf-8 -*-"

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    startApplication(APPNAME)
    
    #Click ok button on the warn message which says it's an internal version
    skipInternalVersionDlg()
    
    userLogin("andy.qin@carestream.com","kdis7")
        
    #Click buttons in "What's new" page
    mouseClick(UiTypes.ScreenPoint(410,920), Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    mouseClick(UiTypes.ScreenPoint(960, 920), Qt.NoModifier, Qt.LeftButton)
    snooze(3)
    

    scanViewButtonsCheck()
    
