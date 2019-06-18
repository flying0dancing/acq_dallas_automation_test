

APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))

#     us_Adult_Upper_Lower_Auto()
#     us_Child_Upper_Lower_Auto()
#     eu_Adult_Upper_Lower_Auto()
#     eu_Child_Upper_Lower_Auto()
#     us_Adult_Upper_Auto()
#     us_Child_Upper_Auto()
#     eu_Adult_Upper_Auto()
#     eu_Child_Upper_Auto()
#     us_Adult_Lower_Auto()
#     us_Child_Lower_Auto()
#     eu_Adult_Lower_Auto()
#     eu_Child_Lower_Auto()
#     us_Adult_Upper_Lower_Manual()
#     us_Child_Upper_Lower_Manual()
#     eu_Adult_Upper_Lower_Manual()
#     eu_Child_Upper_Lower_Manual()
#     us_Adult_Upper_Manual()
#     us_Child_Upper_Manual()
#     eu_Adult_Upper_Manual()
#     eu_Child_Upper_Manual()
#     us_Adult_Lower_Manual()
#     us_Child_Lower_Manual()
#     eu_Adult_Lower_Manual()
#     eu_Child_Lower_Manual()
    
  
def us_Adult_Upper_Lower_Auto():
    switchToothNumberSTD("American")    
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_Lower_[2019-04-26T13-45-45].cszx", "orth")
    refineMesh("Low")
    autoMarginLineUpper(1046, 475, "Adult")
    autoMarginLineLower(1148, 511, "Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)

def us_Child_Upper_Lower_Auto():
    switchToothNumberSTD("American")
    startApplication(APPNAME)
    
    importData("D:\\Eva\\restore\\Upper_Lower_[2019-04-26T13-45-45].cszx", "orth")
    refineMesh("Low")
    autoMarginLineUpper(1046, 475, "Child")
    autoMarginLineLower(1148, 511, "Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)

def eu_Adult_Upper_Lower_Auto():
    switchToothNumberSTD("European")
    startApplication(APPNAME)
    
    importData("D:\\Eva\\restore\\Upper_Lower_[2019-04-26T13-45-45].cszx", "orth")
    refineMesh("Low")
    autoMarginLineUpper(1046, 475, "Adult")
    autoMarginLineLower(1148, 511, "Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)

def eu_Child_Upper_Lower_Auto():
    switchToothNumberSTD("European")    
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_Lower_[2019-04-26T13-45-45].cszx", "orth")
    refineMesh("Low")
    autoMarginLineUpper(1046, 475, "Child")
    autoMarginLineLower(1148, 511, "Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def us_Adult_Upper_Auto():
    switchToothNumberSTD("American")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_[2019-04-26T13-51-15].cszx", "orth")
    refineMesh("Low")
    autoMarginLineUpper(836, 566, "Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)

def us_Child_Upper_Auto():
    switchToothNumberSTD("American")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_[2019-04-26T13-51-15].cszx", "orth")
    refineMesh("Low")
    autoMarginLineUpper(836, 566, "Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)

def eu_Adult_Upper_Auto():
    switchToothNumberSTD("European")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_[2019-04-26T13-51-15].cszx", "orth")
    refineMesh("Low")
    autoMarginLineUpper(836, 566, "Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)

def eu_Child_Upper_Auto():
    switchToothNumberSTD("European")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_[2019-04-26T13-51-15].cszx", "orth")
    refineMesh("Low")
    autoMarginLineUpper(836, 566, "Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)

def us_Adult_Lower_Auto():
    switchToothNumberSTD("American")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Lower_[2019-04-26T13-57-42].cszx", "orth")
    refineMesh("Low")
    autoMarginLineLower(766, 578, "Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)

def us_Child_Lower_Auto():
    switchToothNumberSTD("American")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Lower_[2019-04-26T13-57-42].cszx", "orth")
    refineMesh("Low")
    autoMarginLineLower(766, 578, "Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)

def eu_Adult_Lower_Auto():
    switchToothNumberSTD("European")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Lower_[2019-04-26T13-57-42].cszx", "orth")
    refineMesh("Low")
    autoMarginLineLower(766, 578, "Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def eu_Child_Lower_Auto():
    switchToothNumberSTD("European")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Lower_[2019-04-26T13-57-42].cszx", "orth")
    refineMesh("Low")
    autoMarginLineLower(766, 578, "Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)

def us_Adult_Upper_Lower_Manual():
    switchToothNumberSTD("American")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_Lower_[2019-04-26T13-45-45].cszx", "orth")
    refineMesh("Low")
    manualMarginLineUpper("Adult")
    manualMarginLineLower("Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def us_Child_Upper_Lower_Manual():
    switchToothNumberSTD("American")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_Lower_[2019-04-26T13-45-45].cszx", "orth")
    refineMesh("Low")
    manualMarginLineUpper("Child")
    manualMarginLineLower("Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def eu_Adult_Upper_Lower_Manual():
    switchToothNumberSTD("European")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_Lower_[2019-04-26T13-45-45].cszx", "orth")
    refineMesh("Low")
    manualMarginLineUpper("Adult")
    manualMarginLineLower("Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def eu_Child_Upper_Lower_Manual():
    switchToothNumberSTD("European")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_Lower_[2019-04-26T13-45-45].cszx", "orth")
    refineMesh("Low")
    manualMarginLineUpper("Child")
    manualMarginLineLower("Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def us_Adult_Upper_Manual():
    switchToothNumberSTD("American")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_[2019-04-26T13-51-15].cszx", "orth")
    refineMesh("Low")
    manualMarginLineUpper("Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def us_Child_Upper_Manual():
    switchToothNumberSTD("American")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_[2019-04-26T13-51-15].cszx", "orth")
    refineMesh("Low")
    manualMarginLineUpper("Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def eu_Adult_Upper_Manual():
    switchToothNumberSTD("European")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_[2019-04-26T13-51-15].cszx", "orth")
    refineMesh("Low")
    manualMarginLineUpper("Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def eu_Child_Upper_Manual():
    switchToothNumberSTD("European")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Upper_[2019-04-26T13-51-15].cszx", "orth")
    refineMesh("Low")
    manualMarginLineUpper("Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def us_Adult_Lower_Manual():
    switchToothNumberSTD("American")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Lower_[2019-04-26T13-57-42].cszx", "orth")
    refineMesh("Low")
    manualMarginLineLower("Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def us_Child_Lower_Manual():
    switchToothNumberSTD("American")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Lower_[2019-04-26T13-57-42].cszx", "orth")
    refineMesh("Low")
    manualMarginLineLower("Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def eu_Adult_Lower_Manual():
    switchToothNumberSTD("European")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Lower_[2019-04-26T13-57-42].cszx", "orth")
    refineMesh("Low")
    manualMarginLineLower("Adult")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    
def eu_Child_Lower_Manual():
    switchToothNumberSTD("European")
    #When running distributed test, preference file needs to be transferred to remote computer
    #replacePreferenceFile()
    startApplication(APPNAME)
    importData("D:\\Eva\\restore\\Lower_[2019-04-26T13-57-42].cszx", "orth")
    refineMesh("Low")
    manualMarginLineLower("Child")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)