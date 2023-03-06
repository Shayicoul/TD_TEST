class CartePizza:
    Pizza = []
    
    def  is_empty(self):
        if (len(self.Pizza)) == 0:
            print("carte vide")
            return True 
        else:
            print("carte non vide")
            return False
    
        
        
    def nb_pizzas(self):
        return len(self.Pizza)
        
    def add_pizza(self,pizza):
        P = pizza
        self.Pizza.append(P)
            
    def remove_pizza(self, name):
        for pizza in self.pizzas:
            if pizza == name:
                self.pizzas.remove(pizza)
            return
        raise Exception(f"La Pizza n'existe pas dans la carte.")
    
    
    