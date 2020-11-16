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
                
#Print a random first and last name for females\
                self.ids.Facial_Hair.text = ' ' 
                self.ids.Char_Name.text = 'Name: ' + random.choice(First_Name) + ' ' + random.choice(Last_Name)    
                                      
#Male Name Generation               
    def Male_name_gen(self, *args):
        First_Name = []
        Last_Name = []
        Male = 1
        Male = Male
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
        return Male

 
#Generic Character Generator
    def Gen_Char_Gen(self, *args): 
        Facial_Hair = ('Anchor', 'Balbo', 'Bandholz', 'Chin Curtain', 'Circle Beard', 'Clean Shaven', 'Ducktail', 'Extended Goatee', 'French Fork', 'Full Beard', 'Garibaldi', 'Goatee', 'Horseshoe', 'Hulihee', 'Imperial', 'Klingon', 'Long Stubble', 'Mutton Chops', 'Side Whiskers', 'Soul Patch', 'Stubble', 'Van Dyke', 'Verdi', 'Zappa')
        if self.Male_name_gen():
            self.ids.Facial_Hair.text = 'Facial Hair ' + (str(random.choice(Facial_Hair))) #Grabs a random facial hair if the name generated is for a male
        self.NameGenPop() #Grabs a random name for a male or female
        Class_Choice = ('Alchemist', 'Artificer', 'Assassin', 'Barbarian', 'Bard', 'Blackguard', 'Cavalier', 'Cleric', 'Conjurer', 'Dragoon', 'Druid', 'Eldritch Knight', 'Fighter', 'Gunslinger', 'Illusionist', 'Monk', 'Necromancer', 'Ninja', 'Paladin', 'Psion', 'Ranger', 'Samurai', 'Shaman', 'Sorcerer', 'Spy', 'Swashbuckler', 'Thief', 'Warlock', 'Warrior', 'Witch', 'Witch Doctor', 'Wizard') #Picks a random class
        self.ids.class_label.text = 'Class: ' + (str(random.choice(Class_Choice))) #Picks a random character class
        Race_Choice = ('Dragonborn', 'Drow', 'Dwarf', 'Elf', 'Gnome', 'Half-elf', 'Half-Orc', 'Halfling', 'Human', 'Orc', 'Other', 'Tiefling') #Picks a random race
        Atypical_Race_Choice = ('Aasimar', 'Angel', 'Cyclops', 'Centaur', 'Demon', 'Dryads', 'Fairies', 'Firbolg', 'Giant', 'Ghost', 'Ghoul', 'Goblin', 'Goliath', 'Gnoll', 'Hobgoblin', 'Kenku', 'Kobold', 'Lich', 'Lycanthrope', 'Lizardfolk', 'Mermaids', 'Nymph', 'Satyr', 'Shade', 'Skeleton', 'Troglodyte', 'Troll', 'Vampires', 'Yeti')
        self.ids.race_label.text = 'Race: ' + (str(random.choice(Race_Choice)))
        if self.ids.race_label.text == 'Race: Other' : #If Other is the race then roll from the atypical race choice
            self.ids.race_label.text = 'Race: ' + (str(random.choice(Atypical_Race_Choice)))
        Body_Type = ('Toned','Built', 'Brawny', 'Slender', 'Typical', 'Chubby') #Picks a random body type
        self.ids.bodytype_label.text = 'Body Type: ' + (str(random.choice(Body_Type)))    
        Occupation = ('Alchemist', 'Animal Trainer', 'Apothecarist', 'Armorer', 'Artisan', 'Astrologer', 'Barber', 'Barrister', 'Beadle', 'Beekeeper', 'Blacksmith', 'Butcher', 'Caravan Guard', 'Chandler', 'Cheesemaker', 'Chest-maker', 'Cobbler', 'Confidence artist', 'Cooper', 'Corn Farmer', 'Costermonger', 'Cutpurse', 'Ditch Digger', 'Dock worker', 'Dyer', 'Falconer', 'Forester', 'Fortune Teller', 'Gambler', 'Glassblower', 'Glovemaker', 'Gong Farmer', 'Grave Digger', 'Guild Beggar', 'Gypsy', 'Haberdasher', 'Healer', 'Herbalist', 'Herder', 'Hunter', 'Indentured servant', 'Jester', 'Jeweler', 'Locksmith', 'Mariner', 'Mendicant', 'Mercenary', 'Merchant', 'Miller/baker', 'Miner', 'Minstrel', 'Moneylender', 'Mushroom farmer', 'Navigator', 'Noble', 'Orphan', 'Ostler', 'Outlaw', 'Parsnip Farmer', 'Potato Farmer', 'Radish Farmer', 'Rat catcher', 'Rice Farmer', 'Rope maker', 'Rutabaga Farmer', 'Sage', 'Scribe', 'Shaman', 'Slave', 'Smuggler', 'Soldier', 'Squire', 'Stonemason', 'Tax Collector', 'Trader', 'Trapper', 'Turnip Farmer', 'Urchin', 'Vagrant', 'Wainwright', 'Weaver', 'Wheat Farmer', 'Wizard\'s apprentice', 'Woodcutter') #Picks a random occupation
        self.ids.occupation_label.text = 'Occupation: ' + (str(random.choice(Occupation))) #Picks a random occupation
        Char_Title = ('Abjurer', 'Adept', 'Apparitionist', 'Archveult', 'Astrologist', 'Astrologue', 'Augurer', 'Baleful', 'Beguiler', 'Bonder', 'Capricious', 'Chamberlain', 'Charmer', 'Chronicler', 'Clairvoyant', 'Collector', 'Conjurer', 'Controller', 'Cryomancer', 'Cultist', 'Curse-giver', 'Dangerous', 'Diabolist', 'Diviner', 'Dreamer', 'Elementalist', 'Enchanter', 'Encylopaedist', 'Ensorceller', 'Ensqualmer', 'Epicure', 'Evoker', 'Factotum', 'Fortune-teller', 'Fulgurator', 'Harbinger', 'Haruspex', 'Herald', 'Horologist', 'Hypnotist', 'Illusionist', 'Immolator', 'Infinitist', 'Insidiator', 'Lich', 'Logician', 'Mage', 'Magician', 'Magic-User', 'Magus', 'Marvelous', 'Master', 'Mentalist', 'Mezmerizer', 'Mind-reader', 'Mnemonist', 'Mummer', 'Mysteriarch', 'Mystic', 'Necrope', 'Nigromancer', 'Oath-taker', 'Palmist', 'Pedant', 'Phantasmist', 'Preceptor', 'Prestidigitator', 'Prosecutor', 'Psychic', 'Sage', 'Savant', 'Scientist', 'Seancer', 'Seer', 'Shabbat', 'Shibbol(eth)', 'Soothsayer', 'Sophist', 'Spellbinder', 'Spellslinger', 'Spellweaver', 'Summoner', 'Telepath', 'Teratologist', 'Thaumaturgist', 'Theurgist', 'Thought Master', 'Transformer', 'Transmogrifier', 'Trickster', 'Truth-teller', 'Tyro', 'Vigilant', 'Visionist', 'Warden', 'Demon-Binder', 'Demon-Keeper', 'Devil-Binder', 'Devil-Keeper', 'Dragon-Binder', 'Dragon-Keeper', 'Giant-Binder', 'Giant-Keeper', 'Vampire-Binder', 'Vampire-Keeper', 'Hydra-Binder', 'Hydra-Keeper', 'Medusa-Binder', 'Medusa-Keeper', 'Cyclops-Binder', 'Cyclops-Keeper', 'Abbey', 'Acolyte', 'Advocate', 'Alienist', 'Apostle', 'Ascetic', 'Aspirant', 'Astrologue', 'Beatific', 'Bishop', 'Blackcoat', 'Brother', 'Cabalist', 'Caller', 'Cardinal', 'Celibate', 'Chaplain', 'Conclavist', 'Confessor', 'Convert', 'Curate', 'Deacon', 'Dean', 'Deist', 'Disciple', 'Ecclesiast', 'Elder', 'Eternal', 'Evangelist', 'Evil eye', 'Exorcist', 'Faithful', 'Father', 'Friar', 'Heathen-slayer', 'Hierophant', 'Imam', 'Initiate', 'Inquisitor', 'Judge', 'Keeper', 'Lama', 'Lawyer', 'Medicine Man', 'Medium', 'Missionary', 'Mullah', 'Oath-keeper', 'Occultist', 'Omen-bringer', 'Ovate', 'Padre', 'Parson', 'Patriarch', 'Petitioner', 'Philosopher', 'Pilgrim', 'Pious', 'Pontiff', 'Pope', 'Preacher', 'Priest', 'Primate', 'Prognosticator', 'Prophet', 'Proselytizer', 'Psalmist', 'Pupil', 'Quixotic', 'Rabbi', 'Rector', 'Reverend', 'Revivalist', 'Rakshasa', 'Saint', 'Scholar', 'Seeker', 'Sensei', 'Sermonizer', 'Shepherd', 'Shrinist', 'Soul-saver', 'Speaker', 'Spirit-raiser', 'Theist', 'Vicar', 'Vowmaker', 'Wanderer', 'Witness', 'Wonder worker', 'Zealot', 'Amazon', 'Archer', 'Armigerent', 'Artillerist', 'Athlete', 'Bandit', 'Battler', 'Berserker', 'Bludgeoner', 'Bodyguard', 'Brave', 'Brawler', 'Brigand', 'Bruiser', 'Brute', 'Bushwhacker', 'Cadet', 'Campaigner', 'Captain', 'Cavalier', 'Champion', 'Charger', 'Chevalier', 'Chieftain', 'Colossus', 'Conqueror', 'Defender', 'Defiler', 'Duelist', 'Exemplar', 'Fencer', 'Footman', 'Freelancer', 'Gallant', 'General', 'Gentleman', 'Giant', 'Gladiator', 'Grenadier', 'Guardian', 'Guerilla', 'Headman', 'Horseman', 'Huntsman', 'Impaler', 'Janissary', 'Jouster', 'Justicar', 'Khan', 'Knight', 'Lancer', 'Legionnaire', 'Lieutenant', 'Lord', 'Man-at-arms', 'Manslayer', 'Marauder', 'Marine', 'Mercenary', 'Myrmidon', 'Protector', 'Pugilist', 'Ravager', 'Reaver', 'Scout', 'Sentinel', 'Sergeant', 'Sharpshooter', 'Shield-bearer', 'Skirmisher', 'Soldier', 'Squire', 'Standard-bearer', 'Swordsman', 'Tank', 'Templar', 'Titan', 'Trooper', 'Vanquisher', 'Veteran', 'Victor', 'Viking', 'Vindicator', 'Warlord', 'Warmonger', 'Wildling', 'Wrestler', 'Apprentice', 'Arch-rogue', 'Artisan', 'Balladeer', 'Beggar', 'Bilker', 'Body snatcher', 'Boss', 'Bounty hunter', 'Bravo', 'Bully', 'Burglar', 'Capo', 'Card shark', 'Charlatan', 'Cheat', 'Clockworker', 'Con man', 'Cove', 'Cozener', 'Cracksman', 'Cretin', 'Crony', 'Cutpurse', 'Cutthroat', 'Darksider', 'Devil', 'Dice rattler', 'Embezzler', 'Entrepreneur', 'Executioner', 'Expert', 'Explorer', 'Fence', 'Filcher', 'Footpad', 'Forger', 'Fortunist', 'Gambler', 'Gammoner', 'Godfather', 'Guildmaster', 'Guildsman', 'Hedge creeper', 'Hit man', 'Informer', 'Jongleur', 'Journeyman', 'Juggler', 'Junkman', 'Killer', 'Knave', 'Liar', 'Lorist', 'Lyrist', 'Made man', 'Magnate', 'Magsman', 'Minstrel', 'Moneylender', 'Mugger', 'Murderer', 'Muscle', 'Muse', 'Pawnbroker', 'Racaraide', 'Raconteur', 'Rake', 'Rascal', 'Rhymer', 'Robber', 'Rogue', 'Rowdy', 'Rutterkin', 'Scallywag', 'Scammer', 'Scoundrel', 'Second story man', 'Shadow walker', 'Shark', 'Sharper', 'Shiv', 'Skald', 'Slaver', 'Sonneteer', 'Swindler', 'Thief', 'Thug', 'Tomb robber', 'Trapsmith', 'Treasure hunter', 'Troubadour', 'Villain', 'Waghalter', 'Wordsmith' )
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

