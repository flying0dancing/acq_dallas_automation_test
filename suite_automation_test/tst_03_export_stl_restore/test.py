# -*- coding: utf-8 -*-"

import names

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"
file = "D:\\data\\Restore_Postscan.cszx"
file_type = "restore"

def main():
    source(findFile("scripts", "common.py"))
    snooze(3)
    startApplication(APPNAME)
    #clickButton(waitForObject(names.oK_StyleButton)) 
    mouseClick(waitForObject(names.oK_StyleButton), 153, 30, Qt.LeftButton)
    #Import data
    importData(file, file_type, "normal")
    #Perform refinement
    refineMesh("standard")
    export_STL_PLY(file_type, "D:\\data\\Export")
