
APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    startApplication(APPNAME)
    
    #Click ok button on the warn message which says it's an internal version
    mouseClick(waitForObject(names.oK_StyleButton), 153, 30, Qt.LeftButton)
    
    snooze(2)
    #mouseClick(waitForObject(names.password_PlaceholderText))
    #type(waitForObject(names.txtPassword_ImageTextField), "kdis7")
    if object.exists(names.sign_In_StyleButton):
        mouseClick(waitForObject(names.sign_In_StyleButton))
        snooze(2)
    
    snooze(3)
    #if object.exists("..\\..\\..\\images\\notshow.png"):
    mouseClick(UiTypes.ScreenPoint(410,920), Qt.NoModifier, Qt.LeftButton)
    snooze(3)
    mouseClick(UiTypes.ScreenPoint(960, 920), Qt.NoModifier, Qt.LeftButton)
    scanViewButtonsCheck()
    