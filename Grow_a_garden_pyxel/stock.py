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


