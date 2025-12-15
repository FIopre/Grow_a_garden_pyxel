import pyxel
import Pose_fleur
import stock

PLANT_COLOR = ["rouge", "orange", "bleu", "rose", "violette"]
PLANT_PRICE = [20,30,50,150,220]

class App: 
    def __init__(self):
        pyxel.init(101, 101, title="Grow a garden")
        pyxel.mouse(True)
        pyxel.load("res.pyxres")
        self.fleur = []
        self.plantType = 0
        
        self.flower = Pose_fleur.pose_fleur(pyxel.mouse_x, pyxel.mouse_y, self.fleur, self.plantType) # La pose / recolte des fleurs
        self.graine = stock.Stock() # Le stock de graine
        #self.shop = Shop.shop()
        
        self.graine.gagner_une_graine("rouge")
        
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_M):
            #self.shop.Open()
            pass
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit
        self.flower.graine = self.graine.graine
        self.graine.argent = self.flower.loot
            
        if pyxel.btnp(pyxel.KEY_A) and self.graine.argent >= PLANT_PRICE[self.plantType]:
            self.flower.loot -= PLANT_PRICE[self.plantType]
            self.graine.gagner_une_graine(PLANT_COLOR[self.plantType])
        
        
    
    def draw(self):
        pyxel.cls(11)
        pyxel.rectb(0, 0, 101, 101, 6)
        pyxel.rect(1,1,99,99,4)
        #if self.shop.soil == True:
        #    pyxel.blt(85,85,0,0,16, 16,16,0)
        
        
        
        self.flower.update(self.plantType)
        if self.plantType == 0:
            pyxel.text(3,87,str(self.flower.graine["rouge"]),7)      # plante rouge
        elif self.plantType == 1:
            pyxel.text(10,87,str(self.flower.graine["orange"]),7)    # plante orage
        elif self.plantType == 2:
            pyxel.text(17,87,str(self.flower.graine["bleu"]),7)    # plante bleu
        elif self.plantType == 3:
            pyxel.text(24,87,str(self.flower.graine["rose"]),7)    # plante rose
        elif self.plantType == 4:
            pyxel.text(31,87,str(self.flower.graine["violette"]),7)# violette
        # Pose une fleur
        if pyxel.btn(pyxel.KEY_S) and self.graine.graine[PLANT_COLOR[self.plantType]] > 0:
            self.flower.plante()
        
        
        # Selection des fleurs
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
            
            
        

App()