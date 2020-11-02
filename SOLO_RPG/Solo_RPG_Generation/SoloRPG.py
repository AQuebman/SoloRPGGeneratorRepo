from kivy.app import App

#Builder allows us to call another file such as our kv file
from kivy.lang import Builder

#BoxLayout allows us to use this layout
from kivy.uix.boxlayout import BoxLayout

#Random allows us to use random choice and other random triggers
import random

#Allows us to trigger window size or make the app full screen
from kivy.core.window import Window

#Setting the size of the window that opens
Window.fullscreen = 'auto'

#Deciding if user can resize the window or not
from kivy.config import Config
Config.set('graphics', 'resizable', True)  

#Importing a CSV
import csv   

#Imports setting up a button with Kivy
from kivy.uix.button import Button

#Imports setting up a popup with kivy
from kivy.uix.popup import Popup

#Imports the kivy layout of Grid
from kivy.uix.gridlayout import GridLayout  
        
class Generators(BoxLayout):
#Generates random LOUCHE choice for 7-9 rolls in Dungeon World  
    def louche(self, *args):
        LOUCHE = ('LOCALITY: Something specifically related to the current environment happens.\nThe buildings now on fire. The ground collapses. It\'s flooding. Moonquake!' , 'OFFER: Offer a bargain, an extra, or a perk for a cost.\noffer a better position, with risk. Offer a temptation.', 'UNEXPECTED DANGER: Make something up or roll it up at random.\nTie it in if you want now or worry about how it fits in later', 'CALLBACK: Use something that they\'ve given you. A backstory element.\nAn off-handed comment. Gear. A character sheet aspect', 'HARM: Deal damage', 'END SOMETHING: End an ongoing effect, bonus, or fictional advantage. Take a \nresource away, something you possess, whether it\'s a piece of gear, \nan ability, or an ally')
        self.ids.main_label.text = (str(random.choice(LOUCHE)))

#Female Name Generation
    def Female_name_gen(self, *args):
#Declares the array variables of First_Name and Last_Name
        First_Name = []
        Last_Name = []
#Opens the csv file that contains the random names
        with open(r'C:\Users\Aaron\Desktop\Names_List.csv') as f:
            reader = csv.reader(f, skipinitialspace=True)         
            for col in reader: 
                #This verifies it doesn't get a blank or the column title and if it does it continues until it doesn't get a blank
                if not col[1] or col[1] == "Female First Name": continue
                else:
                #This appends column 1 to First_Name
                    First_Name.append(col[1])
                #This verifies it doesn't get a blank or the column title and if it does it continues until it doesn't get a blank
                if not col[2]: continue
                if not col[2] or col[2] == "Last Names": continue
                else:
                #This appends column 2 to Last_Name
                    Last_Name.append(col[2])
                
#Print a random first and last name for females
                self.ids.Char_Name.text = 'Name: ' + random.choice(First_Name) + ' ' + random.choice(Last_Name)    
                                      
#Male Name Generation               
    def Male_name_gen(self, *args):
        First_Name = []
        Last_Name = []
        with open(r'C:\Users\Aaron\Desktop\Names_List.csv') as f:
            reader = csv.reader(f, skipinitialspace=True)         
            for col in reader: 
                ##This verifies it doesn't get a blank or the column title and if it does it continues until it doesn't get a blank
                if not col[0] or col[0] == "Male First Name": continue
                else:
                #This appends column 0 to First_Name
                    First_Name.append(col[0])
                ##This verifies it doesn't get a blank or the column title and if it does it continues until it doesn't get a blank
                if not col[2] or col[2] == "Last Names": continue
                else:
                #This appends column 2 to Last_Name
                    Last_Name.append(col[2])

#Print a random first and last name for Males
        self.ids.Char_Name.text = 'Name: ' + random.choice(First_Name) + ' ' + random.choice(Last_Name)        
 
