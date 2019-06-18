APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    
    #import_Export_CSZ_Orth("D:\\2018TT\\orth\\Lisa_Georgalis[2018-05-14_09-47-08]_Orthodontics.cszx", "D:\\Eva\\savedCSZ")
    #import_Export_DCM_Orth("D:\\2018TT\\orth\\Lisa_Georgalis[2018-05-14_09-47-08]_Orthodontics.cszx")
    

#Import Orth data and then export to csz
def import_Export_CSZ_Orth(filename, outputPath):
    delFiles(outputPath, "cszx")
    startApplication(APPNAME)
    importData(filename, "orth")
    snooze(5)
    exportToCSZ(outputPath, "orth.cszx")
    currentApplicationContext().detach()
    snooze(2)

#Import Orth and export to DCM
def import_Export_DCM_Orth(filename):
    startApplication(APPNAME)
    importData(filename, "orth")
    snooze(5)
    cutOnUpperJaw()
    cutOnLowerJaw()
    refineMesh("Low")
    exportToDCM()
    