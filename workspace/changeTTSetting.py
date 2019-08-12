import os
import sys, traceback, types
import shutil
import logging
from xml.etree import ElementTree as et
import time

xmlFile = "C:\\ProgramData\\TW\\AcqAltair\\preference.xml"

def changeSetting(type, flag):
    print "====Change TT setting to false===="
    tree = et.parse(xmlFile)
    root = tree.getroot()
    for child in root.iter("option"):
		if child.attrib['key'] == type:
		    child.attrib['value'] = flag
    tree.write(xmlFile)

#Disable what's new page
def disableWhatsNew():
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

changeSetting("ENABLE_TT_LICENSE_CHECK", "false")
#disableWhatsNew()