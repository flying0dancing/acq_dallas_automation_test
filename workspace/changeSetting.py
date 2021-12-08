import os
import shutil
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et
from xml.dom import minidom

xmlFile = "C:\\ProgramData\\TW\\AcqAltair\\preference.xml"

def changeSetting(xmlfile,tagname,attrdict):
    print "==== Change preference.xml setting ===="
    tree = et.parse(xmlfile)
    root = tree.getroot()
    flag=False
    for classChild in root:
        #print classChild.tag, ":", classChild.attrib
        if classChild.attrib=={'key': 'CONFIG'}:
            for child in classChild:
                if child.tag==tagname and child.attrib['key']==attrdict['key']:
                    child.attrib['value'] = attrdict['value']
                    print "changed..."
                    flag=True
            if not flag:
                elt = classChild.makeelement(tagname, attrdict)
                classChild.append(elt)
                print "add new element..."
    tree.write(xmlfile)
    #tree.write(xmlfile, encoding="utf-8", xml_declaration=True)


def addNewElement():
	print "====Disable what's new page===="
	tree = et.parse(xmlFile)
	root = tree.getroot()
	for children in root:
		if children.tag == 'class' and children.attrib['key'] == 'CONFIG':
			attrib = {'key' : 'SHOW_WHATSNEW', 'value' : 'false'}
			element = children.makeelement('option', attrib)
			children.append(element)
			attrib2 = {'key' : 'ACQ_VERSION_WHATSNEW', 'value' : '1.0.1.100'}
			element2 = children.makeelement('option', attrib2)
			children.append(element2)
	tree.write(xmlFile)

def changeSettingbk(type, flag):
    print "==== Change preference.xml setting ===="
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
			
#changeSetting("ENABLE_TT_LICENSE_CHECK", "false")
#changeSetting("ENABLE_DATA_RECOVERY", "false")
changeSetting(xmlFile,'option',{'value': 'false', 'key': 'ENABLE_SN_SCANNER_TYPE_CHECK'})
changeSetting(xmlFile,'option',{'value': 'false', 'key': 'ENABLE_TT_LICENSE_CHECK'})
#CSDATASERVICE_REGISTER_HOST is for CSDPP sn testing
changeSetting(xmlFile,'option',{'value': 'csddsci.azurewebsites.net', 'key': 'CSDATASERVICE_REGISTER_HOST'})
changeSetting(xmlFile,'option',{'value': 'qa21.trophy.ovh', 'key': 'CSCONNECT_AUTH_HOST'})
delAllFiles(r'D:\data\Export')

