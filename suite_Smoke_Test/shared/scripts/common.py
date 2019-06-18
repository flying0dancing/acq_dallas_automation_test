# -*- coding: utf-8 -*-

from xml.etree import ElementTree as et

import names
import subprocess
import os
import shutil
from remotesystem import RemoteSystem

    
# Switch tooth number standard
def switchToothNumberSTD(standard):
    xmlFile = "C:\\ProgramData\\TW\\AcqAltair\\preference.xml"
    tree = et.parse(xmlFile)
    
    for node in tree.find('class'):
        if node.attrib['key'] == "TOOTH_NUMBERING_SYSTEM":
            if standard == 'American':
                node.attrib['value'] = '1'
                test.verify(node.attrib['value'] == '1')
                test.log("Set tooth number to American standard.")
            elif standard == 'European':
                node.attrib['value'] = '0'
                test.verify(node.attrib['value'] == '0')
                test.log("Set tooth number to European standard.")
    tree.write(xmlFile)
    snooze(1)


#Replace preference.xml file in remote computer. Call this function only when you need distributed test
def replacePreferenceFile():
    try:
        remotesys = RemoteSystem()
        test.verify(remotesys.deleteFile("C://ProgramData//TW//AcqAltair//preference.xml"))
        test.verify(remotesys.exists("C://ProgramData//TW//AcqAltair//preference.xml") == False)
        test.verify(remotesys.upload("C://ProgramData//TW//AcqAltair//preference.xml", "C://ProgramData//TW//AcqAltair//preference.xml"))
        test.verify(remotesys.exists("C://ProgramData//TW//AcqAltair//preference.xml"))
        snooze(2)
    except Exception as e:
        test.fail("RemoteSystem error", str(e))

#Delete all files under a assigned path
def delFiles(path, type):
    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(type):
                test.log("%s" % os.path.join(folderName,filename))
                os.unlink(os.path.join(folderName,filename))
                test.verify(os.path.exists(os.path.join(folderName,filename)) == False, "The file '%s' should be deleted." % filename)        
    #Delete all folders and files under path
    #shutil.rmtree(path)

# Read all available cszx files under a directory
def readFiles(dataPath):
    dataFiles = []
    for r, d, f in os.walk(dataPath):
        for file in f:
            if ".cszx" in file:
                dataFiles.append(os.path.join(r,file))
    test.log("Return a list of all cszx files in a directory")
    return dataFiles

