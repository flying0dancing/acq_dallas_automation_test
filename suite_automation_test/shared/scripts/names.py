# encoding: UTF-8

#Main window and workspace
mainWindow_MainWindow = {"name": "MainWindow", "type": "MainWindow", "visible": 1}
mainWindow_workspace_WorkSpace = {"name": "workspace", "type": "WorkSpace", "visible": 1, "window": mainWindow_MainWindow}

#Login dialogue
mainWindow_UserLoginDialog = {"type": "UserLoginDialog", "unnamed": 1, "visible": 1, "window": mainWindow_MainWindow}
continue_without_signing_in_Text = {"container": mainWindow_UserLoginDialog, "text": "Continue without signing in", "type": "Text", "unnamed": 1, "visible": True}

#Main menu
mainWindow_button_menu_csButton = {"name": "button_menu", "type": "csButton", "visible": 1, "window": mainWindow_MainWindow}
mainMenu_MainMenu = {"name": "MainMenu", "type": "MainMenu", "visible": 1}
mainMenu_Export_csButton = {"container": mainMenu_MainMenu, "text": "Export", "type": "csButton", "unnamed": 1, "visible": 1}
mainMenu_Export_Raw_Data_csButton = {"container": mainMenu_MainMenu, "text": "    Export", "type": "csButton", "unnamed": 1, "visible": 1}

#General message box
generalMsgBox_GeneralMsgBox = {"name": "GeneralMsgBox", "type": "GeneralMsgBox", "visible": 1}
generalMsgBox_btn_frame_QFrame = {"name": "btn_frame_", "type": "QFrame", "visible": 1, "window": generalMsgBox_GeneralMsgBox}

#CSD special message box with buttons
btn_frame_btn_box_CsdDialogButtonBox = {"container": generalMsgBox_btn_frame_QFrame, "name": "btn_box_", "type": "CsdDialogButtonBox", "visible": 1}