#Generic Character Generator
    def Gen_Char_Gen(self, *args): 
        self.onButtonPress() #Grabs a random name for a male or female
        Class_Choice = ('Alchemist', 'Artificer', 'Assassin', 'Barbarian', 'Bard', 'Blackguard', 'Cavalier', 'Cleric', 'Conjurer', 'Cultist', 'Dragoon', 'Druid', 'Eldritch Knight', 'Fighter', 'Gunslinger', 'Illusionist', 'Monk', 'Necromancer', 'Ninja', 'Paladin', 'Psion', 'Ranger', 'Sage', 'Samurai', 'Shaman', 'Sorcerer', 'Spy', 'Swashbuckler', 'Tactician', 'Thief', 'Warlock', 'Warrior', 'Witch', 'Witch Doctor', 'Wizard') #Picks a random class
        self.ids.class_label.text = 'Class: ' + (str(random.choice(Class_Choice)))
        Race_Choice = ('Dragonborn', 'Drow', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Human', 'Orc', 'Other', 'Tiefling') #Picks a random race
        Atypical_Race_Choice = ('Angel', 'Cyclops', 'Centaur', 'Demon', 'Dryads', 'Giant', 'Ghost', 'Gnoll', 'Hobgoblin', 'Kobold', 'Lycanthrope', 'Lizardfolk', 'Fairies', 'Goblin', 'Mermaids', 'Nymph', 'Satyr', 'Shade', 'Skeleton', 'Troglodyte', 'Troll', 'Vampires', 'Yeti')
        self.ids.race_label.text = 'Race: ' + (str(random.choice(Race_Choice)))
        if self.ids.race_label.text == 'Race: Other' :
            self.ids.race_label.text = 'Race: ' + (str(random.choice(Atypical_Race_Choice)))
        Body_Type = ('Toned','Built', 'Brawny', 'Slender', 'Typical', 'Chubby') #Picks a random body type
        self.ids.bodytype_label.text = 'Body Type: ' + (str(random.choice(Body_Type)))    
        Occupation = ('Alchemist', 'Animal Trainer', 'Apothecarist', 'Armorer', 'Artisan', 'Astrologer', 'Barber', 'Barrister', 'Beadle', 'Beekeeper', 'Blacksmith', 'Butcher', 'Caravan Guard', 'Chandler', 'Cheesemaker', 'Chest-maker', 'Cobbler', 'Confidence artist', 'Cooper', 'Corn Farmer', 'Costermonger', 'Cutpurse', 'Ditch Digger', 'Dock worker', 'Dyer', 'Falconer', 'Forester', 'Fortune Teller', 'Gambler', 'Glassblower', 'Glovemaker', 'Gong Farmer', 'Grave Digger', 'Guild Beggar', 'Gypsy', 'Haberdasher', 'Healer', 'Herbalist', 'Herder', 'Hunter', 'Indentured servant', 'Jester', 'Jeweler', 'Locksmith', 'Mariner', 'Mendicant', 'Mercenary', 'Merchant', 'Miller/baker', 'Miner', 'Minstrel', 'Moneylender', 'Mushroom farmer', 'Navigator', 'Noble', 'Orphan', 'Ostler', 'Outlaw', 'Parsnip Farmer', 'Potato Farmer', 'Radish Farmer', 'Rat catcher', 'Rice Farmer', 'Rope maker', 'Rutabaga Farmer', 'Sage', 'Scribe', 'Shaman', 'Slave', 'Smuggler', 'Soldier', 'Squire', 'Stonemason', 'Tax Collector', 'Trader', 'Trapper', 'Turnip Farmer', 'Urchin', 'Vagrant', 'Wainwright', 'Weaver', 'Wheat Farmer', 'Wizard\'\s apprentice', 'Woodcutter') #Picks a random occupation
        self.ids.occupation_label.text = 'Occupation: ' + (str(random.choice(Occupation)))

        
        
   

    # On button press - Create a popup dialog with a label and a close button
    def onButtonPress(self):

        layout      = GridLayout(cols=1, padding=10)

       

        MaleNameButton  = Button(text  = "Click for Male Name Generation")

        FemaleNameButton = Button(text = "Click for Female Name Generation")

 

        layout.add_widget(MaleNameButton)

        layout.add_widget(FemaleNameButton)       

   

        # Instantiate the modal popup and display

        popup = Popup(title='Random Name Generator',

                      content=layout)  

        popup.open()   

       
#Need a close for both buttons and send them to different name generators based on gender
        # Dismiss causes the popup to go away. Release generates the call to the name generator specified
        MaleNameButton.bind(on_press=popup.dismiss)
        MaleNameButton.bind(on_release = self.Male_name_gen) 
        FemaleNameButton.bind(on_press=popup.dismiss)
        FemaleNameButton.bind(on_press = self.Female_name_gen)  

#Clears what is showing on the main_label of the application   
    def clear(self, *args):
        self.ids.main_label.text = ''
        self.ids.Char_Name.text = ''
        self.ids.class_label.text = ''      
        
        
class app1(App):
    def build(self):
        return Builder.load_file('SoloRPG.kv')
    
#Beginnings of a DCC Character Generator
"""    def Gen_Char_Gen(self, *args): 
        self.onButtonPress() #Grabs a random name for a male or female
        Class_Choice = ('Barbarian', 'Cleric', 'Druid', 'Fighter', 'Gunslinger', 'Monk', 'Sorcerer', 'Wizard') #Picks a random class
        self.ids.class_label.text = 'Class: ' + (str(random.choice(Class_Choice)))
        Race_Choice = ('Dwarf', 'Halfling', 'Gnome', 'Elf', 'Human', 'Orc', 'Tiefling') #Picks a random race
        self.ids.race_label.text = 'Race: ' + (str(random.choice(Race_Choice)))
        Body_Type = ('Toned','Built', 'Brawny', 'Slender', 'Typical', 'Chubby') #Picks a random body type
        self.ids.bodytype_label.text = 'Body Type: ' + (str(random.choice(Body_Type)))    
        Occupation = ('Alchemist', 'Animal Trainer') #Picks a random occupation
        self.ids.occupation_label.text = 'Occupation: ' + (str(random.choice(Occupation)))
        if (self.ids.occupation_label.text) == 'Occupation: Alchemist': 
            self.ids.trained_weapon_label.text = 'Starting Weapon: Staff'
        elif (self.ids.occupation_label.text) == 'Occupation: Animal Trainer':
            self.ids.trained_weapon_label.text = 'Starting Weapon: Club'"""  

if __name__=="__main__":
    app1().run()