#This section randomly generates if the mother and father are alive, dead, or impaired by a disability or illness
        Mother = random.randint(0,3)
        Father = random.randint(0,3)
        if Mother == 0:
            self.ids.Mother_Status.text = 'Mother\'s Health: Dead '
        if Mother == 1: 
            Disabilities = ('A Learning Disability', 'A Locomotor Disability', 'A Neurological Condition', 'A Speech and Language Disability', 'An Intellectual Disability', 'Autism', 'Blindness', 'Cerebral Palsy', 'Deafness', 'Dwarfism', 'Hearing Loss', 'Low Vision', 'Missing Both Arms', 'Missing Both Eyes', 'Missing Both Feet', 'Missing Both Legs', 'Muscular Dystrophy', 'Missing Fingers', 'Missing Left Arm', 'Missing Left Ear', 'Missing Left Eye', 'Missing Left Foot', 'Missing Left Hand', 'Missing Left Leg', 'Missing Nose', 'Missing Right Arm', 'Missing Right Ear', 'Missing Right Eye', 'Missing Right Foot', 'Missing Right Hand', 'Missing Right Leg', 'Missing Toes') #Picks a random disability
            self.ids.Mother_Status.text = 'Mother\'s Disabled with: ' + (str(random.choice(Disabilities)))
        if Mother == 2:
            Illness = ('Acidblight', 'Alcohol Addiction', 'Beggar\'s Pox', 'Brain Fever', 'Cackle Fever', 'Carrion Fever', 'Creeping Cough', 'Cobblestone Sickness', 'Dementia', 'Demon Ears', 'Desert Fever', 'Devil Rot', 'Dreaded Mallergy', 'Drug Addiction', 'Dryad\'s Rot', 'Gambling Addiction', 'Goblinitis', 'Golden Tumor', 'Grave Grub', 'Hemophilia', 'Hippogryff Hives', 'Hydrophobia', 'Leprousy', 'Mental Illness', 'Medusa Rash', 'Narcolepsy', 'Necrotic Blight', 'Ogre Poisoning', 'Puffs', 'Red Rot', 'Respiratory Disease', 'Screaming Sickness', 'Ser Avidore\'s Fire', 'Sewer Plague', 'Sewer Rat Flu', 'Sex Addiction', 'Sight Rot', 'Slate Fever', 'Slime Stomach', 'Slippery Sickness', 'Soft Bones', 'Spectre\'s Decay', 'Swamp Rage', 'Swordbearer\'s Bane', 'Tapeworm', 'Third Eye Blind', 'Turquoise Death', 'Vertigo', 'Vorel\'s Phage', 'Winter Insomnia', 'Woodland Mania', 'Yellow Plague', 'Wraith Eyes','Wyrm Flu') #Picks a random Illness
            self.ids.Mother_Status.text = 'Mother\'s Ill with: ' + (str(random.choice(Illness)))
        if Mother == 3:
            self.ids.Mother_Status.text = 'Mother\'s Health: Alive & Well '               
        if Father == 0:
            self.ids.Father_Status.text = 'Father\'s Health: Dead '
        if Father == 1: 
            Disabilities = ('A Learning Disability', 'A Locomotor Disability', 'A Neurological Condition', 'A Speech and Language Disability', 'An Intellectual Disability', 'Autism', 'Blindness', 'Cerebral Palsy', 'Deafness', 'Dwarfism', 'Hearing Loss', 'Low Vision', 'Missing Both Arms', 'Missing Both Eyes', 'Missing Both Feet', 'Missing Both Legs', 'Muscular Dystrophy', 'Missing Fingers', 'Missing Left Arm', 'Missing Left Ear', 'Missing Left Eye', 'Missing Left Foot', 'Missing Left Hand', 'Missing Left Leg', 'Missing Nose', 'Missing Right Arm', 'Missing Right Ear', 'Missing Right Eye', 'Missing Right Foot', 'Missing Right Hand', 'Missing Right Leg', 'Missing Toes') #Picks a random disability
            self.ids.Father_Status.text = 'Father\'s Disabled with: ' + (str(random.choice(Disabilities)))
        if Father == 2:
            Illness = ('Acidblight', 'Alcohol Addiction', 'Beggar\'s Pox', 'Brain Fever', 'Cackle Fever', 'Carrion Fever', 'Creeping Cough', 'Cobblestone Sickness', 'Dementia', 'Demon Ears', 'Desert Fever', 'Devil Rot', 'Dreaded Mallergy', 'Drug Addiction', 'Dryad\'s Rot', 'Gambling Addiction', 'Goblinitis', 'Golden Tumor', 'Grave Grub', 'Hemophilia', 'Hippogryff Hives', 'Hydrophobia', 'Leprousy', 'Mental Illness', 'Medusa Rash', 'Narcolepsy', 'Necrotic Blight', 'Ogre Poisoning', 'Puffs', 'Red Rot', 'Respiratory Disease', 'Screaming Sickness', 'Ser Avidore\'s Fire', 'Sewer Plague', 'Sewer Rat Flu', 'Sex Addiction', 'Sight Rot', 'Slate Fever', 'Slime Stomach', 'Slippery Sickness', 'Soft Bones', 'Spectre\'s Decay', 'Swamp Rage', 'Swordbearer\'s Bane', 'Tapeworm', 'Third Eye Blind', 'Turquoise Death', 'Vertigo', 'Vorel\'s Phage', 'Winter Insomnia', 'Woodland Mania', 'Yellow Plague', 'Wraith Eyes','Wyrm Flu') #Picks a random Illness
            self.ids.Father_Status.text = 'Father\'s Ill with: ' + (str(random.choice(Illness)))
        if Father == 3:
            self.ids.Father_Status.text = 'Father\'s Health: Alive & Well '   
 
