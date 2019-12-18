# -*- coding: utf-8 -*-

from xml.etree import ElementTree as et

import names
import subprocess
import os
import time
import shutil
from remotesystem import RemoteSystem
from pyautogui import screenshotUtil

    
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
    #clickButton(waitForObject(names.btn_box_OK_QPushButton))
    snooze(5)
    if object.exists(names.btn_not_show_again_QPushButton):
        clickButton(names.btn_not_show_again_QPushButton)
        clickButton(names.btn_ok_QPushButton)
        snooze(2)
    if object.exists(names.continue_without_signing_in_Text):
        mouseClick(waitForObject(names.continue_without_signing_in_Text))
        snooze(2)
    mouseClick(waitForObject(names.scan_StyleLabel))
    
        
    test.verify(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton).visible == True, "Cut button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_scan_area).visible == True, "Scan area button should be visible.")
    #test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_lock).visible == True, "Lock button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
    test.verify(waitForObject(names.toolbar_btn_delete_all).visible == True, "Delete button should be visible.")
    #test.verify(waitForObject(names.toolbar_btn_measurement).Visible == True, "Measurement button should be disabled")
    #mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
    #test.verify(waitForObject(names.toolbar_btn_parallelism_check).enabled == False, "Parallelism button should be disabled")
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
def importData(filename, type, flag):
    #clickButton(waitForObject(names.btn_box_OK_QPushButton))    
    snooze(5)
    if object.exists(names.continue_without_signing_in_Text):
        mouseClick(waitForObject(names.continue_without_signing_in_Text))
        snooze(2)
    mouseClick(waitForObject(names.import_StyleLabel))
    snooze(2)
    nativeType(filename)
    snooze(2)
    nativeType("<Return>")
    if "shade" == flag:
        try:
            clickButton(waitForObject(names.btn_box_OK_QPushButton, 600000))
            snooze(2)
        except LookupError:
            test.log("The ok doesn't show up.")
    elif "normal" == flag:
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
        test.verify(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton).visible == True, "Cut button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scan_area).visible == True, "Scan area button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_lock).visible == True, "Lock button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_delete_all).visible == True, "Delete button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_measurement).visible == True, "Measurement button should be visible.")
#        if object.exists("..\\..\\..\\images\\scrollUpButton.png"):
#            mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
        snooze(2)
        test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
        test.verify(waitForObject(names.workflow_bar_btn_common).checked == True, "Common scan should be selected.")
        test.log("Verify buttons for Orth data.")
    elif type == "restore":
        #test.verify(waitForObject(names.workflow_bar_btn_common).checked == False, "Common scan should be deselected.")
        test.verify(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton).visible == True, "Cut button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_delete_all).visible == True, "Delete button should be visible.")
        
        
        if object.exists(names.workflow_bar_btn_postscan):
            test.verify(waitForObject(names.workflow_bar_btn_common).checked == False, "Common scan should be deselected.")
            test.verify(waitForObject(names.workflow_bar_btn_postscan).checked == True, "The post scan button should be selected.")
            test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_lock).visible == True, "Lock button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_measurement).visible == True, "Measurement button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
            test.log("Verify buttons for postscan data.")
        else:
            #test.verify(waitForObject(names.workflow_bar_btn_impression).checked == True, "The impression button should be selected.")
            test.verify(waitForObject(names.workflow_bar_btn_common).checked == True, "Common scan should be selected.")
            test.log("Verify buttons for impression data.")
    elif type == "implant":
        test.verify(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton).visible == True, "Cut button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_freeze).visible == True, "Freeze button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scanbody_area).visible == True, "Scanbody area button should be visible")
        test.verify(waitForObject(names.toolbar_btn_scan_history).visible == True, "Scan history button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
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
    mouseClick(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton), 36, 42, Qt.NoModifier, Qt.LeftButton)
    
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
    mouseClick(waitForObject(names.scrollArea_toolbar_btn_cut_GroupButton), 36, 42, Qt.NoModifier, Qt.LeftButton)
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


# Refinement without shade matching
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
    if "high" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_high_csButton))
    elif "standard" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_standard_csButton))
    elif "low" == resolution:
        clickButton(waitForObject(names.refine_view_resolution_frame_button_resolution_low_csButton))
        
    clickButton(waitForObject(names.refine_view_button_frame_button_refine_DelayButton))
    
    try:
        waitForObject(names.scrollArea_toolbar_btn_freecut_GroupButton, 600000)
        snooze(2)
    except LookupError:
        test.log("The wait time isn't long enough")
    test.compare(waitForObjectExists(names.scrollArea_toolbar_btn_freecut_GroupButton).visible, True)
    test.compare(waitForObject(names.toolbar_btn_scan_area).visible, True)
    test.compare(waitForObject(names.toolbar_btn_intraoral).visible, True)
    snooze(2)
    test.log("Perform refinement.")

