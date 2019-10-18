import os

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    #Check buttons for orth file
    check_after_refinement("D:\\data\\Orthodontics.cszx", "orth")
    #Check buttons for restore postscan
    check_after_refinement("D:\\data\\Restore_Postscan.cszx", "restore")
    #Check buttons for restore impression
    check_after_refinement("D:\\data\\Restore_Impression.cszx", "restore")
    #Check buttons for implant
    check_after_refinement("D:\\data\\Implant.cszx", "implant")


def check_after_refinement(file, type):
    snooze(3)
    startApplication(APPNAME)
    #Click ok button on the warn message which says it's an internal version
    #clickButton(waitForObject(names.oK_StyleButton))
    mouseClick(waitForObject(names.oK_StyleButton), 153, 30, Qt.LeftButton)
    #Import Orth data and check buttons on scan view
    importData(file, type, "normal")    
    #Refine mesh
    refineMesh("low")
    #Check buttons after refinement
    checkAfterRefine(type)
    snooze(2)
    os.system("taskkill /f /im cs_scanflow.exe")
