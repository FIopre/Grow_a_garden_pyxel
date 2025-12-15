import pyxel

PLANT_LIFE = [300,500,900,1500,1950]
FLOWER_VALUE = [50,100,155,500,900]
PLANT_COLOR = ["rouge", "orange", "bleu", "rose", "violette"]

class pose_fleur:
    def __init__(self, x, y, fleur, fleurType):
        self.plant = fleur
        self.plantSelect = fleurType
        self.x = x
        self.y = y
        self.loot = 0
    
    def update(self, plantType):
        self.plantSelect = plantType
        self.x = pyxel.mouse_x
        self.y = pyxel.mouse_y
        
        self.draw(self.x, self.y, self.plant)
    
    def plante(self):        
        if self.contour(self.x,self.y):
            # position x, position y, couleur, duree de vie, type de plante
            self.plant.append([self.x,self.y,8,PLANT_LIFE[self.plantSelect],self.plantSelect])
            self.graine[PLANT_COLOR[self.plantSelect]] -= 1
        
    
    
    def draw(self, x, y, plant):
        #cadre pour les couleurs
        pyxel.rect(0,93,8,8,0)
        pyxel.rect(7,93,8,8,0)
        pyxel.rect(14,93,8,8,0)
        pyxel.rect(21,93,8,8,0)
        pyxel.rect(28,93,8,8,0)
        
        #carre de couleur
        pyxel.rect(1,94,6,6,8)      # plante rouge
        pyxel.rect(8,94,6,6,9)     # plante orage
        pyxel.rect(15,94,6,6,5)    # plante bleu
        pyxel.rect(22,94,6,6,14)    # plante rose
        pyxel.rect(29,94,6,6,2)    # plante violette
        
        # Ecris l'argent
        pyxel.text(1,1,str(self.loot),1)
        
        # Plante qui pousse
        for i in range(len(plant)):
            # Plante completement poussee 
            if plant[i][3] <= 0:
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and plant[i][0]-4 <= x <= plant[i][0]+3 and plant[i][1]-6 <= y <= plant[i][1]+2:
                    self.loot += FLOWER_VALUE[plant[i][4]]
                    plant.remove(plant[i]) # Supression de la plante
                    break
                pyxel.blt(plant[i][0]-3,plant[i][1]-6,1,0,8+16*plant[i][4],8,8,0)
            
            # Plante pousse a 2 tiers
            elif plant[i][3] < PLANT_LIFE[plant[i][4]]/3:
                pyxel.blt(plant[i][0]-3,plant[i][1]-6,1,8,0+16*plant[i][4],8,8,0)
                plant[i][3] -= 1
            
            # Plante commence a poussee
            elif plant[i][3] < PLANT_LIFE[plant[i][4]] - 50:
                pyxel.blt(plant[i][0]-3,plant[i][1]-6,1,0,0+16*plant[i][4],8,8,0)
                plant[i][3] -= 1
                
            # Plante sous forme de graine
            elif plant[i][3] <= PLANT_LIFE[plant[i][4]]:
                pyxel.rect(plant[i][0],plant[i][1],2,2,plant[i][2])
                plant[i][3] -= 1
    
    # Verifie le contour
    def contour(self, x, y):
        if (pyxel.pget(x,y) + pyxel.pget(x+2,y) + pyxel.pget(x-2,y) + pyxel.pget(x,y+2) + pyxel.pget(x,y-2) + pyxel.pget(x+2,y+2) + pyxel.pget(x+2,y-2) + pyxel.pget(x-2,y+2) + pyxel.pget(x-2,y-2) + pyxel.pget(x+3,y+1) + pyxel.pget(x+3,y-1) + pyxel.pget(x-3,y+1) + pyxel.pget(x-3,y-1) + pyxel.pget(x+1,y+3) + pyxel.pget(x-1,y+3) + pyxel.pget(x+1,y-3) + pyxel.pget(x-1,y-3) + pyxel.pget(x+3,y+3) + pyxel.pget(x+3,y-3) + pyxel.pget(x-3,y+3) + pyxel.pget(x-3,y-3) ) / 21 == 4:
            return True
        else:
            return False