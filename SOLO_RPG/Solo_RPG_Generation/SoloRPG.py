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

        
class Louche():
#Generates random LOUCHE choice for 7-9 rolls in Dungeon World  
    def louche(self, *args):
        LOUCHE = ('LOCALITY: Something specifically related to the current environment happens.\nThe buildings now on fire. The ground collapses. It\'s flooding. Moonquake!' , 'OFFER: Offer a bargain, an extra, or a perk for a cost.\noffer a better position, with risk. Offer a temptation.', 'UNEXPECTED DANGER: Make something up or roll it up at random.\nTie it in if you want now or worry about how it fits in later', 'CALLBACK: Use something that they\'ve given you. A backstory element.\nAn off-handed comment. Gear. A character sheet aspect', 'HARM: Deal damage', 'END SOMETHING: End an ongoing effect, bonus, or fictional advantage. Take a \nresource away, something you possess, whether it\'s a piece of gear, \nan ability, or an ally')
        App.get_running_app().root.ids.main_label.text = (str(random.choice(LOUCHE)))

class NPC_Generator(BoxLayout):
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
                
#Print a random first and last name for females\
                self.ids.Char_Name.text = " ".join(['Name: ', random.choice(First_Name), ' ', random.choice(Last_Name)])    
                                      
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
        self.ids.Char_Name.text = " ".join(['Name: ', random.choice(First_Name), ' ', random.choice(Last_Name)])
        Facial_Hair = ('Anchor', 
                       'Balbo', 
                       'Bandholz', 
                       'Chin Curtain', 
                       'Circle Beard', 
                       'Clean Shaven', 
                       'Ducktail', 
                       'Extended Goatee', 
                       'French Fork', 
                       'Full Beard', 
                       'Garibaldi', 
                       'Goatee', 
                       'Horseshoe', 
                       'Hulihee', 
                       'Imperial', 
                       'Klingon', 
                       'Long Stubble', 
                       'Mutton Chops', 
                       'Side Whiskers', 
                       'Soul Patch', 
                       'Stubble', 
                       'Van Dyke', 
                       'Verdi', 
                       'Zappa')
        self.ids.Facial_Hair.text = 'Facial Hair: ' + (str(random.choice(Facial_Hair))) #Grabs a random facial hair if the name generated is for a male
        if self.ids.Facial_Hair.text == 'Facial Hair: Anchor':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/anchor-beard/]Facial Hair: Anchor[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Balbo':
            self.ids.Facial_Hair.text = '[ref=https://www.baldingbeards.com/facial-hair-styles/goatee-styles/balbo-beard/]Facial Hair: Balbo[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Bandholz':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/bandholz-beard/]Facial Hair: Bandholz[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Chin Curtain':
            self.ids.Facial_Hair.text = '[ref=https://www.baldingbeards.com/facial-hair-styles/beard-styles/chin-curtain//]Facial Hair: Chin Curtain[/ref]'            
        if self.ids.Facial_Hair.text == 'Facial Hair: Circle Beard':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/circle-beard/]Facial Hair: Circle Beard[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Clean Shaven':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/clean-shaven-style/]Facial Hair: Clean Shaven[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Ducktail':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/ducktail-beard/]Facial Hair: Ducktail[/ref]'            
        if self.ids.Facial_Hair.text == 'Facial Hair: Extended Goatee':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/extended-goatee-beard/]Facial Hair: Extended Goatee[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: French Fork':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/french-fork-beard/]Facial Hair: French Fork[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Full Beard':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/full-beard/]Facial Hair: Full Beard[/ref]'            
        if self.ids.Facial_Hair.text == 'Facial Hair: Garibaldi':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/garibaldi-beard/]Facial Hair: Garibaldi[/ref]'            
        if self.ids.Facial_Hair.text == 'Facial Hair: Goatee':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/goatee-beard/]Facial Hair: Goatee[/ref]' 
        if self.ids.Facial_Hair.text == 'Facial Hair: Horseshoe':
            self.ids.Facial_Hair.text = '[ref=https://www.baldingbeards.com/facial-hair-styles/mustache-styles/horseshoe-mustache/]Facial Hair: Horseshoe[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Hulihee':
            self.ids.Facial_Hair.text = '[ref=https://razors.co/beard-styles/hulihee-beard/]Facial Hair: Hulihee[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Imperial':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/imperial-beard/]Facial Hair: Imperial[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Klingon':
            self.ids.Facial_Hair.text = '[ref=https://www.baldingbeards.com/wp-content/uploads/2017/02/Klingon-beard-1024x715.jpg]Facial Hair: Klingon[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Long Stubble':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/long-stubble-beard/]Facial Hair: Long Stubble[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Mutton Chops':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/mutton-chops-beard/]Facial Hair: Mutton Chops[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Side Whiskers':
            self.ids.Facial_Hair.text = '[ref=https://www.baldingbeards.com/facial-hair-styles/beard-styles/sideburns/]Facial Hair: Side Whiskers[/ref]'            
        if self.ids.Facial_Hair.text == 'Facial Hair: Soul Patch':
            self.ids.Facial_Hair.text = '[ref=https://www.baldingbeards.com/facial-hair-styles/goatee-styles/soul-patch/]Facial Hair: Soul Patch[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Stubble':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/medium-stubble-beard/]Facial Hair: Stubble[/ref]'                                                                                                                                  
        if self.ids.Facial_Hair.text == 'Facial Hair: Van Dyke':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/van-dyke-beard/]Facial Hair: Van Dyke[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Verdi':
            self.ids.Facial_Hair.text = '[ref=https://www.realmenrealstyle.com/verdi-beard/]Facial Hair: Verdi[/ref]'
        if self.ids.Facial_Hair.text == 'Facial Hair: Zappa':
            self.ids.Facial_Hair.text = '[ref=https://www.beardgrowthworld.com/wp-content/uploads/2016/10/beard-styles-Zappa.jpg]Facial Hair: Zappa[/ref]'
                                               
#Generic Character Generator
    def Gen_Char_Gen(self, *args): 
        self.NameGenPop() #Grabs a random name for a male or female
        Class_Choice = ('Alchemist', 'Artificer', 'Assassin', 'Barbarian', 'Bard', 'Blackguard', 'Cavalier', 'Cleric', 'Conjurer', 'Dragoon', 'Druid', 'Eldritch Knight', 'Fighter', 'Gunslinger', 'Illusionist', 'Monk', 'Necromancer', 'Ninja', 'Paladin', 'Psion', 'Ranger', 'Samurai', 'Shaman', 'Sorcerer', 'Spy', 'Swashbuckler', 'Thief', 'Warlock', 'Warrior', 'Witch', 'Witch Doctor', 'Wizard') #Picks a random class
        self.ids.class_label.text = " ".join(['Class: ', (str(random.choice(Class_Choice)))]) #Picks a random character class    
        Race_Choice = ('Dragonborn', 'Drow', 'Dwarf', 'Elf', 'Gnome', 'Half-elf', 'Half-Orc', 'Halfling', 'Human', 'Orc', 'Other', 'Tiefling') #Picks a random race
        Atypical_Race_Choice = ('Aasimar', 'Angel', 'Centaur', 'Cyclops', 'Demon', 'Dryads', 'Fairies', 'Firbolg', 'Giant', 'Ghost', 'Ghoul', 'Goblin', 'Goliath', 'Gnoll', 'Hobgoblin', 'Kenku', 'Kobold', 'Lich', 'Lycanthrope', 'Lizardfolk', 'Merfolk', 'Nymph', 'Satyr', 'Shade', 'Skeleton', 'Troglodyte', 'Troll', 'Vampires', 'Yeti')
        self.ids.race_label.text = " ".join(['Race:',(str(random.choice(Race_Choice)))])   
        if self.ids.race_label.text == 'Race: Other' : #If Other is the race then roll from the atypical race choice
            self.ids.race_label.text = " ".join(['Race:',(str(random.choice(Atypical_Race_Choice)))])   
        Body_Type = ('Toned','Built', 'Brawny', 'Slender', 'Typical', 'Chubby') #Picks a random body type
        self.ids.bodytype_label.text = " ".join(['Body Type: ', (str(random.choice(Body_Type)))])      
        Occupation = ('Abbey', #Picks a random occupation
        'Abjurer', 
        'Acolyte', 
        'Adept', 
        'Advocate', 
        'Alchemist', 
        'Alienist', 
        'Amazon', 
        'Animal Trainer', 
        'Apostle', 
        'Apothecarist', 
        'Apparitionist', 
        'Apprentice', 
        'Archer', 
        'Arch-rogue', 
        'Archveult', 
        'Armigerent', 
        'Armorer', 
        'Artillerist', 
        'Artisan', 
        'Artist', 
        'Ascetic', 
        'Aspirant', 
        'Astrologer', 
        'Astrologist', 
        'Astrologue', 
        'Athlete', 
        'Augurer', 
        'Baleful', 
        'Balladeer', 
        'Bandit',
        'Banker',
        'Barber', 
        'Barrister', 
        'Battler', 
        'Beadle', 
        'Beatific', 
        'Beekeeper', 
        'Beggar', 
        'Beguiler', 
        'Berserker', 
        'Bilker', 
        'Bishop', 
        'Blackcoat',
        'Blackmailer', 
        'Blacksmith', 
        'Bludgeoner', 
        'Body snatcher', 
        'Bodyguard', 
        'Bonder', 
        'Bookseller', 
        'Bounty hunter', 
        'Brave', 
        'Bravo', 
        'Brawler', 
        'Brigand', 
        'Brother', 
        'Bruiser', 
        'Brute', 
        'Bully', 
        'Burglar', 
        'Bushwhacker', 
        'Butcher', 
        'Cabalist', 
        'Cadet', 
        'Caller', 
        'Campaigner', 
        'Capo', 
        'Capricious', 
        'Captain', 
        'Caravan Guard', 
        'Card shark', 
        'Cardinal', 
        'Cavalier', 
        'Celibate', 
        'Chamberlain', 
        'Champion', 
        'Chandler', 
        'Chaplain', 
        'Charger', 
        'Charlatan',
        'Charity Worker',
        'Charmer', 
        'Cheat', 
        'Cheesemaker', 
        'Chest-maker', 
        'Chevalier', 
        'Chieftain', 
        'Chronicler', 
        'Clairvoyant', 
        'Clockworker', 
        'Cobbler', 
        'Collector', 
        'Colossus', 
        'Con man', 
        'Conclavist', 
        'Confessor', 
        'Confidence artist', 
        'Conjurer', 
        'Conqueror', 
        'Controller', 
        'Convert', 
        'Cooper', 
        'Corn Farmer', 
        'Costermonger', 
        'Cove', 
        'Cozener', 
        'Cracksman', 
        'Cretin', 
        'Crony', 
        'Cryomancer', 
        'Cultist', 
        'Curate', 
        'Curse-giver', 
        'Cutpurse', 
        'Cutthroat', 
        'Cyclops-Binder', 
        'Cyclops-Keeper', 
        'Dancer', 
        'Dangerous', 
        'Darksider', 
        'Day Laborer', 
        'Deacon', 
        'Dean', 
        'Defender', 
        'Defiler', 
        'Deist', 
        'Demon-Binder', 
        'Demon-Keeper', 
        'Devil', 
        'Devil-Binder', 
        'Devil-Keeper', 
        'Diabolist', 
        'Dice rattler',
        'Diplomat', 
        'Disciple', 
        'Ditch Digger', 
        'Diviner', 
        'Dock worker', 
        'Dragon-Binder', 
        'Dragon-Keeper', 
        'Dreamer', 
        'Duelist', 
        'Dyer', 
        'Ecclesiast', 
        'Elder', 
        'Elementalist', 
        'Embezzler', 
        'Enchanter', 
        'Encylopaedist', 
        'Ensorceller', 
        'Ensqualmer', 
        'Entrepreneur', 
        'Epicure', 
        'Eternal', 
        'Evangelist', 
        'Evil eye', 
        'Evoker', 
        'Ex-Adventurer',
        'Ex-Noble', 
        'Executioner', 
        'Exemplar', 
        'Exorcist',
        'Explorer', 
        'Factotum',
        'Faithful', 
        'Falconer', 
        'Father', 
        'Fence', 
        'Fencer', 
        'Filcher', 
        'Footman', 
        'Footpad', 
        'Forester', 
        'Forger', 
        'Fortune Teller', 
        'Fortunist', 
        'Freelancer', 
        'Friar', 
        'Fulgurator', 
        'Gallant', 
        'Gambler', 
        'Gammoner', 
        'General', 
        'Gentleman', 
        'Giant', 
        'Giant-Binder', 
        'Giant-Keeper', 
        'Gladiator', 
        'Glassblower', 
        'Glovemaker', 
        'Godfather', 
        'Gong Farmer', 
        'Government Official',
        'Governor', 
        'Grave Digger', 
        'Grave Tender', 
        'Grenadier', 
        'Guardian', 
        'Guerilla', 
        'Guild Beggar', 
        'Guildmaster', 
        'Guildsman', 
        'Gypsy', 
        'Haberdasher', 
        'Harbinger', 
        'Haruspex', 
        'Headman', 
        'Healer', 
        'Heathen-slayer', 
        'Hedge creeper', 
        'Herald', 
        'Herbalist', 
        'Herder', 
        'Hierophant',
        'Hit man', 
        'Horologist', 
        'Horseman', 
        'Hunter', 
        'Huntsman', 
        'Hydra-Binder', 
        'Hydra-Keeper', 
        'Hypnotist', 
        'Illusionist', 
        'Imam', 
        'Immolator', 
        'Impaler', 
        'Indentured servant', 
        'Infinitist', 
        'Informer', 
        'Initiate', 
        'Inquisitor', 
        'Insidiator',
        'Investigator',
        'Janissary', 
        'Jester', 
        'Jeweler', 
        'Jongleur', 
        'Journeyman', 
        'Jouster', 
        'Judge', 
        'Juggler', 
        'Junkman', 
        'Justicar', 
        'Keeper', 
        'Khan', 
        'Killer', 
        'Knave', 
        'Knight',
        'Labor Boss', 
        'Lama', 
        'Lancer', 
        'Lawyer', 
        'Legionnaire',
        'Legbreaker', 
        'Liar', 
        'Lich', 
        'Lieutenant', 
        'Locksmith', 
        'Logician', 
        'Lorist', 
        'Lyrist',
        'Madame',
        'Made man', 
        'Mage', 
        'Magician', 
        'Magic-User',
        'Magistrate',
        'Magnate', 
        'Magsman', 
        'Magus', 
        'Man-at-arms', 
        'Manslayer', 
        'Marauder', 
        'Marine', 
        'Mariner',
        'Marketeer',
        'Marvelous', 
        'Medicine Man', 
        'Medium', 
        'Medusa-Binder', 
        'Medusa-Keeper', 
        'Mendicant', 
        'Mentalist', 
        'Mercenary', 
        'Merchant', 
        'Mezmerizer', 
        'Miller/baker', 
        'Mind-reader', 
        'Miner', 
        'Minstrel', 
        'Missionary', 
        'Mistress', 
        'Mnemonist', 
        'Moneylender', 
        'Mugger', 
        'Mullah', 
        'Mummer', 
        'Murderer', 
        'Muscle', 
        'Muse', 
        'Mushroom farmer', 
        'Myrmidon', 
        'Mysteriarch', 
        'Mystic', 
        'Navigator', 
        'Necrope', 
        'Necromancer',
        'Oath-keeper', 
        'Oath-taker', 
        'Occultist', 
        'Omen-bringer', 
        'Orphan', 
        'Ostler', 
        'Outlaw', 
        'Ovate', 
        'Padre', 
        'Palmist', 
        'Parsnip Farmer', 
        'Parson', 
        'Patriarch', 
        'Pawnbroker', 
        'Pedant', 
        'Petitioner', 
        'Phantasmist', 
        'Philosopher',
        'Physician',
        'Pick Pocket',
        'Pilgrim', 
        'Pious',
        'Plutocrat',
        'Pontiff', 
        'Pope', 
        'Potato Farmer', 
        'Preacher', 
        'Preceptor', 
        'Prestidigitator', 
        'Priest', 
        'Primate', 
        'Prognosticator', 
        'Prophet',
        'Proprietor',
        'Prosecutor', 
        'Proselytizer', 
        'Prostitute',
        'Protector', 
        'Psalmist', 
        'Psychic', 
        'Pugilist', 
        'Pupil',
        'Quixotic', 
        'Rabbi', 
        'Racaraide', 
        'Raconteur', 
        'Radish Farmer', 
        'Rake', 
        'Rakshasa', 
        'Rascal', 
        'Rat catcher', 
        'Ravager', 
        'Reaver', 
        'Rector', 
        'Reverend', 
        'Revivalist', 
        'Rhymer', 
        'Rice Farmer', 
        'Robber', 
        'Rogue', 
        'Rope maker', 
        'Rowdy', 
        'Rutabaga Farmer', 
        'Rutterkin', 
        'Sage', 
        'Saint', 
        'Savant', 
        'Scallywag', 
        'Scammer', 
        'Scholar', 
        'Scientist', 
        'Scoundrel', 
        'Scout', 
        'Scribe',
        'Seancer', 
        'Second story man', 
        'Seeker', 
        'Seer', 
        'Sensei', 
        'Sentinel', 
        'Sergeant', 
        'Sermonizer', 
        'Shabbat', 
        'Shadow walker', 
        'Shaman', 
        'Shark', 
        'Sharper', 
        'Sharpshooter', 
        'Shepherd', 
        'Shibbol(eth)', 
        'Shield-bearer', 
        'Shiv', 
        'Shrinist', 
        'Skald', 
        'Skirmisher', 
        'Slave Trader', 
        'Slave', 
        'Slaver', 
        'Smuggler', 
        'Soldier', 
        'Sonneteer', 
        'Soothsayer', 
        'Sophist', 
        'Soul-saver', 
        'Speaker', 
        'Spellbinder', 
        'Spellslinger', 
        'Spellweaver', 
        'Spice Merchant',
        'Spirit-raiser', 
        'Squire', 
        'Standard-bearer', 
        'Stonemason', 
        'Summoner', 
        'Swindler', 
        'Swordsman', 
        'Tank', 
        'Tavern Owner', 
        'Tax Collector', 
        'Tea House Owner', 
        'Telepath', 
        'Templar', 
        'Teratologist', 
        'Thaumaturgist', 
        'Theist', 
        'Theurgist', 
        'Thief', 
        'Thought Master', 
        'Thug', 
        'Titan', 
        'Tomb robber', 
        'Trader', 
        'Transformer', 
        'Transmogrifier', 
        'Trapper', 
        'Trapsmith', 
        'Treasure hunter', 
        'Trickster', 
        'Trooper', 
        'Troubadour', 
        'Truth-teller', 
        'Turnip Farmer', 
        'Tyro', 
        'Urchin', 
        'Vagrant', 
        'Vampire-Binder', 
        'Vampire-Keeper', 
        'Vanquisher', 
        'Vicar', 
        'Victor', 
        'Vigilant', 
        'Viking', 
        'Villain', 
        'Vindicator', 
        'Visionist', 
        'Vowmaker', 
        'Waghalter', 
        'Wainwright', 
        'Wanderer', 
        'Warden'
        'Warlord', 
        'Warmonger',
        'Watch leader',    
        'Weaver', 
        'Wheat Farmer', 
        'Whore',
        'Wildling', 
        'Witness', 
        'Wizard\'s apprentice', 
        'Wonder worker', 
        'Woodcutter'
        'Wordsmith'
        'Wrestler', 
        'Zealot')
        self.ids.occupation_label.text = " ".join(['Occupation: ', (str(random.choice(Occupation)))]) #Picks a random occupation 
   
        Char_Title = (
       'Ambitious',
       'Amoral',
       'Battered',
       'Beautiful',
       'Bigoted', 
       'Bitter',
       'Bold',
       'Boss',
       'Callous',
       'Capricious',
       'Careworn',
       'Cautious',
       'Cheap',
       'Cheating',
       'City',
       'Clan Leader',
       'Commercial',
       'Compassionate',
       'Cretinous',
       'Crippled',
       'Cunning',
       'Cynical',
       'Deceitful',
       'Degraded',
       'Depraved',
       'Desperate',
       'Discreet',
       'Diseased',
       'Disguised',
       'Dissipated'
       'Doddering',
       'Drunken', 
       'Dubious',
       'Earnest',
       'Earthy',
       'Exhibitionist',
       'Erudite',
       'Exiled',
       'Expert',
       'Exquisite',
       'Famed',
       'Favored',
       'Feared',
       'Fearful',
       'Foreign',
       'Former Noble',
       'Grasping',
       'Grizzled',
       'Gross',
       'Hard-Drinking',
       'Hardened',
       'Haughty',
       'Heartless',
       'High-Military',
       'High-Ranking',
       'Humble',
       'Impartial',
       'Impoverished',
       'Intepid',
       'Instructor',
       'Knife-slinging',
       'Lord',
       'Marriage-minded',
       'Master',
       'Menacing',
       'Mighty',
       'Migrant',
       'Minister',
       'Minor',
       'Miser',
       'Mistreated',
       'Naive',
       'Newlywed',
       'Noble',
       'Official',
       'Pitiless',
       'Polished',
       'Powerful',
       'Pretender',
       'Promising',
       'Provincial',
       'Purveyor',
       'Puzzled',
       'Reputable',
       'Retired',
       'Rich',
       'Riotous',
       'Rough',
       'Ruthless',
       'Sagacious',
       'Scheming',
       'Scion',
       'Sincere',
       'Skillful',
       'Slumming Noble',
       'Social club leader',
       'Stern',
       'Steward',
       'Street-worn',
       'Veteran',
       'War Hero',
       'Wealthy',
       'Weary',
       'Widely-sought',
       'World-weary',
       'Wretched')
        self.ids.Char_Title.text = " ".join(['Title: ', (str(random.choice(Char_Title)))]) #Picks a random character title
        
#Generating Age of the generic NPC based on Race
        if self.ids.race_label.text == 'Race: Aasimar':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(18, 160)))])
        if self.ids.race_label.text == 'Race: Angel':
            self.ids.Age.text = " ".join(['Age: Timeless'])
        if self.ids.race_label.text == 'Race: Centaur':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(18, 60)))])
        if self.ids.race_label.text == 'Race: Cyclops':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(15, 500)))])
        if self.ids.race_label.text == 'Race: Demon':
            self.ids.Age.text = " ".join(['Age: Timeless'])
        if self.ids.race_label.text == 'Race: Dragonborn':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(15, 80)))])
        if self.ids.race_label.text == 'Race: Drow':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(20, 400)))])
        if self.ids.race_label.text == 'Race: Dryads':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(35, 999)))])
        if self.ids.race_label.text == 'Race: Dwarf':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(50, 350)))])
        if self.ids.race_label.text == 'Race: Elf':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(100, 750)))])
        if self.ids.race_label.text == 'Race: Fairies':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(18, 150)))])
        if self.ids.race_label.text == 'Race: Firbolg':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(30, 500)))])
        if self.ids.race_label.text == 'Race: Giant':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(20, 400)))])
        if self.ids.race_label.text == 'Race: Ghost':
            self.ids.Age.text = " ".join(['Age: Unknown'])
        if self.ids.race_label.text == 'Race: Ghoul':
            self.ids.Age.text = " ".join(['Age: Unknown'])
        if self.ids.race_label.text == 'Race: Gnome':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(40, 500)))])
        if self.ids.race_label.text == 'Race: Goblin':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(8, 60)))])
        if self.ids.race_label.text == 'Race: Goliath':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(18, 80)))])
        if self.ids.race_label.text == 'Race: Gnoll':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(2, 30)))])
        if self.ids.race_label.text == 'Race: Half-elf':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(20, 180)))])
        if self.ids.race_label.text == 'Race: Half-Orc':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(14, 175)))])            
        if self.ids.race_label.text == 'Race: Halfling':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(18, 250)))])
        if self.ids.race_label.text == 'Race: Hobgoblin':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(18, 80)))])
        if self.ids.race_label.text == 'Race: Human':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(18, 80)))])
        if self.ids.race_label.text == 'Race: Kenku':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(12, 60)))])
        if self.ids.race_label.text == 'Race: Kobold':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(8, 135)))])
        if self.ids.race_label.text == 'Race: Lich':
            self.ids.Age.text = " ".join(['Age: Unknown'])
        if self.ids.race_label.text == 'Race: Lizardfolk':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(14, 60)))])
        if self.ids.race_label.text == 'Race: Lycanthrope':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(18, 80)))])
        if self.ids.race_label.text == 'Race: Merfolk':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(20, 120)))])
        if self.ids.race_label.text == 'Race: Nymph':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(20, 999999)))])
        if self.ids.race_label.text == 'Race: Orc':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(12, 50)))])
        if self.ids.race_label.text == 'Race: Satyr':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(50, 500)))])
        if self.ids.race_label.text == 'Race: Shade':
            self.ids.Age.text = " ".join(['Age: Unknown'])
        if self.ids.race_label.text == 'Race: Skeleton':
            self.ids.Age.text = " ".join(['Age: Unknown'])           
        if self.ids.race_label.text == 'Race: Tiefling':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(18, 150)))])
        if self.ids.race_label.text == 'Race: Troglodyte':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(15, 50)))])         
        if self.ids.race_label.text == 'Race: Troll':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(10, 100)))])
        if self.ids.race_label.text == 'Race: Vampires':
            self.ids.Age.text = " ".join(['Age: Unknown']) 
        if self.ids.race_label.text == 'Race: Yeti':
            self.ids.Age.text = " ".join(['Age: ',  (str(random.randint(9, 200)))])            
            
                        
                                                
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
        if NumChildren >= 72 and NumChildren <= 90:
            self.ids.siblings_label.text = 'Siblings: 2' 
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
        if NumChildren >= 91 and NumChildren <= 97:
            self.ids.siblings_label.text = 'Siblings: 3'
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
#This section randomly generates if the mother and father are alive, dead, or impaired by a disability or illness
        Mother = random.randint(0,3)
        Father = random.randint(0,3)
        if Mother == 0:
            self.ids.Mother_Status.text = 'Mother\'s Health: Dead '
        if Mother == 1: 
            Disabilities = ('A Learning Disability', 'A Locomotor Disability', 'A Neurological Condition', 'A Speech and Language Disability', 'An Intellectual Disability', 'Autism', 'Blindness', 'Cerebral Palsy', 'Deafness', 'Dwarfism', 'Hearing Loss', 'Low Vision', 'Missing Both Arms', 'Missing Both Eyes', 'Missing Both Feet', 'Missing Both Legs', 'Muscular Dystrophy', 'Missing Fingers', 'Missing Left Arm', 'Missing Left Ear', 'Missing Left Eye', 'Missing Left Foot', 'Missing Left Hand', 'Missing Left Leg', 'Missing Nose', 'Missing Right Arm', 'Missing Right Ear', 'Missing Right Eye', 'Missing Right Foot', 'Missing Right Hand', 'Missing Right Leg', 'Missing Toes') #Picks a random disability
            self.ids.Mother_Status.text = " ".join(['Mother\'s Disabled with: ', (str(random.choice(Disabilities)))])
        if Mother == 2:
            Illness = ('Acidblight', 'Alcohol Addiction', 'Beggar\'s Pox', 'Brain Fever', 'Cackle Fever', 'Carrion Fever', 'Creeping Cough', 'Cobblestone Sickness', 'Dementia', 'Demon Ears', 'Desert Fever', 'Devil Rot', 'Dreaded Mallergy', 'Drug Addiction', 'Dryad\'s Rot', 'Gambling Addiction', 'Goblinitis', 'Golden Tumor', 'Grave Grub', 'Hemophilia', 'Hippogryff Hives', 'Hydrophobia', 'Leprousy', 'Mental Illness', 'Medusa Rash', 'Narcolepsy', 'Necrotic Blight', 'Ogre Poisoning', 'Puffs', 'Red Rot', 'Respiratory Disease', 'Screaming Sickness', 'Ser Avidore\'s Fire', 'Sewer Plague', 'Sewer Rat Flu', 'Sex Addiction', 'Sight Rot', 'Slate Fever', 'Slime Stomach', 'Slippery Sickness', 'Soft Bones', 'Spectre\'s Decay', 'Swamp Rage', 'Swordbearer\'s Bane', 'Tapeworm', 'Third Eye Blind', 'Turquoise Death', 'Vertigo', 'Vorel\'s Phage', 'Winter Insomnia', 'Woodland Mania', 'Yellow Plague', 'Wraith Eyes','Wyrm Flu') #Picks a random Illness
            self.ids.Mother_Status.text = " ".join(['Mother\'s Ill with: ', (str(random.choice(Illness)))])
        if Mother == 3:
            self.ids.Mother_Status.text = 'Mother\'s Health: Alive & Well '               
        if Father == 0:
            self.ids.Father_Status.text = 'Father\'s Health: Dead '
        if Father == 1: 
            Disabilities = ('A Learning Disability', 'A Locomotor Disability', 'A Neurological Condition', 'A Speech and Language Disability', 'An Intellectual Disability', 'Autism', 'Blindness', 'Cerebral Palsy', 'Deafness', 'Dwarfism', 'Hearing Loss', 'Low Vision', 'Missing Both Arms', 'Missing Both Eyes', 'Missing Both Feet', 'Missing Both Legs', 'Muscular Dystrophy', 'Missing Fingers', 'Missing Left Arm', 'Missing Left Ear', 'Missing Left Eye', 'Missing Left Foot', 'Missing Left Hand', 'Missing Left Leg', 'Missing Nose', 'Missing Right Arm', 'Missing Right Ear', 'Missing Right Eye', 'Missing Right Foot', 'Missing Right Hand', 'Missing Right Leg', 'Missing Toes') #Picks a random disability
            self.ids.Father_Status.text = " ".join(['Father\'s Disabled with: ', (str(random.choice(Disabilities)))])
        if Father == 2:
            Illness = ('Acidblight', 'Alcohol Addiction', 'Beggar\'s Pox', 'Brain Fever', 'Cackle Fever', 'Carrion Fever', 'Creeping Cough', 'Cobblestone Sickness', 'Dementia', 'Demon Ears', 'Desert Fever', 'Devil Rot', 'Dreaded Mallergy', 'Drug Addiction', 'Dryad\'s Rot', 'Gambling Addiction', 'Goblinitis', 'Golden Tumor', 'Grave Grub', 'Hemophilia', 'Hippogryff Hives', 'Hydrophobia', 'Leprousy', 'Mental Illness', 'Medusa Rash', 'Narcolepsy', 'Necrotic Blight', 'Ogre Poisoning', 'Puffs', 'Red Rot', 'Respiratory Disease', 'Screaming Sickness', 'Ser Avidore\'s Fire', 'Sewer Plague', 'Sewer Rat Flu', 'Sex Addiction', 'Sight Rot', 'Slate Fever', 'Slime Stomach', 'Slippery Sickness', 'Soft Bones', 'Spectre\'s Decay', 'Swamp Rage', 'Swordbearer\'s Bane', 'Tapeworm', 'Third Eye Blind', 'Turquoise Death', 'Vertigo', 'Vorel\'s Phage', 'Winter Insomnia', 'Woodland Mania', 'Yellow Plague', 'Wraith Eyes','Wyrm Flu') #Picks a random Illness
            self.ids.Father_Status.text = " ".join(['Father\'s Ill with: ', (str(random.choice(Illness)))])
        if Father == 3:
            self.ids.Father_Status.text = 'Father\'s Health: Alive & Well '   

