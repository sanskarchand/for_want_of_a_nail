#!/usr/bin/env python

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPalette, QColor

import config.const as const 

class FicCard(QtWidgets.QWidget):

    def __init__(self, refMainLayout, ficModel):

        super().__init__()

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

        # Looks weird due to the gaps caused by the layout 
        #self.setStyleSheet("background-color: {}".format(const.COLOR_FIC_CARD))
        #self.setStyleSheet("QWidget { border: 1px solid black; }")
        self.setBgColor(const.COL_TUPLE_FIC_CARD) 
        self.setAutoFillBackground(True)

        self.labelTitle = QtWidgets.QLabel(ficModel.metadata.title)
        self.labelTitle.setStyleSheet("font-weight: strong;")
        
        if ficModel.metadata.crossover:
            label = ficModel.metadata.fandomsCrossover[0] + " and " + ficModel.fandomsCrossover[1] + " crossover"
            self.labelFandom = QtWidgets.QLabel(label)
        else:
            self.labelFandom = QtWidgets.QLabel(ficModel.metadata.fandom)

        self.labelAuthor = QtWidgets.QLabel("By " + ficModel.metadata.author)
        self.labelAuthor.setStyleSheet("font-style: italic;")


        self.layout.addWidget(self.labelTitle)
        self.layout.addWidget(self.labelFandom)
        self.layout.addWidget(self.labelAuthor)

        self.refMainLayout  = refMainLayout
        self.ficModel = ficModel

    def setBgColor(self, col_tuple):
        myPalette = self.palette()
        bgColor = QColor(*col_tuple)
        myPalette.setColor(QPalette.Background, bgColor)
        self.setPalette(myPalette)
 
    def mousePressEvent(self, event):
        self.setBgColor(const.COL_TUPLE_FIC_CARD_PRESSED)

    def mouseReleaseEvent(self, event):
        self.refMainLayout.setReadingFic(self.ficModel)
        self.setBgColor(const.COL_TUPLE_FIC_CARD)