#Check buttons after user clicks scan label in home page
def scanViewButtonsCheck():
    clickButton(waitForObject(names.btn_box_OK_QPushButton))
    mouseClick(waitForObject(names.continue_without_signing_in_Text))
    mouseClick(waitForObject(names.scan_StyleLabel))
    test.verify(waitForObject(names.toolbar_btn_cut).visible == True, "Cut button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_scan_area).visible == True, "Scan area button should be visible.")
    #test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_lock).visible == True, "Lock button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_delete_all).visible == True, "Delete button should be visible.")
    test.verify(waitForObject(names.catalog_bar_btn_upper).checked == True, "Upper jaw should be selected.")
    test.verify(waitForObject(names.catalog_bar_btn_lower).checked == False, "Lower jaw shouldn't be selected.")
    test.verify(waitForObject(names.workflow_bar_btn_common).checked == True, "Common scan should be selected.")
    #test.verify(waitForObject(names.workflow_bar_btn_cut_hole).visible == False, "Cut hole button should be hidden before adding.")
    test.verify(object.exists(names.workflow_bar_btn_implant) == False, "Implant button should be hidden before adding.")
    test.verify(object.exists(names.workflow_bar_btn_impression) == False, "Impression button should be hidden before adding.")
    test.verify(object.exists(names.workflow_bar_btn_postscan) == False, "Post scan button should be hidden before adding.")
    test.log("Verify buttons in scan view page")
    snooze(2)

# Import data, make sure the scanner isn't plugged in
def importData(filename, type):
    clickButton(waitForObject(names.btn_box_OK_QPushButton))
    mouseClick(waitForObject(names.import_StyleLabel))
    snooze(2)
    nativeType(filename)
    snooze(2)
    nativeType("<Return>")
    try:
        waitForObject(names.balloonInfoBar_InfoLabel_QLabel, 600000)
        snooze(2)
    except LookupError:
        test.log("The balloon info bar doesn't show up.")
    test.log("Import data with name: %s" % filename)
    checkButtonState(type)      
    snooze(2)
    
#Check buttons with different types
def checkButtonState(type):
    if type == "orth":
        test.verify(waitForObject(names.toolbar_btn_cut).visible == True, "Cut button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scan_area).visible == True, "Scan area button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_lock).visible == True, "Lock button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_delete_all).visible == True, "Delete button should be visible.")
        test.verify(waitForObject(names.workflow_bar_btn_common).checked == True, "Common scan should be selected.")
        test.log("Verify buttons for Orth data.")
    elif type == "restore":
        test.verify(waitForObject(names.workflow_bar_btn_common).checked == False, "Common scan should be deselected.")
        test.verify(waitForObject(names.toolbar_btn_cut).visible == True, "Cut button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_delete_all).visible == True, "Delete button should be visible.")
        if object.exists(names.workflow_bar_btn_postscan):
            test.verify(waitForObject(names.workflow_bar_btn_postscan).checked == True, "The post scan button should be selected.")
            test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_lock).visible == True, "Lock button should be visible.")
            test.log("Verify buttons for postscan data.")
        else:
            test.verify(waitForObject(names.workflow_bar_btn_impression).checked == True, "The impression button should be selected.")
            test.log("Verify buttons for impression data.")
    elif type == "implant":
        test.verify(waitForObject(names.toolbar_btn_cut).visible == True, "Cut button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scanbody_area).visible == True, "Scanbody area button should be visible")
        test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
        test.verify(waitForObject(names.workflow_bar_btn_common).checked == False, "Common scan should be deselected.")
        test.verify(waitForObject(names.workflow_bar_btn_cut_hole).checked == False, "Cut hole button shouldn't be selected.")
        test.verify(waitForObject(names.workflow_bar_btn_implant).checked == True, "Implant button should be selected.")
        test.log("Verify buttons for implant data.")

    
# Perform free cut on upper jaw
def cutOnUpperJaw():
    pointTopLeft = UiTypes.ScreenPoint(337, 450)
    pointTopRight = UiTypes.ScreenPoint(1747, 450)
    pointBottomRight = UiTypes.ScreenPoint(1747, 480)
    pointBottomLeft = UiTypes.ScreenPoint(337, 480)

    mouseClick(waitForObject(names.catalog_bar_btn_upper), 56, 25, Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    #mouseClick(waitForImage("..\\..\\..\\images\\cutButton.png"))
    mouseClick(waitForObject(names.toolbar_btn_cut), 36, 42, Qt.NoModifier, Qt.LeftButton)
    
    snooze(2)
    
    mouseClick(pointTopLeft, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(pointTopRight, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(pointBottomRight, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    doubleClick(pointBottomLeft, Qt.NoModifier, Qt.LeftButton)
    snooze(5)
    mouseClick(waitForImage("..\\..\\..\\images\\restoreButton.png"))
    snooze(2)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    snooze(2)
    test.log("Cut and restore on upper jaw.")


# Perform free cut on lower jaw
def cutOnLowerJaw():
    pointTopLeft = UiTypes.ScreenPoint(337, 450)
    pointTopRight = UiTypes.ScreenPoint(1747, 450)
    pointBottomRight = UiTypes.ScreenPoint(1747, 480)
    pointBottomLeft = UiTypes.ScreenPoint(337, 480)
    
    mouseClick(waitForObject(names.catalog_bar_btn_lower), 50, 41, Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    mouseClick(waitForObject(names.toolbar_btn_cut), 36, 42, Qt.NoModifier, Qt.LeftButton)
    snooze(2)
    
    mouseClick(pointTopLeft, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(pointTopRight, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    mouseClick(pointBottomRight, Qt.NoModifier, Qt.LeftButton)
    snooze(1)
    doubleClick(pointBottomLeft, Qt.NoModifier, Qt.LeftButton)
    snooze(5)
    mouseClick(waitForImage("..\\..\\..\\images\\restoreButton.png"))
    snooze(2)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    snooze(2)
    test.log("Cut and restore on lower jaw.")


# Refinement
def refineMesh(resolution):
    mouseClick(waitForImage("..\\..\\..\\images\\checkButton.png"))
    snooze(2)
    
    if object.exists(names.btn_box_Yes_QPushButton):
        clickButton(names.btn_box_Yes_QPushButton)
        snooze(2)
        
    if object.exists(names.btn_box_Yes_QPushButton):
        clickButton(names.btn_box_Yes_QPushButton)
        snooze(2)
    
    # Refine with different resolutions
    if "High" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_high_csButton))
    elif "Standard" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_standard_csButton))
    elif "Low" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_low_csButton))
        
    clickButton(waitForObject(names.refine_view_button_frame_button_refine_DelayButton))
    
    try:
        waitForObject(names.toolbar_btn_freecut, 600000)
        snooze(2)
    except LookupError:
        test.log("The wait time isn't long enough")
    test.compare(waitForObjectExists(names.toolbar_btn_freecut).visible, True)
    test.compare(waitForObject(names.toolbar_btn_scan_area).visible, True)
    test.compare(waitForObject(names.toolbar_btn_intraoral).visible, True)
    snooze(2)
    test.log("Perform refinement.")


# Draw margin line automatically, this step starts after user enters to restoration tool. x,y represent the drawing position
def autoMarginLineUpper(x, y, person):
    if not object.exists(names.toolbar_btn_restoration):
        mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
        snooze(1)
    mouseClick(waitForObject(names.toolbar_btn_restoration), 36, 42, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.toolbar_btn_margin_line), 36, 42, Qt.NoModifier, Qt.LeftButton)
    # When two catalogs are checked, then uncheck lower jaw catalog
    if waitForObject(names.catalog_bar_btn_upper).checked:
        mouseClick(waitForObject(names.catalog_bar_btn_upper), 50, 41, Qt.NoModifier, Qt.LeftButton)
        mouseClick(waitForObject(names.catalog_bar_btn_upper), 50, 41, Qt.NoModifier, Qt.LeftButton)
    #else:
        #mouseClick(waitForObject(names.catalog_bar_btn_upper), 50, 41, Qt.NoModifier, Qt.LeftButton)
    #Click auto margin line button
    clickButton(waitForObject(names.toolbar_auto_margin_line))
    
    #Check whether the person is adult or child
    if "Adult" == person:
        ##Select a tooth number on upper jaw for adult
        clickButton(waitForObject(names.workspace_18_QPushButton ))
        test.log("Draw margin line on upper jaw automatically for adult")
    elif "Child" == person:
        #Switch to children tooth number showing
        mouseClick(waitForImage("..\\..\\..\\images\\adultToChild.png"))
        #Select a tooth number on upper jaw for child
        clickButton(waitForObject(names.workspace_55_QPushButton ))
        test.log("Draw margin line on upper jaw automatically for child")
    
    #Click on the specific position
    position = UiTypes.ScreenPoint(x, y)
    mouseClick(position, Qt.NoModifier, Qt.LeftButton)
    #Go back to restoration tool mode
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    snooze(2)
    
    
#Draw margin line on lower jaw
def autoMarginLineLower(x, y, person):
    if not object.exists(names.toolbar_btn_restoration):
        mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
        snooze(1)
    #Click restoration tool button
    mouseClick(waitForObject(names.toolbar_btn_restoration), 36, 42, Qt.NoModifier, Qt.LeftButton)
    #Click margin line button
    mouseClick(waitForObject(names.toolbar_btn_margin_line), 36, 42, Qt.NoModifier, Qt.LeftButton)
    # Select lower jaw 
    mouseClick(waitForObject(names.catalog_bar_btn_lower), 50, 41, Qt.NoModifier, Qt.LeftButton)
    #Click auto margin line button
    clickButton(waitForObject(names.toolbar_auto_margin_line))
    
    if "Adult" == person:
        #Select a tooth number for adult
        clickButton(waitForObject(names.workspace_48_QPushButton ))
        snooze(1)
        test.log("Draw margin line on lower jaw automatically for adult")
    elif "Child" == person:
        #Switch to children tooth number showing
        if not object.exists(names.workspace_85_QPushButton):
            mouseClick(waitForImage("..\\..\\..\\images\\adultToChild.png"))
        #Select a tooth number on lower jaw
        clickButton(waitForObject(names.workspace_85_QPushButton))
        snooze(1)
        test.log("Draw margin line on lower jaw automatically for child")
        
    #Click on the specific position
    position = UiTypes.ScreenPoint(x, y)
    mouseClick(position, Qt.NoModifier, Qt.LeftButton)
    #Go back to restoration tool mode
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    snooze(2)
    

def manualMarginLineUpper(person):
    if not object.exists(names.toolbar_btn_restoration):
        mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
    mouseClick(waitForObject(names.toolbar_btn_restoration), 36, 42, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.toolbar_btn_margin_line), 36, 42, Qt.NoModifier, Qt.LeftButton)
    # When two catalogs are checked, then uncheck lower jaw catalog
    if waitForObject(names.catalog_bar_btn_upper).checked:
        mouseClick(waitForObject(names.catalog_bar_btn_upper), 50, 41, Qt.NoModifier, Qt.LeftButton)
        mouseClick(waitForObject(names.catalog_bar_btn_upper), 50, 41, Qt.NoModifier, Qt.LeftButton)
    
    clickButton(waitForObject(names.toolbar_manual_margin_line))
    
    #Check whether the person is adult or child
    if "Adult" == person:
        clickButton(waitForObject(names.workspace_18_QPushButton ))
        test.log("Draw margin line on upper jaw manually for adult")
    elif "Child" == person:
        #Switch to children tooth number showing
        mouseClick(waitForImage("..\\..\\..\\images\\adultToChild.png"))
        #Select a tooth number on upper jaw
        clickButton(waitForObject(names.workspace_55_QPushButton ))
        test.log("Draw margin line on upper jaw manually for child")
    
    #Hard code positions for manual margin line drawing
    mouseClick(UiTypes.ScreenPoint(702, 511), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(740, 437), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(842, 429), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(938, 465), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(954, 593), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(934, 655), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(864, 679), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(764, 675), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(704, 629), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(698, 553), Qt.NoModifier, Qt.LeftButton)
    doubleClick(UiTypes.ScreenPoint(702, 511), Qt.NoModifier, Qt.LeftButton)
    
    #Go back to restoration tool mode
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    snooze(2)
    

