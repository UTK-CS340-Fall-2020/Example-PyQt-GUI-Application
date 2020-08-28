#!/usr/bin/python3

# File: app_window.py
# Author: Dylan Lee
# Description:
#       holds the class definition for our main widget

# import our widget class
from app_widget import App_Widget

# import any and all widgets from PyQt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QStatusBar

# this class inherits from QMainWindow and will be used to set up the applications GUI
class App_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # give the main application window a name
        self.setWindowTitle('Example GUI Application')
        
        # create a central gui widget using our subclass of QWidget named App_Widget
        self.central_widget = App_Widget()
        self.setCentralWidget(self.central_widget)
        
        # Time to create a status bar to show whatever info we need too at the bottom of the window
        # this could be handy to display messages to confirm user actions
        self.statusBar().showMessage('Important Status...')
        
        # create the standard menubar toolbar displayed at the top of the window
        menu_bar = self.menuBar()

        # once the menu bar is created we add more menu options
        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        view_menu = menu_bar.addMenu('View')
        tool_menu = menu_bar.addMenu('Tools')

        # now to add some options for the menus
        
        # first add a save and exit option in the file menu
        # to make it look snazzier you can get icons for your buttons like this
        save_icon = QIcon.fromTheme('document-save')
        save_button = QAction(save_icon, 'Save', self)
        save_button.setShortcut('Ctrl+S')
        save_button.triggered.connect(self.show_Saved)
        
        exit_icon = QIcon.fromTheme('application-exit')
        exit_button = QAction(exit_icon, 'Quit', self)
        # this binds the button to the macro you choose
        exit_button.setShortcut('Ctrl+Q')
        # this is what actually causes the app to close if exit is clicked
        # this type of connection will be important for buttons with more complex actions
        exit_button.triggered.connect(self.close)
        
        # add the created save and exit button to the file_menu
        file_menu.addAction(save_button)
        file_menu.addAction(exit_button)

        # now a copy and paste option for the edit menu
        copy_icon = QIcon.fromTheme('edit-copy')
        copy_button = QAction(copy_icon, 'Copy', self)
        copy_button.setShortcut('Ctrl+C')
        copy_button.triggered.connect(self.show_Copy)
        
        paste_icon = QIcon.fromTheme('edit-paste')
        paste_button = QAction(paste_icon, 'Paste', self)
        paste_button.setShortcut('Ctrl+V')
        paste_button.triggered.connect(self.show_Paste)
        
        # add the newly made buttons to the edit menu
        edit_menu.addAction(copy_button)
        edit_menu.addAction(paste_button)
        # hopefully this gives you an idea of how to design a toolbar

    # an example of how to bind a function to a triggered action
    # in this case all that happens is the status bar says copied, pasted, saved based on which button they click 
    def show_Saved(self):
        self.statusBar().showMessage('Saved')
    
    def show_Copy(self):
        self.statusBar().showMessage('Copied')
    
    def show_Paste(self):
        self.statusBar().showMessage('Pasted')

