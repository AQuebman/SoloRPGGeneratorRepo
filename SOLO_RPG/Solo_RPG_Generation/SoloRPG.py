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

Config.set('graphics', 'maxfps', '')
        
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
    def Gen_Char_Gen(self,*args): 
        self.onButtonPress() #Grabs a random name for a male or female
        Class_Choice = ('Alchemist', 'Artificer', 'Assassin', 'Barbarian', 'Bard', 'Blackguard', 'Cavalier', 'Cleric', 'Conjurer', 'Dragoon', 'Druid', 'Eldritch Knight', 'Fighter', 'Gunslinger', 'Illusionist', 'Monk', 'Necromancer', 'Ninja', 'Paladin', 'Psion', 'Ranger', 'Samurai', 'Shaman', 'Sorcerer', 'Spy', 'Swashbuckler', 'Tactician', 'Thief', 'Warlock', 'Warrior', 'Witch', 'Witch Doctor', 'Wizard') #Picks a random class
        self.ids.class_label.text = 'Class: ' + (str(random.choice(Class_Choice))) #Picks a random character class
        Race_Choice = ('Dragonborn', 'Drow', 'Dwarf', 'Elf', 'Gnome', 'Halfling', 'Human', 'Orc', 'Other', 'Tiefling') #Picks a random race
        Atypical_Race_Choice = ('Angel', 'Cyclops', 'Centaur', 'Demon', 'Dryads', 'Giant', 'Ghost', 'Gnoll', 'Hobgoblin', 'Kobold', 'Lycanthrope', 'Lizardfolk', 'Fairies', 'Goblin', 'Mermaids', 'Nymph', 'Satyr', 'Shade', 'Skeleton', 'Troglodyte', 'Troll', 'Vampires', 'Yeti')
        self.ids.race_label.text = 'Race: ' + (str(random.choice(Race_Choice)))
        if self.ids.race_label.text == 'Race: Other' : #If Other is the race then roll from the atypical race choice
            self.ids.race_label.text = 'Race: ' + (str(random.choice(Atypical_Race_Choice)))
        Body_Type = ('Toned','Built', 'Brawny', 'Slender', 'Typical', 'Chubby') #Picks a random body type
        self.ids.bodytype_label.text = 'Body Type: ' + (str(random.choice(Body_Type)))    
        Occupation = ('Alchemist', 'Animal Trainer', 'Apothecarist', 'Armorer', 'Artisan', 'Astrologer', 'Barber', 'Barrister', 'Beadle', 'Beekeeper', 'Blacksmith', 'Butcher', 'Caravan Guard', 'Chandler', 'Cheesemaker', 'Chest-maker', 'Cobbler', 'Confidence artist', 'Cooper', 'Corn Farmer', 'Costermonger', 'Cutpurse', 'Ditch Digger', 'Dock worker', 'Dyer', 'Falconer', 'Forester', 'Fortune Teller', 'Gambler', 'Glassblower', 'Glovemaker', 'Gong Farmer', 'Grave Digger', 'Guild Beggar', 'Gypsy', 'Haberdasher', 'Healer', 'Herbalist', 'Herder', 'Hunter', 'Indentured servant', 'Jester', 'Jeweler', 'Locksmith', 'Mariner', 'Mendicant', 'Mercenary', 'Merchant', 'Miller/baker', 'Miner', 'Minstrel', 'Moneylender', 'Mushroom farmer', 'Navigator', 'Noble', 'Orphan', 'Ostler', 'Outlaw', 'Parsnip Farmer', 'Potato Farmer', 'Radish Farmer', 'Rat catcher', 'Rice Farmer', 'Rope maker', 'Rutabaga Farmer', 'Sage', 'Scribe', 'Shaman', 'Slave', 'Smuggler', 'Soldier', 'Squire', 'Stonemason', 'Tax Collector', 'Trader', 'Trapper', 'Turnip Farmer', 'Urchin', 'Vagrant', 'Wainwright', 'Weaver', 'Wheat Farmer', 'Wizard\'s apprentice', 'Woodcutter') #Picks a random occupation
        self.ids.occupation_label.text = 'Occupation: ' + (str(random.choice(Occupation))) #Picks a random occupation
        Char_Title = ('Abjurer', 'Adept', 'Apparitionist', 'Archveult', 'Astrologist', 'Astrologue', 'Augurer', 'Baleful', 'Beguiler', 'Bonder', 'Capricious', 'Chamberlain', 'Charmer', 'Chronicler', 'Clairvoyant', 'Collector', 'Conjurer', 'Controller', 'Cryomancer', 'Cultist', 'Curse-giver', 'Dangerous', 'Diabolist', 'Diviner', 'Dreamer', 'Elementalist', 'Enchanter', 'Encylopaedist', 'Ensorceller', 'Ensqualmer', 'Epicure', 'Evoker', 'Factotum', 'Fortune-teller', 'Fulgurator', 'Harbinger', 'Haruspex', 'Herald', 'Horologist', 'Hypnotist', 'Illusionist', 'Immolator', 'Infinitist', 'Insidiator', 'Lich', 'Logician', 'Mage', 'Magician', 'Magic-User', 'Magus', 'Marvelous', 'Master', 'Mentalist', 'Mezmerizer', 'Mind-reader', 'Mnemonist', 'Mummer', 'Mysteriarch', 'Mystic', 'Necrope', 'Nigromancer', 'Oath-taker', 'Palmist', 'Pedant', 'Phantasmist', 'Preceptor', 'Prestidigitator', 'Prosecutor', 'Psychic', 'Sage', 'Savant', 'Scientist', 'Seancer', 'Seer', 'Shabbat', 'Shibbol(eth)', 'Soothsayer', 'Sophist', 'Spellbinder', 'Spellslinger', 'Spellweaver', 'Summoner', 'Telepath', 'Teratologist', 'Thaumaturgist', 'Theurgist', 'Thought Master', 'Transformer', 'Transmogrifier', 'Trickster', 'Truth-teller', 'Tyro', 'Vigilant', 'Visionist', 'Warden', 'Demon-Binder', 'Demon-Keeper', 'Devil-Binder', 'Devil-Keeper', 'Dragon-Binder', 'Dragon-Keeper', 'Giant-Binder', 'Giant-Keeper', 'Vampire-Binder', 'Vampire-Keeper', 'Hydra-Binder', 'Hydra-Keeper', 'Medusa-Binder', 'Medusa-Keeper', 'Cyclops-Binder', 'Cyclops-Keeper', 'Abbey', 'Acolyte', 'Advocate', 'Alienist', 'Apostle', 'Ascetic', 'Aspirant', 'Astrologue', 'Beatific', 'Bishop', 'Blackcoat', 'Brother', 'Cabalist', 'Caller', 'Cardinal', 'Celibate', 'Chaplain', 'Conclavist', 'Confessor', 'Convert', 'Curate', 'Deacon', 'Dean', 'Deist', 'Disciple', 'Ecclesiast', 'Elder', 'Eternal', 'Evangelist', 'Evil eye', 'Exorcist', 'Faithful', 'Father', 'Friar', 'Heathen-slayer', 'Hierophant', 'Imam', 'Initiate', 'Inquisitor', 'Judge', 'Keeper', 'Lama', 'Medicine Man', 'Medium', 'Missionary', 'Mullah', 'Oath-keeper', 'Occultist', 'Omen-bringer', 'Ovate', 'Padre', 'Parson', 'Patriarch', 'Petitioner', 'Philosopher', 'Pilgrim', 'Pious', 'Pontiff', 'Pope', 'Preacher', 'Priest', 'Primate', 'Prognosticator', 'Prophet', 'Proselytizer', 'Psalmist', 'Pupil', 'Quixotic', 'Rabbi', 'Rector', 'Reverend', 'Revivalist', 'Rakshasa', 'Saint', 'Scholar', 'Seeker', 'Sensei', 'Sermonizer', 'Shepherd', 'Shrinist', 'Soul-saver', 'Speaker', 'Spirit-raiser', 'Theist', 'Vicar', 'Vowmaker', 'Wanderer', 'Witness', 'Wonder worker', 'Zealot', 'Amazon', 'Archer', 'Armigerent', 'Artillerist', 'Athlete', 'Bandit', 'Battler', 'Berserker', 'Bludgeoner', 'Bodyguard', 'Brave', 'Brawler', 'Brigand', 'Bruiser', 'Brute', 'Bushwhacker', 'Cadet', 'Campaigner', 'Captain', 'Cavalier', 'Champion', 'Charger', 'Chevalier', 'Chieftain', 'Colossus', 'Conqueror', 'Defender', 'Defiler', 'Duelist', 'Exemplar', 'Fencer', 'Footman', 'Freelancer', 'Gallant', 'General', 'Gentleman', 'Giant', 'Gladiator', 'Grenadier', 'Guardian', 'Guerilla', 'Headman', 'Horseman', 'Huntsman', 'Impaler', 'Janissary', 'Jouster', 'Justicar', 'Khan', 'Knight', 'Lancer', 'Legionnaire', 'Lieutenant', 'Lord', 'Man-at-arms', 'Manslayer', 'Marauder', 'Marine', 'Mercenary', 'Myrmidon', 'Protector', 'Pugilist', 'Ravager', 'Reaver', 'Scout', 'Sentinel', 'Sergeant', 'Sharpshooter', 'Shield-bearer', 'Skirmisher', 'Soldier', 'Squire', 'Standard-bearer', 'Swordsman', 'Tank', 'Templar', 'Titan', 'Trooper', 'Vanquisher', 'Veteran', 'Victor', 'Viking', 'Vindicator', 'Warlord', 'Warmonger', 'Wildling', 'Wrestler', 'Apprentice', 'Arch-rogue', 'Artisan', 'Balladeer', 'Beggar', 'Bilker', 'Body snatcher', 'Boss', 'Bounty hunter', 'Bravo', 'Bully', 'Burglar', 'Capo', 'Card shark', 'Charlaton', 'Cheat', 'Clockworker', 'Con man', 'Cove', 'Cozener', 'Cracksman', 'Cretin', 'Crony', 'Cutpurse', 'Cutthroat', 'Darksider', 'Devil', 'Dice rattler', 'Embezzler', 'Entrepreneur', 'Executioner', 'Expert', 'Explorer', 'Fence', 'Filcher', 'Footpad', 'Forger', 'Fortunist', 'Gambler', 'Gammoner', 'Godfather', 'Guildmaster', 'Guildsman', 'Hedge creeper', 'Hit man', 'Informer', 'Jongleur', 'Journeyman', 'Juggler', 'Junkman', 'Killer', 'Knave', 'Liar', 'Lorist', 'Lyrist', 'Made man', 'Magnate', 'Magsman', 'Minstrel', 'Moneylender', 'Mugger', 'Murderer', 'Muscle', 'Muse', 'Pawnbroker', 'Racaraide', 'Raconteur', 'Rake', 'Rascal', 'Rhymer', 'Robber', 'Rogue', 'Rowdy', 'Rutterkin', 'Scallywag', 'Scammer', 'Scoundrel', 'Second story man', 'Shadow walker', 'Shark', 'Sharper', 'Shiv', 'Skald', 'Slaver', 'Sonneteer', 'Swindler', 'Thief', 'Thug', 'Tomb robber', 'Trapsmith', 'Treasure hunter', 'Troubadour', 'Villain', 'Waghalter', 'Wordsmith' )
        self.ids.Char_Title.text = 'Title: ' + (str(random.choice(Char_Title))) #Picks a random character title
        
