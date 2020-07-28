import names

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"
file = "D:\\data\\Orthodontics.cszx"
file_type = "orth"

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
#    export_STL_PLY("D:\\data\\Restore_Postscan.cszx", "restore", "D:\\data\\Export")
#    export_STL_PLY("D:\\data\\Implant.cszx", "implant", "D:\\data\\Export")
    

