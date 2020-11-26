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
        Occupation = ( #Picks a random occupation
        'Abbot/Abbess', #the head of an abbey of monks.
        'Abcedarian', #teaches the illiterate.
        'Abjurer', #a mage focused in protective spells.
        'Acater', #provides and prepares foodstuffs or delicacies for events such as festivals.
        'Accoucheur/Obstetrician/Midwife', #assists in childbirth and the care of women giving birth. 
        'Accountant', #keeps and inspects financial accounts.
        'Accoutrementer/Coinsmith', #makes currency for the government.
        'Acolyte', #assists the celebrant in a religious service or procession.
        'Acrobat', #performs spectacular gymnastic feats.
        'Actor', #impersonates characters, typically on stage in a theatrical production.
        'Actuary', #compiles and analyzes statistics and uses them to calculate risk. 
        'Adept',
        'Admiral', #commands a fleet or naval squadron. 
        'Advocate',
        'Aerialist/Trapezist', #performs acrobatics high above the ground on a tightrope or trapeze. 
        'Affeeror', #determines the values of fines and amercements.
        'Agister', #affords pasture to the livestock of others for a price.
        'Alchemist', #transforms or creates something within nature through (usually) ritualist magic.
        'Alderman', #a civic dignitary in the local council ranked below the mayor.
        'Alienist', #assesses the competence of a defendant in a court of law.
        'Almoner', #distributes money and food to poor people.
        'Amazon',
        'Animal Collector', #collects and deals in rare and exotic animals and monsters.
        'Animal Handler', 
        'Animal Trainer',
        'Anthropologist', #studies the customs, beliefs, and relationships of humanoids and intellectually and culturally advanced creatures. 
        'Apostle', 
        'Apothecarist', #prepares and sells medicines, drugs, and potions. 
        'Apparitionist',
        'Appraiser', #assesses the monetary value of something. 
        'Apprentice', #studies a trade under a skilled employer.
        'Arborist',
        'Archaeologist', #studies humanoid history and prehistory through the excavation of sites and the analysis of artifacts and other physical remains.
        'Arch-rogue',
        'Archbishop', #responsible for an archdiocese, their surrounding district.
        'Archivist', #maintains and is in charge of archives.
        'Archmage', #an extremely powerful mage. 
        'Archveult',
        'Architect', #designs buildings or landscapes and in many cases supervises their construction. 
        'Armigerent', 
        'Armorer', #specializes in making and repairing armor.
        'Arranger', #adapts a musical composition for performance.
        'Artillerist', 
        'Artisan', 
        'Artist', 
        'Ascetic', 
        'Aspirant',
        'Assay Master', #oversees the testing of currency. 
        'Assayer', #determiner of the proportions of metal in ore and the amount of copper, silver, gold, or platinum in coins.
        'Astrologer', #uses astrology to tell others about their character or to predict their future.
        'Astrologist', 
        'Astrologue', 
        'Athlete', #proficient in sports and other forms of physical exercise.
        'Auctioneer', #conducts auctions by accepting bids and declaring goods sold. 
        'Augurer', 
        'Bagniokeeper', #owner of a bath house or brothel.
        'Bailiff', #looks after prisoners.
        'Baker', #bakes bread and cakes.
        'Baler', 
        'Balladeer', 
        'Bandit', #a robber or outlaw belonging to a gang and typically operating in an isolated or lawless area.
        'Banker', #an officer or owner of a bank or group of banks.
        'Barber', #cuts hair and shaves or trims beards.
        'Barkeep', #works and serves drinks in a bar.
        'Barmaid/Barboy', #serves drinks and food in a bar as well as engaging with customers.
        'Baron/Baroness', #a member of the lowest order of the British nobility.
        'Barrister', 
        'Battler', 
        'Beadle',  
        'Beekeeper', 
        'Beggar', 
        'Beguiler', 
        'Berserker', 
        'Bilker',
        'Billboardposter', #a person who puts up notices, signs and advertisements. 
        'Bishop', #a senior member of the clergy, usually in charge of a diocese and empowered to confer holy orders.
        'Blackcoat',
        'Blackmailer', 
        'Blacksmith', #forges and repairs things in metal, including weapons, armor, utensils, etc.
        'Bladesmith', #specializes in making and repairing bladed weapons, especially swords and daggers. 
        'Bludgeoner', 
        'Body snatcher', 
        'Bodyguard', #escorts and protects another person, especially a dignitary.
        'Bonder', 
        'Bookbinder', #binds books and wraps scrolls.
        'Bookkeeper', #keeps records of financial affairs.
        'Bookseller', 
        'Bottler', #bottles drinks and other liquids.
        'Bouncer', #prevents troublemakers from entering or to eject them from the premises of an establishment.
        'Bounty hunter', 
        'Bowyer', #makes bows and crossbows.
        'Brave', 
        'Bravo', 
        'Brawler',
        'Breeder',
        'Brewer', #brews ale.
        'Brickmaker', #crafts bricks from clay, stone, or other materials.
        'Brickmason', #builds with mineral products such as stones, bricks, cinder blocks, or tiles, usually with the use of mortar as a bonding agent. 
        'Brigand',
        'Broom Maker', #makes brooms and brushes. 
        'Brother', 
        'Bruiser', 
        'Brute', 
        'Bully', 
        'Burglar', #illegally enters buildings and steals things.
        'Bushwhacker',
        'Business Owner', #owns a business entity in an attempt to profit from its successful operations.
        'Busker/Street Musician', #performs in a public place, often for money. 
        'Butcher', #cuts up and sells meat.
        'Butler', #the chief servant of a household.
        'Cabalist', 
        'Cadet', 
        'Caller', 
        'Campaigner',
        'Candlemaker', #makes candles and wax from honey and tallow. 
        'Cantor', #sings liturgical music and leads prayer in a synagogue.
        'Capo', 
        'Capricious', 
        'Captain', #an army officer of high rank in charge of commanding squadrons of soldiers.
        'Caravan Guard', 
        'Card shark', 
        'Cardinal', #a leading dignitary of a church, nominated by the highest official.
        'Caregiver', #looks after a sick, elderly, or disabled person.
        'Carpenter', #makes and repairs wooden objects and structures.
        'Cartwright', #makes and repairs carts and wagons. 
        'Castellan', #the governor of a castle.
        'Cavalryman/Cavalier', #a skilled horseback rider.
        'Celebrity', #a famous person.
        'Celibate', 
        'Chamberlain', 
        'Champion', 
        'Chancellor', #a senior state or legal official.
        'Chandler', #deals in provisions and supplies.
        'Chaplain', #a member of the clergy attached to a private chapel, institution, ship, branch of the armed forces, etc.
        'Charcoal Maker', #manufactures charcoal by carbonizing wood in a kiln.
        'Charger', 
        'Charlatan',
        'Charity Worker',
        'Charlatan/Conman', #tricks people by gaining their trust and persuading them to believe something that is not true in order to benefit from the encounter.
        'Charmer',
        'Chatelaine/Majordomo', #a person in charge of a large household. 
        'Cheat', 
        'Cheesemaker',
        'Chef', #a professional cook trained in the culinary arts. 
        'Chest-maker', 
        'Chevalier', 
        'Chieftain', #leads or rules a people or clan.
        'Chimney Sweeper', #a small person, typically a child, who ascends chimneys to clean them.
        'Choirmaster', #trains a choir and orchestrates their singing when they perform. 
        'Chronicler', 
        'City Watch', #an officer of law enforcement who resides in larger towns or cities.
        'Clairvoyant',
        'Clerk', #undertakes routine administrative duties in a business or bank. 
        'Clockworker',
        'Clown', #comic entertainer who wears a traditional costume and exaggerated makeup. 
        'Cobbler', #makes and repairs footwear.
        'Cockfighter/Gamefighter', #engages in arena matches in which animals or monsters are pitted against one another, typically to the death.
        'Collector', #collects things of a specified type, professionally or as a hobby.
        'Colossus',
        'Comedian', #entertainer whose act is designed to make an audience laugh. 
        'Commissar', #teaches principles and policies to military units.
        'Con man', 
        'Conclavist',
        'Conductor', #directs the performance of an orchestra. 
        'Confessor', #hears confessions and gives absolution and spiritual counsel.
        'Confidence artist', 
        'Conjurer',
        'Constable', #an officer with limited policing authority, typically in a small town.
        'Cook', #prepares food for eating.
        'Cooper/Hooper', #makes and repairs casks and barrels. 
        'Conqueror',
        'Conservationist', #advocates for the protection and preservation of the environment and wildlife.
        'Construction Worker', #a laborer in the physical construction of a built environment and its infrastructure. 
        'Contortionist', #twists and bends their body into strange and unnatural positions.
        'Controller', 
        'Convert', 
        'Cooper',
        'Copyist', #makes copies of handwritten documents or music. 
        'Corn Farmer', 
        'Costermonger',
        'Costumer', #makes theatrical costumes.
        'Count/Earl/Countess', #a nobleperson ranking above a viscount and below a marquess.
        'Courier', #transports packages and documents. 
        'Courtier', #attends court as a companion or adviser to the king or queen.
        'Cove',
        'Cowherd', 
        'Cozener', 
        'Cracksman', 
        'Cretin',
        'Crime Boss', #controls and supervises a criminal organization. 
        'Crony', 
        'Croupier', #runs a gaming table by gathering in and paying out money or tokens.
        'Cryomancer', 
        'Cult Leader', #the organizational leader of a cult who is occasionally also the founder.
        'Cultist', #a member of a cult who generally lives outside of conventional society and worships an unorthodox patron.
        'Curator', #keeper and custodian of a museum or other collections of precious items.
        'Curse-giver', 
        'Cutler', #makes cutlery.
        'Cutpurse', #a pickpocket or thief.
        'Cutthroat', 
        'Cyclops-Binder', 
        'Cyclops-Keeper',
        'Dairyboy/Dairymaid', 
        'Dancer', #moves their body rhythmically with or without musical accompaniment.
        'Dangerous', 
        'Darksider', 
        'Day Laborer', 
        'Deacon', #an ordained minister of an order ranking below that of priest.
        'Dean',
        'Debt Collector', #recovers money owed on delinquent accounts. 
        'Defender', 
        'Defiler', 
        'Deist', 
        'Demon-Binder', 
        'Demon-Keeper',
        'Detective/Investigator', #investigates and solves crimes. 
        'Devil', 
        'Devil-Binder', 
        'Devil-Keeper', 
        'Diabolist', 
        'Dice rattler',
        'Diplomat', #an official representing a country abroad.
        'Disciple', 
        'Ditch Digger', 
        'Diviner', #seeks ultimate divination in order to further understand or meet godly substance.
        'Dock worker', 
        'Dragon-Binder', 
        'Dragon-Keeper',
        'Draper', #an alcohol merchant. 
        'Dreamer', 
        'Drug Dealer', #dealer of illegal substances.
        'Drug Lord', #controls a network of persons involved in the illegal drugs trade and transactions.
        'Drummer/Fifer', #a non-combatant foot soldier who sounds signals for changes in formation in combat.
        'Duelist', #skilled in one-on-one combat.
        'Duke/Duchess', #rules over a duchy and is of the highest rank below the monarch.
        'Dyer', #dyes cloth and other materials. 
        'Ecclesiast', 
        'Elder', 
        'Elementalist', #manipulates nature’s elements to their will.
        'Embezzler',
        'Embroiderer', #ornaments with needlework. 
        'Emperor/Empress', #the supreme sovereign ruler of an extensive group of states or countries under a single authority.
        'Enchanter', #uses sorcery to put someone or something under a spell.
        'Encylopaedist',
        'Engraver', #incises a design onto a hard surface by cutting grooves into it. 
        'Ensorceller', 
        'Ensqualmer', 
        'Entrepreneur', #organizes and operates a business or businesses, taking on greater than normal financial risks in order to do so.
        'Epicure',
        'Equilibrist', #performs balancing feats. 
        'Eternal', 
        'Evangelist', 
        'Evil eye', 
        'Evoker', #manipulates energy or taps into an unseen source of power in order to produce a desired kinetic end.
        'Ex-Adventurer',
        'Ex-Noble', 
        'Executioner', #carries out a sentence of death on a legally condemned person.
        'Exemplar', 
        'Exorcist', #expels or attempts to expel evil spirits from a person or place.
        'Explorer',
        'Exterminator', #exterminates unwanted rodents and insects.
        'Extortioner', #extorts money from someone by threatening to expose embarrassing information about them. 
        'Factotum',
        'Faithful', 
        'Falconer',
        'Farmer',
        'Farrier', #trims and shoes horses’ hooves. 
        'Fashion Designer', #applies design, aesthetics and natural beauty to garments and their accessories.
        'Father', 
        'Fence', #deals in stolen goods.
        'Fencer', 
        'Filcher',
        'Firefighter', #extinguishes fires.
        'Fisher',
        'Fletcher', #makes and repairs arrows.
        'Florist', 
        'Food & Drink Taster', #ingests food that was prepared for someone else to confirm it is safe to eat.
        'Footman', 
        'Footpad',
        'Forager', 
        'Forester', 
        'Forger', #produces fraudulent copies or imitations.
        'Fortune Teller', 
        'Fortunist',
        'Fowler', 
        'Freelancer', 
        'Friar', 
        'Fugitive', #a person who has escaped from a place or is in hiding, especially to avoid arrest or persecution.
        'Fulgurator',
        'Furniture Artisan', #makes and repairs furniture.
        'Furrier', #prepares furs for adornment. 
        'Gallant', 
        'Gambler',
        'Gamekeeper' #breeds and protects game, typically for a large estate
        'Gammoner', # A thief's accomplice who distracts the victim while the thief steals.
        'Gardener/Landscaper', #tends and cultivates a garden.
        'General', #the chief commander of an army.
        'General Contractor', #supervises a construction site, manages its vendors and trades, and communicates information to all involved parties. 
        'Gentleman', 
        'Giant', 
        'Giant-Binder', 
        'Giant-Keeper', 
        'Gladiator', # fights against other people, wild animals, or monsters in an arena.
        'Glassworker', # blows glass planes and items.
        'Glasspainter', #produces colorful designs on or in glass.
        'Glazier', #fits glass into windows and doors. 
        'Glovemaker', #makes and repairs gloves.
        'Godfather', 
        'Goldsmith/Silversmith', #a smith who specializes in precious metals.
        'Gong Farmer', #digs out and removes excrement from privies and cesspits.
        'Government Official',
        'Governor', 
        'Gravedigger', #digs graves for the purposes of a funeral ceremony.
        'Grave Tender', 
        'Grenadier',
        'Grocer', #a food merchant.
        'Groom', #cleans and brushes the coats horses, dogs, or other animals.
        'Groundskeeper', #maintains an athletic field, a park, or the grounds of a graveyard or other institution.\
        'Guard/Sentinel', #a person who keeps watch, especially a soldier or other person formally assigned to protect a person or to control access to a place. 
        'Guardian', 
        'Guerilla', 
        'Guild Beggar', 
        'Guildmaster', #leads an economically independent producer (a “guild,” an association of craftsmen or merchants that often holds considerable bureaucratic power).
        'Guildsman', 
        'Gypsy', 
        'Haberdasher', 
        'Harbinger', 
        'Haruspex',
        'Hatter/Milliner', #makes and repairs headwear. 
        'Headman', 
        'Healer', #able to cure a disease or injury using magic.
        'Hearth Witch/Hearth Wizard', #incorporates spells and enchantments in cooking.
        'Heathen-slayer', 
        'Hedge creeper', 
        'Herald', #a messenger who carries important news.
        'Herbalist', 
        'Herder', #supervises a herd of livestock or makes a living from keeping livestock, especially in open country.
        'Hierophant',
        'High Priest/Pope', #the chief priest of a religion.
        'Highwayman', #robs travelers on a road.
        'Hit man', 
        'Horologist', 
        'Horseman',
        'Horse Trainer', #tends to horses and teaches them different disciplines. 
        'Hunter', #hunts game or other wild animals.
        'Huntsman', 
        'Hydra-Binder', 
        'Hydra-Keeper', 
        'Hypnotist',
        'Illuminator', #paints and calligraphs to adorn or enlighten scrolls and manuscripts. 
        'Illusionist', #performs tricks and spells that deceive the senses.
        'Imam', 
        'Immolator', 
        'Impaler', 
        'Indentured servant', 
        'Infinitist', 
        'Informer', 
        'Initiate', 
        'Innkeeper', #owns and runs an inn.
        'Inquisitor', #seeks to eliminate heresy and other things contrary to the doctrine or teachings of their faith.
        'Insidiator',
        'Inspection Officer', #responsible for the inspection of military units to ensure they meet appropriate standards of training and efficiency.
        'Instrument Maker', #makes and repairs musical instruments.
        'Intelligence Officer', #collects, compiles and organizes information about the enemy.
        'Interpreter', #interprets language and its meaning, especially within ancient manuscripts.
        'Investigator',
        'Jailer', #supervises a jail and the prisoners in it.
        'Janissary', 
        'Jester', #professional joker or “fool” at court, typically wearing a cap with bells on it and carrying a mock scepter.
        'Jeweler', #designs, makes, and repairs necklaces, bracelets, watches, etc., often containing jewels.
        'Jongleur', 
        'Journeyman', 
        'Jouster', 
        'Judge', #decides cases in a court of law.
        'Juggler', #keeps several objects in motion in the air at the same time by alternately tossing and catching them. 
        'Junkman', 
        'Justicar', 
        'Keeper', 
        'Khan',
        'Kidnapper', #abducts people and holds them captive, typically to obtain a ransom. 
        'Killer', 
        'King/Queen', #the ruler of an independent state and its people.
        'Kitchen Drudge', #performs menial work in a kitchen.
        'Knacker', #disposes of dead or unwanted animals.
        'Knave', 
        'Knight', #serves his or her sovereign after being bestowed a rank of royal honor.
        'Labor Boss', 
        'Lady-in-Waiting', #attends a queen, princess, or other high-ranking feminine nobleperson.
        'Lama', 
        'Lamplighter', #lights street or road lights at dusk.
        'Lancer',
        'Land Surveyor', #establishes maps and boundaries for ownership or other purposes required by government or civil law.
        'Lapidary', #turns stone, minerals, or gemstones into decorative items such as cabochons, engraved gems, and faceted designs.
        'Laundry Worker', #a laborer who takes part in the washing, drying, and ironing of clothes and other fabric items. 
        'Lawyer/Advocate', #practices or studies law, typically an attorney or a counselor.
        'Leatherworker', #makes items from leather such as pouches, scabbards, straps, etc. 
        'Lector', #reads to others while they work for entertainment.
        'Legionnaire',
        'Legbreaker', 
        'Liar', 
        'Lich', 
        'Lieutenant', #an officer of middle rank in the armed forces.
        'Limner', #paints portraits or miniatures.
        'Linguist', #studies the essence of communication, including the units, nature, structure, and modification of language.
        'Loan Shark', #charges extremely high rates of interest for moneylending, typically under illegal conditions.
        'Locksmith', #makes and repairs locks.
        'Logician', 
        'Longshoreman', #loads and unloads ships in a port.
        'Lorist',
        'Lumberjack', #fells trees, cuts them into logs, and transports them to a sawmill. 
        'Luthier', #makes and repairs stringed instruments.
        'Lyrist',
        'Made man', 
        'Mage', #a magic-user.
        'Magician', 
        'Magic-User',
        'Magistrate',
        'Magnate', 
        'Magsman', 
        'Magus',
        'Maid', #a domestic servant of a household. 
        'Makeup Artist', #applies cosmetics to models, actors, nobles, etc.
        'Man-at-arms', 
        'Manslayer', 
        'Marauder', 
        'Marine', 
        'Mariner',
        'Marketeer',
        'Marksman/Archer', 
        'Marquess/Marchioness', #a nobleperson ranking above a count and below a duke.
        'Marshall', #has the charge of the cavalry in the household of a monarch.
        'Marvelous',
        'Master-of-Coin', #supervises the royal treasury, advises the monarch on financial matters, and is responsible for raising money through taxation.
        'Master-of-Horses', #supervises and commands all horses under a jurisdiction.
        'Master-of-Hounds', #maintains a pack of hounds and their associated staff, equipment, and hunting arrangements. 
        'Master-of-the-Revels', #responsible for overseeing royal festivities.
        'Medic', #a medical practitioner equipped for the battlefield. 
        'Medium', #uses extrasensory perception, magic, or divine powers to identify information hidden from the normal senses. 
        'Medusa-Binder', 
        'Medusa-Keeper', 
        'Mendicant', 
        'Mentalist', 
        'Mercenary', #a soldier without allegiance who works for money, typically a member of a company or guild.
        'Mercer', #weaves textile fabrics, especially silks, velvets, and other fine materials.
        'Merchant', #sells and trades goods.
        'Messenger', #carries messages between recipients.
        'Meteorologist', #forecasts and manipulates weather.
        'Mezmerizer', 
        'Miller/baker', #owns or works in a grain mill. 
        'Mind-reader', 
        'Miner', #works underground in mines in order to obtain minerals such as coal, diamonds, or gold
        'Minister' #assists with the administration of business.
        'Minstrel', #recites lyric or heroic poetry for nobility.
        'Missionary', #goes on a religious mission to promote their faith in a foreign place.
        'Mistress', 
        'Mnemonist',
        'Moneychanger', #exchanges one currency for another. 
        'Moneylender', #lends money to others who pay interest.
        'Model', #poses as a subject for an artist, fashion designer, or sculptor.
        'Monster Collector', #collects and deals in rare and exotic animals and monsters.
        'Monster Handler', #Handles and managers exotic animals and monsters
        'Mugger', 
        'Mullah', 
        'Mummer', 
        'Muse', 
        'Mushroom farmer',
        'Musician', #plays a musical instrument. 
        'Myrmidon', 
        'Mysteriarch', 
        'Mystic',
        'Nanny/Nursemaid', #a servant employed to look after a young child or children. 
        'Navigator', 
        'Necrope', 
        'Necromancer', #communicates with and conjures the spirits of the dead.
        'Noble/Aristocrat', #a person belonging to a class with high social or political status.
        'Notary', #performs certain legal formalities, especially to draw up or certify contracts, deeds, and other documents for use in other jurisdictions.
        'Nun', #a member of a religious community of women, especially a cloistered one, living under vows of poverty, chastity, and obedience.
        'Oath-keeper', 
        'Oath-taker', 
        'Occultist', 
        'Omen-bringer',
        'Operator', #a laborer who operates equipment, typically in construction.
        'Optician' #makes and repairs eyeglasses.
        'Orator/Spokesman', #makes statements on behalf of a group or individual nobleperson. 
        'Orphan', 
        'Ostler', 
        'Outlaw', 
        'Ovate', 
        'Padre',
        'Page', #a young attendant to a person of noble rank. 
        'Painter', #paints pictures.
        'Palmist', 
        'Pardoner', #raises money for religious works by soliciting offerings and granting indulgences.
        'Parsnip Farmer', 
        'Parson',
        'Pastry Chef', #makes desserts, especially cakes and pastries.
        'Pathfinder', #scouts ahead and discovers a path or way for others. 
        'Patriarch', 
        'Pawnbroker', 
        'Pedant', 
        'Peddler', #travels from place to place selling assorted items.
        'Petitioner', 
        'Phantasmist', 
        'Philosopher',
        'Physician',
        'Pick Pocket',
        'Pilgrim',
        'Pimp/Madame', #controls prostitutes and arranges clients for them, taking part of their earnings in return. 
        'Pious',
        'Pirate', #attacks and robs ships at sea.
        'Plantation Owner', #an owner of an estate on which crops are cultivated by resident labor, typically slave labor.
        'Plasterer', #applies plaster to walls, ceilings, or other surfaces.
        'Playwright', #writes plays or musicals.
        'Plumber', #installs and repairs the fittings of water supply and sanitation.
        'Plumer', #hunts birds for their plumes.
        'Plutocrat',
        'Poacher', #hunts illegal game.
        'Poet', #writes ballads, epics, sonnets, or other forms of poetry.
        'Poisoner', #makes poisons to harm or kill.
        'Pontiff', 
        'Porter', #carries luggage and other loads. 
        'Potato Farmer', #A farmer who specializes in potatoes
        'Potter', #makes pots, bowls, plates, etc., out of clay.
        'Preceptor', 
        'Prestidigitator', 
        'Priest', #has the authority to perform certain rites and administer certain sacraments.
        'Primate',
        'Prince/Princess', #the direct descendant of a monarch.
        'Printer', #a person who applies pressure to an inked surface resting upon a print medium (such as paper or cloth), thereby transferring the ink to manufacture a text. 
        'Privateer', #engages in maritime warfare under a commission of war.
        'Prognosticator', 
        'Prophet', #regarded as an inspired teacher or proclaimer of the will of God.
        'Proprietor',
        'Prosecutor', 
        'Proselytizer',
        'Prospector', #searches for mineral deposits, especially by drilling and excavation. 
        'Prostitute', #engages in sexual activity for payment.
        'Protector', 
        'Psalmist', 
        'Psychic', 
        'Pugilist', 
        'Pupil',
        'Quarryman/Quarrywoman', #quarries stone.
        'Quartermaster', #responsible for providing quarters, rations, clothing, and other supplies.
        'Quixotic', 
        'Rabbi', 
        'Racaraide', 
        'Raconteur', 
        'Radish Farmer',
        'Raider/Marauder', #makes sudden, unprompted attacks against defenseless or near-defenseless settlements. 
        'Rake', 
        'Rakshasa', 
        'Rascal', 
        'Rat catcher', 
        'Ravager', 
        'Reaver', 
        'Rector',
        'Renderer', #converts waste animal tissue into usable materials.
        'Restorer', #repairs or renovates a work of art so as to return it to its original condition. 
        'Reverend', 
        'Revivalist', 
        'Rhymer', 
        'Rice Farmer',
        'Ringmaster/Ringmistress', #master of ceremony who introduces the circus acts to the audience.
        'Ritualist', #practices or advocates the observance of ritual (formula intended to trigger a magical effect on a person or objects).
        'Roadlayer/Streetlayer', #paves roads or streets. 
        'Robber', 
        'Rogue',
        'Roofer/Thatcher', #builds and repairs roofs. 
        'Rope maker', #braids rope.
        'Ropewalker', #walks along a tightrope to entertain others. 
        'Rowdy',
        'Royal Guard', #responsible for the protection of a royal person.
        'Rugmaker', #makes and repairs rugs by braiding, hooking, weaving, etc.
        'Runecaster', #uses special alphabets to create runes (symbols possessing magical effects capable of being used multiple times). 
        'Runner', #carries information between lines in wartime.
        'Rutabaga Farmer', 
        'Rutterkin',
        'Saddler', #makes and repairs saddlery. 
        'Sage', #a wise and experienced magic-user.
        'Saint',
        'Sapper', #a soldier responsible for tasks such as building and repairing roads and bridges, laying and clearing mines, etc. 
        'Savant', 
        'Scallywag', 
        'Scammer', 
        'Scholar', 
        'Scientist', 
        'Scoundrel', 
        'Scout', #sent ahead of a main force so as to gather information about the enemy’s position, strength, or movements.
        'Scribe',
        'Sculptor', #crafts art by carving or casting blocks of marble, stones, or other hardened minerals.
        'Seamstress/Tailor', #makes, alters, repairs, as well as occasionally designing garments.
        'Seancer', 
        'Second story man', 
        'Seeker', 
        'Seer/Oracle', #able to see what the future holds through supernatural insight.
        'Senator', #partakes in governmental decision-making after being elected. 
        'Sensei', 
        'Sentinel', 
        'Sergeant', #an officer instructed with a protective duty, typically worth “half a knight” in regard.
        'Sergeant-at-Arms', #charged with keeping order during meetings and, if necessary, participates in battle. 
        'Sermonizer', 
        'Servant', #performs duties for others, especially a person employed in a house or as a personal attendant.
        'Sexton', #looks after a church and churchyard, sometimes acting as bell-ringer and formerly as a gravedigger.
        'Shabbat', 
        'Shadow walker', 
        'Shapeshifter', #a person with the ability to change their physical form.
        'Shark', 
        'Sharper', 
        'Sharpshooter', 
        'Shepherd', #herds, tends, and guards sheep.
        'Sheriff', #the chief executive officer in a county, having various administrative and judicial functions. 
        'Shield-bearer', 
        'Shiv', 
        'Shrinist',
        'Siege Artillerist', #works the artillery machines of an army.
        'Singer/Soprano', #sings with or without instrumental accompaniment.
        'Skald', #composes and recites poems honoring heroes and their deeds.
        'Skirmisher', 
        'Slave Driver', #oversees and urges on slaves at work.
        'Slave Trader', #A merchant who specializes in the buying/trading of enslaved people
        'Slave', 
        'Slaver', 
        'Smuggler', #manages the import or export of goods secretly, in violation of the law, especially without payment of legal duty.
        'Soaper', #makes soap from accumulated mutton fat, wood ash, and natural soda. 
        'Soldier/Man-at-Arms', #serves in an army. 
        'Sonneteer', 
        'Soothsayer', 
        'Sophist', 
        'Soul-saver', 
        'Speaker',
        'Special Force Soldier', #carries out special operations.
        'Speculator', #invests in stocks, property, or other ventures in the hope of making a profit. 
        'Spellbinder', 
        'Spellslinger', 
        'Spellweaver', 
        'Spice Merchant',
        'Spirit-raiser',
        'Spy', #secretly collects and reports information on the activities, movements, and plans of an enemy or competitor.
        'Spymaster', #directs a network of subordinate espionage agents for a state, kingdom, or empire. 
        'Squire', #acts as an attendant to a knight before attempting to become a knight themselves.
        'Standard-bearer',
        'Stablehand', #works in a stable.
        'Stage Magician', #deceives their audience with seemingly impossible feats while using only natural means.
        'Stagehand', #moves scenery or props before or during the performance of a theatrical production.
        'Steward', #supervises both the estate and household of his lord or lady while they are away.
        'Street Cleaner', #cleans streets and alleyways after dark. 
        'Stonemason', #cuts and prepares stone for use in construction.
        'Stuntman/Stuntwoman', #performs dangerous stunts for their audience.
        'Summoner', #a mage able to summon forth magical beasts, creatures, and monsters. 
        'Swindler', 
        'Swordsman', 
        'Tactician', #uses a carefully planned military strategy to achieve a specific end.
        'Talent Scout', #searches for talented individuals who can be employed or promoted.
        'Tanner', #treats the skins and hides of animals to produce leather.
        'Tattooist', #illustrates the skin with indelible patterns, pictures, legends, etc.
        'Tax Collector', #collects unpaid taxes from people, guilds, or businesses.
        'Taxidermist', #prepares, stuffs, and mounts the skins of animals. 
        'Tea House Owner', #Someone who owns a Tea House business
        'Templar', #fights in a religious military order. 
        'Telepath', 
        'Templar', 
        'Teratologist', 
        'Thaumaturgist',
        'Theater Director', #supervises and orchestrates the mounting of a theatre production by unifying various endeavors and aspects of production. 
        'Theist', 
        'Theurgist', 
        'Thief', #steals people’s property, especially by stealth and without using force or violence. 
        'Thought Master',
        'Thresher', #separates grain from the plants by beating. 
        'Thug',
        'Thriftdealer', #deals in secondhand items.
        'Tinker', #travels from place to place mending utensils. 
        'Titan',
        'Tollkeeper', #collects tolls at a bridge, road etc. where a charge is made. 
        'Tomb robber', 
        'Torturer', #inflicts severe pain on someone as a punishment or in order to force them to do or say something.
        'Town Crier', #makes public announcements in the streets or marketplace.
        'Toymaker', #makes and repairs toys.
        'Tradesman', #deals exclusively in bartering. 
        'Trainer', #trains someone in a particular skill, usually physical, for money.
        'Transformer', 
        'Translator', #translates between languages.
        'Transmogrifier', 
        'Transmuter', #alters matter in form, appearance, or nature.
        'Trapper', #traps wild animals, especially for their fur.
        'Trapsmith', 
        'Treasure hunter', 
        'Trickster', 
        'Trooper', 
        'Troubadour', 
        'Truth-teller',
        'Tunner', #fills casks in a brewery or winery. 
        'Turnip Farmer', #A farmer who specializes in Turnip production 
        'Tyro', 
        'Urchin', 
        'Vagrant', 
        'Vampire-Binder', 
        'Vampire-Keeper', 
        'Vanquisher',
        'Vendor', #deals items in the street. 
        'Vicar', 
        'Victor', 
        'Vigilant', 
        'Viking', 
        'Villain', 
        'Vindicator',
        'Vintner', #engages in winemaking, especially with monitoring and harvesting the grapes. 
        'Viscount/Viscountess', #a nobleperson ranking above a baron and below a count.
        'Visionist', 
        'Vowmaker', 
        'Waghalter', 
        'Wainwright', 
        'Wanderer', 
        'Ward', #a member of a noble house who has been taken in by another noble family to be raised for a time.
        'Warden' #responsible for the supervision of a particular place or thing or for ensuring that regulations associated with it are obeyed.
        'Warlord', 
        'Warmage', #a soldier skilled in destructive battle magic.
        'Warmonger',
        'Watch leader', 
        'Watchmaker', #makes and repairs watches and clocks.
        'Water Bearer', #brings water from rivers, wells, and lakes back to their settlement.
        'Weaponsmith', #specializes in making and repairing weapons.   
        'Weaver', #makes fabric by weaving fiber together.
        'Wet Nurse', #a woman employed to suckle another woman’s child.
        'Wheat Farmer', #A farmer specialized in growing wheat
        'Wheelwright', #makes and repairs wooden wheels.
        'Whittler/Woodcarver', #fashions wood into various shapes.
        'Whore',
        'Wildling', 
        'Witness', 
        'Wizard\'s apprentice', 
        'Wonder worker', 
        'Woodcutter'
        'Wordsmith' #draws their power from language and casts by dictation.
        'Wrestler', #performs in matches involving grappling and grappling-type techniques.
        'Writer', #commits his or her thoughts, ideas, etc., into written language. 
        'Zealot',
        'Zookeeper') #maintains and cares for animals or monsters in a zoo.
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
        App.get_running_app().root.ids.Dragons.text = ''
        App.get_running_app().root.ids.DragonImage.source = ''


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
        HumanoidButton.bind(on_press=popup.dismiss)
        HumanoidButton.bind(on_press = self.Humanoid_gen)
        
#Dragon-kind Monster Generation
    def Dragon_kind_gen(self, *args): 
        Dragons = ('Adult White Dragon', 'Adult White Dragon')        
        App.get_running_app().root.ids.Dragons.text = " ".join(['Monster:',(str(random.choice(Dragons)))])
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult White Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Adult White Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 520)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Black Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Ancient Black Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (770, 450)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Blue Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Ancient Blue Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (500, 250)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Brass Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Ancient Brass Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (760, 450)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Bronze Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Ancient Bronze Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (720, 350)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Copper Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Ancient Copper Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (850, 525)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Gold Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Ancient Gold Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (670, 325)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Green Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Ancient Green Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (740, 330)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Red Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Ancient Red Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (650, 500)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Silver Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Ancient Silver Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (750, 350)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient White Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Ancient White Dragon.png'
            App.get_running_app().root.ids.DragonImage.pos = (500, 250)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Black Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Black Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (630, 250)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Blue Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Blue Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 350)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Brass Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Brass Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 400)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Bronze Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Bronze Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (850, 600)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
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