#Buttons on message box
o_MessageDialog = {"type": "MessageDialog", "unnamed": 1, "visible": 1}
o_QtQuickWidget = {"type": "QtQuickWidget", "unnamed": 1, "visible": 1, "window": o_MessageDialog}
btn_box_OK_QPushButton = {"container": btn_frame_btn_box_CsdDialogButtonBox, "text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1}

btn_box_Yes_QPushButton = {"container": btn_frame_btn_box_CsdDialogButtonBox, "text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1}
btn_box_No_QPushButton = {"container": btn_frame_btn_box_CsdDialogButtonBox, "text": "No", "type": "QPushButton", "unnamed": 1, "visible": 1}
#oK_StyleButton = {"checkable": True, "container": o_QtQuickWidget, "text": "OK", "type": "StyleButton", "unnamed": 1, "visible": True}
oK_StyleButton = {"checkable": True, "container": o_QtQuickWidget, "text": "OK, got it", "type": "StyleButton", "unnamed": 1, "visible": True}

#BallonInfoLabel
workspace_BalloonInfoBar_BalloonInfoBar = {"container": mainWindow_workspace_WorkSpace, "name": "BalloonInfoBar", "type": "BalloonInfoBar", "visible": 1}
#balloonInfoBar_InfoLabel_QLabel = {"container": workspace_BalloonInfoBar_BalloonInfoBar, "name": "InfoLabel", "type": "QLabel", "visible": 1}
balloonInfoBar_QtQuickWidget = {"container": workspace_BalloonInfoBar_BalloonInfoBar, "type": "QtQuickWidget", "unnamed": 1, "visible": 1}
balloonInfoBar_InfoLabel_QLabel = {"container": balloonInfoBar_QtQuickWidget, "occurrence": 4, "type": "Rectangle", "unnamed": 1, "visible": True}


#Busy dialogue
mainWindow_BusyDialog = {"type": "BusyDialog", "unnamed": 1, "visible": 1, "window": mainWindow_MainWindow}
animateRect_Rectangle = {"container": mainWindow_BusyDialog, "id": "animateRect", "type": "Rectangle", "unnamed": 1, "visible": True}


#Startup screen with scan and import labels, can be used by mouseClick API
mainWindow_StartupScreen = {"type": "StartupScreen", "unnamed": 1, "visible": 1, "window": mainWindow_MainWindow}
import_StyleLabel = {"container": mainWindow_StartupScreen, "text": "Import", "type": "StyleLabel", "unnamed": 1, "visible": True}
scan_StyleLabel = {"container": mainWindow_StartupScreen, "text": "Scan", "type": "StyleLabel", "unnamed": 1, "visible": True}



#Catalog buttons
catalog_bar_btn_upper = {"container": mainWindow_workspace_WorkSpace, "name": "catalog_bar.btn_upper", "type": "csStateButton", "visible": 1}
catalog_bar_btn_lower = {"container": mainWindow_workspace_WorkSpace, "name": "catalog_bar.btn_lower", "type": "csStateButton", "visible": 1}
catalog_bar_btn_bite = {"container": mainWindow_workspace_WorkSpace, "name": "catalog_bar.btn_bite", "type": "csStateButton", "visible": 1}
catalog_bar_btn_switch = {"container": mainWindow_workspace_WorkSpace, "name": "catalog_bar.btn_switch", "type": "csStateButton", "visible": 1}

#Work flow bar buttons
workflow_bar_btn_common = {"container": mainWindow_workspace_WorkSpace, "name": "workflow_bar.btn_common", "type": "csStateButton", "visible": 1}
workflow_bar_btn_cut_hole = {"container": mainWindow_workspace_WorkSpace, "name": "workflow_bar.btn_cut", "type": "csStateButton", "visible": 1}
workflow_bar_btn_implant = {"container": mainWindow_workspace_WorkSpace, "name": "workflow_bar.btn_implant", "type": "csStateButton", "visible": 1}
workflow_bar_btn_impression = {"container": mainWindow_workspace_WorkSpace, "name": "workflow_bar.btn_impression", "type": "csStateButton", "visible": 1}
workflow_bar_btn_postscan = {"container": mainWindow_workspace_WorkSpace, "name": "workflow_bar.btn_postscan", "type": "csStateButton", "visible": 1}
workflow_bar_btn_extra = {"container": mainWindow_workspace_WorkSpace, "name": "workflow_bar.btn_extra", "type": "csStateButton", "visible": 1}
general_increase_csButton = {"container": mainWindow_workspace_WorkSpace, "name": "general_increase", "type": "csButton", "visible": 1}

#Toolbar buttons, relative position = (36, 42)
toolbar_btn_cut = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_cut", "type": "csStateButton", "visible": 1}
workspace_ScrollArea_QScrollArea = {"container": mainWindow_workspace_WorkSpace, "name": "ScrollArea", "type": "QScrollArea", "visible": 1}
scrollArea_toolbar_btn_cut_GroupButton = {"container": workspace_ScrollArea_QScrollArea, "name": "toolbar.btn_cut", "type": "GroupButton", "visible": 1}
scrollArea_toolbar_btn_freecut_GroupButton = {"container": workspace_ScrollArea_QScrollArea, "name": "toolbar.btn_freecut", "type": "GroupButton", "visible": 1}

toolbar_btn_scan_area = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_scan_area", "type": "csStateButton", "visible": 1}
toolbar_btn_intraoral = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_intraoral", "type": "csStateButton", "visible": 1}
toolbar_btn_impression_brush = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_impression_brush", "type": "csStateButton", "visible": 1}
toolbar_btn_lock = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_lock", "type": "csStateButton", "visible": 1}
toolbar_btn_freeze = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_freeze", "type": "csStateButton", "visible": 1}
toolbar_btn_scan_history = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_scan_history", "type": "csStateButton", "visible": 1}
toolbar_btn_delete_all = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_delete_all", "type": "csStateButton", "visible": 1}
toolbar_btn_freecut = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_freecut", "type": "csStateButton", "visible": 1}
toolbar_btn_circlecut = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_circlecut", "type": "csStateButton", "visible": 1}
toolbar_btn_restore = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_restore", "type": "csStateButton", "visible": 1}
toolbar_btn_reset = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_reset", "type": "csStateButton", "visible": 1}
toolbar_btn_scanbody_area = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_scanbody_area", "type": "csStateButton", "visible": 1}
toolbar_toolbar_scan_body_area_selection = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar/toolbar_scan_body_area_selection", "type": "csButton", "visible": 1}
#Added toolbar buttons in check view
toolbar_btn_quadrant_snapshot = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_quadrant_snapshot", "type": "csStateButton", "visible": 1}
toolbar_btn_transparency = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_transparency", "type": "csStateButton", "visible": 1}
toolbar_btn_measurement = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_measurement", "type": "csStateButton", "visible": 1}
#toolbar_btn_orientation_adjustment = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_orientation_adjustment", "type": "csStateButton", "visible": 1}
toolbar_btn_orientation_adjustment = {"container": workspace_ScrollArea_QScrollArea, "name": "toolbar.btn_orientation_adjustment", "type": "GroupButton", "visible": 1}
toolbar_btn_occlusion_pressure = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_occlusion_pressure", "type": "csStateButton", "visible": 1}
toolbar_btn_restoration = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_restoration", "type": "csStateButton", "visible": 1}
toolbar_btn_shade_matching = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_shade_matching", "type": "csStateButton", "visible": 1}
toolbar_btn_manual_bite_adjustment = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_manual_bite_adjustment", "type": "csStateButton", "visible": 1}


#Toolbar buttons under cut in scan view


#Toolbar buttons under scan area


#Toolbar buttons under intraoral


#Toolbar buttons under impression brush


#Toolbar buttons under lock


#Toolbar buttons under shade matching



#Resolution type buttons
workspace_refine_view_resolution_frame_QFrame = {"container": mainWindow_workspace_WorkSpace, "name": "refine_view_resolution_frame", "type": "QFrame", "visible": 1}
refine_view_resolution_frame_button_resolution_low_csButton = {"container": workspace_refine_view_resolution_frame_QFrame, "name": "button_resolution_low", "type": "csButton", "visible": 1}
refine_view_resolution_frame_button_resolution_standard_csButton = {"container": workspace_refine_view_resolution_frame_QFrame, "name": "button_resolution_standard", "type": "csButton", "visible": 1}
refine_view_resolution_frame_button_resolution_high_csButton = {"container": workspace_refine_view_resolution_frame_QFrame, "name": "button_resolution_high", "type": "csButton", "visible": 1}


#Refine button and cancel button
workspace_refine_view_button_frame_QFrame = {"container": mainWindow_workspace_WorkSpace, "name": "refine_view_button_frame", "type": "QFrame", "visible": 1}
workspace_progress_view_button_frame_QFrame = {"container": mainWindow_workspace_WorkSpace, "name": "progress_view_button_frame", "type": "QFrame", "visible": 1}
refine_view_button_frame_button_refine_DelayButton = {"container": workspace_refine_view_button_frame_QFrame, "name": "button_refine", "type": "DelayButton", "visible": 1}
refine_view_button_frame_button_cancel = {"container": workspace_refine_view_button_frame_QFrame, "name": "button_cancel", "type": "QPushButton", "visible": 1}
progress_view_button_cancel_progress = {"container": workspace_progress_view_button_frame_QFrame, "name": "button_cancel_progress", "type": "QPushButton", "visible": 1}


#Buttons under restoration tool
toolbar_btn_preparation_check = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_preparation_check", "type": "csStateButton", "visible": 1}
#toolbar_btn_margin_line = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_margin_line", "type": "csStateButton", "visible": 1}
toolbar_btn_margin_line = {"container": workspace_ScrollArea_QScrollArea, "name": "toolbar.btn_margin_line", "type": "GroupButton", "visible": 1}
toolbar_btn_undercut = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_undercut", "type": "csStateButton", "visible": 1}
#parallelism button on scan view
toolbar_btn_parallelism_check = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_parallelism_check", "type": "csStateButton", "visible": 1}
toolbar_btn_dual_view = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_dual_view", "type": "csStateButton", "visible": 1}
#Buttons under margin line buttons
toolbar_auto_margin_line = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar_auto_margin_line", "type": "csButton", "visible": 1}
toolbar_manual_margin_line = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar_manual_margin_line", "type": "csButton", "visible": 1}
toolbar_edit_margin_line = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar_edit_margin_line", "type": "csButton", "visible": 1}
toolbar_delete = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar_delete", "type": "csButton", "visible": 1}
general_general_restore = {"container": mainWindow_workspace_WorkSpace, "name": "general/general_restore", "type": "csButton", "visible": 1}
general_general_reset = {"container": mainWindow_workspace_WorkSpace, "name": "general/general_reset", "type": "csButton", "visible": 1}

#Tooth number for adults: European standard
workspace_11_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 11, "type": "QPushButton", "visible": 1} #8 for American STD
workspace_12_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 12, "type": "QPushButton", "visible": 1} #7 for American STD
workspace_13_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 13, "type": "QPushButton", "visible": 1} #6 for American STD
workspace_14_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 14, "type": "QPushButton", "visible": 1} #5 for American STD
workspace_15_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 15, "type": "QPushButton", "visible": 1} #4 for American STD
workspace_16_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 16, "type": "QPushButton", "visible": 1} #3 for American STD
workspace_17_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 17, "type": "QPushButton", "visible": 1} #2 for American STD
workspace_18_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 18, "type": "QPushButton", "visible": 1} #1 for American STD
workspace_21_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 21, "type": "QPushButton", "visible": 1} #9 for American STD
workspace_22_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 22, "type": "QPushButton", "visible": 1} #10 for American STD
workspace_23_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 23, "type": "QPushButton", "visible": 1} #11 for American STD
workspace_24_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 24, "type": "QPushButton", "visible": 1} #12 for American STD
workspace_25_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 25, "type": "QPushButton", "visible": 1} #13 for American STD
workspace_26_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 26, "type": "QPushButton", "visible": 1} #14 for American STD
workspace_27_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 27, "type": "QPushButton", "visible": 1} #15 for American STD
workspace_28_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 28, "type": "QPushButton", "visible": 1} #16 for American STD
workspace_31_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 31, "type": "QPushButton", "visible": 1} #24 for American STD
workspace_32_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 32, "type": "QPushButton", "visible": 1} #23 for American STD
workspace_33_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 33, "type": "QPushButton", "visible": 1} #22 for American STD
workspace_34_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 34, "type": "QPushButton", "visible": 1} #21 for American STD
workspace_35_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 35, "type": "QPushButton", "visible": 1} #20 for American STD
workspace_36_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 36, "type": "QPushButton", "visible": 1} #19 for American STD
workspace_37_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 37, "type": "QPushButton", "visible": 1} #18 for American STD
workspace_38_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 38, "type": "QPushButton", "visible": 1} #17 for American STD
workspace_41_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 41, "type": "QPushButton", "visible": 1} #25 for American STD
workspace_42_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 42, "type": "QPushButton", "visible": 1} #26 for American STD
workspace_43_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 43, "type": "QPushButton", "visible": 1} #27 for American STD
workspace_44_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 44, "type": "QPushButton", "visible": 1} #28 for American STD
workspace_45_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 45, "type": "QPushButton", "visible": 1} #29 for American STD
workspace_46_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 46, "type": "QPushButton", "visible": 1} #30 for American STD
workspace_47_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 47, "type": "QPushButton", "visible": 1} #31 for American STD
workspace_48_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 48, "type": "QPushButton", "visible": 1} #32 for American STD
#Tooth numbers for children: European standard
workspace_51_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 51, "type": "QPushButton", "visible": 1} #E for American STD
workspace_52_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 52, "type": "QPushButton", "visible": 1} #D for American STD
workspace_53_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 53, "type": "QPushButton", "visible": 1} #C for American STD
workspace_54_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 54, "type": "QPushButton", "visible": 1} #B for American STD
workspace_55_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 55, "type": "QPushButton", "visible": 1} #A for American STD
workspace_61_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 61, "type": "QPushButton", "visible": 1} #F for American STD
workspace_62_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 62, "type": "QPushButton", "visible": 1} #G for American STD
workspace_63_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 63, "type": "QPushButton", "visible": 1} #H for American STD
workspace_64_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 64, "type": "QPushButton", "visible": 1} #I for American STD
workspace_65_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 65, "type": "QPushButton", "visible": 1} #J for American STD
workspace_71_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 71, "type": "QPushButton", "visible": 1} #O for American STD
workspace_72_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 72, "type": "QPushButton", "visible": 1} #N for American STD
workspace_73_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 73, "type": "QPushButton", "visible": 1} #M for American STD
workspace_74_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 74, "type": "QPushButton", "visible": 1} #L for American STD
workspace_75_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 75, "type": "QPushButton", "visible": 1} #K for American STD
workspace_81_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 81, "type": "QPushButton", "visible": 1} #P for American STD
workspace_82_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 82, "type": "QPushButton", "visible": 1} #Q for American STD
workspace_83_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 83, "type": "QPushButton", "visible": 1} #R for American STD
workspace_84_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 84, "type": "QPushButton", "visible": 1} #S for American STD
workspace_85_QPushButton = {"container": mainWindow_workspace_WorkSpace, "name": 85, "type": "QPushButton", "visible": 1} #T for American STD