#Generating random relationship status for the generated NPC         
        Relationship_Status = ('Single','Divorced', 'In a relationship', 'Married', 'Married and having an affair')
        self.ids.Relationship_Status.text = 'Relationship Status: ' + (str(random.choice(Relationship_Status))) #Picks a random Relationship Status

#Generating random sexual orientation for the generated NPC
        Sexual_Orientation = ('Heterosexual', 'Homosexual', 'Bi-Sexual', 'Asexual', 'Transgender', 'Questioning')
        self.ids.Sexual_Orientation.text = 'Sexual Orientation: ' + (str(random.choice(Sexual_Orientation))) #Picks a random Sexual Orientation
           

#Generating 3 Personality Traits for generic npc
        Personality_Traits = {'Abrasive',
                              'Absent-Minded',
                              'Aggressive',
                              'Alcoholic',
                              'Always carries food in their pockets',
                              'Always goes straight to the point',
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
                              'Carries out a complicated religious ritual every morning',
                              'Cautious',
                              'Changes subject very often',
                              'Claims to worship one god but secretly worships another',
                              'Collects something',
                              'Compares everything to a fight',
                              'Constantly flattering people they talk to',
                              'Constantly looks for the loophole',
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
                              'Enjoys tavern brawls',
                              'Feels more comfortable underwater',
                              'Flattery is my preferred trick for getting what I want', 
                              'Focused',
                              'Frequently asks for help',
                              'Frequently thinks aloud',
                              'Gets bored easily',
                              'Goes out every night looking for something',
                              'Great at hiding',
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
                              'Lies poorly on purpose',
                              'Likes to eat like it\'s his last meal',
                              'Likes to swim',
                              'Local sports champion',
                              'Loudly worships a deity',
                              'Loves discovering new mysteries and solving them',
                              'Makes anyone they speak to feel like the most important person in the world',
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
                              'Occasionally gives money to the poor',
                              'Occasionally hums old dwarven songs',
                              'Only talks in whispers',
                              'Only talks loudly',
                              'Openly worships a deity',
                              'Prone to violence',
                              'Proudly worships a deity',
                              'Quick',
                              'Quick to forgive',
                              'Rarely speaks',
                              'Rarely thinks ahead',
                              'Reacts violently to weird clothes',
                              'Relentless',
                              'Runs everywhere instead of walking',
                              'Sarcasm and insults are my weapons of choice',
                              'Sees everything as a challenge',
                              'Sees fighting as a solution to any problem',
                              'Self confident',
                              'Share everything I own', 
                              'Sleeps fully dressed, ready to run',
                              'Slow',
                              'Specialized',
                              'Sporadically lies',
                              'Sporadically quotes their father',
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
                              'Works hard to play hard afterwards',
                              'Would rather act than talk or think',
                              'Zealously worships a deity'}
        self.ids.Personality_Traits.text = ('Personality Traits: ') + '\n' + '\n' + '1.) ' + (','.join((random.sample(list(Personality_Traits), 1)))) + '\n' + '\n' + '2.) ' + (','.join((random.sample(list(Personality_Traits), 1)))) + '\n'+ '\n' + '3.) ' + (','.join((random.sample(list(Personality_Traits), 1))))


