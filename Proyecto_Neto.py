import math as m
import cmath as cm
import numpy as np
import matplotlib.pyplot as plt

Lf = 1.33E-6        #H/m fase
Cf = 8.86E-12       #F/m fase
Rf = 0.92E-4        #ohm/m fase
Gf = 0              #Ohm-1/m fase
V0 = 220E3          #V
P = (150 + 50j)*1E6     #VA
f = 60              #Hz
w = 2*m.pi*f        #Rad/s
Longitud = 300000   #m

I0 = np.conj(P)/(V0*m.sqrt(3))

###############IMPEDANCIA DE UNA FASE################
Zw_Previo = ((Rf + w*Lf*1j)/(Gf + w*Cf*1j))


Mod_Zw = m.sqrt(abs(Zw_Previo))
Fase_Zw = cm.phase(Zw_Previo)/2

#R = McosF
Real_Zw = Mod_Zw*np.cos(Fase_Zw)
#I = MsenF
Imag_Zw = Mod_Zw*np.sin(Fase_Zw)

Zw = Real_Zw + 1j*Imag_Zw
######################################################

##############CONSTANTE DE PROPAGACIÓN################
gamma_Previo = (Rf + 1j*w*Lf)*(Gf + 1j*w*Cf)

Mod_gamma = m.sqrt(abs(gamma_Previo))
Fase_gamma = cm.phase(gamma_Previo)/2

#R = McosF
Real_gamma = Mod_gamma*np.cos(Fase_gamma)
#I = MsenF
Imag_gamma = Mod_gamma*np.sin(Fase_gamma)

gamma = Real_gamma + 1j*Imag_gamma

######################################################

#xx = np.arange(1,300001,1)
#V = ((V0/m.sqrt(3))*np.cosh(gamma*xx))-(Zw*I0*np.sinh(gamma*xx))
#I = (I0*np.cosh(gamma*xx))-((V0*np.sinh(gamma*xx))/(Zw*m.sqrt(3)))
#mV = abs(V)
#mI = abs(I)
#pV = np.angle(V)
#pI = np.angle(I)

#otro, axs = plt.subplots(2,2)

#otro.suptitle('Parte 2 - Proyecto Apli 5')
#axs[0,0].grid()
#axs[0,0].plot(xx, mV,'tab:orange')
#axs[0,0].set_title('|V(x)|')
#axs[0,1].grid()
#axs[0,1].plot(xx, mI,'tab:green')
#axs[0,1].set_title('|I(x)|')
#xs[1,0].grid()
#axs[1,0].plot(xx, pV,'tab:red')
#axs[1,0].set_title('<V(x)')
#axs[1,1].grid()
#axs[1,1].plot(xx, pI)
#axs[1,1].set_title('<I(x)')
#plt.show()

#plt.plot(xx,Vxxx)
#plt.grid()
#plt.title('Voltaje[kV] vs Longitud[m]')
#plt.xlabel('Longitud[m]')
#plt.ylabel('V(x)[kV]')
#plt.xlim([0, 300000])
#plt.show()


#plt.plot(xx,Ixxx)
#plt.grid()
#plt.title('Corriente[kA] vs Longitud[m]')
#plt.xlabel('Longitud[m]')
#plt.ylabel('I(x)[kA]')
#plt.xlim([0, 300000])
#plt.show()

xx = 150000
V = ((V0/m.sqrt(3))*np.cosh(gamma*xx))-(Zw*I0*np.sinh(gamma*xx))
I = (I0*np.cosh(gamma*xx))-((V0*np.sinh(gamma*xx))/(Zw*m.sqrt(3)))

print('El voltaje en forma cartesiana en '+str(xx)+' metros es')
print(str(V))
print('\nLa corriente en forma cartesiana en '+str(xx)+' metros es')
print(str(I))

print('\nEl voltaje en forma polar en '+str(xx)+' metros es')
print('Magnitud,Fase')
print(str(abs(V))+','+str(np.angle(V)))
print('\nLa corriente en forma polar en '+str(xx)+' metros es')
print('Magnitud,Fase')
print(str(abs(I))+','+str(np.angle(I)))

xx = 300000
V = ((V0/m.sqrt(3))*np.cosh(gamma*xx))-(Zw*I0*np.sinh(gamma*xx))
I = (I0*np.cosh(gamma*xx))-((V0*np.sinh(gamma*xx))/(Zw*m.sqrt(3)))

print('El voltaje en forma cartesiana en '+str(xx)+' metros es')
print(str(V))
print('\nLa corriente en forma cartesiana en '+str(xx)+' metros es')
print(str(I))

print('\nEl voltaje en forma polar en '+str(xx)+' metros es')
print('Magnitud,Fase')
print(str(abs(V))+','+str(np.angle(V)))
print('\nLa corriente en forma polar en '+str(xx)+' metros es')
print('Magnitud,Fase')
print(str(abs(I))+','+str(np.angle(I)))

def Vx(x):
    return (V0/m.sqrt(3))*np.cosh(gamma*x) - Zw*I0*np.sinh(gamma*x)
    
def Ix(x):
    return I0*np.cosh(gamma*x) - (V0*np.sinh(gamma*x))/Zw*m.sqrt(3)


#print('Impedancia caracteristica de la linea Zw es \n'+str(Zw))
#print('El módulo de Zw es '+str(Mod_Zw))
#print('La fase de Zw es '+str(Fase_Zw))
#print('\nConstante de propagación de la linea Gamma es \n'+str(gamma))
#print('El módulo de Gamma es '+str(Mod_gamma))
#print('La fase de Gamma es '+str(Fase_gamma))


#x=np.arange(0,2*3.14168,0.01)
#y=np.sin(x)
#plot.plot(x,y)
#plot.show()
