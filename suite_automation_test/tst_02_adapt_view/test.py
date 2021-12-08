import names

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    #Check buttons for orth file
    adapt_view_check("D:\\data\\Orthodontics.cszx", "orth")
    
def adapt_view_check(file, file_type):
    snooze(3)
    startApplication(APPNAME)
    #Click ok button on the warn message which says it's an internal version
    #clickButton(waitForObject(names.oK_StyleButton))
    #mouseClick(waitForObject(names.oK_StyleButton), 153, 30, Qt.LeftButton)
    #Click ok button on the warn message which says it's an internal version
    skipInternalVersionDlg()
    
    mouseClick(UiTypes.ScreenPoint(410,950), Qt.NoModifier, Qt.LeftButton)
    #Import Orth data and check buttons on scan view
    importData(file, file_type, "normal")  
    # check button status after import
    checkButtonState(file_type)   
    #Refine mesh
    refineMesh("low")
    snooze(2)
    #mouseClick(waitForImage("..\\..\\..\\images\\adaptButton.png"))#Kun mark it as comments at 20210129
    mouseClick(waitForObject(names.mainWindow_csStateButton_4))#Kun add at 20210129
    snooze(2)
    test.verify(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton).visible == True, "Free cut button should be visible.")
    
    test.verify(waitForObject(names.scrollArea_toolbar_btn_mesh_cleaning_GroupButton).visible == True, "Mesh cleaning button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_mesh_closure).visible == True, "Mesh closure button should be visible.")
    #next button names.toolbar_btn_intraoral not find in v1.0.3.202.d180
    if object.exists(names.toolbar_btn_intraoral):
        test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be ")
    snooze(2)
    