#Creating Family label: 
        self.ids.Family.text = 'Family: '
#Generating random relationship status for the generated NPC         
        Relationship_Status = ('Single','Divorced', 'In a relationship', 'Married', 'Married and having an affair')
        self.ids.Relationship_Status.text = " ".join(['Relationship Status: ', (str(random.choice(Relationship_Status)))]) #Picks a random Relationship Status

#Generating random sexual orientation for the generated NPC
        Sexual_Orientation = ('Heterosexual', 'Homosexual', 'Bi-Sexual', 'Asexual', 'Transgender', 'Questioning')
        self.ids.Sexual_Orientation.text = " ".join(['Sexual Orientation: ', (str(random.choice(Sexual_Orientation)))]) #Picks a random Sexual Orientation
           

#Generating 3 Personality Traits for generic npc
        Personality_Traits = {'Abrasive',
                              'Absent-Minded',
                              'Aggressive',
                              'Alcoholic',
                              'Always carries food in their pockets',
                              'Always carries things',
                              'Always goes straight to the point',
                              'Always hurried',
                              'Always ironic',
                              'Always obeys superiors',
                              'Always plays fair',
                              'Always prioritizes their own needs'
                              'Always ready to help others',
                              'Always sharing their wisdom',
                              'Always tries to perch on furniture',
                              'Argues about everything',
                              'Beautiful singing voice',
                              'Believes something is planning to destroy the world',
                              'Believes in soulmates',
                              'Believes in whatever deity is most helpful to his at a given moment',
                              'Brawler',
                              'Can\'t keep a secret',
                              'Can\'t stand laziness',
                              'Careless dresser', 
                              'Carries out a complicated religious ritual every morning',
                              'Cautious',
                              'Changes subject very often',
                              'Claims to worship one god but secretly worships another',
                              'Collects something',
                              'Compares everything to a fight',
                              'Constantly flattering people they talk to',
                              'Constantly looks for the loophole',
                              'Constantly watchful',
                              'Crude sense of humor',
                              'Deeply xenophobic',
                              'Despises the aristocracy',
                              'Despite my birth, I do not place myself above other folk. We all have the same blood',
                              'Detached',
                              'Discretely worships a deity',
                              'Disregards poorer people',
                              'Doesn\'t care about risks or odds',
                              'Doesn\'t like change',
                              'Doesn\'t like listening to jokes',
                              'Doesn\'t like parting with money or possessions',
                              'Doesn\'t like their profession',
                              'Dresses in very expensive clothes',
                              'Easily holds grudges',
                              'Easygoing',
                              'Emphatic Speech', 
                              'Enjoys tavern brawls',
                              'Feels more comfortable underwater',
                              'Flattery is my preferred trick for getting what I want', 
                              'Focused',
                              'Frequently asks for help',
                              'Frequently thinks aloud',
                              'Garrulous',
                              'Gets bored easily',
                              'Goes out every night looking for something',
                              'Great at hiding',
                              'Greedy',
                              'Hardy',
                              'Has a pet companion',
                              'Has no concept of propriety',
                              'Has no self confidence',
                              'Hates fair play',
                              'Haunted by horrible memories',
                              'Holds grudges',
                              'Honest',
                              'I always have a plan for what to do when things go wrong',
                              'I always want to know how things work and what makes people tick',
                              'I am always calm, no matter what the situation. I never raise my voice or let my emotions control me',
                              'I am horribly, horribly awkward in social situations',
                              'I am incredibly slow to trust. Those who seem the fairest often have the most to hide',
                              'I am tolerant (or intolerant) of other faiths and respect (or condemn) the worship of other gods', 
                              'I am utterly serene, even in the face of disaster',
                              'I am working on a grand philosophical theory and love sharing my ideas',
                              'I ask a lot of questions',
                              'I believe that everything worth doing is worth doing right. I can\'t help it--I\'m a perfectionist',
                              'I blow up at the slightest insult',
                              'I bluntly say what other people are hinting or hiding',
                              'I can find common ground between the fiercest enemies, empathizing with them and always working toward peace. ', 
                              'I can stare down a hellhound without flinching',
                              'I change my mood or my mind as quickly as I change key in a song',
                              'I connect everything that happens to me to a grand cosmic plan',
                              'I don\'t like to bathe',
                              'I don\'t like to get my hands dirty, and I won\'t be caught dead in unsuitable accommodations'
                              'I don\'t part with my money easily and will haggle tirelessly to get the best deal possible',
                              'I don\'t pay attention to the risks in a situation. Never tell me the odds',
                              'I eat like a pig and have bad manners',
                              'I enjoy being strong and like breaking things',
                              'I enjoy sailing into new ports and making new friends over a flagon of ale',
                              'I face problems head-on. A simple direct solution is the best path to success',
                              'I fall in and out of love easily, and am always pursuing someone', 
                              'I feel far more comfortable around animals than people',
                              'I feel tremendous empathy for all who suffer',
                              'I get bitter if I\'m not the center of attention',
                              'I get bored easily. When am I going to get on with my destiny',
                              'I have a joke for every occasion, especially occasions where humor is inappropriate', 
                              'I have a lesson for every situation, drawn from observing nature',
                              'I have a strong sense of fair play and always try to find the most equitable solution to arguments',
                              'I idolize a particular hero of my faith and constantly refer to that person\'s deeds and example.',
                              'I hide scraps of food and trinkets away in my pockets',
                              'I judge people by their actions, not their words',
                              'I keep multiple holy symbols on me and invoke whatever deity might come in useful at any given moment',
                              'I know a story relevant to almost every situation',
                              'I lie about almost everything, even when there\'s no good reason to', 
                              'I like a job well done, especially if I can convince someone else to do it',
                              'I like to squeeze into small places where no one else can get to me',
                              'I like to talk at length about my profession',
                              'I love a good insult, even one directed at me',
                              'I misuse long words in an attempt to sound smarter',
                              'I never pass up a friendly wager',
                              'I often get lost in my own thoughts and contemplations, becoming oblivious to my surroundings',
                              'I once ran twenty-five miles without stopping to warn my clan of an approaching threat.I\'d do it again if I had to',
                              'I place no stock in wealthy or well-mannered folk. Money and manners won\'t save you from a hungry owlbear',
                              'I pocket anything I see that might have some value',
                              'I quote (or misquote) the sacred texts and proverbs in almost every situation', 
                              'I see omens in every event and action. The gods try to speak to us, we just need to listen', 
                              'I sleep with my back to a wall or tree, with everything I own wrapped in a bundle in my arms',
                              'I stretch the truth for the sake of a good story',
                              'I take great pains to always look my best and follow the latest fashions',
                              'I think anyone who\'s nice to me is hiding evil intent',
                              'I use polysyllabic words to convey the impression of great erudition',
                              'I was, in fact, raised by wolves',
                              'I watch over my friends as if they were a litter of newborn pups',
                              'I work hard so that I can play hard when the work is done',
                              'I would rather make a new friend than a new enemy',
                              'I...speak...slowly...when talking...to idiots...which...almost...everyone...is...compared...to me',
                              'I\'ll settle for nothing less than perfection',
                              'I\'m a born gambler who can\'t resist taking a risk for a potential payoff', 
                              'I\'m a hopeless romantic, always searching for that \'special someone',
                              'I\'m a snob who looks down on those who can\'t appreciate fine art',
                              'I\'m always picking things up, absently fiddling with them, and sometimes accidentally breaking them',
                              'I\'m always polite and respectful',
                              'I\'m confident in my own abilities and do what I can to instill confidence in others',
                              'I\'m convinced that people are always trying to steal my secrets',
                              'I\'m driven by a wanderlust that led me away from home',
                              'I\'m full of inspiring and cautionary tales from my military experience relevant to almost every combat situation',
                              'I\'m full of witty aphorisms and have a proverb for every occasion',
                              'I\'m haunted by memories of war. I can\'t get the images of violence out of my mind',
                              'I\'m oblivious to etiquette and social expectations',
                              'I\'m rude to people who lack my commitment to hard work and fair play',
                              'I\'m used to helping out those who aren\'t as smart as I am, and I patiently explain anything and everything to others',
                              'I\'m well known for my work, and I want to make sure everyone appreciates it. I\'m always taken aback when people haven\'t heard of me',
                              'I\'m willing to listen to every side of an argument before I make my own judgment',
                              'Indecisive',
                              'Inquisitive',
                              'I\'ve been isolated for so long that I rarely speak, preferring gestures and the occasional grunt',
                              'I\'ve enjoyed fine food, drink, and high society among my temple\'s elite. Rough living grates on me', 
                              'I\'ve lost too many friends, and I\'m slow to make new ones',
                              'I\'ve read every book in the world\'s greatest libraries--or like to boast that I have',
                              'I\'ve spent so long in the temple that I have little practical experience dealing with people in the outside world', 
                              'If someone is in trouble, I\'m always willing to lend help',
                              'If you do me an injury, I will crush you, ruin your name, and salt your fields',
                              'Illiterate',
                              'Inattentive',
                              'Intermittently asks for help',
                              'Is always late',
                              'Is always prepared',
                              'Is materialistic',
                              'Is a pacifist',
                              'Is an example of modesty',
                              'Judges people on their fighting skills',
                              'Judges people by their actions, not their words',
                              'Kleptomaniac',
                              'Knows all the gossip around town',
                              'Laconic Speaker', 
                              'Lazy',
                              'Lies poorly on purpose',
                              'Likes to eat like it\'s his last meal',
                              'Likes to swim',
                              'Local sports champion',
                              'Loudly worships a deity',
                              'Loves discovering new mysteries and solving them',
                              'Loyal',
                              'Lustful',
                              'Makes anyone they speak to feel like the most important person in the world',
                              'Merciful',
                              'My eloquent flattery makes everyone I talk to feel like the most wonderful and important person in the world',
                              'My favor, once lost, is lost forever',
                              'My friends know they can rely on me, no matter what',
                              'My language is as foul as an otyugh nest',
                              'Never knows the current time and date',
                              'Never sits on a chair',
                              'No one could doubt by looking at my regal bearing that I am a cut above the unwashed masses',
                              'No self-confidence',
                              'Nobody stays angry at me or around me for long, since I can defuse any amount of tension',
                              'Not very obstinate',
                              'Nothing can shake my optimistic attitude', 
                              'Observant',
                              'Occasionally gives money to the poor',
                              'Occasionally hums old dwarven songs',
                              'Often drunk',
                              'Only talks in whispers',
                              'Only talks loudly',
                              'Openly worships a deity',
                              'Patient',
                              'Prone to violence',
                              'Proud',
                              'Proudly worships a deity',
                              'Quick',
                              'Quick to forgive',
                              'Rarely speaks',
                              'Rarely thinks ahead',
                              'Reacts violently to weird clothes',
                              'Relentless',
                              'Runs everywhere instead of walking',
                              'Sarcasm and insults are my weapons of choice',
                              'Scornful',
                              'Sees everything as a challenge',
                              'Sees fighting as a solution to any problem',
                              'Self confident',
                              'Share everything I own',
                              'Shy', 
                              'Sleeps fully dressed, ready to run',
                              'Slow',
                              'Specialized',
                              'Sporadically lies',
                              'Sporadically quotes their father',
                              'Stubborn',
                              'Swims every day',
                              'Suspicious',
                              'Takes everything at face value',
                              'The best way to get me to do something is to tell me I can\'t do it',
                              'The common folk love me for my kindness and generosity',
                              'The first thing I do in a new place is note the locations of everything valuable--or where such things could be hidden',
                              'The leader of my community has something wise to say on every topic, and I am eager to share that wisdom',
                              'There\'s nothing I like more than a good mystery',
                              'Thinking is for other people. I prefer action',
                              'Tries to conver everyone they meet',
                              'To me, a tavern brawl is a nice way to get to know a new city',
                              'Uncivilized',
                              'Used to be bullied as a child and learned to fight so it wouldn\'t happen again',
                              'Uses very foul language',
                              'Valorous',
                              'Vicious',
                              'Very benevolent',
                              'Very calm',
                              'Very competitive',
                              'Very conceited',
                              'Very courages, to a fault',
                              'Very cowardly',
                              'Very cynical',
                              'Very detached from emotions',
                              'Very empathic towards others',
                              'Very little empathy towards others',
                              'Very little practical experience',
                              'Very focused',
                              'Very generous',
                              'Very good at keeping secrets',
                              'Very good diplomat always working towards resolution of conflict',
                              'Very greedy',
                              'Very impatient',
                              'Very lazy',
                              'Very modest',
                              'Very obstinate',
                              'Very optimistic',
                              'Very paranoid',
                              'Very patient',
                              'Very pessimistic',
                              'Very quick to trust other people',
                              'Very self-confident',
                              'Very selfish',
                              'Very slow to trust other people',
                              'Very talkative',
                              'Wants to know every side of a story before expressing an opinion',
                              'Wears a lot of cheap jewelry',
                              'Wears cheap spectacles',
                              'When I set my mind to something, I follow through no matter what gets in my way',
                              'Whenever I come to a new place, I collect local rumors and spread gossip',
                              'Will never say no to a duel',
                              'Will only speak common if forced to',
                              'Will ponder the pros and cons before making a decision',
                              'Wrathful',
                              'Works hard to play hard afterwards',
                              'Would rather act than talk or think',
                              'Zealously worships a deity'}
        self.ids.Personalitylabel.text = ('Personality Traits: ')
        self.ids.Personality_Traits.text =  '\n' + '\n' + '1.) ' + (','.join((random.sample(list(Personality_Traits), 1)))) + '\n' + '\n' + '2.) ' + (','.join((random.sample(list(Personality_Traits), 1)))) + '\n'+ '\n' + '3.) ' + (','.join((random.sample(list(Personality_Traits), 1))))