#Toolbar buttons under Adapt menu
toolbar_btn_mesh_cleaning = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_mesh_cleaning", "type": "csStateButton", "visible": 1}
toolbar_btn_mesh_closure = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_mesh_closure", "type": "csStateButton", "visible": 1}
#toolbar_btn_bracket_removal = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_bracket_removal", "type": "csStateButton", "visible": 1}
toolbar_btn_plane_cut = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar.btn_plane_cut", "type": "csStateButton", "visible": 1}
workspace_QtQuickWidget = {"container": mainWindow_workspace_WorkSpace, "type": "QtQuickWidget", "unnamed": 1, "visible": 1}
#workspace_VTKMeshWidget = {"container": mainWindow_workspace_WorkSpace, "type": "VTKMeshWidget", "unnamed": 1, "visible": 1}
scrollArea_toolbar_btn_cut_GroupButton = {"container": workspace_ScrollArea_QScrollArea, "name": "toolbar.btn_cut", "type": "GroupButton", "visible": 1}


#Sliders under mesh cleaning tools
slider_radius_Slider = {"container": workspace_QtQuickWidget, "id": "slider_radius", "type": "Slider", "unnamed": 1, "visible": True}
slider_strength_Slider = {"container": workspace_QtQuickWidget, "id": "slider_strength", "type": "Slider", "unnamed": 1, "visible": True}