#Draw margin line on lower jaw
def manualMarginLineLower(person):
    if not object.exists(names.toolbar_btn_restoration):
        mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
    mouseClick(waitForObject(names.toolbar_btn_restoration), 36, 42, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.toolbar_btn_margin_line), 36, 42, Qt.NoModifier, Qt.LeftButton)
    
    mouseClick(waitForObject(names.catalog_bar_btn_lower), 50, 41, Qt.NoModifier, Qt.LeftButton)
    #Click auto margin line button
    clickButton(waitForObject(names.toolbar_manual_margin_line))
    
    if "Adult" == person:
        #Select a tooth number for adult
        clickButton(waitForObject(names.workspace_48_QPushButton ))
        test.log("Draw margin line on lower jaw manually for adult")
    elif "Child" == person:
        #Switch to children tooth number showing
        if not object.exists(names.workspace_85_QPushButton):
            mouseClick(waitForImage("..\\..\\..\\images\\adultToChild.png"))
        #Select a tooth number on lower jaw for child
        clickButton(waitForObject(names.workspace_85_QPushButton))
        test.log("Draw margin line on lower jaw manually for child")
    
    #Hard code positions for manual margin line drawing
    mouseClick(UiTypes.ScreenPoint(724, 562), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(739, 498), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(782, 503), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(806, 521), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(827, 566), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(823, 622), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(783, 643), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(740, 639), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(715, 615), Qt.NoModifier, Qt.LeftButton)
    mouseClick(UiTypes.ScreenPoint(710, 563), Qt.NoModifier, Qt.LeftButton)
    doubleClick(UiTypes.ScreenPoint(724, 562), Qt.NoModifier, Qt.LeftButton)
    
    #Go back to restoration tool mode
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True)
    mouseClick(waitForImage("..\\..\\..\\images\\backButton.png"))
    #test.log("Draw a margin line on lower jaw successfully")
    snooze(2)
    