#Generating eye color for the generated NPC
        Eye_Color = ('Light Blue', 'Ice Blue', 'Blue', 'Grey-blue', 'White', 'Black', 'Grey', 'Teal', 'Ice Green', 'Green', 'Grey-green', 'Pale gold', 'Yellow', 'Gold', 'Orange', 'Brown', 'Dark Brown', 'Red', 'Pale Purple', 'Purple', 'Magenta', 'Yellow-green', 'Brown & Green', 'Gold & Green', 'Albino', 'Blind')
        self.ids.Eye_Color.text = " ".join(['Eye Color: ', (str(random.choice(Eye_Color)))]) #Picks a random Eye color
        
#Generating Hair Style/Hair color for the generated NPC
        Hair_Style = ('Afro', 'Afro Puffs', 'Asymmetric Cut', 'Bangs', 'Beehive', 'Big Hair', 'Blowout', 'Bowl Cut', 'Bob Cut', 'Bouffant', 'Braid', 'Brush Cut', 'Bun', 'Butch Cut', 'Buzz Cut', 'Caesar Cut', 'Chignon', 'Chonmage', 'Comb Over', 'Comma Hair', 'Conk', 'Cornrows', 'Crew Cut', 'Crop', 'Crown Braid', 'Croydon Facelift', 'Curtained Hair', 'Devilock', 'Dido Flip', 'Double Buns', 'Dreadlocks', 'Ducktail', 'Eton Crop', 'Extensions', 'Fade', 'Fallera Hairdo', 'Fauxhawk', 'Feather Cut', 'Feathered Hair', 'Finger Waves', 'Fishtail Hair', 'Flattop', 'Flipped-up ends', 'Fontange', 'French Braid', 'French Twist', 'Fringe(bangs)', 'Frosted Tips', 'Full Crown', 'Half Crown', 'Half Updo', 'Harvard Clip', 'Hi-Top Fade', 'High and Tight', 'Highlights', 'Hime Cut', 'Induction Cut', 'Ivy league', 'Jewfro', 'Jheri Curl', 'Layered Curl', 'Liberty Spikes', 'Line Up', 'Lob', 'Marcel Waves', 'Mod Cut', 'Mohawk', 'Mop Top', 'Mullet', 'Odango', 'Oseledets', 'Pageboy', 'Payot', 'Perm', 'Pigtails', 'Pixie Cut', 'Pompadour', 'Ponyhawk', 'Ponytail', 'Psychobilly Wedge', 'Queue', 'Quiff', 'Rattail', 'Razor Cut', 'Ringlets', 'Shag Cut', 'Shape-Up', 'Shingle-Bob', 'Short Back and Sides', 'Short Brush Cut', 'Short Hair', 'Slicked Back', 'Spiky Cut', 'Step Cut', 'Surfer Hair', 'Tail on Back', 'Taper Cut', 'The Rachel', 'Tonsure', 'Undercut', 'Updo', 'Waves', 'Weave', 'Widow\'s Peak', 'Wings')
        Hair_Color = ('Black', 'Blonde', 'Brown', 'Grey', 'Red', 'White')
        self.ids.Hair_Style.text = " ".join(['Hair Style: ', (str(random.choice(Hair_Color))), ' ', (str(random.choice(Hair_Style)))])#Picks a random Hair Style

        
