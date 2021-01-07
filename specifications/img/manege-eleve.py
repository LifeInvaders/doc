"""
===========================
The double pendulum problem
===========================

This animation illustrates the double pendulum problem.
"""

# Double pendulum formula translated from the C code at
# http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


R1 = 5.58 # 
R2 = 2.29 # 

# 
Tmax=6     # durée de simulation
dt = 0.01  # intervalle de temps

t = np.arange(0.0, Tmax, dt) # liste des temps

th1 = 0.0    # Position initiale
w10 = 1.11   # Vitesse de rotation en rad/s du bras par rapport au sol
th2 = 0.0    # Position initiale
w21 = -2.22 # Q2- Q3: Vitesse de rotation des nacelles par rapport au bras  

#Coordonnées du point A dans R0
xA = R1*np.cos(w10*t)
yA = R1*np.sin(w10*t)


# Q2- Q3: Coordonnées du vecteur AB, à modifier
ABx=R2*np.cos(w10*t)
ABy=R2*np.sin((-w10)*t)


#Coordonnées du point  B dans R0 ( à modifier)
xB =xA+ABx
yB =yA-ABy





# Q6 - Fonction à écrire 
def deriv(T,L):
    De=[0]# à définir 
    De=De+[(L[k]-L[k-1])/dt  for k in range(1,len(L))]
    return De

# Q7
VBx=deriv(t,xB)
VBy=deriv(t,yB)
VAx=deriv(t,xA)  # J'ajoute les composantes de la vitesse du point A
VAy=deriv(t,yA)
AcBy=deriv(t,VBy) # Ici les composantes de l'accélération du point B
AcBx=deriv(t,VBx)

# Définition de la figure supérieure (animation)
# Ne pas modifier
fig = plt.figure(figsize=(8, 12))
ax = fig.add_subplot(211, autoscale_on='true', xlim=(-8, 8), ylim=(-8, 8))
ax.grid()

line, = ax.plot([], [], 'ro-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
# Ne pas modifier
def init():
    time_text.set_text('')
    return line, time_text



# Q9
def animate(i):
    Px = [0, xA[i], xB[i]] #coordonnées des segments OAB sur x
    Py = [0, yA[i], yB[i]]  #coordonnées des segments OAB sur y
    line.set_data(Px, Py)
    # arrow permet de dessiner une flèche
    # les 2 premiers paramètres sont les coordonnées du point de départ (x, y)
    # les deux suivant les projections du vecteur sur x et y (VBx, VBy)
    #ne pas nodifier les autres!
    VecteurV = ax.arrow(xB[i],yB[i],VBx[i],VBy[i], fc="k", ec="k",head_width=0.5, head_length=1)
    VecteurV2 = ax.arrow(xB[i],yB[i],AcBx[i],AcBy[i], fc="k", ec="k",head_width=0.5, head_length=1) #Accélération au point B
    VecteurV3 = ax.arrow(xA[i],yA[i],VAx[i],VAy[i], fc="k", ec="k",head_width=0.5, head_length=1) #Vitesse au point A
    
    time_text.set_text(time_template % (i*dt))
    return line, VecteurV, VecteurV2, VecteurV3, time_text
  

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(yA)),
                              interval=50, blit=True, init_func=init)

# Q4 - Tracé de la trajectoire
ax.plot(xA,yA)
ax.plot(xB,yB)

# Q8 - Définition de la figure inféreure (courbes)

ax2 = fig.add_subplot(212, autoscale_on=False, xlim=(0,Tmax), ylim=(-8, 8))
ax2.grid()
ax2.plot(t,yB)

#ani.save('manege.mp4', fps=15)
plt.show()