#Check buttons after refinement
def checkAfterRefine(type):
    try:
        test.verify(waitForObject(names.scrollArea_toolbar_btn_freecut_GroupButton).visible == True, "Cut button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_scan_area).visible == True, "Scan area button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_intraoral).visible == True, "Intraoral button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_quadrant_snapshot).visible == True, "Quadrant button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_transparency).visible == True, "Transparency button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_measurement).visible == True, "Measurement button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_orientation_adjustment).visible == True, "Orientation button should be visible.")
        test.verify(waitForObject(names.toolbar_btn_occlusion_pressure).visible == True, "Occlusion pressure button should be visible.")
        
        test.verify(waitForObject(names.workflow_bar_btn_common).checked == True, "Common scan should be selected.")
        if type == "orth":
            #mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
            snooze(2)
            test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True, "Margin line button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_undercut).visible == True, "Under cut button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
            test.log("Verify buttons after refinement for Orth data.")
        elif type == "restore":
            if object.exists(names.workflow_bar_btn_postscan):
                test.verify(waitForObject(names.workflow_bar_btn_postscan).checked == False, "The post scan button should be visible and unchecked.")
                mouseClick(names.workflow_bar_btn_postscan, 36, 42, Qt.NoModifier, Qt.LeftButton)
                #mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
                snooze(2)
                test.verify(waitForObject(names.toolbar_btn_preparation_check).visible == True, "Preparation button should be visible.")
                test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True, "Margin line button should be visible.")
                test.verify(waitForObject(names.toolbar_btn_undercut).visible == True, "Under cut button should be visible.")
                test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
                test.verify(waitForObject(names.toolbar_btn_dual_view).visible == True, "Dual view button should be visible.")
                test.log("Verify buttons for postscan data.")
            else:
                #mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
                snooze(2)
                test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True, "Margin line button should be visible.")
                test.verify(waitForObject(names.toolbar_btn_undercut).visible == True, "Under cut button should be visible.")
                test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
                test.log("Verify buttons for impression data.")
        elif type == "implant": 
            #mouseClick(waitForImage("..\\..\\..\\images\\scrollUpButton.png"))
            snooze(2)
            #test.verify(waitForObject(names.toolbar_btn_margin_line).visible == True, "Margin line button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_undercut).visible == True, "Under cut button should be visible.")
            test.verify(waitForObject(names.toolbar_btn_parallelism_check).visible == True, "Parallelism button should be visible.")
            test.verify(waitForObject(names.workflow_bar_btn_implant).visible == True, "Implant button should be visible after refinement.")       
            test.verify(waitForObject(names.workflow_bar_btn_implant).checked == False, "Implant button should be shown and unchecked.")
            test.log("Verify buttons for implant data.")
    except LookupError as e:
        test.log("Fail to find object: %s" % str(e))
        
#Refinement with shade matching info
def refineMeshWithShade(resolution):
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
        mouseClick(waitForImage("..\\..\\..\\images\\backButton.png", {"timeout":600000}))
        snooze(2)
    except LookupError:
        test.log("The wait time isn't long enough")
    test.compare(waitForObjectExists(names.scrollArea_toolbar_btn_freecut_GroupButton).visible, True)
    test.compare(waitForObject(names.toolbar_btn_scan_area).visible, True)
    test.compare(waitForObject(names.toolbar_btn_intraoral).visible, True)
    snooze(2)
    test.log("Perform refinement with shade matching")

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
    mouseClick(waitForObject(names.save_StyleButton), 70, 17, Qt.LeftButton)
    snooze(1)
    test.log("Export data to DCM.")


#Set a directory to save PLY or STL file
def setDirectory(directory):
    snooze(3)
    mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\exportButton.png"))
    snooze(1)
    mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\saveButton.png"))
    snooze(1)
    #Click browser button to define a directory
    mouseClick(waitForObject(names.btnBrowseExportPath_StyleButton), 31, 37, Qt.LeftButton)
    snooze(2)
    nativeType(directory)
    snooze(2)
    nativeType("<Return>")
    snooze(2)
    nativeType("<Return>")
    snooze(4)
    mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\shareButton.png"))
    snooze(2)
    mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\checkButton2.png"))
    snooze(2)