#Generating Height for the generated NPC
        Height = ('Very Short', 'Short', 'Rather Short', 'Medium Height', 'Rather Tall', 'Tall', 'Very Tall')
        self.ids.Height.text = " ".join(['Height: ', (str(random.choice(Height)))]) #Picks a random generic height

#Generating Unique Traits for the generated NPC
        Unique_Trait = ('Albino', 'Allergic to gnomes', 'Asthmatic', 'Blind in an eye', 'Curved Spine', 'Dark, sober clothes', 'Deaf in left Ear', 'Deaf in right ear', 'Elaborate tattoos', 'Facial Scarring', 'Four tiny piercings on left eyebrow', 'Four tiny piercings on right eyebrow', 'Frequently smokes a pipe', 'Frequently Squints', 'Gaudy jewelry', 'Gestures profusely during a conversation', 'Hard of hearing', 'Has a large scar on left arm', 'Has a large scar on left hand', 'Has a large scar on right arm', 'Has a large scar on right hand', 'Heavily scarred on face', 'High pitched voice', 'Immaculate clothes', 'Impressive lisp', 'Inherited a family estate', 'Inherited a small forest', 'Magnificent Hair', 'Missing an appendage', 'Numerous piercings', 'Out of shape', 'Piercing through nose', 'Piercings on both ears', 'Piercing on left ear', 'Piercing on right ear', 'Precise hands', 'Smells of Cabbage', 'Smells of dog', 'Smells of garbage', 'Smells lightly of dirt', 'Stutters', 'Subtle fragrance', 'Sunken Breastbone', 'Uses a beautiful walking cane', 'Tattoos on face', 'Twitches regularly', 'Wears dark glasses to mask eyes', 'Wears an eye patch on left eye', 'Wears an eye patch on right eye')
        self.ids.Unique_Trait.text = " ".join(['Unique Physical Trait: ', (str(random.choice(Unique_Trait)))]) #Picks a random unique trait   


    # Name Gen Pop - Create a popup dialog to creating a random generated name when were creating a random npc
    def NameGenPop(self):

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
        self.ids.Mother_Status.text = ''
        self.ids.Father_Status.text = ''
        self.ids.Relationship_Status.text = ''
        self.ids.Sexual_Orientation.text = ''
        self.ids.Personality_Traits.text = ''
        self.ids.Personalitylabel.text = ''
        self.ids.Eye_Color.text = ''
        self.ids.Hair_Style.text = ''
        self.ids.Facial_Hair.text = ''
        self.ids.Height.text = ''
        self.ids.Unique_Trait.text = ''
        self.ids.Age.text = ''
        self.ids.Family.text = ''