#Buttons under mesh closure option
showUpper_StyleButton = {"checkable": True, "container": workspace_QtQuickWidget, "id": "showUpper", "type": "StyleButton", "unnamed": 1, "visible": True}
showLower_StyleButton = {"checkable": True, "container": workspace_QtQuickWidget, "id": "showLower", "type": "StyleButton", "unnamed": 1, "visible": True}
unknown_StyleButton = {"checkable": True, "container": workspace_QtQuickWidget, "id": "unknow_btn", "text": "Unknown", "type": "StyleButton", "unnamed": 1, "visible": True}
ortho_StyleButton = {"checkable": True, "container": workspace_QtQuickWidget, "id": "ortho_btn", "text": "Ortho", "type": "StyleButton", "unnamed": 1, "visible": True}
full_StyleButtonV = {"checkable": True, "container": workspace_QtQuickWidget, "id": "full_btn", "text": "Full", "type": "StyleButtonV", "unnamed": 1, "visible": True}
hollow_StyleButtonV = {"checkable": True, "container": workspace_QtQuickWidget, "id": "hollow_btn", "text": "Hollow", "type": "StyleButtonV", "unnamed": 1, "visible": True}
drain_StyleButtonV = {"checkable": True, "container": workspace_QtQuickWidget, "id": "drain_btn", "text": "Drain", "type": "StyleButtonV", "unnamed": 1, "visible": True}
vestibular_slider_Slider = {"container": workspace_QtQuickWidget, "id": "vestibular_slider", "type": "Slider", "unnamed": 1, "visible": True}
lingual_margin_slider_Slider = {"container": workspace_QtQuickWidget, "id": "lingual_margin_slider", "type": "Slider", "unnamed": 1, "visible": True}
cut_switch_SwitchButton = {"checkable": True, "container": workspace_QtQuickWidget, "id": "cut_switch", "type": "SwitchButton", "unnamed": 1, "visible": True}