#This section randomizes how many siblings the character has then determines their sex randomly and rolls the appropriate male or female name generator                                                           
        NumChildren = random.randint(0,100)
        SubSex = random.randint(0,1)
        
        if NumChildren <= 51:
            self.ids.siblings_label.text = 'Siblings: 0 '
            self.ids.Sibling_Name1.text = ''
        if NumChildren >= 52 and NumChildren <= 71:
            self.ids.siblings_label.text = 'Siblings: 1' 
            if SubSex == 0:
                self.Male_name_gen()
                self.ids.Sibling_Name1.text = self.ids.Char_Name.text
            elif SubSex == 1:
                self.Female_name_gen()
                self.ids.Sibling_Name1.text = self.ids.Char_Name.text
        if NumChildren >= 72 and NumChildren <= 90:
            self.ids.siblings_label.text = 'Siblings: 2' 
            if SubSex == 0:
                self.Male_name_gen()
                self.ids.Sibling_Name1.text = self.ids.Char_Name.text
                self.Male_name_gen()
                self.ids.Sibling_Name2.text = self.ids.Char_Name.text
            elif SubSex == 1:
                self.Female_name_gen()
                self.ids.Sibling_Name1.text = self.ids.Char_Name.text
                self.Female_name_gen()
                self.ids.Sibling_Name2.text = self.ids.Char_Name.text
        if NumChildren >= 91 and NumChildren <= 97:
            self.ids.siblings_label.text = 'Siblings: 3'
            if SubSex == 0:
                self.Male_name_gen()
                self.ids.Sibling_Name1.text = self.ids.Char_Name.text
                self.Male_name_gen()
                self.ids.Sibling_Name2.text = self.ids.Char_Name.text
                self.Male_name_gen()
                self.ids.Sibling_Name3.text = self.ids.Char_Name.text
            elif SubSex == 1:
                self.Female_name_gen()
                self.ids.Sibling_Name1.text = self.ids.Char_Name.text
                self.Female_name_gen()
                self.ids.Sibling_Name2.text = self.ids.Char_Name.text
                self.Female_name_gen()
                self.ids.Sibling_Name3.text = self.ids.Char_Name.text
        if NumChildren >= 98 and NumChildren <= 100:
            self.ids.siblings_label.text = 'Siblings: 4'
            if SubSex == 0:
                self.Male_name_gen()
                self.ids.Sibling_Name1.text = self.ids.Char_Name.text
                self.Male_name_gen()
                self.ids.Sibling_Name2.text = self.ids.Char_Name.text
                self.Male_name_gen()
                self.ids.Sibling_Name3.text = self.ids.Char_Name.text
                self.Male_name_gen()
                self.ids.Sibling_Name4.text = self.ids.Char_Name.text
            elif SubSex == 1:
                self.Female_name_gen()
                self.ids.Sibling_Name1.text = self.ids.Char_Name.text
                self.Female_name_gen()
                self.ids.Sibling_Name2.text = self.ids.Char_Name.text
                self.Female_name_gen()
                self.ids.Sibling_Name3.text = self.ids.Char_Name.text
                self.Female_name_gen()
                self.ids.Sibling_Name4.text = self.ids.Char_Name.text


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
        self.ids.race_label.text = '' 
        self.ids.bodytype_label.text = ''  
        self.ids.occupation_label.text = ''
        self.ids.Char_Title.text = ''
        self.ids.siblings_label.text = ''
        self.ids.Sibling_Name1.text = ''
        self.ids.Sibling_Name2.text = ''
        self.ids.Sibling_Name3.text = ''
        self.ids.Sibling_Name4.text = ''
         
        
        
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