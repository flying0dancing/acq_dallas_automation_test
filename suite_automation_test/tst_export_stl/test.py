import os

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    #setDirectory(r"D:\\data\\Export")
    export_STL_PLY("D:\\data\\Orthodontics.cszx", "orth", "D:\\data\\Export")
    export_STL_PLY("D:\\data\\Restore_Postscan.cszx", "restore", "D:\\data\\Export")
    export_STL_PLY("D:\\data\\Implant.cszx", "implant", "D:\\data\\Export")
    

def export_STL_PLY(file, type, path):
    snooze(3)
    startApplication(APPNAME)
    clickButton(waitForObject(names.btn_box_OK_QPushButton)) 
    #Import data
    importData(file, type, "normal")
    #Perform refinement
    refineMesh("standard")
        
    #Export to PLY format
    exportFile("PLY", type, path)
    #Export to STL format
    exportFile("STL", type, path)
    
    #Close scanflow
    snooze(2)
    os.system("taskkill /f /im cs_scanflow.exe")
