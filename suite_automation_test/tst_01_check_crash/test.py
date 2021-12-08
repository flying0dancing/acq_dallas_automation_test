# -*- coding: utf-8 -*-"
import os
APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"
file = "D:\\data\\refine_crash.cszx"
file_type = "restore"

import names

def main():
     
    test.log("nothing in this case, it is a temp")
    import_folder="D:\\20210329\\"
    export_folder="D:\\20210329\\export"
    import_names=readFiles(import_folder)
    for file in import_names:
        test.log("import file is "+file)
        testCash(file,export_folder)
        break
    #for i in range(0,200):
        #test.log('running times '+str(i+1))
        #testCash()
        
    
def testCash(import_file,export_folder):  
    source(findFile("scripts", "common.py")) 
    startApplication(APPNAME)
    snooze(1)
    #Click ok button on the warn message which says it's an internal version
    skipInternalVersionDlg()
    
    mouseClick(UiTypes.ScreenPoint(410,950), Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    #Import Orth data and check buttons on scan view
    importData(import_file, file_type, "normal")    
    # check button status after import
    checkButtonState(file_type) 
    #Refine mesh
    refineMesh("high")
    export_STL_PLY(file_type, export_folder)
    
    #closeApplication()
    #Check buttons after refinement
    #checkAfterRefine(file_type)
    snooze(2)
    
# Read all available cszx files under a directory
def readFiles(dataPath):
    dataFiles = []
    for r, d, f in os.walk(dataPath):
        for file in f:
            if ".cszx" in file:
                dataFiles.append(os.path.join(r,file))
    test.log("Return a list of all cszx files in a directory")
    return dataFiles