import os

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    #Check buttons for orth file
    adapt_view_check("D:\\data\\Orthodontics.cszx", "orth")
    
def adapt_view_check(file, type):
    snooze(3)
    startApplication(APPNAME)
    #Click ok button on the warn message which says it's an internal version
    #clickButton(waitForObject(names.oK_StyleButton))
    mouseClick(waitForObject(names.oK_StyleButton), 153, 30, Qt.LeftButton)
    #Import Orth data and check buttons on scan view
    importData(file, type, "normal")    
    #Refine mesh
    refineMesh("low")
    mouseClick(waitForImage("..\\..\\..\\images\\adaptButton.png"))
    snooze(2)
    test.verify(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton).visible == True, "Free cut button should be visible.")
    #test.verify(waitForObject(names.toolbar_btn_mesh_cleaning).visible == True, "Mesh cleaning button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_mesh_closure).visible == True, "Mesh closure button should be visible.")
    snooze(2)
    os.system("taskkill /f /im cs_scanflow.exe")