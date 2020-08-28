#!/user/bin/python3

# File: app_widget.py
# Author: Dylan Lee
# Description:
#       holds the class definition for our main widget

from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout

# This class holds our main widget that will contain all the other parts of the GUI
class App_Widget(QWidget):
     def __init__(self):
        super().__init__()

        # to keep things organized and allow any buttons or text boxes to auto resize
        # when the window is adjusted we will use a layout, as you will see layouts can be nested
        self.central_layout = QVBoxLayout()

        # now lets create and add some basic widgets to our GUI
        # first a simple text box using QLineEdit
        self.text_box = QLineEdit('Simple Text Box')
        # add it to the layout
        self.central_layout.addWidget(self.text_box)

        # you can create radio buttons
        self.radio_button1 = QRadioButton('Red Pill')
        self.radio_button2 = QRadioButton('Blue Pill')
        # too keep these close togther you can put them in their own layout
        self.rad_layout = QVBoxLayout()
        self.rad_layout.addWidget(self.radio_button1)
        self.rad_layout.addWidget(self.radio_button2)
        # now add that layout to the central 
        self.central_layout.addLayout(self.rad_layout)

        # you can also create push buttons, sometimes easiest done in a loop
        # to keep these well organized you can use a grid layout
        self.grid_layout = QGridLayout()
        for i in range(6):
            self.grid_layout.addWidget(QPushButton('Button ' + str(i)), i/3, i%3)
        # add to central layout
        self.central_layout.addLayout(self.grid_layout)

        # one more widget and layout to look at is the form layout
        self.form_layout = QFormLayout()
        self.form_layout.addRow('First Name:', QLineEdit())
        self.form_layout.addRow('Last Name:', QLineEdit())
        self.form_layout.addRow('Net ID:', QLineEdit())
        # why not through in a combo box for good measure
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Computer Engineering", "Computer Science", "Electrical Engineering"])
        self.form_layout.addRow('Major:', self.combo_box)
        self.central_layout.addLayout(self.form_layout)

        # now that everything is added to the central_layout we set it for our main widget object
        self.setLayout(self.central_layout)