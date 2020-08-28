#!/usr/bin/python3

# File: main.py
# Author: Dylan Lee
# Description: 
#         holds the main function for our app

import sys
from app_window import App_Window
from PyQt5.QtWidgets import QApplication

def main():
    # declare an instance of the application
    app_example = QApplication(sys.argv)

    # create an instance of the GUI_Example class and display the main window
    main_window = App_Window()
    main_window.show()

    # this triggers the event loop for the application
    # calling it inside sys.exit() just ensures a leak free exit
    sys.exit(app_example.exec_())
    
if __name__ == '__main__':
    main()
