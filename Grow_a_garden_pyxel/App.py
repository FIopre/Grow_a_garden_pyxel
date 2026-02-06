import pyxel

PLANT_COLOR = ["rouge", "orange", "bleu", "rose", "violette"]
PLANT_PRICE = [20,30,50,150,220]
PLANT_LIFE = [300,500,900,1500,1950]
PLANT_VALEUR = [50,100,155,500,900]

class Upgrade:
    def __init__(self):
        self.lvl_arrosoire = 1
        self.prix_arrosoire = [60, 1000, 20000, "Max"]
        
        self.lvl_angrais = 1
        self.prix_angrais = [1000, 5000, 50000, "Max"]
        
        self.lvl_sac = 1
        self.prix_sac = [200, 5000, 10000, "Max"]
        
        self.lvl_terrain = 1
        self.prix_terrain = [10000, 25000,50000, "Max"]

class Shop:
    def __init__(self):
        self.soil=True
        self.cam_x = 0
        self.cam_y = 0
    
    def Open(self):
        self.soil = not self.soil
        if self.soil == True:
            self.cam_x = 0
            self.cam_y = 0
        else:
            self.cam_x = 101
            self.cam_y = 101
        pyxel.camera(self.cam_x, self.cam_y)

class Hud:
    def update(self, argent, stat, graine, plantType):
        pyxel.cls(11)
        
        
        for i in range(4):
            pyxel.rectb(0, 0 + i*101, 101, 101, 6)
            pyxel.rect(1, 1 + i*101,99,99,4)
            
            # Cadre pour les couleurs
            pyxel.rect(0, 93 + i*101,8,8,0)
            pyxel.rect(7, 93 + i*101,8,8,0)
            pyxel.rect(14, 93 + i*101,8,8,0)
            pyxel.rect(21, 93 + i*101,8,8,0)
            pyxel.rect(28, 93 + i*101,8,8,0)
        
            # Carre de couleur
            pyxel.rect(1, 94 + i*101,6,6,8)      # plante rouge
            pyxel.rect(8, 94 + i*101,6,6,9)     # plante orage
            pyxel.rect(15, 94 + i*101,6,6,5)    # plante bleu
            pyxel.rect(22, 94 + i*101,6,6,14)    # plante rose
            pyxel.rect(29, 94 + i*101,6,6,2)    # plante violette
            
            # Place le bouton du shop
            pyxel.blt(85,85 + i*101,0,0,16, 16,16,0)
        
            # Ecris l'argent
            pyxel.text(2,2 + i*101,str(argent),1)
            
                    # Affiche le nombre de graine en fonction de la couleur selectionnee
            if plantType == 0:
                pyxel.text(2,87 + i*101,str(graine.graine["rouge"]),7)      # plante rouge
            elif plantType == 1:
                pyxel.text(9,87 + i*101,str(graine.graine["orange"]),7)    # plante orage
            elif plantType == 2:
                pyxel.text(16,87 + i*101,str(graine.graine["bleu"]),7)    # plante bleu
            elif plantType == 3:
                pyxel.text(23,87 + i*101,str(graine.graine["rose"]),7)    # plante rose
            elif plantType == 4:
                pyxel.text(30,87 + i*101,str(graine.graine["violette"]),7) # violette  

        # Shop
        pyxel.rect(101, 101, 101, 101, 6)

        
        # Bouton et argent exclusif au shop
        pyxel.text(103,103,str(argent),1)
        pyxel.blt(185,185,0,0,16, 16,16,0)
        
        #Arrosoir
        pyxel.blt(120,120,2,16*(stat.lvl_arrosoire-1),16,16,16,0)
        pyxel.text(170,125,str(stat.prix_arrosoire[stat.lvl_arrosoire-1]),1)
        
        #Engrais
        pyxel.blt(120,136,2,16*(stat.lvl_angrais-1),32,16,16,0)
        pyxel.text(170,141,str(stat.prix_angrais[stat.lvl_angrais-1]),1)
        
        #Sac
        pyxel.blt(120,152,2,16*(stat.lvl_sac-1),48,16,16,0)
        pyxel.text(170,157,str(stat.prix_sac[stat.lvl_sac-1]),1)
        
        #Terrain
        pyxel.blt(120,168,2,16*(stat.lvl_terrain-1),64,16,16,0)
        pyxel.text(170,173,str(stat.prix_terrain[stat.lvl_terrain-1]),1)

