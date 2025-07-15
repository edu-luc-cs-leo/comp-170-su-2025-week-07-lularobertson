class Beer:
    def __init__(self, name:str, abv:int):
        self.name = name
        self.abv = abv

    def alcohol_content(self, volume_in_oz):
        return self.abv*volume_in_oz
    
    def description(self):
        return f"{self.name}: {self.abv*100:.1f}% ABV"
    
class Pale_Ale(Beer): # new SUBclass. pale ale is still a beer.
    def __init__(self):
        super().__init__("Pale Ale", 0.055)
         # refering back to "superclass" beer, name is ".." and ABV is an int.

class IPA(Beer):
    def __init__(self):
        super().__init__("IPA", 0.065)

class Stout(Beer):
    def __init__(self):
        super().__init__("Stout", 0.07)

class Porter(Beer):
    def __init__(self):
        super().__init__("Porter", 0.06)

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 