def countFolder(path):
    folders = []
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path,folder)):
            folders.append(os.path.join(path,folder))
    return len(folders)

#Export to stl or ply format
def exportFile(format, type, path):
    mouseClick(waitForImage("D:\\Eva\\acq_dallas_automation_test\\images\\exportButton.png"))
    snooze(3)
    mouseClick(findImage("D:\\Eva\\acq_dallas_automation_test\\images\\saveButton.png"))
    snooze(2)   
    #Export format drop down list
    mouseClick(waitForObject(names.scrollView_cbExportFormat_StyleComboBox), 381, 28, Qt.LeftButton)
    snooze(2)
    if "PLY" == format:
        mouseClick(waitForObject(names.o_ItemDelegate), 262, 42, Qt.LeftButton)
    elif "STL" == format:
        mouseClick(waitForObject(names.o_ItemDelegate_2), 285, 34, Qt.LeftButton)
    snooze(2)
    
    #ClinicalIndication drop down list
    #mouseClick(waitForObject(names.cbExportClinicalIndication_StyleComboBox), 451, 41, Qt.LeftButton)
    snooze(2)
    if "orth" == type:
        #mouseClick(waitForObject(names.o_ItemDelegate), 151, 40, Qt.LeftButton)
        mouseClick(waitForObject(names.scrollView_Orthodontics_StyleRadioButton), 83, 21, Qt.LeftButton)
    elif "restore" == type:
        mouseClick(waitForObject(names.scrollView_Restoration_StyleRadioButton), 72, 24, Qt.LeftButton)
    elif "implant" == type:
        mouseClick(waitForObject(names.scrollView_Implant_StyleRadioButton), 63, 22, Qt.LeftButton)
    snooze(2)
    previousFolders = countFolder(path)
    mouseClick(waitForObject(names.save_StyleButton), 70, 17, Qt.LeftButton)
    snooze(7)
    laterFolder = countFolder(path)
    test.verify(laterFolder == previousFolders + 1, "The folder count should be added 1.")
    while object.exists(names.save_DICOM_File_StyleLabel):
        snooze(5)
    mouseClick(findImage("D:\\Eva\\acq_dallas_automation_test\\images\\shareButton.png"))
    snooze(1)
    mouseClick(waitForImage(r"D:\Eva\acq_dallas_automation_test\images\checkButton2.png"))
    snooze(2)

#Open with 3rd party software
def openWithMeshViewer():
    mouseClick(waitForImage("..\\..\\..\\images\\exportButton.png"))
    snooze(1)
    mouseClick(waitForImage("..\\..\\..\\images\\openWithButton.png"))
    snooze(1)
    mouseClick(waitForObject(names.cS_MeshViewer_StyleLabel))
    snooze(1)
    #Click Clinical Indication drop down list
    mouseClick(waitForObject(names.o_Image_3), 12, 3, Qt.LeftButton)
    snooze(1)
    #Select Restoration option
    mouseClick(waitForObject(names.o_ItemDelegate_2), 183, 46, Qt.LeftButton)
    snooze(1)
    mouseClick(waitForObject(names.open_StyleButton), 132, 52, Qt.LeftButton)
    snooze(15)
    #Take a screenshot
    now = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
    imageName = now + "_screenshot.png"
    screenshotPath = "D:\\Eva\\TestSuites\\screenshots"
    screenshotUtil.screenshot(os.path.join(screenshotPath, imageName))
    snooze(5)
    test.verify(os.path.isfile(os.path.join(screenshotPath, imageName)) == True, "Screenshot is saved.")
    os.system("taskkill /f /im CSMeshViewer.exe")
    snooze(2)
    

#Cut file of any type from source directory to dest directory
def moveFile(source, dest, type):
    for filename in os.listdir(source):
        if filename.endswith(type):
            shutil.move(os.path.join(source,filename),dest)
            test.verify(os.path.isfile(os.path.join(source,filename)) == False, "The '%s' file should be moved." % os.path.join(source,filename))

#Export to CSZ
def exportToCSZ(path, name):
    clickButton(waitForObject(names.mainWindow_button_menu_csButton))
    snooze(1)
    clickButton(waitForObject(names.mainMenu_Export_Raw_Data_csButton))
    snooze(2)
    filename = path + "\\" + name
    test.log("Saved CSZ name: %s" % filename)
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