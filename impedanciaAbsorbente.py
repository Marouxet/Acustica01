import numpy as np

class ImpedanciaAbsorbente():
    '''
    Calcula la  impedancia equivalente de un material absorbente a partir del modelo 
    empírico de Delany- Bazley.

    el metodo ImpedanciaAbsorbente.grafico() requiere pyqtgraph para generar una pantalla con los datos del material dado que se usa como
    complemento de otras apps.

    Si freqUnica se setea como False, el objeto genera una lista de frecuencis como un logspace de

    1 a 10kHz en 100 Puntos. Así se pueden  hacer gráficos
    '''
    def __init__(self, porosidad = 0.9, resAire = 32000, d = 0.1, freqUnica = True, freq = 1000, bins =100):

        if not freqUnica:
            freq = np.logspace(0,4,bins)
            self.freq = freq
        rho0 = 1.18 # Densidad del Aire [kg/m3]
        c0 = 343 # Velocidad del Sonido [m/s]

        self.z0 = rho0 * c0 # Impedancia Característica del Aire [Rayle]
        self.X = rho0 * freq / resAire # Variable independiente del Modelo 

        self.ze = self.z0*(1+0.0571*self.X**(-0.754) - 0.087*self.X**(-0.732)*1j) # Impedancia detro del material
        self.ke = (2*np.pi*freq/c0) * (1+0.0978*self.X**(-0.700) - 0.189*self.X**(-0.595)*1j)

        self.zs = -1j*self.ze/(porosidad*np.tan(self.ke*d))

        self.R = (self.zs-self.z0)/(self.zs+self.z0) 

        self.alpha = 1 - abs(self.R)**2

        if freqUnica:
            self.text = '\n Material Absorbente - Modelo de Delany-Bazley \n \n \
            Parámetros (input): \n \n \
                Porosidad (\u03A6): {porosidad} \n \
                Resistividad al Paso del Aire: {resAire} [Pa*s/m2] \n \
                Espesor: {espesor} [m] \n \
                Frecuencia de la onda: {frecuencia} [Hz] \n \n \
            Resultados (output): \n \n \
                Impedancia equivalente: {impEq} [Rayle] \n \
                Módulo del coeficiente de Reflexión de Presion (R) : {R} \n \
                Fase del coeficiente de Reflexión de Presion (R) : {Rfaserad} [rad] , {Rfasegrad}° \n \
                Coeficiente de Absorción (\u03B1):  {abs}' \
                .format(porosidad = porosidad, resAire = resAire, espesor = d, \
                        frecuencia = freq, impEq = np.round(self.zs,2), R = round(abs(self.R),2), \
                        Rfaserad = round(np.angle(self.R),2), Rfasegrad = round(np.angle(self.R,deg = True),2), \
                        abs = round(self.alpha,2))

    def __str__(self):
        return self.text  

    def grafico(self):

        import pyqtgraph as pg

        self.win = pg.GraphicsWindow(title = "Material Absorbente usado en simulación - Datos",size = (500,500))
        self.win.setBackground('w')
        vb = pg.ViewBox()
        text = pg.TextItem(text =self.text, color=[0,0,0])
        vb.addItem(text)
        self.win.addItem(vb)      
