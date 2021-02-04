# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:07:46 2019

@author: marouxet
"""

from pyqtgraph.Qt import QtGui, QtCore 
import numpy as np
import pyqtgraph as pg
import sys
import pyaudio

class Plot2D(object):
    
    def __init__(self):

        self.A = 1
        self.R = 0.8
        self.R_phase = np.pi/5
        self.f = 1     
        self.traces1 = dict()
        self.traces2 = dict()
        self.traces3 = dict() 
        self.phase = 0
        self.t = np.arange(-4*np.pi,0,0.01)
        self.app = QtGui.QApplication([])
        self.win = pg.GraphicsWindow(title = "Ondas Estacionarias", size = (1000,600))

        self.canvas = self.win.addPlot()
        self.win.nextRow()
        self.canvas2 = self.win.addPlot()
        self.win.nextRow()
        self.canvas3 = self.win.addPlot()
        
        self.canvas.setYRange(-2, 2, padding=0)   
        self.canvas.setXRange(-3, 0, padding=0)  
        self.canvas.getAxis('bottom').setLabel('Fracción de longitud de onda')
        self.canvas.getAxis('left').setLabel('Presión acústica [Pa]')
        self.canvas2.setYRange(0, 5, padding=0)
        self.canvas2.setXRange(-3, 0, padding=0)  
        self.canvas2.getAxis('bottom').setLabel('Fracción de longitud de onda')
        self.canvas2.getAxis('left').setLabel('Presión acústica al cuadrado [Pa^2] ')
        self.canvas3.setYRange(-2 , 2, padding=0)
        self.canvas3.setXRange(-3, 0, padding=0)  
        self.canvas3.getAxis('bottom').setLabel('Fracción de longitud de onda')
        self.canvas3.getAxis('left').setLabel('Varias Magnitudes ')
    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()
#' if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            
    def trace(self,name,dataset_x,dataset_y):
        if name in self.traces1:
            self.traces1[name].setData(dataset_x,dataset_y)
        elif name == "inc":         
            self.traces1[name] = self.canvas.plot(pen='y')
        elif name == "ref":
            self.traces1[name] = self.canvas.plot(pen='g')
        elif name == "sum":
            self.traces1[name] = self.canvas.plot(pen='m')

    def trace2(self,name,dataset_x,dataset_y):
        if name in self.traces2:
            self.traces2[name].setData(dataset_x,dataset_y)
        elif name == "inc":         
            self.traces2[name] = self.canvas2.plot(pen='y')
        elif name == "ref":
            self.traces2[name] = self.canvas2.plot(pen='g')
        elif name == "sum":
            self.traces2[name] = self.canvas2.plot(pen='m')
            
    def trace3(self,name,dataset_x,dataset_y):
        if name in self.traces3:
            self.traces3[name].setData(dataset_x,dataset_y)
        elif name == "inc":         
            self.traces3[name] = self.canvas3.plot(pen='y')
        elif name == "ref":
            self.traces3[name] = self.canvas3.plot(pen='g')
        elif name == "sum":
            self.traces3[name] = self.canvas3.plot(pen='m')
            
    def update(self):
        s = self.A*np.sin(2 * np.pi * self.f*(-self.t) + self.phase )
        c = self.A*self.R*np.sin(2 * np.pi * self.f* self.t + self.phase + self.R_phase)
        sume = s + c
        s2 = np.power(s, 2)
        c2 = np.power(c, 2)
        sume2 = np.power(sume, 2)

        
        vel_inc=self.A*np.sin(2 * np.pi * self.f*(-self.t) + self.phase + np.pi/4)
        vel_ref=self.A*self.R*np.sin(2 * np.pi * self.f* self.t + self.phase + np.pi/4)
        vel_sum = vel_inc+vel_ref
        
        
        self.trace("inc", self.t, s)
        self.trace("ref", self.t, c)
        self.trace("sum", self.t, sume)
        self.trace2("inc", self.t, s2)
        self.trace2("ref", self.t, c2)
        self.trace2("sum", self.t, sume2)
        self.trace3("inc", self.t, vel_inc)
        self.trace3("ref", self.t, vel_ref)
        self.trace3("sum", self.t, vel_sum)
        self.phase += 0.1
        
    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(75)
        self.start()
        
# Ejecuto el programa en Sí - Omití la parte condicional
        # if __name__ == '__main__':
p = Plot2D()
p.animation()
            
        