class Stock:
    def __init__(self):
        self.graine = {"rouge":0, "orange":0, "bleu":0, "rose":0, "violette":0}
        self.argent = 0
    
    def gagner_une_graine(self, typeFleur):
        match(typeFleur):
            case "rouge": self.graine["rouge"] += 1
            case "orange": self.graine["orange"] += 1
            case "bleu": self.graine["bleu"] += 1
            case "rose": self.graine["rose"] += 1
            case "violette": self.graine["violette"] += 1

class Fleur:
    def __init__(self, x, y, fleurType, fleurVie, vitesse):
        self.x = x
        self.y = y
        
        self.is_alive = True
        
        self.fleurType = fleurType
        self.fleurVie = fleurVie
        self.fleurMaxVie = fleurVie
        
        # Upgrade
        self.vitesse = vitesse
    
    def update(self, x, y):
        # Plante completement pousse 
        if self.fleurVie <= 0:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.x-4 <= x <= self.x+3 and self.y-6 <= y <= self.y+2:
                self.is_alive = False
            pyxel.blt(self.x-3,self.y-6,1,0,8+16*self.fleurType,8,8,0)
            
            # Plante pousse a 2 tiers
        elif self.fleurVie < self.fleurMaxVie/3:
            pyxel.blt(self.x-3,self.y-6,1,8,0+16*self.fleurType,8,8,0)
            self.fleurVie -= 1+self.vitesse
            
            # Plante commence a pousse 
        elif self.fleurVie < self.fleurMaxVie - 50:
            pyxel.blt(self.x-3,self.y-6,1,0,0+16*self.fleurType,8,8,0)
            self.fleurVie -= 1+self.vitesse
                
            # Plante sous forme de graine
        elif self.fleurVie <= self.fleurMaxVie:
            pyxel.rect(self.x, self.y, 2, 2, 8)
            self.fleurVie -= 1+self.vitesse




