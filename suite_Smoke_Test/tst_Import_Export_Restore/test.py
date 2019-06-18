APPNAME = "cs_scanflow C:\\ProgramData\\TW\\AcqAltair\\InputData.xml"

def main():
    source(findFile("scripts", "common.py"))
    
    #import_Export_CSZ_Orth("D:\\2018TT\\restore\\Monica_Martin[2018-05-24_12-32-17]_Restore.cszx", "D:\\Eva\\savedCSZ", "restore_impression.cszx")
    #import_Export_CSZ_Orth("D:\\2018TT\\restore\\Nils_Fellbom[2018-07-10_10-20-06]_Restore.cszx", "D:\\Eva\\savedCSZ", "restore_postscan.cszx")
    
    #import_Export_DCM_Orth("D:\\2018TT\\restore\\Monica_Martin[2018-05-24_12-32-17]_Restore.cszx")
    #import_Export_DCM_Orth("D:\\2018TT\\restore\\Nils_Fellbom[2018-07-10_10-20-06]_Restore.cszx")
    

#Import Orth data and then export to csz
def import_Export_CSZ_Orth(filename, outputPath, cszName):
    #delFiles(outputPath, "cszx")
    startApplication(APPNAME)
    importData(filename, "restore")
    snooze(5)
    exportToCSZ(outputPath, cszName)
    currentApplicationContext().detach()
    snooze(2)

#Import Orth and export to DCM
def import_Export_DCM_Orth(filename):
    startApplication(APPNAME)
    importData(filename, "restore")
    snooze(5)
    cutOnUpperJaw()
    #cutOnLowerJaw()
    refineMesh("Low")
    exportToDCM()
    currentApplicationContext().detach()
    snooze(2)
    