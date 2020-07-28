# -*- coding: utf-8 -*-"

import names

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"
file = "D:\\data\\Implant.cszx"
file_type = "implant"

def main():
    source(findFile("scripts", "common.py"))

    startApplication(APPNAME)
    mouseClick(waitForObject(names.oK_StyleButton), 153, 30, Qt.LeftButton)
    #Import Orth data and check buttons on scan view
    importData(file, file_type, "normal")    
    #Refine mesh
    refineMesh("low")
    #Check buttons after refinement
    checkAfterRefine(file_type)
    snooze(2)
    