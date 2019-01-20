###dissorg 1.0

##with neighborhood convergence
##with movement, attraction/rejection

##to add: no-go-zones, carioca placers, different levels of imitativity


##import libraries:
from random import *
from time import *
from tkinter import *
from uuid import *


##set up base variables
mapsize = 500
unitsize = 20
section = int(mapsize/unitsize)
stages = ["Papaya Whip", "Chartreuse", "Peru", "Orchid", "Steel Blue"]
squares = []

##set up canvas (stage 1)
master = Tk()
cvs = Canvas(master, width=mapsize, height=mapsize, bg="Slate Gray")
cvs.pack()
cvs.create_line(0, mapsize/2, mapsize, mapsize/2, fill="#d3d3d3")
cvs.create_line(mapsize/2, 0, mapsize/2, mapsize, fill="#d3d3d3")
cvs.create_line(0, 0, unitsize, unitsize, fill="#476042")

##create background functions

def populate():

    print("populating")
    
    global squares
    squares = []
    cindex = 0
    #sqindex is the index position in the list of squares
    for x in range(0, mapsize, unitsize):
        for y in range(0, mapsize, unitsize):
            squares.append(Square(x, y, choice(stages), str(x) + "_" + str(y), [], cindex, {}))
            cindex += 1
            
    for square in squares:
        square.draw()

    print("populated")
    print("_________________________")

def sensearound(square):
    neighbors = []
    for i in range(-1, 2):
        for p in range(-1, 2):
            neighbors.append(str(square.posx + i*unitsize) + "_" + str(square.posy + p*unitsize))
    #print(neighbors)
    return neighbors
    ### TO ADD: clear up negative neighbors and itself from list

def react():
    for square in squares:
        square.basereact()
    for square in squares:
        square.basechange()


##create helper functions

def neighborhood(ID):
    return

##create agents

class Square():
    def __init__(self, posx, posy, stage, ID, neigh, sqindex, neighstages):
        self.posx = posx
        self.posy= posy
        self.stage = stage
        self.ID = ID
        self.neigh = neigh
        self.sqindex = sqindex
        self.neighstages = neighstages
        self.neigh = sensearound(self)

    def draw(self):
        cvs.delete(self.ID)
        cvs.create_rectangle(self.posx, self.posy, self.posx+unitsize, self.posy+unitsize, fill=self.stage, tag=self.ID)
        

    
    def basereact(self):
        
        #print("around me in basereact")
        #print(self.neigh)
        self.neighstages = {"Papaya Whip":0, "Chartreuse":0, "Peru":0, "Orchid":0, "Steel Blue":0}


        count = 0
        for square in squares:
            if square.ID in self.neigh:
                
                #print(self.ID)
                #print("is checking around and found neigh")
                #print(square.ID)
                #print(self.neigh)
                count += 1
                #print(square.stage)
                if square.stage == "Papaya Whip":
                    self.neighstages["Papaya Whip"] += 1
                elif square.stage == "Chartreuse":
                    self.neighstages["Chartreuse"] += 1
                elif square.stage == "Peru":
                    self.neighstages["Peru"] += 1
                elif square.stage == "Orchid":
                    self.neighstages["Orchid"] += 1
                elif square.stage == "Steel Blue":
                    self.neighstages["Steel Blue"] += 1
                else:
                    print("error -- no color/stage on neigh")        
        #print(count)
        #print(count)
        #print(count)
        #print(count)
        #print(self.neighstages)
        #print(count)
        #print(count)
        #print(count)
        #print(max(neighstages, key=neighstages.get))

    def basechange(self):
        self.stage = (max(self.neighstages, key=self.neighstages.get))
        self.draw()
        self.neighstages = {}
        #print ("i changed")
        #print ("i'm empty")
        #print(self.neighstages)



            
##            if n.stage == "Papaya Whip":
##                papy += 1
##                print("papy +1")
##            if n.stage == "Chartreuse":
##                chrt += 1
##            if n.stage == "Peru":
##                peru += 1
##
##        if papy > chrt and papy > peru:
##            self.stage = "Papaya Whip"
##        if chrt > papy and chrt > peru:
##            self.stage = "Chartreuse"
##        if peru > papy and peru > chrt:
##            self.stage = "Papaya Whip"

        self.draw()


        
populate()

print("__________")
print("end tests")
testindex = 2
print(len(squares))
print(squares[testindex].sqindex)





##set up canvas (stage 2)
#buttons
Button(master, text="populate", command=populate).pack(side=LEFT)
Button(master, text="react", command=react).pack(side=LEFT)
mainloop()
