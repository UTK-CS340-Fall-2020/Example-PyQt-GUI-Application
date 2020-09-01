#!/user/bin/python3

# File: app_widget.py
# Author: Dylan Lee
# Description:
#       holds the class definition for our main widget

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QRadioButton
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QLCDNumber

# This class holds our main widget that will contain all the other parts of the GUI
class App_Widget(QWidget):
    def __init__(self):
        super().__init__()
        
        # lets add some style to the widget
        
        # to keep things organized and allow any buttons or text boxes to auto resize
        # when the window is adjusted we will use a layout, as you will see layouts can be nested
        self.central_layout = QVBoxLayout()
        
        # now lets create and add some basic widgets to our GUI
        # first a simple text box using QLineEdit
        self.text_box = QLineEdit('Simple Text Box')
        # add it to the layout
        self.central_layout.addWidget(self.text_box)

        # labels are nice
        self.label = QLabel('Select One: ')
        # you can create radio buttons
        self.radio_button1 = QRadioButton('Red Pill')
        self.radio_button1.toggled.connect(self.redPill)
        self.radio_button2 = QRadioButton('Blue Pill')
        self.radio_button2.toggled.connect(self.bluePill)
        # too keep these close togther you can put them in their own layout
        self.rad_layout = QHBoxLayout()
        self.rad_layout.addWidget(self.label)
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

        # lets add a form layout also
        self.form_layout = QFormLayout()
        self.form_layout.addRow('First Name:', QLineEdit())
        self.form_layout.addRow('Last Name:', QLineEdit())
        self.form_layout.addRow('Net ID:', QLineEdit())
        # why not throw in a combo box for good measure
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Computer Engineering", "Computer Science", "Electrical Engineering"])
        self.form_layout.addRow('Major:', self.combo_box)

        # add the created layouts holding the widgets
        self.central_layout.addLayout(self.form_layout)
        self.central_layout.addSpacing(10)
        
        # slider bars 
        self.slider_layout = QHBoxLayout()
        self.slider_bar1 = QSlider()
        self.slider_bar2 = QSlider()
        self.slider_bar3 = QSlider()
        self.slider_bar4 = QSlider()
        self.slider_bar4.setValue(20)
        self.slider_bar4.setOrientation(Qt.Horizontal)
        # connect the last slider to a function when adjusted
        self.slider_bar4.valueChanged.connect(self.updateLCD)
        self.slider_layout.addWidget(self.slider_bar1)
        self.slider_layout.addSpacing(10)
        self.slider_layout.addWidget(self.slider_bar2)
        self.slider_layout.addSpacing(10)
        self.slider_layout.addWidget(self.slider_bar3)
        self.slider_layout.addSpacing(10)
        # put an lcd number with this slider
        # that will eventually be connected to display the slider value in the lcd 
        self.lcd_num = QLCDNumber()
        self.lcd_num.display(24)
        self.slider_layout.addWidget(self.lcd_num)
        self.slider_layout.addWidget(self.slider_bar4)
        self.central_layout.addLayout(self.slider_layout)

        # there are also cool progress bars
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(42)
        self.central_layout.addWidget(self.progress_bar)

        # now that everything is added to the central_layout we set it for our main widget object
        self.setLayout(self.central_layout)

    def redPill(self):
        self.radio_button1.setStyleSheet('background: red; color: white')
        self.radio_button2.setStyleSheet('')

    def bluePill(self):
        self.radio_button2.setStyleSheet('background: blue; color: white')
        self.radio_button1.setStyleSheet('')

    # function to connect the lcd display to the slider
    def updateLCD(self):
        # set the lcd to display the slider value
        self.lcd_num.display(self.slider_bar4.value())
