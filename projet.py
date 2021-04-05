from tkinter import * 
import tkinter as tk
import random
import math
import numpy as np
import time

Passe = True
Arret = True 
angle = random.uniform(0,2*math.pi) 
Rayon = 150
c = 0  
tps = 50

def masseG() : 
    global Rayon
    Rayon = 200
    tps = 60
def masseP() : 
    global Rayon
    Rayon = 120
    tps = 45

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
        if (seconds == tps): #Choisi quand l'étoile s'arrète de se former . 
            Passe = True  
        elif(minutes == 2) : 
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
    global Arret,Passe
    t = random.uniform(0,2*math.pi)
    R = random.uniform(0,Rayon)
    x = R*math.cos(t) + Largeur/2
    y = R*math.sin(t) + Hauteur/2 
    if Arret == False and Passe == False :
        r = 2
        oval = Canevas.create_oval(x-r, y-r, x+r, y+r, outline='white', fill='white')
        # appel de la fonction Cercle() après une pause de 1 millisecondes
        Mafenetre.after(1,Cercle)
    elif Arret == False and Passe == True :  
        r = 8 
        oval = Canevas.create_oval(x-r, y-r, x+r, y+r, outline='light blue', fill='light blue')
        # appel de la fonction Cercle() après une pause de 20 millisecondes
        Mafenetre.after(20,Cercle)

def pied() : 
    global Arret,Passe
    L=[] 
    for i in range(0,8) : 
        L.append(i*math.pi/4 + angle)
    d = random.randint(0,7)
    x0 = Rayon*math.cos(L[d]) + Largeur/2
    y0 = Rayon*math.sin(L[d]) + Hauteur/2 
    t = random.uniform(0,math.pi)
    R = random.uniform(0,Rayon/2)  
    m = random.choice([0,2])
    x = x0 + m + R*math.cos(L[d])*math.tan(t)
    y = y0 + m + R*math.sin(L[d])*math.tan(t) 
    r = 2
    Canevas.create_oval(x-r, y-r, x+r, y+r, outline='white', fill='white')
    if Arret == False and Passe == False:
        Mafenetre.after(1,pied)
        
def Pause():
    """" Met en pause l'animation"""
    global Arret
    sw.Stop()
    Arret = True

def Demarrer(): 
    """ Démarre l'animation """ 
    global Arret,Passe,c
    Canevas.delete(ALL)
    if (c>1):
        sw.Reset()
        c = 0 
    sw.Start()
    Arret = False
    Passe = False
    Cercle() # un seul appel à cette fonction
    pied() 
        
def Reprendre():
    """" Permet de reprendre l'animation"""
    global Arret 
    sw.Start()
    Arret = False
    Cercle()
    pied()
    
# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Animation')

# Création d'un widget Canvas
Largeur = 700
Hauteur = 700
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='black')
Canevas.pack(padx =5, pady =5)
sw = StopWatch(Mafenetre)
sw.pack(side = TOP)

#création des boutons 
Boutonmasse1 = Button(Mafenetre,text="Masse > 1,989 × 10^30 kg", command = masseG)
Boutonmasse1.pack(side = RIGHT,padx=10,pady=10) 

Boutonmasse2 = Button(Mafenetre,text="Masse < 1,989 × 10^30 kg", command = masseP)
Boutonmasse2.pack(side = RIGHT,padx=10,pady=10)
# Création d'un widget Button (bouton Démarrer)
BoutonGo = Button(Mafenetre, text ='Démarrer', command = Demarrer)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button (bouton Pause)
BoutonArreter = Button(Mafenetre, text ='Pause', command = Pause)
BoutonArreter.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Reprendre)
Button(Mafenetre, text='Reprendre', command=Reprendre).pack(side=LEFT)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)
Mafenetre.mainloop()

