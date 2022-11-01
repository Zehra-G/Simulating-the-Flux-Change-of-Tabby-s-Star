'''Zehra Gundogdu
CS152 A
12/10/2021
Final Project
Simulation of Tabby's Star'''

'''This code simulates how the flux of Tabby's Star changes over time. Flux data is taken from NASA website. No additional command line arguments necessary to run this code. After you run the code, click to exit out of the simulation.'''

import graphicsPlus as gr
import time
import random

win =gr.GraphWin("Tabby's Star Simulation", 500, 500) #the window for the simulation

'''This is the parent class for all objects in the background.'''

class Celestial:
    def __init__(self, win, the_type):
        self.type = the_type
        self.win = win
        self.scale = 10
        self.position = [win.getWidth()/(2*self.scale),win.getHeight()/(2*self.scale)]
        self.vis = []

    def getType(self): #returns the type of the object
        return self.type

    def getScale(self): #returns the scale of the object
        return self.scale

    def getPosition(self): # returns a 2-element tuple with the x, y position.
        return (self.position[0], self.position[1])

    def draw(self): #draws the objects in the self.vis list into the window
        for item in self.vis:
            item.draw(self.win)
        self.drawn = True

    def undraw(self): #undraws the objects in the self.vis list
        for item in self.vis:
            item.undraw()
        self.drawn = False

    def setPosition(self, px, py): #sets the position of the object to a px and py
        dx = px - self.position[0]
        dy = py - self.position[1]

        self.position[0] = px
        self.position[1] = py
        dx = dx*self.scale
        dy = dy*self.scale*(-1)
        for item in self.vis:
            item.move(dx,dy)


'''This is the class that inherits from Celestial class and creates moving shooting star image objects.'''
class ShootingStar(Celestial):
    def __init__(self, win):
        Celestial.__init__(self, win, "shooting star")
        self.refresh()

    def refresh(self): #this method draws the image object into the window
        self.vis = [gr.Image(gr.Point(50, 100), "shootingstar.gif")]
        self.vis[0].draw(win)

    def move(self): #this method moves the shooting star to random positions on the window, displays it for a given time and undraws them.
        for i in self.vis:
            dx= random.randint(-500, 500)
            dy = random.randint(-500, 500)
            i.move(dx, dy)
            time.sleep(0.01)
            i.undraw()


'''This is the Galaxy class that inherits from the Celestial class which is the class for spinning galaxy image objects that might be added to the simulation in the future.'''
class Galaxy(Celestial):
    def __init__(self, win, x0=0, y0= 0, Ax= None, Ay= None):
        Celestial.__init__(self, win, "Galaxy")
        self.position = [x0, y0]

        self.angle = 0.0
        self.rvel = 0.0

        '''The anchor point is the point of which the object spins about.'''
        if Ax != None and Ay != None:
            self.anchor = [Ax, Ay]
        else:
            self.anchor = [x0, y0]
        self.drawn = False

    def refresh(self):
        drawn = self.drawn
        if drawn:
            self.undraw()
       
        if drawn:
            self.draw()

    '''getter and setter methods for the angle and the anchor point below'''
    def getAngle(self):
        return self.angle

    def setAngle(self, angle):
        self.angle = angle
        self.refresh()

    def rotate(self, angleToMove):
        self.angle += angleToMove
        self.refresh()

    def getAnchor(self):
        return self.anchor


''' The lists created below reading data from the data file hold the flux and the time data in the data file'''

fp= open("TabbysStarFlux.csv", "r") #TabbysStarFlux.csv is the data filed used for this project.
line = fp.readline()[1:]

#Here, tabbydata is the list that holds all entries in the TabbyStarFlux.csv file.
tabbydata = []
for line in fp:
    words = line.split(",")
    tabbydata.append(words)
    
#tabbytime is the list that holds the time values for every entry in tabbydata.
tabbytime = []
for entry in tabbydata:
    tabbytime.append(float(entry[0]))
    
#tabbyflux is the list that holds the flux values for every entry in tabbydata.
tabbyflux = []
for entry in tabbydata:
    tabbyflux.append(float(entry[1]))

tabbyfluxsorted = sorted(tabbyflux, key=float) #this list was used to divide flux values to ten categories according to magnitude.

#timedifferences is the list that holds the differences between consecutive time values.
timedifferences = []
for i in range(len(tabbytime)-1):
    difference = float(tabbytime[i+1]) - float(tabbytime[i])
    timedifferences.append(difference)