#Buttons under plane cut option
toolbar_toolbar_apply = {"container": mainWindow_workspace_WorkSpace, "name": "toolbar/toolbar_apply", "type": "csStateButton", "visible": 1}

#Export options
exportFormatCombo_ComboBox = {"container": workspace_QtQuickWidget, "id": "exportFormatCombo", "type": "ComboBox", "unnamed": 1, "visible": True}
orthodontics_StyleImageButton = {"checkable": True, "container": workspace_QtQuickWidget, "text": "Orthodontics", "type": "StyleImageButton", "unnamed": 1, "visible": True}
restoration_StyleImageButton = {"checkable": True, "container": workspace_QtQuickWidget, "text": "Restoration", "type": "StyleImageButton", "unnamed": 1, "visible": True}
implant_StyleImageButton = {"checkable": True, "container": workspace_QtQuickWidget, "text": "Implant", "type": "StyleImageButton", "unnamed": 1, "visible": True}

# Buttons on Export page
workspace_QtQuickWidget = {"container": mainWindow_workspace_WorkSpace, "type": "QtQuickWidget", "unnamed": 1, "visible": 1}
o_ListView = {"container": workspace_QtQuickWidget, "occurrence": 2, "type": "ListView", "unnamed": 1, "visible": True}

#Save view on export page
o_ExportPage_2 = {"container": o_ListView, "index": 2, "type": "ExportPage", "unnamed": 1, "visible": True}
btnBrowseExportPath_StyleButton = {"checkable": False, "container": o_ExportPage_2, "id": "btnBrowseExportPath", "type": "StyleButton", "unnamed": 1, "visible": True}
#Drop down list for export format
o_Image = {"container": o_ExportPage_2, "source": "qrc:///image/general/general_combobox_down_dark.svg", "type": "Image", "unnamed": 1, "visible": True}
o_Overlay = {"container": workspace_QtQuickWidget, "type": "Overlay", "unnamed": 1, "visible": True}
cbExportFormat_StyleComboBox = {"container": o_ExportPage_2, "id": "cbExportFormat", "type": "StyleComboBox", "unnamed": 1, "visible": True}