class App: 
    def __init__(self):
        pyxel.init(101, 101, title="Grow a garden")
        pyxel.mouse(True)
        pyxel.load("res.pyxres")
        
        self.fleurs = []
        self.plantType = 0
        
        self.graine = Stock() # Le stock de graine
        self.shop = Shop() # Le shop
        self.hud = Hud() # L'hud
        self.stat = Upgrade() # les niveau d'upgrade (lvl_arrosoire, lvl_angrais, lvl_sac, lvl_terrain)
        
        # Terrain select
        self.scene = 0
        
        # Instruction de demarage
        self.graine.gagner_une_graine("rouge")
        
        pyxel.run(self.update, self.draw)
    
    
    def update(self):
        # Ouvre et ferme le shop 
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and 85<=pyxel.mouse_x<=100 and 85<=pyxel.mouse_y<=100  :
            self.shop.Open()
        
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and 20<=pyxel.mouse_x<=67 and 20<=pyxel.mouse_y<=35 and self.shop.soil==False and self.stat.lvl_arrosoire < 4 and self.stat.prix_arrosoire[self.stat.lvl_arrosoire-1] <= self.graine.argent:
            
            self.graine.argent -= self.stat.prix_arrosoire[self.stat.lvl_arrosoire-1]
            self.stat.lvl_arrosoire = self.stat.lvl_arrosoire + 1
            
        elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and 20<=pyxel.mouse_x<=67 and 37<=pyxel.mouse_y<=51 and self.shop.soil==False and self.stat.lvl_angrais < 4 and self.stat.prix_angrais[self.stat.lvl_angrais-1] <= self.graine.argent:
            
            self.graine.argent -= self.stat.prix_angrais[self.stat.lvl_angrais-1]
            self.stat.lvl_angrais = self.stat.lvl_angrais + 1
            
        elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and 20<=pyxel.mouse_x<=67 and 53<=pyxel.mouse_y<=67 and self.shop.soil==False and self.stat.lvl_sac < 4 and self.stat.prix_sac[self.stat.lvl_sac-1] <= self.graine.argent :
            
            self.graine.argent -= self.stat.prix_sac[self.stat.lvl_sac-1]
            self.stat.lvl_sac = self.stat.lvl_sac + 1
            
        elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT) and 20<=pyxel.mouse_x<=67 and 68<=pyxel.mouse_y<=83 and self.shop.soil==False and self.stat.lvl_terrain < 4 and self.stat.prix_terrain[self.stat.lvl_terrain-1] <= self.graine.argent:
            
            self.graine.argent -= self.stat.prix_terrain[self.stat.lvl_terrain-1]
            self.stat.lvl_terrain = self.stat.lvl_terrain + 1
        
        
        # Update l'hud 
        self.hud.update(self.graine.argent, self.stat, self.graine, self.plantType)
        
        # Ajoute une graine si les ressources sont suffisantes et qu'il en a mois que le nombre de graine max par sacher
        if pyxel.btnp(pyxel.KEY_A) and self.graine.argent >= PLANT_PRICE[self.plantType] and self.graine.graine[PLANT_COLOR[self.plantType]] < 10 * self.stat.lvl_sac:
            self.graine.argent -= PLANT_PRICE[self.plantType]
            self.graine.gagner_une_graine(PLANT_COLOR[self.plantType])
        
        # Trace les fleurs
        for fleur in self.fleurs:
            if(fleur.is_alive):
                fleur.update(pyxel.mouse_x, pyxel.mouse_y+self.scene*101)
        
        # Detruit la fleur et ajoute sa valeur
        for fleur in self.fleurs:
            if(not fleur.is_alive):
                self.graine.argent += PLANT_VALEUR[fleur.fleurType] * self.stat.lvl_angrais
                self.fleurs.remove(fleur)         
        
        self.selectType()
        
        
        # Bouton pour les differents terrains
        if pyxel.btn(pyxel.KEY_1):
            pyxel.camera(0,0)
            self.scene = 0
        elif pyxel.btn(pyxel.KEY_2) and self.stat.lvl_terrain >= 2:
            pyxel.camera(0,101)
            self.scene = 1
        elif pyxel.btn(pyxel.KEY_3) and self.stat.lvl_terrain >= 3:
            pyxel.camera(0,202)
            self.scene = 2
        elif pyxel.btn(pyxel.KEY_4) and self.stat.lvl_terrain >= 4:
            pyxel.camera(0,303)
            self.scene = 3
            
        # Pose une fleur
        if pyxel.btn(pyxel.KEY_S) and self.graine.graine[PLANT_COLOR[self.plantType]] > 0:            
            if(self.contour(pyxel.mouse_x, pyxel.mouse_y)):
                self.fleurs.append(Fleur(pyxel.mouse_x, pyxel.mouse_y+self.scene*101, self.plantType, PLANT_LIFE[self.plantType], self.stat.lvl_arrosoire))
                self.graine.graine[PLANT_COLOR[self.plantType]] -= 1
        
    
    def draw(self):
        pass
            
    # Selection des fleurs
    def selectType(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 8:
                self.plantType = 0
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 9:
                self.plantType = 1
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 5:
                self.plantType = 2
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 14:
                self.plantType = 3
            if pyxel.pget(pyxel.mouse_x, pyxel.mouse_y) == 2:
                self.plantType = 4

    # Verifie le contour
    def contour(self, x, y):
        if (pyxel.pget(x,y) + pyxel.pget(x+2,y) + pyxel.pget(x-2,y) + pyxel.pget(x,y+2) + pyxel.pget(x,y-2) + pyxel.pget(x+2,y+2) + pyxel.pget(x+2,y-2) + pyxel.pget(x-2,y+2) + pyxel.pget(x-2,y-2) + pyxel.pget(x+3,y+1) + pyxel.pget(x+3,y-1) + pyxel.pget(x-3,y+1) + pyxel.pget(x-3,y-1) + pyxel.pget(x+1,y+3) + pyxel.pget(x-1,y+3) + pyxel.pget(x+1,y-3) + pyxel.pget(x-1,y-3) + pyxel.pget(x+3,y+3) + pyxel.pget(x+3,y-3) + pyxel.pget(x-3,y+3) + pyxel.pget(x-3,y-3) ) / 21 == 4:
            return True
        else:
            return False

App()