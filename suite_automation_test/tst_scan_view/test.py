APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    startApplication(APPNAME)
    
    #Click ok button on the warn message which says it's an internal version
    mouseClick(waitForObject(names.oK_StyleButton), 153, 30, Qt.LeftButton)
    
    scanViewButtonsCheck()