tdsorted = sorted(timedifferences, key=float) #this list was used to divide time differences to ten categories according to how long of a time difference they are.

fp.close()


'''This recursive function takes in a list of values and returns their mean.'''
def calc_mean(values):  
    if len(values) == 1:  
        return values[0]  
    else:  
        n = len(values)
        return (values[0] + (n - 1) * calc_mean(values[1:])) / n  

'''This function takes in a list of values and returns a tuple containing the maximum value and its index'''
def maxvalue(values):
    max = -325534
    for i in range (len(values)):
        if values[i] >= max:
            max = values[i]
            maxindex = i
    return (max, maxindex)

'''Below, I divided the sorted flux list to ten groups according to the values and created a limitvalues list which holds the flux conditions for each tabbystar image (there are 10 of them).'''
limitvalues = []
for i in range (1,10):
    limitvalues.append(tabbyfluxsorted[i*int(len(tabbyfluxsorted)/10)])

'''Below, I divided the sorted time differences list to ten groups according to the values and created a limitvaluestime list which holds the time difference conditions for each display time (there are 10 of them).'''
limitvaluestime = []
for i in range(1, 10):
    limitvaluestime.append(tdsorted[i*int(len(tdsorted)/10)])

def main():

    win.setBackground("black")

    '''Below are the image objects that I created to simulate Tabby's Star, only their sizes are different.'''
    tabbyimage1 = gr.Image(gr.Point(250,250), "tabby1.png")
    tabbyimage2 = gr.Image(gr.Point(250,250), "tabby2.png")
    tabbyimage3 = gr.Image(gr.Point(250,250), "tabby3.png")
    tabbyimage4 = gr.Image(gr.Point(250,250), "tabby4.png")
    tabbyimage5 = gr.Image(gr.Point(250,250), "tabby5.png")
    tabbyimage6 = gr.Image(gr.Point(250,250), "tabby6.png")
    tabbyimage7 = gr.Image(gr.Point(250,250), "tabby7.png")
    tabbyimage8 = gr.Image(gr.Point(250,250), "tabby8.png")
    tabbyimage9 = gr.Image(gr.Point(250,250), "tabby9.png")
    tabbyimage10 = gr.Image(gr.Point(250,250), "tabby10.png")

    '''Below are the text objects that display the mean and maximum flux values'''
    meantext = gr.Text(gr.Point(100,100), "Mean Flux Value = " + str(calc_mean(tabbyflux)))
    meantext.setTextColor("white")
    meantext.setSize(8)

    maxtext = gr.Text(gr.Point(100,110), "Maximum Flux Value = " + str(maxvalue(tabbyflux)))
    maxtext.setTextColor("white")
    maxtext.setSize(8)

    meantext.draw(win)
    maxtext.draw(win)
    
    '''This for loop goes through each element in tabbyflux list and creates the appropriate visual for it & displays its value and the time that it had occured.'''
    for i in range (len(tabbyflux)):
        fluxtext = gr.Text(gr.Point(100,50), "FLUX = " + str(tabbyflux[i]))
        fluxtext.setTextColor("white")
        fluxtext.setSize(15)
        fluxtext.setStyle("bold italic")
        timetext = gr.Text(gr.Point(100,75), "TIME = " + str(tabbytime[i]))
        timetext.setTextColor("white")
        timetext.setSize(15)
        timetext.setStyle("bold italic")

        '''Conditionals below place the flux value into the appropriate flux category comparing it with the limits of the categories & draws the image object associated with that category into the window.'''

        if tabbyflux[i] <= limitvalues[0]:
            tabbyimage1.draw(win)
            image = tabbyimage1
            fluxtext.draw(win)
            timetext.draw(win)
        elif tabbyflux[i] > limitvalues[0] and tabbyflux[i] <= limitvalues[1]:
            tabbyimage2.draw(win)
            image = tabbyimage2
            fluxtext.draw(win)
            timetext.draw(win)
        elif tabbyflux[i] > limitvalues[1] and tabbyflux[i] <= limitvalues[2]:
            tabbyimage3.draw(win)
            image = tabbyimage3
            fluxtext.draw(win)
            timetext.draw(win)
        elif tabbyflux[i] > limitvalues[2] and tabbyflux[i] <= limitvalues[3]:
            tabbyimage4.draw(win)
            image = tabbyimage4
            fluxtext.draw(win)
            timetext.draw(win)
        elif tabbyflux[i] > limitvalues[3] and tabbyflux[i] <= limitvalues[4]:
            tabbyimage5.draw(win)
            image = tabbyimage5
            fluxtext.draw(win)
            timetext.draw(win)
        elif tabbyflux[i] > limitvalues[4] and tabbyflux[i] <= limitvalues[5]:
            tabbyimage6.draw(win)
            image = tabbyimage6
            fluxtext.draw(win)
            timetext.draw(win)
        elif tabbyflux[i] > limitvalues[5] and tabbyflux[i] <= limitvalues[6]:
            tabbyimage7.draw(win)
            image = tabbyimage7
            fluxtext.draw(win)
            timetext.draw(win)
        elif tabbyflux[i] > limitvalues[6] and tabbyflux[i] <= limitvalues[7]:
            tabbyimage8.draw(win)
            image = tabbyimage8
            fluxtext.draw(win)
            timetext.draw(win)
        elif tabbyflux[i] > limitvalues[7] and tabbyflux[i] <= limitvalues[8]:
            tabbyimage9.draw(win)
            image = tabbyimage9
            fluxtext.draw(win)
            timetext.draw(win)
        elif tabbyflux[i] > limitvalues[8]:
            tabbyimage10.draw(win)
            image = tabbyimage10
            fluxtext.draw(win)
            timetext.draw(win)

        for i in range (5): #This for loop draws shooting stars into the window moving the shooting star class object
            shootingstar = ShootingStar(win)
            shootingstar.move()

        '''Conditionals below place the time difference value into the appropriate time difference category comparing it with the limits of the categories & displays the image object for the amount of time associated with that category.'''

        if i == 0: #this is the special condition for the first list entry
            time.sleep(0.03)
            image.undraw()
            fluxtext.undraw()
            timetext.undraw()
        if i == len(tabbytime)-1: #this is the special condition for the last list entry
            time.sleep(0.03)
            image.undraw()
            fluxtext.undraw()
            timetext.undraw()
           
        else:
            if tabbytime[i+1] - tabbytime[i] <= limitvaluestime[0]:
                time.sleep(0.03)
                image.undraw()
                fluxtext.undraw()
                timetext.undraw()
            elif tabbytime[i+1] - tabbytime[i] > limitvaluestime[0] and tabbytime[i+1] - tabbytime[i] <= limitvaluestime[1]:
                time.sleep(0.05)
                image.undraw()
                fluxtext.undraw()
                timetext.undraw()
            elif tabbytime[i+1] - tabbytime[i] > limitvaluestime[1] and tabbytime[i+1] - tabbytime[i] <= limitvaluestime[2]:
                time.sleep(0.07)
                image.undraw()
                fluxtext.undraw()
                timetext.undraw()
            elif tabbytime[i+1] - tabbytime[i] > limitvaluestime[2] and tabbytime[i+1] - tabbytime[i] <= limitvaluestime[3]:
                time.sleep(0.09)
                image.undraw()
                fluxtext.undraw()
                timetext.undraw()
            elif tabbytime[i+1] - tabbytime[i] > limitvaluestime[3] and tabbytime[i+1] - tabbytime[i] <= limitvaluestime[4]:
                time.sleep(0.11)
                image.undraw()
                fluxtext.undraw()
                timetext.undraw()
            elif tabbytime[i+1] - tabbytime[i] > limitvaluestime[4] and tabbytime[i+1] - tabbytime[i] <= limitvaluestime[5]:
                time.sleep(0.13)
                image.undraw()
                fluxtext.undraw()
                timetext.undraw()
            elif tabbytime[i+1] - tabbytime[i] > limitvaluestime[5] and tabbytime[i+1] - tabbytime[i] <= limitvaluestime[6]:
                time.sleep(0.15)
                image.undraw()
                fluxtext.undraw()
                timetext.undraw()
            elif tabbytime[i+1] - tabbytime[i] > limitvaluestime[6] and tabbytime[i+1] - tabbytime[i] <= limitvaluestime[7]:
                time.sleep(0.17)
                image.undraw()
                fluxtext.undraw()
                timetext.undraw()
            elif tabbytime[i+1] - tabbytime[i] > limitvaluestime[7] and tabbytime[i+1] - tabbytime[i] <= limitvaluestime[8]:
                time.sleep(0.2)
                image.undraw()
                fluxtext.undraw()
                timetext.undraw()
            elif tabbytime[i+1] - tabbytime[i] > limitvaluestime[8]:
                time.sleep(0.23)
                image.undraw()
                fluxtext.undraw()
                timetext.undraw()

    win.getMouse() #exit out of the window by clicking
    win.close()

if __name__ == "__main__":
    main()