#The first selection for a drop down overlay
o_ItemDelegate = {"checkable": False, "container": o_Overlay, "type": "ItemDelegate", "unnamed": 1, "visible": True}
#The second selection for a drop down overlay
o_ItemDelegate_2 = {"checkable": False, "container": o_Overlay, "occurrence": 2, "type": "ItemDelegate", "unnamed": 1, "visible": True}
#The third selection for a drop down overlay
o_ItemDelegate_3 = {"checkable": False, "container": o_Overlay, "occurrence": 3, "type": "ItemDelegate", "unnamed": 1, "visible": True}


cancel_Text = {"container": o_ExportPage_2, "text": "Cancel", "type": "Text", "unnamed": 1, "visible": True}
save_Text = {"container": workspace_QtQuickWidget, "occurrence": 2, "text": "Save", "type": "Text", "unnamed": 1, "visible": True}
save_and_Exit_Text = {"container": o_ExportPage_2, "text": "Save and Exit", "type": "Text", "unnamed": 1, "visible": True}

#Open with view on export page
o_OpenPage = {"container": o_ListView, "index": 1, "type": "OpenPage", "unnamed": 1, "visible": True}

#Drop down list for type selection
o_Image_3 = {"container": o_OpenPage, "source": "qrc:///image/general/general_combobox_down_dark.svg", "type": "Image", "unnamed": 1, "visible": True}
#Meshviewer button
cS_MeshViewer_StyleLabel = {"container": o_OpenPage, "text": "CS MeshViewer", "type": "StyleLabel", "unnamed": 1, "visible": True}
#Open button
open_StyleButton = {"checkable": False, "container": o_OpenPage, "id": "btnOpen", "text": "Open", "type": "StyleButton", "unnamed": 1, "visible": True}

