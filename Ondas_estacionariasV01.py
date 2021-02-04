# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:07:46 2019

@author: marouxet
"""

from pyqtgraph.Qt import QtGui, QtCore 
import numpy as np
import pyqtgraph as pg
import sys


class Plot2D(object):
    
    def __init__(self):
        self.A = 1
        self.R = 0.7
        self.f = 1     
        self.traces = dict()
        self.phase = 0
        self.t = np.arange(0,5,0.01)
        self.app = QtGui.QApplication([])
        self.win = pg.GraphicsWindow(title = "Ondas Estacionarias", size = (1000,600))
        self.canvas = self.win.addPlot(title = "WTF")
        self.canvas.setYRange(-2, 2, padding=0)        
        
    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

            
    def trace(self,name,dataset_x,dataset_y):
        if name in self.traces:
            self.traces[name].setData(dataset_x,dataset_y)
        elif name == "sin":         
            self.traces[name] = self.canvas.plot(pen='y')
        elif name == "cos":
            self.traces[name] = self.canvas.plot(pen='g')
        elif name == "sum":
            self.traces[name] = self.canvas.plot(pen='m')


    def update(self):
        s = self.A*np.sin(2 * np.pi * self.f*(-self.t) + self.phase)
        c = self.A*self.R*np.sin(2 * np.pi * self.f* self.t + self.phase)
        sume = s + c
        self.trace("sin", self.t, s)
        self.trace("cos", self.t, c)
        self.trace("sum", self.t, sume)
        self.phase += 0.1
        
    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(30)
        self.start()
        
# Ejecuto el programa en Sí - Omití la parte condicional
        # if __name__ == '__main__':
p = Plot2D()
p.animation()
            
        