class NameGenOriginal():
    # Name Gen Orig - Create a popup dialog with a label and a close button
    def NameGenOrig(self):

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
        MaleNameButton.bind(on_release = self.Random_Male) 
        FemaleNameButton.bind(on_press=popup.dismiss)
        FemaleNameButton.bind(on_press = self.Random_Female)
                        
#Female Name Generation
    def Random_Female(self, *args):
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
                
#Print a random first and last name for females\
        App.get_running_app().root.ids.Char_Name.text = " ".join(['Name: ', random.choice(First_Name), ' ', random.choice(Last_Name)])
                                      
#Male Name Generation               
    def Random_Male(self, *args):
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
        App.get_running_app().root.ids.Char_Name.text = " ".join(['Name: ', random.choice(First_Name), ' ', random.choice(Last_Name)])
         





class MonsterGenerator(GridLayout):  
    # Monster Generation - Gives users buttons to select to randomly generate a monster
    def MonsterGeneration(self):

        layout      = GridLayout(cols=2, padding=10)

       

        DragonButton  = Button(text  = "Click for a random dragon type monster")

        HumanoidButton = Button(text = "Click for a random humanoid type monster")

 

        layout.add_widget(DragonButton)

        layout.add_widget(HumanoidButton)       

   

        # Instantiate the modal popup and display

        popup = Popup(title='Monster Generator',

                      content=layout)  

        popup.open()   

       
        # Dismiss causes the popup to go away. Release generates the call to the monster generator specified
        DragonButton.bind(on_press=popup.dismiss)
        DragonButton.bind(on_release = self.Dragon_kind_gen)
