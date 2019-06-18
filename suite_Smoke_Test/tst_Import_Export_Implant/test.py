APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    
    #import_Export_CSZ_Orth("D:\\2018TT\\implant\\Robert_Keeler[2018-04-19_08-34-04]_Implant.cszx", "D:\\Eva\\savedCSZ")
    #import_Export_DCM_Orth("D:\\2018TT\\implant\\Robert_Keeler[2018-04-19_08-34-04]_Implant.cszx")
    

#Import Orth data and then export to csz
def import_Export_CSZ_Orth(filename, outputPath):
    #delFiles(outputPath, "cszx")
    startApplication(APPNAME)
    importData(filename, "implant")
    snooze(5)
    exportToCSZ(outputPath, "implant.cszx")
    currentApplicationContext().detach()
    snooze(2)

#Import Orth and export to DCM
def import_Export_DCM_Orth(filename):
    startApplication(APPNAME)
    importData(filename, "oimplant")
    snooze(5)
    cutOnUpperJaw()
    cutOnLowerJaw()
    refineMesh("Low")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)