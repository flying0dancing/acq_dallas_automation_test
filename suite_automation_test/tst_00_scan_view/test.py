
APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    startApplication(APPNAME)
    
    #Click ok button on the warn message which says it's an internal version
    skipInternalVersionDlg()
    
    if object.exists(names.sign_In_StyleButton):

        mouseDrag(waitForObject(names.o_Rectangle), 235, 33, -257, -5, Qt.NoModifier, Qt.LeftButton)
        type(waitForObject(names.txtUsername_ImageTextField), "andy.qin@carestream.com")
        mouseClick(waitForObject(names.password_PlaceholderText), Qt.ShiftModifier, Qt.LeftButton)
        type(waitForObject(names.txtPassword_ImageTextField), "kdis7")
        mouseClick(waitForObject(names.o_Image_2), 23, 29, Qt.ShiftModifier, Qt.LeftButton)
        mouseClick(waitForObject(names.o_Image_4), 23, 29, Qt.ShiftModifier, Qt.LeftButton)
        mouseClick(waitForObject(names.sign_In_Text), Qt.ShiftModifier, Qt.LeftButton)

        mouseClick(waitForObject(names.sign_In_StyleButton))
        snooze(2)
    #Click buttons in "What's new" page
    mouseClick(UiTypes.ScreenPoint(410,920), Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    mouseClick(UiTypes.ScreenPoint(960, 920), Qt.NoModifier, Qt.LeftButton)
    snooze(3)
    
    #mouseClick(waitForObject(names.password_PlaceholderText))
    #type(waitForObject(names.txtPassword_ImageTextField), "kdis7")
    if object.exists(names.sign_In_StyleButton):
        mouseClick(waitForObject(names.sign_In_StyleButton))
        snooze(2)
    
    
    scanViewButtonsCheck()
    