#Check button in what's new page
o_BackgroundDialog = {"type": "BackgroundDialog", "unnamed": 1, "visible": 1}
btn_not_show_again_QPushButton = {"name": "btn_not_show_again_", "type": "QPushButton", "visible": 1, "window": o_BackgroundDialog}
btn_ok_QPushButton = {"name": "btn_ok_", "type": "QPushButton", "visible": 1, "window": o_BackgroundDialog}

save_DICOM_File_StyleLabel = {"container": mainWindow_BusyDialog, "text": "Save DICOM File", "type": "StyleLabel", "unnamed": 1, "visible": True}
scrollView_ScrollView = {"container": workspace_QtQuickWidget, "id": "scrollView", "type": "ScrollView", "unnamed": 1, "visible": True}
scrollView_cbExportFormat_StyleComboBox = {"container": scrollView_ScrollView, "id": "cbExportFormat", "type": "StyleComboBox", "unnamed": 1, "visible": True}

save_StyleButton = {"checkable": False, "container": workspace_QtQuickWidget, "id": "id_save_btn", "text": "Save", "type": "StyleButton", "unnamed": 1, "visible": True}
save_and_Exit_StyleButton = {"checkable": False, "container": workspace_QtQuickWidget, "id": "id_save_and_exit_btn", "text": "Save and Exit", "type": "StyleButton", "unnamed": 1, "visible": True}
cancel_StyleButton = {"checkable": False, "container": workspace_QtQuickWidget, "id": "id_cancel_btn", "text": "Cancel", "type": "StyleButton", "unnamed": 1, "visible": True}

content_page_SwipeView = {"container": workspace_QtQuickWidget, "id": "content_page", "type": "SwipeView", "unnamed": 1, "visible": True}
content_page_Rectangle = {"container": content_page_SwipeView, "occurrence": 34, "type": "Rectangle", "unnamed": 1, "visible": True}
content_page_Rectangle_2 = {"container": content_page_SwipeView, "occurrence": 36, "type": "Rectangle", "unnamed": 1, "visible": True}
content_page_Rectangle_3 = {"container": content_page_SwipeView, "occurrence": 38, "type": "Rectangle", "unnamed": 1, "visible": True}

content_page_Orthodontics_StyleRadioButton = {"checkable": True, "container": content_page_SwipeView, "occurrence": 3, "text": "Orthodontics", "type": "StyleRadioButton", "unnamed": 1, "visible": True}
content_page_Restoration_StyleRadioButton = {"checkable": True, "container": content_page_SwipeView, "occurrence": 3, "text": "Restoration", "type": "StyleRadioButton", "unnamed": 1, "visible": True}
content_page_Implant_StyleRadioButton = {"checkable": True, "container": content_page_SwipeView, "occurrence": 3, "text": "Implant", "type": "StyleRadioButton", "unnamed": 1, "visible": True}