#Generating eye color for the generated NPC
        Eye_Color = ('Light Blue', 'Ice Blue', 'Blue', 'Grey-blue', 'White', 'Black', 'Grey', 'Teal', 'Ice Green', 'Green', 'Grey-green', 'Pale gold', 'Yellow', 'Gold', 'Orange', 'Brown', 'Dark Brown', 'Red', 'Pale Purple', 'Purple', 'Magenta', 'Yellow-green', 'Brown & Green', 'Gold & Green', 'Albino', 'Blind')
        self.ids.Eye_Color.text = 'Eye Color: ' + (str(random.choice(Eye_Color))) #Picks a random Eye color
        
#Generating Hair Style/Hair color for the generated NPC
        Hair_Style = ('Afro', 'Afro Puffs', 'Asymmetric Cut', 'Bangs', 'Beehive', 'Big Hair', 'Blowout', 'Bowl Cut', 'Bob Cut', 'Bouffant', 'Braid', 'Brush Cut', 'Bun', 'Butch Cut', 'Buzz Cut', 'Caesar Cut', 'Chignon', 'Chonmage', 'Comb Over', 'Comma Hair', 'Conk', 'Cornrows', 'Crew Cut', 'Crop', 'Crown Braid', 'Croydon Facelift', 'Curtained Hair', 'Devilock', 'Dido Flip', 'Double Buns', 'Dreadlocks', 'Ducktail', 'Eton Crop', 'Extensions', 'Fade', 'Fallera Hairdo', 'Fauxhawk', 'Feather Cut', 'Feathered Hair', 'Finger Waves', 'Fishtail Hair', 'Flattop', 'Flipped-up ends', 'Fontange', 'French Braid', 'French Twist', 'Fringe(bangs)', 'Frosted Tips', 'Full Crown', 'Half Crown', 'Half Updo', 'Harvard Clip', 'Hi-Top Fade', 'High and Tight', 'Highlights', 'Hime Cut', 'Induction Cut', 'Ivy league', 'Jewfro', 'Jheri Curl', 'Layered Curl', 'Liberty Spikes', 'Line Up', 'Lob', 'Marcel Waves', 'Mod Cut', 'Mohawk', 'Mop Top', 'Mullet', 'Odango', 'Oseledets', 'Pageboy', 'Payot', 'Perm', 'Pigtails', 'Pixie Cut', 'Pompadour', 'Ponyhawk', 'Ponytail', 'Psychobilly Wedge', 'Queue', 'Quiff', 'Rattail', 'Razor Cut', 'Ringlets', 'Shag Cut', 'Shape-Up', 'Shingle-Bob', 'Short Back and Sides', 'Short Brush Cut', 'Short Hair', 'Slicked Back', 'Spiky Cut', 'Step Cut', 'Surfer Hair', 'Tail on Back', 'Taper Cut', 'The Rachel', 'Tonsure', 'Undercut', 'Updo', 'Waves', 'Weave', 'Widow\'s Peak', 'Wings')
        Hair_Color = ('Black', 'Blonde', 'Brown', 'Grey', 'Red', 'White')
        self.ids.Hair_Style.text = 'Hair Style: ' + (str(random.choice(Hair_Color)))  + ' ' + (str(random.choice(Hair_Style)))#Picks a random Hair Style

        