#Export to DCM
def exportToDCM():
    mouseClick(waitForImage("..\\..\\..\\images\\exportButton.png"))
    snooze(1)
    mouseClick(waitForImage("..\\..\\..\\images\\saveButton.png"))
    snooze(1)
    mouseClick(waitForObject(names.save_Text))
    snooze(1)
    clickButton(waitForObject(names.btn_box_OK_QPushButton))
    snooze(1)
    test.log("Export data to DCM.")

#Cut file of any type from source directory to dest directory
def moveFile(source, dest, type):
    for filename in os.listdir(source):
        if filename.endswith(type):
            shutil.move(os.path.join(source,filename),dest)
            test.verify(os.path.isfile(os.path.join(source,filename)) == False, "The '%s' file should be moved." % os.path.join(source,filename))

#Export to CSZ
def exportToCSZ(path, name):
    clickButton(waitForObject(names.mainWindow_button_menu_csButton))
    clickButton(waitForObject(names.mainMenu_Export_csButton))
    snooze(2)
    filename = path + "\\" + name
    test.log("CSZ name: %s" % filename)
    nativeType(filename)
    snooze(2)
    nativeType("<Return>")
    snooze(2)
    while object.exists(names.animateRect_Rectangle):
        snooze(10)
        test.log("Waiting for exporting...")
    #Check whether the file exported successfully
    fileCheck = os.path.isfile(filename)
    if fileCheck:
        test.passes("Export to CSZ file successfully.")
    else:
        test.fail("No CSZ file found")
    snooze(2)
    
    
    
#Check whether user need to switch to common scan
def restoreCheckBeforeCut():
    snooze(2)
    if (waitForObject(names.workflow_bar_btn_common).checked == False):
        mouseClick(waitForObject(names.workflow_bar_btn_common),32, 23, Qt.NoModifier, Qt.LeftButton)
        snooze(2)
    
    if object.exists(names.btn_box_Yes_QPushButton):
        clickButton(names.btn_box_Yes_QPushButton)
        snooze(3)
      

#Post scan check before refinement
def postscanCheck():
    snooze(2)
    if (object.exists(names.workflow_bar_btn_postscan)):
        mouseClick(waitForObject(names.workflow_bar_btn_postscan),46, 35, Qt.NoModifier, Qt.LeftButton)
        while(object.exists(names.mainWindow_BusyDialog)):
            continue
        snooze(3)
        cutOnUpperJaw()
        cutOnLowerJaw()
    test.log("Perform cut and restore if post scan is available")

#Kill ACQ software
def killApp():
    subprocess.call([r'C:\auto_click_run\kill_io_3d_acq.exe.bat'])
    snooze(2)
    test.log("Kill ACQ application")