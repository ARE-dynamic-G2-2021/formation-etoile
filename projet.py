from tkinter import * 
import tkinter as tk
import random
import math
import numpy as np
import time


Pause = True 
Arret = True 
angle = random.uniform(0,2*math.pi) 
Rayon = 80
c = 0 
s = 15
Largeur = 700
Hauteur = 700
X0 = Largeur/2
Y0 = Hauteur/2   
TEMP = 55538

def masseG() : 
    global Rayon,s
    if Arret == True : 
        Rayon = 100
        s = 20
    
def masseP() : 
    global Rayon,s
    if Arret == True : 
        Rayon = 60 
        s = 10  
    
class StopWatch(Frame):  
    """ Implémentation du chronomètre """                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()              
        self.makeWidgets()      

    def makeWidgets(self):                        
        """Crée l'étiquette du  chronomètre """
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)                      
   
    def _update(self):
        """ Met à jour l'étiquette du chronomètre  """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
        
    def _setTime(self, elap):
        """ Définit le temps """
        global Arret,Passe,c
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        c+=1
        if (seconds == s): #Choisi quand l'étoile s'arrète de se former . 
            Arret = True
            
            
    def Stop(self):                                    
        """ Arrête le chronomètre  """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
            
    def Reset(self):                                  
        """ Reset le chronomètre """
        self._start = time.time()        
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)
              
    def Start(self):                                                    
        """ Lance le chronomère """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1
def Cercle():
    """ Dessine un cercle de centre (x,y) et de rayon r """
    global Arret,Pause,ovale,bloque
    t = random.uniform(0,2*math.pi)
    R = random.uniform(0,Rayon)
    x = R*math.cos(t) + Largeur/2
    y = R*math.sin(t) + Hauteur/2 
    if Arret == False and Pause == False :
        r = 2
        oval = Canevas.create_oval(x-r, y-r, x+r, y+r, outline='white', fill='white')
        #appel de la fonction Cercle() après une pause de 1 millisecondes
        Mafenetre.after(1,Cercle)
    elif Arret == True and Pause == False: 
        ovale = Canevas.create_oval(X0-Rayon-2,Y0-Rayon-2,X0+Rayon+2,Y0+Rayon+2,outline = "white",fill="white")
        Temp() 
        Mafenetre.after(1,Cercle)

def Temp() :  
    global ovale,Pause
    sw.Stop()
    Pause = True 
    if float(temp.get()) >= 1649 and float(temp.get()) <= 3316 : 
        Canevas.itemconfigure(ovale,outline="red",fill = "red")
    elif float(temp.get()) > 3316 and float(temp.get()) <= 4704:
        Canevas.itemconfigure(ovale,outline="orange",fill = "orange")
    elif float(temp.get()) > 4704 and float(temp.get()) <= 5816 : 
        Canevas.itemconfigure(ovale,outline="light yellow",fill = "light yellow")
    elif float(temp.get()) > 5816 and float(temp.get()) <= 9704 : 
        Canevas.itemconfigure(ovale,outline="white",fill = "white")
    elif float(temp.get()) > 9704 and float(temp.get()) <= 27760: 
        Canevas.itemconfigure(ovale,outline="light blue",fill = "light blue")
    else : 
        Canevas.itemconfigure(ovale,outline="blue",fill = "Blue")
        
def pied() : 
    global Arret,Pause
    L=[] 
    for i in range(0,4) : 
        L.append(i*math.pi/2 + angle)
    d = random.randint(0,3)
    x0 = Rayon*math.cos(L[d]) + Largeur/2
    y0 = Rayon*math.sin(L[d]) + Hauteur/2 
    t = random.uniform(0,math.pi)
    R = random.uniform(0,Rayon/2)  
    m = random.choice([0,2])
    x = x0 + m + R*math.cos(L[d])*math.tan(t)
    y = y0 + m + R*math.sin(L[d])*math.tan(t) 
    r = 2
    Canevas.create_oval(x-r, y-r, x+r, y+r, outline='white', fill='white')
    if Arret == False and Pause == False:
        Mafenetre.after(1,pied)
        
def Pause():
    """" Met en pause l'animation"""
    global Pause
    sw.Stop()
    Pause = True

def Demarrer(): 
    """ Démarre l'animation """ 
    global Arret,Pause,c
    Canevas.delete(ALL)
    if (c>1):
        sw.Reset()
        c = 0 
    sw.Start()
    Pause = False
    Arret = False
    Cercle() # un seul appel à cette fonction
    pied() 
    
        
def Reprendre():
    """" Permet de reprendre l'animation"""
    global Pause
    sw.Start()
    Pause = False
    Cercle()
    pied()

    
#Temp()
# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Animation')

# Création d'un widget Canvas
Largeur = 700
Hauteur = 700
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='black')
Canevas.pack(side = LEFT, padx =5, pady =5)
sw = StopWatch(Mafenetre)
sw.pack(side = TOP) 


#création des boutons de Masse
Boutonmasse1 = Button(Mafenetre,text="Masse > 1,989 × 10^30 kg", command = masseG,activebackground= "light blue",bg = "light blue")
Boutonmasse1.pack(padx=5,pady=5) 

Boutonmasse2 = Button(Mafenetre,text="Masse < 1,989 × 10^30 kg", command = masseP,activebackground= "light blue",bg = "light blue")
Boutonmasse2.pack(padx=10,pady=10)
# Création d'un widget Button (bouton Démarrer)
BoutonGo = Button(Mafenetre, text ='Démarrer', command = Demarrer,activebackground= "light green",bg = "light green")
BoutonGo.pack(padx = 10, pady = 15)

# Création d'un widget Button (bouton Pause)
BoutonArreter = Button(Mafenetre, text ='Pause', command = Pause,activebackground= "red",bg = "red")
BoutonArreter.pack(padx = 5, pady = 20)

# Création d'un widget Button (bouton Reprendre)
Button(Mafenetre, text='Reprendre', command=Reprendre,activebackground= "light yellow",bg = "light yellow").pack(padx = 15,pady= 20)

# Création d'un widget température
temp = tk.StringVar()
temp.set(5000)
widget_temp = tk.Scale(Mafenetre,from_=1649,to=TEMP,resolution=1,orient=tk.HORIZONTAL,\
length=300,width=20,label="Temperature",tickinterval=0.2,variable=temp)#,command=maj)
widget_temp.pack(padx=10,pady=10)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy,activebackground= "white",bg = "white")
BoutonQuitter.pack(side = BOTTOM, padx = 15, pady = 20)
Mafenetre.mainloop()
