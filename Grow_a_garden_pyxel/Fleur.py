import pyxel

'''
PLANT_LIFE = [300,500,900,1500,1950]
FLOWER_VALUE = [50,100,155,500,900]
PLANT_COLOR = ["rouge", "orange", "bleu", "rose", "violette"]

class Fleur:
    def __init__(self, x, y, fleurType):
        self.x = x
        self.y = y
        
        self.fleurType = fleurType
        self.fleurVie = PLANT_LIFE[fleurType]
        self.fleurValeur = FLOWER_VALUE[fleurType]
    
    def update(self, x, y):
        
        # Plante completement poussé  
        if self.fleurVie <= 0:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.x-4 <= x <= self.x+3 and self.y-6 <= y <= self.y+2:
                self.loot += self.fleurValeur
            pyxel.blt(self.x-3,self.y-6,1,0,8+16*self.fleurType,8,8,0)
            
            # Plante poussé à 2 tiers
            elif self.fleurVie < PLANT_LIFE[self.fleurType]/3:
                pyxel.blt(self.x-3,self.y-6,1,8,0+16*self.fleurType,8,8,0)
                plant[i][3] -= 1
            
            # Plante commence à poussé
            elif plant[i][3] < PLANT_LIFE[plant[i][4]] - 50:
                pyxel.blt(self.x-3,self.y-6,1,0,0+16*plant[i][4],8,8,0)
                plant[i][3] -= 1
                
            # Plante sous forme de graine
            elif plant[i][3] <= PLANT_LIFE[plant[i][4]]:
                pyxel.rect(plant[i][0],plant[i][1],2,2,plant[i][2])
                plant[i][3] -= 1     
        
'''