#Generating Height for the generated NPC
        Height = ('Very Short', 'Short', 'Rather Short', 'Medium Height', 'Rather Tall', 'Tall', 'Very Tall')
        self.ids.Height.text = 'Height: ' + (str(random.choice(Height))) #Picks a random generic height

#Generating Unique Traits for the generated NPC
        Unique_Trait = ('Albino', 'Allergic to gnomes', 'Curved Spine', 'Deaf in left Ear', 'Deaf in right ear', 'Elaborate abstract tattoo on left leg', 'Four tiny piercings on left eyebrow', 'Four tiny piercings on right eyebrow', 'Frequently smokes a pipe', 'Frequently Squints', 'Gestures profusely during a conversation', 'Has a large scar on left arm', 'Has a large scar on left hand', 'Has a large scar on right arm', 'Has a large scar on right hand', 'Heavily scarred on face', 'High pitched voice', 'Impressive lisp', 'Inherited a family estate', 'Inherited a small forest', 'Missing all fingers from left hand', 'Missing all toes from left foot', 'Missing all fingers from right hand', 'Missing all toes from right foot', 'Missing both feet', 'Missing both legs', 'Missing left ear', 'Missing left foot', 'Missing left leg', 'Missing right ear', 'Missing right foot', 'Missing right leg', 'Missing four fingers from left hand', 'Missing four toes from left foot', 'Missing four fingers from right hand', 'Missing four toes from right foot', 'Missing one finger from left hand', 'Missing one toe from left foot', 'Missing one finger from right hand', 'Missing one toe from right foot', 'Missing three fingers from left hand', 'Missing three toes from left foot', 'Missing three fingers from right hand', 'Missing three toes from right foot', 'Missing two fingers from left hand', 'Missing two toes from left foot', 'Missing two fingers from right hand', 'Missing two toes from right foot', 'Piercing through nose', 'Piercings on both ears', 'Piercing on left ear', 'Piercing on right ear', 'Smells of Cabbage', 'Smells of dog', 'Smells of garbage', 'Smells lightly of dirt', 'Sunken Breastbone', 'Uses a beautiful walking cane', 'Tattoos on face', 'Wears dark glasses to mask eyes', 'Wears an eye patch on left eye', 'Wears an eye patch on right eye')
        self.ids.Unique_Trait.text = 'Unique Physical Trait: ' + (str(random.choice(Unique_Trait)))#Picks a random unique trait   

    # Name Gen Pop - Create a popup dialog with a label and a close button
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
        self.ids.Eye_Color.text = ''
        self.ids.Hair_Style.text = ''
        self.ids.Facial_Hair.text = ''
        self.ids.Height.text = ''
        self.ids.Unique_Trait.text = ''
         

class MonsterGenerator(GridLayout):  
    # Monster Generation - Gives users buttons to select to randomly generate a monster
    def MonsterGeneration(self):

        layout      = GridLayout(cols=1, padding=10)

       

        DragonButton  = Button(text  = "Click for a random dragon type monster")

        HumanoidButton = Button(text = "Click for a random humanoid type monster")

 

        layout.add_widget(DragonButton)

        layout.add_widget(HumanoidButton)       

   

        # Instantiate the modal popup and display

        popup = Popup(title='Monster Generator',

                      content=layout)  

        popup.open()   

       
        # Dismiss causes the popup to go away. Release generates the call to the name generator specified
        DragonButton.bind(on_press=popup.dismiss)
        DragonButton.bind(on_release = self.Dragon_kind_gen) 
        HumanoidButton.bind(on_press=popup.dismiss)
        HumanoidButton.bind(on_press = self.Humanoid_gen)  

      
class app1(App):
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