#        DragonButton.bind(on_release = self.Dragon_kind_gen) 
        HumanoidButton.bind(on_press=popup.dismiss)
        HumanoidButton.bind(on_press = self.Humanoid_gen)
        
#Dragon-kind Monster Generation
    def Dragon_kind_gen(self, *args): 
#        LOUCHE = ('LOCALITY: Something specifically related to the current environment happens.\nThe buildings now on fire. The ground collapses. It\'s flooding. Moonquake!' , 'OFFER: Offer a bargain, an extra, or a perk for a cost.\noffer a better position, with risk. Offer a temptation.', 'UNEXPECTED DANGER: Make something up or roll it up at random.\nTie it in if you want now or worry about how it fits in later', 'CALLBACK: Use something that they\'ve given you. A backstory element.\nAn off-handed comment. Gear. A character sheet aspect', 'HARM: Deal damage', 'END SOMETHING: End an ongoing effect, bonus, or fictional advantage. Take a \nresource away, something you possess, whether it\'s a piece of gear, \nan ability, or an ally')

        Dragons = ('Copper Dragon Wyrmling', 'Copper Dragon Wyrmling')        
        App.get_running_app().root.ids.Dragons.text = " ".join(['Monster:',(str(random.choice(Dragons)))])
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Copper Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Copper Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (500, 200)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Dragon Turtle':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragon Turtle.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (810, 650)
            App.get_running_app().root.ids.Dragons.halign = 'center'
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Gold Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Gold Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 50)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Green Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Green Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 150)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Pseudodragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Pseudodragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (650, 20)
            App.get_running_app().root.ids.Dragons.halign = 'center'
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Red Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Red Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 250)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Silver Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Silver Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 200)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: White Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'White Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 300)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Wyvern':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Wyvern.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (750, 600)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Black Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Young_Black_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 50)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Blue Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Young_Blue_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 50)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Brass Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Young_Brass_Dragon.jpg'
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Bronze Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Young_Bronze_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 400)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Copper Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Young_Copper_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (660, 350)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Gold Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Young_Gold_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (660, 100)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Green Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Young_Green_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (850, 600)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Red Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Young_Red_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (850, 600)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Silver Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Young_Silver_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (850, 600)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young White Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Young_White_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 150)
                

#Humanoid Monster Generation
    def Humanoid_gen(self, *args): 
        pass

      
class app1(App):
    Name_Variable = NameGenOriginal()  
    Louche_Variable = Louche()  
    Monster_Variable = MonsterGenerator()
    def build(self):
        return Builder.load_file('SoloRPG.kv')
    
#Beginnings of a DCC Character Generator
"""    def Gen_Char_Gen(self, *args): 
        self.NameGenPop() #Grabs a random name for a male or female
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