import os
import shutil
from xml.etree import ElementTree as et


xmlFile = "C:\\ProgramData\\TW\\AcqAltair\\preference.xml"

def changeSetting(type, flag):
    print "====Change TT setting to false===="
    tree = et.parse(xmlFile)
    root = tree.getroot()
    for child in root.iter("option"):
		if child.attrib['key'] == type:
		    child.attrib['value'] = flag
    tree.write(xmlFile)

def delAllFiles(path):
    for file in os.listdir(path):
        #Delete all files
        if os.path.isfile(os.path.join(path, file)):
            os.unlink(os.path.join(path, file))
        #Delete all folders
        elif os.path.isdir(os.path.join(path, file)):
            shutil.rmtree(os.path.join(path, file))
			
changeSetting("ENABLE_TT_LICENSE_CHECK", "false")
changeSetting("ENABLE_DATA_RECOVERY", "false")
delAllFiles(r'D:\data\Export')
