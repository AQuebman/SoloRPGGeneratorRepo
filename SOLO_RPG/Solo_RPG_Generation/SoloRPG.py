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

from kivy.uix.spinner import Spinner

        
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
        with open(r'Names_List.csv') as f:
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
        with open(r'Names_List.csv') as f:
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
        'Admiral', #commands a fleet or naval squadron. 
        'Adventurer', #wanders the world in search of knowledge, treasure, fame, glory or a multitude of additional wants and desires
        'Advocate', #Advises on all matters of law
        'Aerialist/Trapezist', #performs acrobatics high above the ground on a tightrope or trapeze. 
        'Affeeror', #determines the values of fines and amercements.
        'Agister', #affords pasture to the livestock of others for a price.
        'Alchemist', #transforms or creates something within nature through (usually) ritualist magic.
        'Alderman', #a civic dignitary in the local council ranked below the mayor.
        'Alienist', #assesses the competence of a defendant in a court of law.
        'Almoner', #distributes money and food to poor people.
        'Animal Collector', #collects and deals in rare and exotic animals and monsters.
        'Animal Handler', #care for, train, and study animals in such places as zoos, parks, research laboratories, animal breeding facilities, rodeos, and museums
        'Animal Trainer', #knows how to teach dogs, horses, or even marine animals to display certain behaviors or keep them from exhibiting others
        'Anthropologist', #studies the customs, beliefs, and relationships of humanoids and intellectually and culturally advanced creatures. 
        'Apostle', #A religious teacher
        'Apothecarist', #prepares and sells medicines, drugs, and potions. 
        'Apparitionist', #A believer in apparitions
        'Appraiser', #assesses the monetary value of something. 
        'Apprentice', #studies a trade under a skilled employer.
        'Arborist', #a tree surgeon
        'Archaeologist', #studies humanoid history and prehistory through the excavation of sites and the analysis of artifacts and other physical remains.
        'Arch-rogue', #An extremely powerful and skilled rogue
        'Archbishop', #responsible for an archdiocese, their surrounding district.
        'Archivist', #maintains and is in charge of archives.
        'Archmage', #an extremely powerful mage. 
        'Architect', #designs buildings or landscapes and in many cases supervises their construction. 
        'Armorer', #specializes in making and repairing armor.
        'Arranger', #adapts a musical composition for performance.
        'Artillerist', #A person who operates artillery 
        'Artisan', #a worker in a skilled trade, especially one that involves making things by hand
        'Artist', #a person who produces paintings or drawings as a profession or hobby
        'Ascetic', #a person who practices severe self-discipline and abstention
        'Aspirant', #a person who has ambitions to achieve something
        'Assay Master', #oversees the testing of currency. 
        'Assayer', #determiner of the proportions of metal in ore and the amount of copper, silver, gold, or platinum in coins.
        'Astrologer', #uses astrology to tell others about their character or to predict their future.
        'Astronomer', #makes observations of celestial and scientific phenomena within the material plane.
        'Athlete', #proficient in sports and other forms of physical exercise.
        'Auctioneer', #conducts auctions by accepting bids and declaring goods sold. 
        'Augurer', #a priest and official whose main role is the practice of augury: Interpreting the will of the gods by studying the flight of birds
        'Bagniokeeper', #owner of a bath house or brothel.
        'Bailiff', #looks after prisoners.
        'Baker', #bakes bread and cakes.
        'Balladeer', #a singer or composer of ballads
        'Bandit', #a robber or outlaw belonging to a gang and typically operating in an isolated or lawless area.
        'Banker', #an officer or owner of a bank or group of banks.
        'Barber', #cuts hair and shaves or trims beards.
        'Barkeep', #works and serves drinks in a bar.
        'Barmaid/Barboy', #serves drinks and food in a bar as well as engaging with customers.
        'Baron/Baroness', #a member of the lowest order of the British nobility.
        'Barrister', # lawyer entitled to practice as an advocate
        'Battler', #a person who battles or fights
        'Beadle', #ceremonial officer of a church, college, or similar institution  
        'Beekeeper', #a person who owns and breeds bees, especially for their honey
        'Beggar/Pauper', #lives by asking for money or food. 
        'Beguiler', #someone who leads you to believe something that is not true
        'Berserker', #A warrior who fights in a wild frenzy
        'Bilker', #A cheat, especially one who evades payment
        'Billboardposter', #a person who puts up notices, signs and advertisements. 
        'Bishop', #a senior member of the clergy, usually in charge of a diocese and empowered to confer holy orders.
        'Blackmailer', #a person who demands money or another benefit from someone in return for not revealing compromising or damaging information about them
        'Blacksmith', #forges and repairs things in metal, including weapons, armor, utensils, etc.
        'Bladesmith', #specializes in making and repairing bladed weapons, especially swords and daggers. 
        'Blood Hunter/Monster Hunter', #takes on jobs to hunt down and kill or capture dangerous creatures.
        'Bloodletter', #surgically removes some of a patient’s blood for therapeutic purposes.
        'Bludgeoner', #an assailant who uses a bludgeon. aggressor, assailant, assaulter, attacker 
        'Boatman', #mans a small seacraft
        'Body snatcher', #a person who steals corpses from a graveyard for dissection or other purposes
        'Bodyguard', #escorts and protects another person, especially a dignitary.
        'Bookbinder', #binds books and wraps scrolls.
        'Bookkeeper', #keeps records of financial affairs.
        'Bookseller', #responsible for selling books, magazines, and related items to customers
        'Bottler', #bottles drinks and other liquids.
        'Botanist', #an expert in or student of the scientific study of plants.
        'Bosun', #in charge of organizing the equipment and crew of a ship.
        'Bouncer', #prevents troublemakers from entering or to eject them from the premises of an establishment.
        'Bounty hunter', #pursues a criminal or fugitive for whom a reward is offered
        'Bowyer', #makes bows and crossbows.
        'Brawler', #a person who engages in rough or noisy fights or quarrels
        'Breeder', #a person who breeds livestock, racehorses, other animals, or plants
        'Brewer', #brews ale.
        'Brickmaker', #crafts bricks from clay, stone, or other materials.
        'Brickmason', #builds with mineral products such as stones, bricks, cinder blocks, or tiles, usually with the use of mortar as a bonding agent. 
        'Brigand', #a member of a gang that ambushes and robs people in forests and mountains
        'Broom Maker', #makes brooms and brushes. 
        'Bruiser', #a professional boxer or brawler
        'Bully', #a person who habitually seeks to harm or intimidate those whom they perceive as vulnerable
        'Burglar', #illegally enters buildings and steals things.
        'Bushwhacker', #a guerrilla fighter
        'Business Owner', #owns a business entity in an attempt to profit from its successful operations.
        'Busker/Street Musician', #performs in a public place, often for money. 
        'Butcher', #cuts up and sells meat.
        'Butler', #the chief servant of a household.
        'Cabbie/Wagoner', #drives a horse-drawn wagon.
        'Cabin Boy/Cabin Girl', #waits on the orders of a ship’s officers and passengers.
        'Cadet', #a young trainee in the armed services or police force
        'Campaigner', #a person who actively promotes the goals of a cause
        'Candlemaker', #makes candles and wax from honey and tallow. 
        'Cantor', #sings liturgical music and leads prayer in a synagogue.
        'Capo', #Captain or leadership in a criminal organization
        'Captain', #an army officer of high rank in charge of commanding squadrons of soldiers.
        'Caravan Guard', #A guard who protects a caravan
        'Caravaneer', #travels or lives in a caravan.
        'Card shark', #a person who cheats at cards in order to win money
        'Cardinal', #a leading dignitary of a church, nominated by the highest official.
        'Caregiver', #looks after a sick, elderly, or disabled person.
        'Carpenter', #makes and repairs wooden objects and structures.
        'Carter', #transports goods by cart.
        'Cartographer', #a scholar and illustrator of maps.
        'Cartwright', #makes and repairs carts and wagons. 
        'Castellan', #the governor of a castle.
        'Cavalryman/Cavalier', #a skilled horseback rider.
        'Celebrity', #a famous person.
        'Chamberlain', #n officer who manages the household of a monarch or noble
        'Champion', #a person who has defeated or surpassed all rivals in a competition
        'Chancellor', #a senior state or legal official.
        'Chandler', #deals in provisions and supplies.
        'Chaplain', #a member of the clergy attached to a private chapel, institution, ship, branch of the armed forces, etc.
        'Charcoal Maker', #manufactures charcoal by carbonizing wood in a kiln.
        'Charlatan', #a person falsely claiming to have a special knowledge or skill; a fraud
        'Charioteer', #drives a chariot.
        'Charity Worker', # Someone who works for charitable organizations, distributing aid, or evaluating the need for aid
        'Charlatan/Conman', #tricks people by gaining their trust and persuading them to believe something that is not true in order to benefit from the encounter.
        'Chatelaine/Majordomo', #a person in charge of a large household. 
        'Cheat', #a person who behaves dishonestly in order to gain an advantage
        'Cheesemaker', #a person who makes cheese
        'Chef', #a professional cook trained in the culinary arts.
        'Chemist', #engaged in chemical research or experiments. 
        'Chest-maker', #A person who makes chests
        'Chevalier', #A chivalrous Knight
        'Chieftain', #leads or rules a people or clan.
        'Chimney Sweeper', #a small person, typically a child, who ascends chimneys to clean them.
        'Choirmaster', #trains a choir and orchestrates their singing when they perform. 
        'Chronicler', #a person who writes accounts of important or historical events
        'City Watch', #an officer of law enforcement who resides in larger towns or cities.
        'Clairvoyant', #a person who claims to have a supernatural ability to perceive events in the future or beyond normal sensory contact
        'Clerk', #undertakes routine administrative duties in a business or bank. 
        'Clockworker', #A person who specializes in creation and repair of clocks and clock like devices
        'Clown', #comic entertainer who wears a traditional costume and exaggerated makeup. 
        'Cobbler', #makes and repairs footwear.
        'Cockfighter/Gamefighter', #engages in arena matches in which animals or monsters are pitted against one another, typically to the death.
        'Collector', #collects things of a specified type, professionally or as a hobby.
        'Comedian', #entertainer whose act is designed to make an audience laugh. 
        'Commissar', #teaches principles and policies to military units.
        'Con man', #a person who tricks other people in order to get their money
        'Conclavist', #Personal aide to the priesthood
        'Conductor', #directs the performance of an orchestra. 
        'Confessor', #hears confessions and gives absolution and spiritual counsel.
        'Confidence artist', #a person adept at swindling by means of confidence games
        'Constable', #an officer with limited policing authority, typically in a small town.
        'Cook', #prepares food for eating.
        'Cooper/Hooper', #makes and repairs casks and barrels. 
        'Conqueror', #a person who conquers a place or people
        'Conservationist', #advocates for the protection and preservation of the environment and wildlife.
        'Construction Worker', #a laborer in the physical construction of a built environment and its infrastructure. 
        'Contortionist', #twists and bends their body into strange and unnatural positions.
        'Cooper', #a maker or repairer of casks and barrels
        'Copyist', #makes copies of handwritten documents or music. 
        'Corn Farmer', #A farmer who specializes in the production of Corn
        'Costermonger', #a person who sells goods, especially fruit and vegetables, from a handcart in the street
        'Costumer', #makes theatrical costumes.
        'Count/Earl/Countess', #a nobleperson ranking above a viscount and below a marquess.
        'Courier', #transports packages and documents. 
        'Courtier', #attends court as a companion or adviser to the king or queen.
        'Cowherd', #a person who tends grazing cattle
        'Cozener', #An imposter, a swindler
        'Cracksman', #a thief who breaks open safes to steal valuable contents
        'Crime Boss', #controls and supervises a criminal organization. 
        'Crossing Sweeper', #sweeps a path ahead of people crossing dirty urban streets in exchange for a gratuity 
        'Croupier', #runs a gaming table by gathering in and paying out money or tokens.
        'Cryomancer', #A user of magic who focuses on cold related spells and spell like effects
        'Cult Leader', #the organizational leader of a cult who is occasionally also the founder.
        'Cultist', #a member of a cult who generally lives outside of conventional society and worships an unorthodox patron.
        'Curator', #keeper and custodian of a museum or other collections of precious items.
        'Curse-giver', #Either via natural or magical means someone who specializes in cursing others usually for a fee or a group for which they belong 
        'Cutler', #makes cutlery.
        'Cutpurse', #a pickpocket or thief.
        'Cutthroat', #a murderer or other violent criminal
        'Cyclops-Binder', #A spellcaster who specializes in binding Cyclops to it's will
        'Cyclops-Keeper', #A person who specializes in trapping Cyclops and keeping them for personal use
        'Dairyboy/Dairymaid', #A person employed at a dairy
        'Dancer', #moves their body rhythmically with or without musical accompaniment.
        'Day Laborer', #A person employed on day to day jobs normally working during daylight hours
        'Deacon', #an ordained minister of an order ranking below that of priest.
        'Dean', #the head of a college or university.
        'Debt Collector', #recovers money owed on delinquent accounts. 
        'Defender', #a person who defends someone or something
        'Defiler', #a person or organization that causes pollution of the environment
        'Demon-Binder', #A spellcaster who specializes in binding Demons to it's will
        'Demon-Keeper', #A person who specializes in trapping Demons and keeping them for personal use
        'Deserter', #a member of the armed forces who has deserted
        'Detective/Investigator', #investigates and solves crimes. 
        'Devil-Binder', #A spellcaster who specializes in binding Devils to it's will
        'Devil-Keeper', #A person who specializes in trapping Devils and keeping them for personal use
        'Diabolist', #someone who worships devils
        'Diplomat', #an official representing a country abroad.
        'Disgraced Noble', #a person of high birth who has since loss their respect, honor, or esteem in some or all noble circles
        'Disciple', #a follower or student of a teacher, leader, or philosopher
        'Ditch Digger', #A person who digs ditches
        'Diviner', #seeks ultimate divination in order to further understand or meet godly substance.
        'Dock worker', #A person who works on the docks usually on fishing boats and boats incoming/outgoing from port
        'Doctor/Physician', #a qualified practitioner of medicine.
        'Dragon-Binder', #A spellcaster who specializes in binding Dragons to it's will
        'Dragon-Keeper', #A person who specializes in trapping Dragons and keeping them for personal use
        'Drakologist', #studies or is an expert in the branch of zoology concerned with dragons.
        'Draper', #an alcohol merchant. 
        'Drug Dealer', #dealer of illegal substances.
        'Drug Lord', #controls a network of persons involved in the illegal drugs trade and transactions.
        'Drummer/Fifer', #a non-combatant foot soldier who sounds signals for changes in formation in combat.
        'Drunkard', #a person who is habitually drunk and considers themselves a professional in the task
        'Duelist', #skilled in one-on-one combat.
        'Duke/Duchess', #rules over a duchy and is of the highest rank below the monarch.
        'Dungeon Delver', #navigates underground labyrinths in search of any treasure they may find.
        'Dyer', #dyes cloth and other materials. 
        'Ecclesiast', #Someone who adminsters a church or other religious gathering/group
        'Elder', #a person of a greater age, especially one with a respected position in society.
        'Elementalist', #manipulates nature’s elements to their will.
        'Embezzler', #someone who secretly takes money that is in their care or that belongs to an organization or business they work for
        'Embroiderer', #ornaments with needlework. 
        'Emperor/Empress', #the supreme sovereign ruler of an extensive group of states or countries under a single authority.
        'Enchanter', #uses sorcery to put someone or something under a spell.
        'Encylopaedist', #a person who writes, edits, or contributes to an encyclopedia
        'Engraver', #incises a design onto a hard surface by cutting grooves into it. 
        'Engineer', #designer of a machine or structure.
        'Entomologist', #studies or is an expert in the branch of zoology concerned with insects.
        'Entrepreneur', #organizes and operates a business or businesses, taking on greater than normal financial risks in order to do so.
        'Epicure', #a person who takes particular pleasure in fine food and drink
        'Equilibrist', #performs balancing feats. 
        'Evangelist', #A person who seeks to convert others to their faith especially by public preaching
        'Evoker', #manipulates energy or taps into an unseen source of power in order to produce a desired kinetic end.
        'Ex-Adventurer', #Someone who has retired from traveling the world for adventure and treasure
        'Ex-Criminal', #a person who has been convicted of a crime and has since served their sentence, or who has preemptively given up their life of crime
        'Ex-Noble', #Someone who used to be part of the noble class either stepping down or stripped of their title
        'Executioner', #carries out a sentence of death on a legally condemned person.
        'Exemplar', #a person or thing serving as a typical example or excellent model
        'Exile', #lives away from their native country, either from choice or compulsion 
        'Exorcist', #expels or attempts to expel evil spirits from a person or place.
        'Explorer', #explores unfamiliar areas in search of geographical or scientific information
        'Exterminator', #exterminates unwanted rodents and insects.
        'Extortioner', #extorts money from someone by threatening to expose embarrassing information about them. 
        'Falconer', #someone who practises the sport of pursuing live prey with a raptor, such as a hawk, falcon or eagle
        'Farmer', #a person who owns or manages a farm
        'Farrier', #trims and shoes horses’ hooves. 
        'Fashion Designer', #applies design, aesthetics and natural beauty to garments and their accessories.
        'Fence', #deals in stolen goods.
        'Fencer', #a person who practices the art of fencing with a sword, foil, etc.
        'Ferryman', #operates a ferry. 
        'Filcher', #A thief
        'Firefighter', #extinguishes fires.
        'First Mate', #the deck officer second in command to the master of a ship.
        'Fisher', #Someone who hunts in rivers, seas, and oceans and sells their catch for a living
        'Fletcher', #makes and repairs arrows.
        'Florist', #someone who arranges flowers and other plant elements into a pleasing design
        'Food & Drink Taster', #ingests food that was prepared for someone else to confirm it is safe to eat.
        'Folk Hero', #a celebrity who is greatly admired by many people of a particular kind or in a particular place
        'Footman', #a liveried servant whose duties include admitting visitors and waiting at table
        'Footpad', #a highwayman operating on foot rather than riding a horse
        'Forager', #a person or animal that searches widely for food or provisions
        'Forester', #a person in charge of a forest or skilled in planting, managing, or caring for trees
        'Forger', #produces fraudulent copies or imitations.
        'Fortune Teller', #a person who is supposedly able to predict a person's future by palmistry, using a crystal ball, or similar methods
        'Fowler', #a person who hunts wildfowl
        'Freelancer', #a person who works freelance
        'Friar', #a member of any of certain religious orders of men
        'Fugitive', #a person who has escaped from a place or is in hiding, especially to avoid arrest or persecution.
        'Furniture Artisan', #makes and repairs furniture.
        'Furrier', #prepares furs for adornment. 
        'Gambler', #bets money on sports, card games, or games of chance in the hope of a profit.
        'Gamekeeper' #breeds and protects game, typically for a large estate
        'Gammoner', # A thief's accomplice who distracts the victim while the thief steals.
        'Gardener/Landscaper', #tends and cultivates a garden.
        'General', #the chief commander of an army.
        'General Contractor', #supervises a construction site, manages its vendors and trades, and communicates information to all involved parties. 
        'Giant-Binder', #A spellcaster who specializes in binding Giants to it's will
        'Giant-Keeper', #A person who specializes in trapping Giants and keeping them for personal use
        'Gladiator', # fights against other people, wild animals, or monsters in an arena.
        'Glassworker', # blows glass planes and items.
        'Glasspainter', #produces colorful designs on or in glass.
        'Glazier', #fits glass into windows and doors. 
        'Glovemaker', #makes and repairs gloves.
        'Godfather', #a man who is influential or pioneering in a movement or organization
        'Goldsmith/Silversmith', #a smith who specializes in precious metals.
        'Gong Farmer', #digs out and removes excrement from privies and cesspits.
        'Government Official',
        'Governor', #the head of a public institution
        'Gravedigger', #digs graves for the purposes of a funeral ceremony.    
        'Grave Tender', #Tends to the upkeep of graves and mausoleums in a cemetary
        'Grenadier', #A soldier specialized in working with explosive devices
        'Grocer', #a food merchant.
        'Groom', #cleans and brushes the coats horses, dogs, or other animals.
        'Groundskeeper', #maintains an athletic field, a park, or the grounds of a graveyard or other institution.\
        'Guard/Sentinel', #a person who keeps watch, especially a soldier or other person formally assigned to protect a person or to control access to a place. 
        'Guardian', #a defender, protector, or keeper
        'Guerilla', #a member of a small independent group taking part in irregular fighting, typically against larger regular forces
        'Guild Beggar', #Someone who hangs outside of guildhalls begging for money
        'Guildmaster', #leads an economically independent producer (a “guild,” an association of craftsmen or merchants that often holds considerable bureaucratic power).
        'Guildsman', #a member of a guild
        'Gypsy', #a nomadic or free-spirited person
        'Haberdasher', #a dealer in men's clothing
        'Haruspex', #a religious official who interpreted omens by inspecting the entrails of sacrificial animals.
        'Hatter/Milliner', #makes and repairs headwear. 
        'Headman', #the chief or leader of a community or tribe.
        'Healer', #able to cure a disease or injury using magic.
        'Hearth Witch/Hearth Wizard', #incorporates spells and enchantments in cooking.
        'Heathen-slayer', #Someone who belongs to a church and specializes in destroying those who stand for the opposite of what the religion stands for
        'Hedge creeper', #a common or cheap prostitute, one who would lay on her back in the open air 
        'Helmsman', #steers a ship or boat
        'Herald', #a messenger who carries important news.
        'Herbalist', #practices healing by the use of herbs.
        'Herder', #supervises a herd of livestock or makes a living from keeping livestock, especially in open country.
        'Heretic', #differs in opinion from established religious dogma
        'Hermit', #lives in solitude, typically as a religious or spiritual discipline
        'Hierophant', #A person who interprets sacred mysteries or esoteric principles
        'High Priest/Pope', #the chief priest of a religion.
        'Highwayman', #robs travelers on a road.
        'Historian', #an expert in or student of history, especially that of a particular period, geographical region, or social phenomenon.
        'Hit man', #a person who is paid to kill someone, especially for a criminal or political organization
        'Horologist', #a scholar of time and entropy. 
        'Horse Trainer', #tends to horses and teaches them different disciplines.
        'Housewife/Househusband', #cares for his or her family by managing household affairs and completing housework 
        'Hunter', #hunts game or other wild animals.
        'Hydra-Binder', #A spellcaster who specializes in binding Hydra to it's will
        'Hydra-Keeper', #A person who specializes in trapping Hydra and keeping them for personal use
        'Hypnotist', #a person who carries out hypnosis, either for medical reasons or for entertainment
        'Illuminator', #paints and calligraphs to adorn or enlighten scrolls and manuscripts. 
        'Illusionist', #performs tricks and spells that deceive the senses.
        'Imam', #the person who leads prayers in a mosque
        'Indentured servant', #Someone who took out a loan and works as a servant to whomever they owe until the debt has been paid 
        'Initiate', #A person who is instructed or adept in some special field
        'Innkeeper', #owns and runs an inn.
        'Inquisitor', #seeks to eliminate heresy and other things contrary to the doctrine or teachings of their faith.
        'Inspection Officer', #responsible for the inspection of military units to ensure they meet appropriate standards of training and efficiency.
        'Instrument Maker', #makes and repairs musical instruments.
        'Intelligence Officer', #collects, compiles and organizes information about the enemy.
        'Interpreter', #interprets language and its meaning, especially within ancient manuscripts.
        'Investigator', #a person who carries out a formal inquiry or investigation
        'Jailer', #supervises a jail and the prisoners in it.
        'Janissary', #a devoted follower or supporter
        'Jester', #professional joker or “fool” at court, typically wearing a cap with bells on it and carrying a mock scepter.
        'Jeweler', #designs, makes, and repairs necklaces, bracelets, watches, etc., often containing jewels.
        'Jongleur', #an itinerant minstrel
        'Journeyman', #a trained worker who is employed by someone else
        'Jouster', #A knight who specializes in lance and horse combat
        'Judge', #decides cases in a court of law.
        'Juggler', #keeps several objects in motion in the air at the same time by alternately tossing and catching them. 
        'Junkman', #a person who buys, trades, or collects disparate items (scrap and usable/repairable things) considered of little or no value to their owners
        'Justicar', #A representative and enforcer of the king or ruler's justice
        'Keeper', #An attendant, a guard, a warden,or gamekeeper
        'Khan', #A warrior politician
        'Kidnapper', #abducts people and holds them captive, typically to obtain a ransom. 
        'Killer', #Someone who murders either for money or fun
        'King/Queen', #the ruler of an independent state and its people.
        'Kitchen Drudge', #performs menial work in a kitchen.
        'Knacker', #disposes of dead or unwanted animals.
        'Knave', #a dishonest or unscrupulous man
        'Knight', #serves his or her sovereign after being bestowed a rank of royal honor.
        'Lady-in-Waiting', #attends a queen, princess, or other high-ranking feminine nobleperson.
        'Lama', #A spiritual leader
        'Lamplighter', #lights street or road lights at dusk.
        'Lancer', #A cavalryman who fights with a lance
        'Land Surveyor', #establishes maps and boundaries for ownership or other purposes required by government or civil law.
        'Lapidary', #turns stone, minerals, or gemstones into decorative items such as cabochons, engraved gems, and faceted designs.
        'Laundry Worker', #a laborer who takes part in the washing, drying, and ironing of clothes and other fabric items. 
        'Lawyer/Advocate', #practices or studies law, typically an attorney or a counselor.
        'Leatherworker', #makes items from leather such as pouches, scabbards, straps, etc. 
        'Lector', #reads to others while they work for entertainment.
        'Legionnaire', #A member of a military legion
        'Librarian', #administers or assists in a library.
        'Lich', #A person usually a wizard who has reached immortality via a difficult ritual that turns them into an undead
        'Lieutenant', #an officer of middle rank in the armed forces.
        'Limner', #paints portraits or miniatures.
        'Linguist', #studies the essence of communication, including the units, nature, structure, and modification of language.
        'Loan Shark', #charges extremely high rates of interest for moneylending, typically under illegal conditions.
        'Locksmith', #makes and repairs locks.
        'Logician', #An expert in or student of logic
        'Longshoreman', #loads and unloads ships in a port.
        'Lorist', #A person who studies epic's, a long narrative poem usually related to heroic deeds of a person of an unusually courage and unparalleled bravery
        'Lumberjack', #fells trees, cuts them into logs, and transports them to a sawmill. 
        'Luthier', #makes and repairs stringed instruments.
        'Lyrist', #A person who plays the lyre
        'Made man', #A person who has been officially inducted into a criminal organization
        'Mage', #a magic-user.
        'Magician', #A person who performs magic tricks for entertainment
        'Magic-User', #One who has skill with magic
        'Magistrate', #A civil officer or lay judge who adminsters the law
        'Magnate', #A wealthy an influential person, especially in business
        'Magsman', #A con man who tries to deceive members of the public
        'Magus', #A sorcerer or a member of a priestly caste
        'Maid', #a domestic servant of a household. 
        'Makeup Artist', #applies cosmetics to models, actors, nobles, etc.
        'Man-at-arms', #Soldier well versed in the use of arms and served as a fully armoured heavy cavalryman
        'Manslayer', #A criminal who commits homicide
        'Marauder', #A person who marauds, a raider
        'Marine', #Veteran warriors
        'Mariner', #A Sailor
        'Marketeer', #A person who sells goods or services in a market
        'Marksman/Archer', #A person skilled in shooting, especially with a pistol, rifle, or bow
        'Marquess/Marchioness', #a nobleperson ranking above a count and below a duke.
        'Marshall', #has the charge of the cavalry in the household of a monarch.
        'Master-of-Coin', #supervises the royal treasury, advises the monarch on financial matters, and is responsible for raising money through taxation.
        'Master-of-Horses', #supervises and commands all horses under a jurisdiction.
        'Master-of-Hounds', #maintains a pack of hounds and their associated staff, equipment, and hunting arrangements. 
        'Master-of-the-Revels', #responsible for overseeing royal festivities.
        'Mathematician', #a scholar of the abstract science of number, quantity, and space.
        'Medic', #a medical practitioner equipped for the battlefield. 
        'Medium', #uses extrasensory perception, magic, or divine powers to identify information hidden from the normal senses. 
        'Medusa-Binder', #A spellcaster who specializes in binding a Medusa to it's will
        'Medusa-Keeper', #A person who specializes in trapping Giants and keeping them for personal use
        'Mendicant', #A beggar
        'Mentalist', # People who have the talent for mind reading, often used on stage to entertain
        'Mercenary', #a soldier without allegiance who works for money, typically a member of a company or guild.
        'Mercer', #weaves textile fabrics, especially silks, velvets, and other fine materials.
        'Merchant', #sells and trades goods.
        'Messenger', #carries messages between recipients.
        'Meteorologist', #forecasts and manipulates weather.
        'Miller/baker', #owns or works in a grain mill. 
        'Miner', #works underground in mines in order to obtain minerals such as coal, diamonds, or gold
        'Minister' #assists with the administration of business.
        'Minstrel', #recites lyric or heroic poetry for nobility.
        'Missionary', #goes on a religious mission to promote their faith in a foreign place.
        'Mnemonist', #Someone able to perform unusual feats of memory
        'Moneychanger', #exchanges one currency for another. 
        'Moneylender', #lends money to others who pay interest.
        'Model', #poses as a subject for an artist, fashion designer, or sculptor.
        'Mortician', #prepares dead bodies for burial or cremation and makes arrangements for funerals.
        'Monster Collector', #collects and deals in rare and exotic animals and monsters.
        'Monster Handler', #Handles and managers exotic animals and monsters
        'Mugger', #A person who attacks and robs another in a public place 
        'Mummer', #A masked mime
        'Mushroom farmer', #A farmer who specializes in the growth and harvesting of Mushrooms
        'Musician', #plays a musical instrument. 
        'Myrmidon', #A subordinate of a powerful person who carries out orders unquestioningly
        'Mysteriarch', #One that presides over mysteries
        'Mystic', #A person who claims to attain insight into mysteries transcending ordinary human knowledge via direct communication with the divine or in a state of spiritual ecstasy
        'Nanny/Nursemaid', #a servant employed to look after a young child or children. 
        'Navigator', #directs the route or course of a ship or other form of transportation, especially by using instruments and maps.
        'Necromancer', #communicates with and conjures the spirits of the dead.
        'Noble/Aristocrat', #a person belonging to a class with high social or political status.
        'Notary', #performs certain legal formalities, especially to draw up or certify contracts, deeds, and other documents for use in other jurisdictions.
        'Nun', #a member of a religious community of women, especially a cloistered one, living under vows of poverty, chastity, and obedience.
        'Nurse', #cares for the sick or infirm, especially in a hospital.
        'Occultist', #One who studies the action or influence of supernatural or supernormal powers
        'Omen-bringer', #One who studies and shares stories of great omens within the culture they reside
        'Operator', #a laborer who operates equipment, typically in construction.
        'Optician' #makes and repairs eyeglasses.
        'Optometrist', #examines the eyes for visual defects and prescribes eyeglasses.
        'Orator/Spokesman', #makes statements on behalf of a group or individual nobleperson. 
        'Ostler', #a groom or stableman, who is employed in a stable to take care of horses 
        'Outlaw', #a person who has broken the law, especially one who remains at large or is a fugitive
        'Padre', #A chaplain in the armed services
        'Page', #a young attendant to a person of noble rank. 
        'Painter', #paints pictures.
        'Palmist', #A palm raider 
        'Pardoner', #raises money for religious works by soliciting offerings and granting indulgences.
        'Parsnip Farmer', #A farmer who specializes in the growth and harvesting of Parsnips
        'Parson', #Priest of a church not affiliated with a monastic organization
        'Pastry Chef', #makes desserts, especially cakes and pastries.
        'Pathfinder', #scouts ahead and discovers a path or way for others. 
        'Pawnbroker', #a person who lends money at interest on the security of an article pawned. 
        'Peddler', #travels from place to place selling assorted items.
        'Philosopher', #a scholar of the fundamental nature of knowledge, reality, and existence.
        'Pick Pocket', # person who steals from people's pockets.
        'Pilgrim', #journeys to some sacred place as an act of religious devotion, occasionally to settle there
        'Pimp/Madame', #controls prostitutes and arranges clients for them, taking part of their earnings in return. 
        'Pirate', #attacks and robs ships at sea.
        'Plantation Owner', #an owner of an estate on which crops are cultivated by resident labor, typically slave labor.
        'Plasterer', #applies plaster to walls, ceilings, or other surfaces.
        'Playwright', #writes plays or musicals.
        'Plumber', #installs and repairs the fittings of water supply and sanitation.
        'Plumer', #hunts birds for their plumes.
        'Plutocrat', #a person whose power derives from their wealth
        'Poacher', #hunts illegal game.
        'Poet', #writes ballads, epics, sonnets, or other forms of poetry.
        'Poisoner', #makes poisons to harm or kill.
        'Pontiff', #The pope/head of a large monastic religion
        'Porter', #carries luggage and other loads. 
        'Potato Farmer', #A farmer who specializes in potatoes
        'Potter', #makes pots, bowls, plates, etc., out of clay.
        'Preceptor', #a teacher or instructor.
        'Prestidigitator', #a sleight-of-hand artist
        'Priest', #has the authority to perform certain rites and administer certain sacraments.
        'Prince/Princess', #the direct descendant of a monarch.
        'Printer', #a person who applies pressure to an inked surface resting upon a print medium (such as paper or cloth), thereby transferring the ink to manufacture a text. 
        'Prisoner', #held in confinement as a punishment for crimes they have been convicted of
        'Privateer', #engages in maritime warfare under a commission of war.
        'Professor', #a teacher of the highest rank in a college or university.
        'Prognosticator', #a person who foretells or prophesies a future event
        'Prophet', #regarded as an inspired teacher or proclaimer of the will of God.
        'Proprietor', #the owner of a business, or a holder of property
        'Prosecutor', #a lawyer who conducts the case against a defendant in a criminal court
        'Prospector', #searches for mineral deposits, especially by drilling and excavation. 
        'Prostitute', #engages in sexual activity for payment.
        'Psalmist', #the author or composer of a psalm
        'Psychic', #a person considered or claiming to have psychic powers
        'Pugilist', #a boxer 
        'Pupil', #a student in school.
        'Purser', #keeps the accounts of a ship, especially as the head steward on a passenger vessel.
        'Quarryman/Quarrywoman', #quarries stone.
        'Quartermaster', #responsible for providing quarters, rations, clothing, and other supplies.
        'Rabbi', #A religious scholar or teacher
        'Radish Farmer', #A farmer who specializes in the growth and harvesting of Radishes
        'Rag-and-Bone Man', #collects unwanted household items and sells them to merchants.
        'Raider/Marauder', #makes sudden, unprompted attacks against defenseless or near-defenseless settlements. 
        'Rat catcher', #a person who practices rat-catching as a professional form of pest control.
        'Rebel/Political Dissident', #rises in opposition or armed resistance against an established government or ruler 
        'Rector', #the head of certain universities, colleges, and schools
        'Refugee', #leaves their home in order to escape war, persecution, or natural disaster
        'Renderer', #converts waste animal tissue into usable materials.
        'Restorer', #repairs or renovates a work of art so as to return it to its original condition. 
        'Reverend', #a member of the clergy
        'Revivalist', #a person who holds, promotes, or presides over religious revivals
        'Rhymer', #One who makes, composes, or recites rhymes or simple poems
        'Rice Farmer', #A farmer who specializes in the growth and harvesting of Rice
        'Ringmaster/Ringmistress', #master of ceremony who introduces the circus acts to the audience.
        'Ritualist', #practices or advocates the observance of ritual (formula intended to trigger a magical effect on a person or objects).
        'Roadlayer/Streetlayer', #paves roads or streets. 
        'Robber', #a person who commits robbery.
        'Roofer/Thatcher', #builds and repairs roofs. 
        'Rope maker', #braids rope.
        'Ropewalker', #walks along a tightrope to entertain others. 
        'Royal Guard', #responsible for the protection of a royal person.
        'Rugmaker', #makes and repairs rugs by braiding, hooking, weaving, etc.
        'Runaway Slave', #a slave who has left their master and traveled without authorization
        'Runecaster', #uses special alphabets to create runes (symbols possessing magical effects capable of being used multiple times). 
        'Runner', #carries information between lines in wartime.
        'Rutabaga Farmer', #A farmer who specializes in the growth and harvesting of Rutabagas
        'Saddler', #makes and repairs saddlery. 
        'Sage', #a wise and experienced magic-user.
        'Saint', #a person who is recognized as having an exceptional degree of holiness or likeness or closeness to God
        'Sailor', #works as a member of the crew of a commercial or naval ship or boat.
        'Sapper', #a soldier responsible for tasks such as building and repairing roads and bridges, laying and clearing mines, etc. 
        'Savant', #a learned person, especially a distinguished scientist.
        'Scammer', #a person who commits fraud or participates in a dishonest scheme. 
        'Scavenger/Mudlark/Tosher', #searches for and collects discarded items
        'Scholar', #a specialist in a particular branch of study who pursues the acquisition of knowledge.
        'Scientist', #a person who is studying or has expert knowledge of one or more of the natural or physical sciences
        'Scout', #sent ahead of a main force so as to gather information about the enemy’s position, strength, or movements.
        'Scribe', #copies out manuscripts.
        'Sculptor', #crafts art by carving or casting blocks of marble, stones, or other hardened minerals.
        'Sea Captain', #commands a ship.
        'Seamstress/Tailor', #makes, alters, repairs, as well as occasionally designing garments.
        'Seer/Oracle', #able to see what the future holds through supernatural insight.
        'Senator', #partakes in governmental decision-making after being elected. 
        'Sensei', #A teacher of the martial arts
        'Sentinel', #a soldier or guard whose job is to stand and keep watch
        'Sergeant', #an officer instructed with a protective duty, typically worth “half a knight” in regard.
        'Sergeant-at-Arms', #charged with keeping order during meetings and, if necessary, participates in battle. 
        'Sermonizer', #someone whose occupation is preaching the gospel.
        'Servant', #performs duties for others, especially a person employed in a house or as a personal attendant.
        'Sexton', #looks after a church and churchyard, sometimes acting as bell-ringer and formerly as a gravedigger.
        'Shapeshifter', #a person with the ability to change their physical form.
        'Sharper', #A swindler, especially at cards 
        'Sharpshooter', #An expert shot with a ranged weapon
        'Shepherd', #herds, tends, and guards sheep.
        'Sheriff', #the chief executive officer in a county, having various administrative and judicial functions. 
        'Shield-bearer', #An attendant who carries a warriors shield
        'Shipwright', #a carpenter skilled in ship construction and repair.
        'Siege Artillerist', #works the artillery machines of an army.
        'Singer/Soprano', #sings with or without instrumental accompaniment.
        'Skald', #composes and recites poems honoring heroes and their deeds.
        'Skirmisher', #a soldier usually sent ahead of a main body of troops to harass the enemy
        'Slave Driver', #oversees and urges on slaves at work.
        'Slave Trader', #A merchant who specializes in the buying/trading of enslaved people
        'Slave', #a person who is the legal property of another and forced to obey them
        'Slaver', #a person dealing in or owning slaves
        'Smuggler', #manages the import or export of goods secretly, in violation of the law, especially without payment of legal duty.
        'Soaper', #makes soap from accumulated mutton fat, wood ash, and natural soda. 
        'Soldier/Man-at-Arms', #serves in an army. 
        'Sonneteer', #a writer of sonnets
        'Soothsayer', #a person supposed to be able to foresee the future.
        'Sophist', #a paid teacher of philosophy and rhetoric
        'Speaker', #A person paid to give speeches to large groups
        'Special Force Soldier', #carries out special operations.
        'Speculator', #invests in stocks, property, or other ventures in the hope of making a profit. 
        'Spice Merchant', #A merchant who specializes in the sale of various herbs and spices usually from far off locations
        'Spy', #secretly collects and reports information on the activities, movements, and plans of an enemy or competitor.
        'Spymaster', #directs a network of subordinate espionage agents for a state, kingdom, or empire.
        'Squatter', #unlawfully occupies an uninhabited building or unused land 
        'Squire', #acts as an attendant to a knight before attempting to become a knight themselves.
        'Standard-bearer', #a soldier who is responsible for carrying the distinctive flag of a unit, regiment, or army
        'Stablehand', #works in a stable.
        'Stage Magician', #deceives their audience with seemingly impossible feats while using only natural means.
        'Stagehand', #moves scenery or props before or during the performance of a theatrical production.
        'Steward', #supervises both the estate and household of his lord or lady while they are away.
        'Street Cleaner', #cleans streets and alleyways after dark. 
        'Stonemason', #cuts and prepares stone for use in construction.
        'Student', #attends school or learns under other to enter and pursue a particular subject.
        'Stuntman/Stuntwoman', #performs dangerous stunts for their audience.
        'Summoner', #a mage able to summon forth magical beasts, creatures, and monsters. 
        'Surgeon/Chirurgeon', #practices surgery.
        'Swindler', #a person who uses deception to deprive someone of money or possessions 
        'Swordsman', #A person skilled at using swords in sport or comba
        'Tactician', #uses a carefully planned military strategy to achieve a specific end.
        'Talent Scout', #searches for talented individuals who can be employed or promoted.
        'Tanner', #treats the skins and hides of animals to produce leather.
        'Tattooist', #illustrates the skin with indelible patterns, pictures, legends, etc.
        'Tax Collector', #collects unpaid taxes from people, guilds, or businesses.
        'Taxidermist', #prepares, stuffs, and mounts the skins of animals. 
        'Taxonomist', #groups organisms into categories.
        'Tea House Owner', #Someone who owns a Tea House business
        'Teacher', #instructs on a particular skill or subject.
        'Templar', #fights in a religious military order. 
        'Telepath', #one who is able to communicate by telepathy
        'Templar', #a knight of a religious military order
        'Teratologist', #One who studies abnormalities of physiological development
        'Thaumaturgist', #a performer of miracles
        'Theater Director', #supervises and orchestrates the mounting of a theatre production by unifying various endeavors and aspects of production. 
        'Theologian', #engages in the study of the nature of God and religious belief.
        'Thief', #steals people’s property, especially by stealth and without using force or violence. 
        'Thresher', #separates grain from the plants by beating. 
        'Thug', #a violent person, especially a criminal
        'Thriftdealer', #deals in secondhand items.
        'Tinker', #travels from place to place mending utensils. 
        'Tollkeeper', #collects tolls at a bridge, road etc. where a charge is made. 
        'Tomb robber/Grave Robber', #steals valuables from graves and tombs 
        'Torturer', #inflicts severe pain on someone as a punishment or in order to force them to do or say something.
        'Town Crier', #makes public announcements in the streets or marketplace.
        'Toymaker', #makes and repairs toys.
        'Tradesman', #deals exclusively in bartering. 
        'Trainer', #trains someone in a particular skill, usually physical, for money.
        'Translator', #translates between languages.
        'Transmuter', #alters matter in form, appearance, or nature.
        'Trapper', #traps wild animals, especially for their fur.
        'Trapsmith', #A person who specializes in the creation of traps
        'Traveler/Wanderer/Vagabond', #wanders from place to place without a permanent home or job
        'Treasure hunter', #A person who spends their time searching for sunken, buried, lost, or hidden treasure and artifacts
        'Trickster', #a person who cheats or deceives people
        'Trooper', #a private soldier in a cavalry, armored, or airborne unit.
        'Troubadour', #a poet who writes verse to music
        'Tunner', #fills casks in a brewery or winery. 
        'Turnip Farmer', #A farmer who specializes in Turnip production 
        'Tutor', #charged with the instruction and guidance of another.
        'Urchin', #a child who lives or spends most of their time in the streets, occasionally working as a thief or pickpocket
        'Vagrant', #A beggar
        'Vampire-Binder', #A person who binds vampires to their will
        'Vampire-Keeper', #A person who catches and keeps Vampires as pets or for show or some other purpose
        'Vendor', #deals items in the street. 
        'Veterinarian', #treats diseased or injured animals.
        'Vintner', #engages in winemaking, especially with monitoring and harvesting the grapes. 
        'Viscount/Viscountess', #a nobleperson ranking above a baron and below a count.
        'Visionist', #One who sees, or believes that he sees, visions
        'Wainwright', #A trades person skilled in the making and repairing of wagons and carts
        'Wanderer', #An aimless traveler
        'Ward', #a member of a noble house who has been taken in by another noble family to be raised for a time.
        'Warden' #responsible for the supervision of a particular place or thing or for ensuring that regulations associated with it are obeyed.
        'Warlord', #a military commander, especially an aggressive regional commander with individual autonomy
        'Warmage', #a soldier skilled in destructive battle magic.
        'Warmonger', #a person who encourages or advocates aggression towards other countries or groups
        'Watch leader', #Leader of the guard of a particular distract, area, or town
        'Watchmaker', #makes and repairs watches and clocks.
        'Water Bearer', #brings water from rivers, wells, and lakes back to their settlement.
        'Weaponsmith', #specializes in making and repairing weapons.   
        'Weaver', #makes fabric by weaving fiber together.
        'Wet Nurse', #a woman employed to suckle another woman’s child.
        'Wheat Farmer', #A farmer specialized in growing wheat
        'Wheelwright', #makes and repairs wooden wheels.
        'Whittler/Woodcarver', #fashions wood into various shapes.
        'Whore', #A prostitute
        'Wizard\'s apprentice', #The understudy or student to a wizard or other spellcaster
        'Woodcutter' #Someone who specializes in felling trees and processing of wood
        'Wordsmith' #draws their power from language and casts by dictation.
        'Wrestler', #performs in matches involving grappling and grappling-type techniques.
        'Writer', #commits his or her thoughts, ideas, etc., into written language. 
        'Zealot', #a person who is fanatical and uncompromising in pursuit of their religious, political, or other ideals
        'Zookeeper' #maintains and cares for animals or monsters in a zoo.
        'Zoologist') #an expert in or a student of the behavior, physiology, classification, and distribution of animals.
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
                              'Likes to eat like it\'s their last meal',
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
        App.get_running_app().root.ids.Aberrations.text = ''
        App.get_running_app().root.ids.AberrationImage.source = ''
        App.get_running_app().root.ids.Humanoids.text = ''
        App.get_running_app().root.ids.HumanoidImage.source = ''
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
        with open(r'Names_List.csv') as f:
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
        with open(r'Names_List.csv') as f:
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

        layout      = GridLayout(cols=5, padding=10)
        
        AberrationButton  = Button(text  = "Click for a random Aberration type monster")        

        BeastButton  = Button(text  = "Click for a random Beast type monster")

        CelestialButton  = Button(text  = "Click for a random Celestial type monster")
               
        ConstructButton  = Button(text  = "Click for a random Construct type monster")
        
        DemonButton  = Button(text  = "Click for a random Demon type monster")
        
        DevilButton  = Button(text  = "Click for a random Devil type monster")
                
        DragonButton  = Button(text  = "Click for a random Dragon type monster")
        
        ElementalButton  = Button(text  = "Click for a random Elemental type monster")

        FeyButton  = Button(text  = "Click for a random Fey type monster")
        
        FiendButton  = Button(text  = "Click for a random Fiend type monster")
        
        GiantButton  = Button(text  = "Click for a random Giant type monster")

        HumanoidButton = Button(text = "Click for a random Humanoid type monster")
        
        MonstrosityButton = Button(text = "Click for a random Monstrosity type monster")

        OozeButton = Button(text = "Click for a random Ooze type monster")

        PlantButton = Button(text = "Click for a random Plant type monster")
        
        SwarmButton = Button(text = "Click for a random Swarm monster")
        
        UndeadButton = Button(text = "Click for a random Undead type monster")

        layout.add_widget(AberrationButton)

        layout.add_widget(BeastButton)

        layout.add_widget(CelestialButton)
 
        layout.add_widget(ConstructButton)
        
        layout.add_widget(DemonButton)
        
        layout.add_widget(DevilButton)
        
        layout.add_widget(DragonButton)
        
        layout.add_widget(ElementalButton)
        
        layout.add_widget(FeyButton)
        
        layout.add_widget(FiendButton)
        
        layout.add_widget(GiantButton)

        layout.add_widget(HumanoidButton)   

        layout.add_widget(MonstrosityButton)
        
        layout.add_widget(OozeButton)
        
        layout.add_widget(PlantButton)
        
        layout.add_widget(SwarmButton)
        
        layout.add_widget(UndeadButton)    

   

        # Instantiate the modal popup and display

        popup = Popup(title='Monster Generator',

                      content=layout)  

        popup.open()   

       
        # Dismiss causes the popup to go away. Release generates the call to the monster generator specified
        AberrationButton.bind(on_press=popup.dismiss)
        AberrationButton.bind(on_release = self.Aberration_gen)
        
        BeastButton.bind(on_press=popup.dismiss)
        BeastButton.bind(on_release = self.Beast_gen)
        
        CelestialButton.bind(on_press=popup.dismiss)
        CelestialButton.bind(on_release = self.Celestial_gen)
        
        ConstructButton.bind(on_press=popup.dismiss)
        ConstructButton.bind(on_release = self.Construct_gen)
        
        DemonButton.bind(on_press=popup.dismiss)
        DemonButton.bind(on_release = self.Demon_gen)
        
        DevilButton.bind(on_press=popup.dismiss)
        DevilButton.bind(on_release = self.Devil_gen)
        
        DragonButton.bind(on_press=popup.dismiss)
        DragonButton.bind(on_release = self.Dragon_kind_gen)
        
        ElementalButton.bind(on_press=popup.dismiss)
        ElementalButton.bind(on_release = self.Elemental_gen)
        
        FeyButton.bind(on_press=popup.dismiss)
        FeyButton.bind(on_release = self.Fey_gen)
        
        FiendButton.bind(on_press=popup.dismiss)
        FiendButton.bind(on_release = self.Fiend_gen)
        
        GiantButton.bind(on_press=popup.dismiss)
        GiantButton.bind(on_release = self.Giant_gen)
        
        HumanoidButton.bind(on_press=popup.dismiss)
        HumanoidButton.bind(on_press = self.Humanoid_gen)
        
        MonstrosityButton.bind(on_press=popup.dismiss)
        MonstrosityButton.bind(on_press = self.Monstrosity_gen)
        
        OozeButton.bind(on_press=popup.dismiss)
        OozeButton.bind(on_press = self.Ooze_gen)
        
        PlantButton.bind(on_press=popup.dismiss)
        PlantButton.bind(on_press = self.Plant_gen)
        
        SwarmButton.bind(on_press=popup.dismiss)
        SwarmButton.bind(on_press = self.Swarm_gen)
        
        UndeadButton.bind(on_press=popup.dismiss)
        UndeadButton.bind(on_press = self.Undead_gen)

#Aberration Monster Generation
    def Aberration_gen(self, *args):
        Aberrations = ('Aboleth', 'Aboleth')        
        App.get_running_app().root.ids.Aberrations.text = " ".join(['Monster:',(str(random.choice(Aberrations)))])
        if App.get_running_app().root.ids.Aberrations.text == 'Monster: Aboleth':
            App.get_running_app().root.ids.AberrationImage.opacity = 1
            App.get_running_app().root.ids.AberrationImage.source = 'Aberrations\Aboleth.jpg'
            App.get_running_app().root.ids.AberrationImage.pos = (800, 50)
            App.get_running_app().root.ids.Aberrations.halign = 'center'
            App.get_running_app().root.ids.Aberrations.text_size = (500, 700)
        if App.get_running_app().root.ids.Aberrations.text == 'Monster: Chuul':
            App.get_running_app().root.ids.AberrationImage.opacity = 1
            App.get_running_app().root.ids.AberrationImage.source = 'Aberrations\Chuul.jpg'
            App.get_running_app().root.ids.AberrationImage.pos = (800, 50)
            App.get_running_app().root.ids.Aberrations.halign = 'center'
            App.get_running_app().root.ids.Aberrations.text_size = (500, 1785)
        if App.get_running_app().root.ids.Aberrations.text == 'Monster: Cloaker':
            App.get_running_app().root.ids.AberrationImage.opacity = 1
            App.get_running_app().root.ids.AberrationImage.source = 'Aberrations\Cloaker.jpg'
            App.get_running_app().root.ids.AberrationImage.pos = (800, 50)
            App.get_running_app().root.ids.Aberrations.halign = 'center'
            App.get_running_app().root.ids.Aberrations.text_size = (500, 1785)
        if App.get_running_app().root.ids.Aberrations.text == 'Monster: Gibbering Mouther':
            App.get_running_app().root.ids.AberrationImage.opacity = 1
            App.get_running_app().root.ids.AberrationImage.source = 'Aberrations\Gibbering Mouther.jpg'
            App.get_running_app().root.ids.AberrationImage.pos = (800, 50)
            App.get_running_app().root.ids.Aberrations.halign = 'center'
            App.get_running_app().root.ids.Aberrations.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Aberrations.text == 'Monster: Otyugh':
            App.get_running_app().root.ids.AberrationImage.opacity = 1
            App.get_running_app().root.ids.AberrationImage.source = 'Aberrations\Otyugh.jpg'
            App.get_running_app().root.ids.AberrationImage.pos = (800, 50)
            App.get_running_app().root.ids.Aberrations.halign = 'center'
            App.get_running_app().root.ids.Aberrations.text_size = (500, 1785)                      

#Beast Monster Generation
    def Beast_gen(self, *args):
        Beasts = ('Ape', 'Ape')        
        App.get_running_app().root.ids.Beasts.text = " ".join(['Monster:',(str(random.choice(Beasts)))])
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Ape':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Ape.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Axe Beak':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Axe Beak.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Baboon':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Baboon.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Badger':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Badger.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)         
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Bat':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Bat.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)      
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Black Bear':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Black Bear.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)             
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Blood Hawk':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Blood Hawk.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)             
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Boar':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Boar.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)       
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Brown Bear':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Brown Bear.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)             
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Camel':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Camel.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)        
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Cat':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Cat.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)   
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Beasts Snake':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Constrictor Snake.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)                    
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Crab':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Crab.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Crocodile':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Crocodile.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)       
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Deer':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Deer.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Dire Wolf':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Dire Wolf.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)       
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Draft Horse':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Draft Horse.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)         
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Eagle':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Eagle.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)   
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Elephant':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Elephant.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)      
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Elk':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Elk.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Flying Snake':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Flying Snake.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)          
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Frog':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Frog.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Ape':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Ape.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)       
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Crab':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Badger.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Bat':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Crab.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)   
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Boar':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Boar.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)        
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Centipede':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Centipede.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)             
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Crab':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Constrictor Snake.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)                     
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Crab':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Crab.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)        
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Crocodile':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Crocodile.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)             
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Eagle':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Eagle.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)         
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Elk':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Elk.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)       
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Fire Beetle':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Fire Beetle.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)               
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Frog':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Frog.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)        
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Goat':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Goat.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)        
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Hyena':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Hyena.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)         
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Lizard':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Lizard.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)          
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Octopus':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Octopus.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)           
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Owl':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Owl.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)       
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Poisonous Snake':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Poisonous Snake.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)                   
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Rat':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Rat.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)       
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Scorpion':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Scorpion.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)            
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Sea Horse':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Sea Horse.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)             
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Shark':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Shark.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)         
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Spider':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Spider.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)          
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Toad':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Toad.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)        
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Vulture':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Vulture.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)           
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Wasp':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Wasp.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)        
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Weasel':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Weasel.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)          
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Giant Wolf Spider':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Giant Wolf Spider.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)               
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Goat':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Goat.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Hawk':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Hawk.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Hunter Shark':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Hunter Shark.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)          
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Hyena':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Hyena.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)   
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Jackal':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Jackal.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)    
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Killer Whale':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Killer Whale.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)          
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Lion':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\lion.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Lizard':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Lizard.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)    
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Mammoth':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Mammoth.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)     
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Mastiff':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Mastiff.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)     
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Mule':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Mule.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Octopus':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Octopus.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)     
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Owl':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Owl.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Panther':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Panther.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)     
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Plesiosaurus':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Plesiosaurus.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)          
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Poisonous Snake':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Poisonous Snake.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)             
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Polar Bear':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Polar Bear.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)        
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Pony':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Pony.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Quipper':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Quipper.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)     
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Rat':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Rat.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Raven':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Raven.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)   
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Reef Shark':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Reef Shark.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)        
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Rhinoceros':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Rhinoceros.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)        
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Riding Horse':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Riding Horse.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)          
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Saber-Toothed Tiger':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Saber-Toothed Tiger.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)                 
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Scorpion':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Scorpion.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)      
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Sea Horse':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Sea Horse.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)       
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Spider':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Spider.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)    
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Stirge':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Stirge.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)    
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Tiger':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Tiger.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)   
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Triceratops':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Triceratops.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)         
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Tyrannosaurus Rex':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Tyrannosaurus Rex.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)               
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Vulture':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Vulture.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)     
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Warhorse':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Warhorse.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)      
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Weasel':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Weasel.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)    
        if App.get_running_app().root.ids.Beasts.text == 'Monster: Wolf':
            App.get_running_app().root.ids.BeastImage.opacity = 1
            App.get_running_app().root.ids.BeastImage.source = 'Beasts\Wolf.jpg'
            App.get_running_app().root.ids.BeastImage.pos = (800, 50)
            App.get_running_app().root.ids.Beasts.halign = 'center'
            App.get_running_app().root.ids.Beasts.text_size = (500, 1785)                                                                          
                                                                                                                                                                                                  
                                                                                                                                        
#Celestial Monster Generation
    def Celestial_gen(self, *args): 
        Celestials = ('Couatl', 'Couatl')        
        App.get_running_app().root.ids.Celestials.text = " ".join(['Monster:',(str(random.choice(Celestials)))])
        if App.get_running_app().root.ids.Celestials.text == 'Monster: Couatl':
            App.get_running_app().root.ids.CelestialImage.opacity = 1
            App.get_running_app().root.ids.CelestialImage.source = 'Celestials\Couatl.jpg'
            App.get_running_app().root.ids.CelestialImage.pos = (800, 50)
            App.get_running_app().root.ids.Celestials.halign = 'center'
            App.get_running_app().root.ids.Celestials.text_size = (500, 1785)
        if App.get_running_app().root.ids.Celestials.text == 'Monster: Deva':
            App.get_running_app().root.ids.CelestialImage.opacity = 1
            App.get_running_app().root.ids.CelestialImage.source = 'Celestials\Deva.jpg'
            App.get_running_app().root.ids.CelestialImage.pos = (800, 50)
            App.get_running_app().root.ids.Celestials.halign = 'center'
            App.get_running_app().root.ids.Celestials.text_size = (500, 1785)    
        if App.get_running_app().root.ids.Celestials.text == 'Monster: Pegasus':
            App.get_running_app().root.ids.CelestialImage.opacity = 1
            App.get_running_app().root.ids.CelestialImage.source = 'Celestials\Pegasus.jpg'
            App.get_running_app().root.ids.CelestialImage.pos = (800, 50)
            App.get_running_app().root.ids.Celestials.halign = 'center'
            App.get_running_app().root.ids.Celestials.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Celestials.text == 'Monster: Planetar':
            App.get_running_app().root.ids.CelestialImage.opacity = 1
            App.get_running_app().root.ids.CelestialImage.source = 'Celestials\Planetar.jpg'
            App.get_running_app().root.ids.CelestialImage.pos = (800, 50)
            App.get_running_app().root.ids.Celestials.halign = 'center'
            App.get_running_app().root.ids.Celestials.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Celestials.text == 'Monster: Solar':
            App.get_running_app().root.ids.CelestialImage.opacity = 1
            App.get_running_app().root.ids.CelestialImage.source = 'Celestials\Solar.jpg'
            App.get_running_app().root.ids.CelestialImage.pos = (800, 50)
            App.get_running_app().root.ids.Celestials.halign = 'center'
            App.get_running_app().root.ids.Celestials.text_size = (500, 1785)    
        if App.get_running_app().root.ids.Celestials.text == 'Monster: Unicorn':
            App.get_running_app().root.ids.CelestialImage.opacity = 1
            App.get_running_app().root.ids.CelestialImage.source = r'Celestials\Unicorn.jpg'
            App.get_running_app().root.ids.CelestialImage.pos = (800, 50)
            App.get_running_app().root.ids.Celestials.halign = 'center'
            App.get_running_app().root.ids.Celestials.text_size = (500, 1785)                                                                   

#Construct Monster Generation
    def Construct_gen(self, *args): 
        Constructs = ('Animated Armor', 'Animated Armor')        
        App.get_running_app().root.ids.Constructs.text = " ".join(['Monster:',(str(random.choice(Constructs)))])
        if App.get_running_app().root.ids.Constructs.text == 'Monster: Animated Armor':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\Animated Armor.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785)
        if App.get_running_app().root.ids.Constructs.text == 'Monster: Clay Golem':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\Clay Golem.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Constructs.text == 'Monster: Flesh Golem':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\Flesh Golem.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Constructs.text == 'Monster: Flying Sword':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\Flying Sword.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Constructs.text == 'Monster: Homunculus':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\Homunculus.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Constructs.text == 'Monster: Iron Golem':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\Iron Golem.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Constructs.text == 'Monster: Rug of Smothering':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\Rug of Smothering.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Constructs.text == 'Monster: Servitor Construct':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\Servitor Construct.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Constructs.text == 'Monster: Shield Guardian':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\Shield Guardian.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785)   
        if App.get_running_app().root.ids.Constructs.text == 'Monster: Stone Golem':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\Stone Golem.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Constructs.text == 'Monster: War Construct':
            App.get_running_app().root.ids.ConstructImage.opacity = 1
            App.get_running_app().root.ids.ConstructImage.source = 'Constructs\War Construct.jpg'
            App.get_running_app().root.ids.ConstructImage.pos = (800, 50)
            App.get_running_app().root.ids.Constructs.halign = 'center'
            App.get_running_app().root.ids.Constructs.text_size = (500, 1785)                                                                                                             
#Demon Monster Generation
    def Demon_gen(self, *args):
        Demons = ('Balor', 'Balor')        
        App.get_running_app().root.ids.Demons.text = " ".join(['Monster:',(str(random.choice(Demons)))])
        if App.get_running_app().root.ids.Demons.text == 'Monster: Balor':
            App.get_running_app().root.ids.DemonImage.opacity = 1
            App.get_running_app().root.ids.DemonImage.source = 'Demons\Balor.jpg'
            App.get_running_app().root.ids.DemonImage.pos = (800, 50)
            App.get_running_app().root.ids.Demons.halign = 'center'
            App.get_running_app().root.ids.Demons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Demons.text == 'Monster: Dretch':
            App.get_running_app().root.ids.DemonImage.opacity = 1
            App.get_running_app().root.ids.DemonImage.source = 'Demons\Dretch.jpg'
            App.get_running_app().root.ids.DemonImage.pos = (800, 50)
            App.get_running_app().root.ids.Demons.halign = 'center'
            App.get_running_app().root.ids.Demons.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Demons.text == 'Monster: Glabrezu':
            App.get_running_app().root.ids.DemonImage.opacity = 1
            App.get_running_app().root.ids.DemonImage.source = 'Demons\Glabrezu.jpg'
            App.get_running_app().root.ids.DemonImage.pos = (800, 50)
            App.get_running_app().root.ids.Demons.halign = 'center'
            App.get_running_app().root.ids.Demons.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Demons.text == 'Monster: Hezrou':
            App.get_running_app().root.ids.DemonImage.opacity = 1
            App.get_running_app().root.ids.DemonImage.source = 'Demons\Hezrou.jpg'
            App.get_running_app().root.ids.DemonImage.pos = (800, 50)
            App.get_running_app().root.ids.Demons.halign = 'center'
            App.get_running_app().root.ids.Demons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Demons.text == 'Monster: Marilith':
            App.get_running_app().root.ids.DemonImage.opacity = 1
            App.get_running_app().root.ids.DemonImage.source = 'Demons\Marilith.jpg'
            App.get_running_app().root.ids.DemonImage.pos = (800, 50)
            App.get_running_app().root.ids.Demons.halign = 'center'
            App.get_running_app().root.ids.Demons.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Demons.text == 'Monster: Nalfeshnee':
            App.get_running_app().root.ids.DemonImage.opacity = 1
            App.get_running_app().root.ids.DemonImage.source = r'Demons\Nalfeshnee.jpg'
            App.get_running_app().root.ids.DemonImage.pos = (800, 50)
            App.get_running_app().root.ids.Demons.halign = 'center'
            App.get_running_app().root.ids.Demons.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Demons.text == 'Monster: Quasit':
            App.get_running_app().root.ids.DemonImage.opacity = 1
            App.get_running_app().root.ids.DemonImage.source = 'Demons\Quasit.jpg'
            App.get_running_app().root.ids.DemonImage.pos = (800, 50)
            App.get_running_app().root.ids.Demons.halign = 'center'
            App.get_running_app().root.ids.Demons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Demons.text == 'Monster: Succubus/Incubus':
            App.get_running_app().root.ids.DemonImage.opacity = 1
            App.get_running_app().root.ids.DemonImage.source = 'Demons\Succubus-Incubus.jpg'
            App.get_running_app().root.ids.DemonImage.pos = (800, 50)
            App.get_running_app().root.ids.Demons.halign = 'center'
            App.get_running_app().root.ids.Demons.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Demons.text == 'Monster: Tengu Demon':
            App.get_running_app().root.ids.DemonImage.opacity = 1
            App.get_running_app().root.ids.DemonImage.source = 'Demons\Tengu Demon.jpg'
            App.get_running_app().root.ids.DemonImage.pos = (800, 50)
            App.get_running_app().root.ids.Demons.halign = 'center'
            App.get_running_app().root.ids.Demons.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Demons.text == 'Monster: Vrock':
            App.get_running_app().root.ids.DemonImage.opacity = 1
            App.get_running_app().root.ids.DemonImage.source = 'Demons\Vrock.jpg'
            App.get_running_app().root.ids.DemonImage.pos = (800, 50)
            App.get_running_app().root.ids.Demons.halign = 'center'
            App.get_running_app().root.ids.Demons.text_size = (500, 1785)                                                                                         

#Devil Monster Generation
    def Devil_gen(self, *args):
        Devils = ('Barbed Devil', 'Barbed Devil')        
        App.get_running_app().root.ids.Devils.text = " ".join(['Monster:',(str(random.choice(Devils)))])
        if App.get_running_app().root.ids.Devils.text == 'Monster: Barbed Devil':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Barbed Devil.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Devils.text == 'Monster: Bearded Devil':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Bearded Devil.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785)    
        if App.get_running_app().root.ids.Devils.text == 'Monster: Bone Devil':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Bone Devil.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785)
        if App.get_running_app().root.ids.Devils.text == 'Monster: Chain Devil':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Chain Devil.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Devils.text == 'Monster: Erinyes':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Erinyes.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Devils.text == 'Monster: Horned Devil':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Horned Devil.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785)   
        if App.get_running_app().root.ids.Devils.text == 'Monster: Ice Devil':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Ice Devil.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Devils.text == 'Monster: Imp':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Imp.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785)
        if App.get_running_app().root.ids.Devils.text == 'Monster: Lemure':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Lemure.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785)   
        if App.get_running_app().root.ids.Devils.text == 'Monster: Pig Devil':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Pig Devil.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Devils.text == 'Monster: Pit Fiend':
            App.get_running_app().root.ids.DevilImage.opacity = 1
            App.get_running_app().root.ids.DevilImage.source = 'Devils\Pit Fiend.jpg'
            App.get_running_app().root.ids.DevilImage.pos = (800, 50)
            App.get_running_app().root.ids.Devils.halign = 'center'
            App.get_running_app().root.ids.Devils.text_size = (500, 1785)                                                                                                                
#Dragon-kind Monster Generation
    def Dragon_kind_gen(self, *args): 
        Dragons = ('Adult Black Dragon', 'Adult Blue Dragon', 'Adult Brass Dragon', 'Adult Bronze Dragon', 'Adult Copper Dragon', 'Adult Gold Dragon', 'Adult Green Dragon', 'Adult Red Dragon', 'Adult Silver Dragon', 'Adult White Dragon', 'Ancient Black Dragon', 'Ancient Blue Dragon', 'Ancient Brass Dragon', 'Ancient Bronze Dragon', 'Ancient Copper Dragon', 'Ancient Gold Dragon', 'Ancient Green Dragon', 'Ancient Red Dragon', 'Ancient Silver Dragon', 'Ancient White Dragon', 'Black Dragon Wyrmling', 'Blue Dragon Wyrmling', 'Brass Dragon Wyrmling', 'Bronze Dragon Wyrmling', 'Copper Dragon Wyrmling', 'Dragon Turtle', 'Gold Dragon Wyrmling', 'Green Dragon Wyrmling', 'Pseudodragon', 'Red Dragon Wyrmling', 'Silver Dragon Wyrmling', 'White Dragon Wyrmling', 'Wyvern', 'Young Black Dragon', 'Young Blue Dragon', 'Young Brass Dragon', 'Young Bronze Dragon', 'Young Copper Dragon', 'Young Gold Dragon', 'Young Green Dragon', 'Young Red Dragon', 'Young Silver Dragon', 'Young White Dragon')           
        App.get_running_app().root.ids.Dragons.text = " ".join(['Monster:',(str(random.choice(Dragons)))])
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult Black Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Adult Black Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (710, 500)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1400)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult Blue Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Adult Blue Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (750, 540)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult Brass Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Adult Brass Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (800, 440)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult Bronze Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Adult Bronze Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (680, 140)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult Copper Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Adult Copper Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (630, 380)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult Gold Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Adult Gold Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (630, 380)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult Green Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Adult Green Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (680, 480)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult Red Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Adult Red Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (680, 480)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult Silver Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Adult Silver Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (870, 580)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Adult White Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Adult White Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 520)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Black Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Ancient Black Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (770, 450)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Blue Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Ancient Blue Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (500, 250)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Brass Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Ancient Brass Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (760, 450)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Bronze Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Ancient Bronze Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (720, 350)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Copper Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Ancient Copper Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (850, 525)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Gold Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Ancient Gold Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (670, 325)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Green Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Ancient Green Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (740, 330)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Red Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Ancient Red Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (650, 500)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient Silver Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Ancient Silver Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (750, 350)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Ancient White Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Ancient White Dragon.png'
            App.get_running_app().root.ids.DragonImage.pos = (500, 250)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Black Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Black Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (630, 250)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Blue Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Blue Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 350)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Brass Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Brass Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (820, 540)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Bronze Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Bronze Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (850, 600)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Copper Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Copper Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (500, 200)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Dragon Turtle':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Dragon Turtle.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (810, 650)
            App.get_running_app().root.ids.Dragons.halign = 'center'
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Gold Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Gold Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 50)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Green Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Green Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 150)
            App.get_running_app().root.ids.Dragons.halign = 'center'
            App.get_running_app().root.ids.Dragons.text_size = (500, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Pseudodragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Pseudodragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (650, 20)
            App.get_running_app().root.ids.Dragons.halign = 'center'
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Red Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Red Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 250)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Silver Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Silver Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 200)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: White Dragon Wyrmling':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\White Dragon Wyrmling.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 300)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Wyvern':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Wyvern.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (840, 650)
            App.get_running_app().root.ids.Dragons.text_size = (200, 1785)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Black Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Young_Black_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 50)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Blue Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Young_Blue_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 50)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Brass Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Young_Brass_Dragon.jpg'
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Bronze Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Young_Bronze_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (700, 400)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Copper Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Young_Copper_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (660, 350)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Gold Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Young_Gold_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (660, 100)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Green Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Young_Green_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (850, 600)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Red Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Young_Red_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (850, 600)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young Silver Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Young_Silver_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (850, 600)
        if App.get_running_app().root.ids.Dragons.text == 'Monster: Young White Dragon':
            App.get_running_app().root.ids.DragonImage.opacity = 1
            App.get_running_app().root.ids.DragonImage.source = 'Dragons\Young_White_Dragon.jpg'
            App.get_running_app().root.ids.DragonImage.pos = (600, 150)

#Elemental Monster Generation
    def Elemental_gen(self, *args): 
        Elementals = ('Air Elemental', 'Air Elemental')        
        App.get_running_app().root.ids.Elementals.text = " ".join(['Monster:',(str(random.choice(Elementals)))])
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Air Elemental':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Air Elemental.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Azer':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Azer.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Djinni':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Djinni.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785)    
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Dust Mephit':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Dust Mephit.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Earth Elemental':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Earth Elemental.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Gargoyle':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Gargoyle.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Ice Mephit':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Ice Mephit.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Invisible Stalker':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Invisible Stalker.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Magma Mephit':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Magma Mephit.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Magmin':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Magmin.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Salamander':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Salamander.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Steam Mephit':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Steam Mephit.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Water Elemental':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Water Elemental.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Elementals.text == 'Monster: Xorn':
            App.get_running_app().root.ids.ElementalImage.opacity = 1
            App.get_running_app().root.ids.ElementalImage.source = 'Elementals\Xorn.jpg'
            App.get_running_app().root.ids.ElementalImage.pos = (800, 50)
            App.get_running_app().root.ids.Elementals.halign = 'center'
            App.get_running_app().root.ids.Elementals.text_size = (500, 1785)                                                                                                                                                    
    
#Fey Monster Generation
    def Fey_gen(self, *args):
        Feys = ('Blink Dog', 'Blink Dog')        
        App.get_running_app().root.ids.Feys.text = " ".join(['Monster:',(str(random.choice(Feys)))])
        if App.get_running_app().root.ids.Feys.text == 'Monster: Blink Dog':
            App.get_running_app().root.ids.FeyImage.opacity = 1
            App.get_running_app().root.ids.FeyImage.source = 'Feys\Blink Dog.jpg'
            App.get_running_app().root.ids.FeyImage.pos = (800, 50)
            App.get_running_app().root.ids.Feys.halign = 'center'
            App.get_running_app().root.ids.Feys.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Feys.text == 'Monster: Dryad':
            App.get_running_app().root.ids.FeyImage.opacity = 1
            App.get_running_app().root.ids.FeyImage.source = 'Feys\Dryad.jpg'
            App.get_running_app().root.ids.FeyImage.pos = (800, 50)
            App.get_running_app().root.ids.Feys.halign = 'center'
            App.get_running_app().root.ids.Feys.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Feys.text == 'Monster: Green Hag':
            App.get_running_app().root.ids.FeyImage.opacity = 1
            App.get_running_app().root.ids.FeyImage.source = 'Feys\Green Hag.jpg'
            App.get_running_app().root.ids.FeyImage.pos = (800, 50)
            App.get_running_app().root.ids.Feys.halign = 'center'
            App.get_running_app().root.ids.Feys.text_size = (500, 1785)
        if App.get_running_app().root.ids.Feys.text == 'Monster: Satyr':
            App.get_running_app().root.ids.FeyImage.opacity = 1
            App.get_running_app().root.ids.FeyImage.source = 'Feys\Satyr.jpg'
            App.get_running_app().root.ids.FeyImage.pos = (800, 50)
            App.get_running_app().root.ids.Feys.halign = 'center'
            App.get_running_app().root.ids.Feys.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Feys.text == 'Monster: Sea Hag':
            App.get_running_app().root.ids.FeyImage.opacity = 1
            App.get_running_app().root.ids.FeyImage.source = 'Feys\Sea Hag.jpg'
            App.get_running_app().root.ids.FeyImage.pos = (800, 50)
            App.get_running_app().root.ids.Feys.halign = 'center'
            App.get_running_app().root.ids.Feys.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Feys.text == 'Monster: Sprite':
            App.get_running_app().root.ids.FeyImage.opacity = 1
            App.get_running_app().root.ids.FeyImage.source = 'Feys\Sprite.jpg'
            App.get_running_app().root.ids.FeyImage.pos = (800, 50)
            App.get_running_app().root.ids.Feys.halign = 'center'
            App.get_running_app().root.ids.Feys.text_size = (500, 1785)                                                          

#Fiend Monster Generation
    def Fiend_gen(self, *args):
        Fiends = ('Hell Hound', 'Hell Hound')        
        App.get_running_app().root.ids.Fiends.text = " ".join(['Monster:',(str(random.choice(Fiends)))])
        if App.get_running_app().root.ids.Fiends.text == 'Monster: Hell Hound':
            App.get_running_app().root.ids.FiendImage.opacity = 1
            App.get_running_app().root.ids.FiendImage.source = 'Fiends\Hell Hound.jpg'
            App.get_running_app().root.ids.FiendImage.pos = (800, 50)
            App.get_running_app().root.ids.Fiends.halign = 'center'
            App.get_running_app().root.ids.Fiends.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Fiends.text == 'Monster: Night Hag':
            App.get_running_app().root.ids.FiendImage.opacity = 1
            App.get_running_app().root.ids.FiendImage.source = r'Fiends\Night Hag.jpg'
            App.get_running_app().root.ids.FiendImage.pos = (800, 50)
            App.get_running_app().root.ids.Fiends.halign = 'center'
            App.get_running_app().root.ids.Fiends.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Fiends.text == 'Monster: Nightmare':
            App.get_running_app().root.ids.FiendImage.opacity = 1
            App.get_running_app().root.ids.FiendImage.source = r'Fiends\Nightmare.jpg'
            App.get_running_app().root.ids.FiendImage.pos = (800, 50)
            App.get_running_app().root.ids.Fiends.halign = 'center'
            App.get_running_app().root.ids.Fiends.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Fiends.text == 'Monster: Rakshasa':
            App.get_running_app().root.ids.FiendImage.opacity = 1
            App.get_running_app().root.ids.FiendImage.source = 'Fiends\Rakshasa.jpg'
            App.get_running_app().root.ids.FiendImage.pos = (800, 50)
            App.get_running_app().root.ids.Fiends.halign = 'center'
            App.get_running_app().root.ids.Fiends.text_size = (500, 1785)                                  

#Giant Monster Generation
    def Giant_gen(self, *args):
        Giants = ('Cloud Giant', 'Cloud Giant')        
        App.get_running_app().root.ids.Giants.text = " ".join(['Monster:',(str(random.choice(Giants)))])
        if App.get_running_app().root.ids.Giants.text == 'Monster: Cloud Giant':
            App.get_running_app().root.ids.GiantImage.opacity = 1
            App.get_running_app().root.ids.GiantImage.source = 'Giants\Cloud Giant.jpg'
            App.get_running_app().root.ids.GiantImage.pos = (800, 50)
            App.get_running_app().root.ids.Giants.halign = 'center'
            App.get_running_app().root.ids.Giants.text_size = (500, 1785)   
        if App.get_running_app().root.ids.Giants.text == 'Monster: Ettin':
            App.get_running_app().root.ids.GiantImage.opacity = 1
            App.get_running_app().root.ids.GiantImage.source = 'Giants\Ettin.jpg'
            App.get_running_app().root.ids.GiantImage.pos = (800, 50)
            App.get_running_app().root.ids.Giants.halign = 'center'
            App.get_running_app().root.ids.Giants.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Giants.text == 'Monster: Fire Giant':
            App.get_running_app().root.ids.GiantImage.opacity = 1
            App.get_running_app().root.ids.GiantImage.source = 'Giants\Fire Giant.jpg'
            App.get_running_app().root.ids.GiantImage.pos = (800, 50)
            App.get_running_app().root.ids.Giants.halign = 'center'
            App.get_running_app().root.ids.Giants.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Giants.text == 'Monster: Frost Giant':
            App.get_running_app().root.ids.GiantImage.opacity = 1
            App.get_running_app().root.ids.GiantImage.source = 'Giants\Frost Giant.jpg'
            App.get_running_app().root.ids.GiantImage.pos = (800, 50)
            App.get_running_app().root.ids.Giants.halign = 'center'
            App.get_running_app().root.ids.Giants.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Giants.text == 'Monster: Hill Giant':
            App.get_running_app().root.ids.GiantImage.opacity = 1
            App.get_running_app().root.ids.GiantImage.source = 'Giants\Hill Giant.jpg'
            App.get_running_app().root.ids.GiantImage.pos = (800, 50)
            App.get_running_app().root.ids.Giants.halign = 'center'
            App.get_running_app().root.ids.Giants.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Giants.text == 'Monster: Ogre':
            App.get_running_app().root.ids.GiantImage.opacity = 1
            App.get_running_app().root.ids.GiantImage.source = 'Giants\Ogre.jpg'
            App.get_running_app().root.ids.GiantImage.pos = (800, 50)
            App.get_running_app().root.ids.Giants.halign = 'center'
            App.get_running_app().root.ids.Giants.text_size = (500, 1785)
        if App.get_running_app().root.ids.Giants.text == 'Monster: Oni':
            App.get_running_app().root.ids.GiantImage.opacity = 1
            App.get_running_app().root.ids.GiantImage.source = 'Giants\Oni.jpg'
            App.get_running_app().root.ids.GiantImage.pos = (800, 50)
            App.get_running_app().root.ids.Giants.halign = 'center'
            App.get_running_app().root.ids.Giants.text_size = (500, 1785) 
        if App.get_running_app().root.ids.Giants.text == 'Monster: Storm Giant':
            App.get_running_app().root.ids.GiantImage.opacity = 1
            App.get_running_app().root.ids.GiantImage.source = 'Giants\Storm Giant.jpg'
            App.get_running_app().root.ids.GiantImage.pos = (800, 50)
            App.get_running_app().root.ids.Giants.halign = 'center'
            App.get_running_app().root.ids.Giants.text_size = (500, 1785)  
        if App.get_running_app().root.ids.Giants.text == 'Monster: Troll':
            App.get_running_app().root.ids.GiantImage.opacity = 1
            App.get_running_app().root.ids.GiantImage.source = 'Giants\Troll.jpg'
            App.get_running_app().root.ids.GiantImage.pos = (800, 50)
            App.get_running_app().root.ids.Giants.halign = 'center'
            App.get_running_app().root.ids.Giants.text_size = (500, 1785)                                                                                                    

#Humanoid Monster Generation
    def Humanoid_gen(self, *args): 
        Humanoids = ('Acolyte', 'Archmage')        
        App.get_running_app().root.ids.Humanoids.text = " ".join(['Monster:',(str(random.choice(Humanoids)))])
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Acolyte':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Acolyte.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (880, 550)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Archmage':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Archmage.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Assassin':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Assassin.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Bandit':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Bandit.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)                       
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Bandit Captain':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Bandit Captain.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Berserker':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Berserker.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Bugbear':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Bugbear.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)   
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Commoner':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Commoner.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)     
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Cult Fanatic':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Cult Fanatic.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Cultist':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Cultist.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Deep Gnome':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Deep Gnome.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)                                                                      
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Drow':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Drow.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Druid':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Druid.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Duergar':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Duergar.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Dwarf':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Dwarf.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)   
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Elf':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Elf.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Gladiator':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Gladiator.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Gnoll':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Gnoll.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Goblin':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Goblin.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Grimlock':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Grimlock.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Guard':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Guard.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Halfling':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Halfling.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)   
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Half-Red Dragon Veteran':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Half-Red Dragon Veteran.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Hobgoblin':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Hobgoblin.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Human':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Human.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)   
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Knight':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Knight.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Kobold':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Kobold.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)     
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Lizardfolk':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Lizardfolk.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Mage':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Mage.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)   
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Merfolk':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Merfolk.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)    
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Noble':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = r'Humanoids\Noble.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)   
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Orc':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Orc.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Priest':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Priest.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Sahaugain':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Sahaugain.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Scout':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Scout.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Spy':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Spy.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Thug':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Thug.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Tribal Warrior':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Tribal Warrior.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Veteran':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Veteran.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Werebear':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Werebear.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Wereboar':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Wereboar.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Wererat':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Wererat.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Weretiger':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Weretiger.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Humanoids.text == 'Monster: Werewolf':
            App.get_running_app().root.ids.HumanoidImage.opacity = 1
            App.get_running_app().root.ids.HumanoidImage.source = 'Humanoids\Werewolf.jpg'
            App.get_running_app().root.ids.HumanoidImage.pos = (780, 380)
            App.get_running_app().root.ids.Humanoids.halign = 'center'
            App.get_running_app().root.ids.Humanoids.text_size = (500, 1685)                                                                                                                                                                                                                                                                                                                                                  
                    
#Monstrosity Monster Generation
    def Monstrosity_gen(self, *args):
        Monstrosities = ('Androsphinx', 'Androsphinx')        
        App.get_running_app().root.ids.Monstrosities.text = " ".join(['Monster:',(str(random.choice(Monstrosities)))])
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Androsphinx':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Androsphinx.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Ankheg':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Ankheg.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Basilisk':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Basilisk.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Behir':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Behir.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Bulette':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Bulette.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)    
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Centaur':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Centaur.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)   
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Centipede Woman':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Centipede Woman.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Chimera':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Chimera.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Cockatrice':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Cockatrice.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Darkmantle':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Darkmantle.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Death Dog':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Death Dog.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Doppelganger':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Doppelganger.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Drider':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Drider.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Ettercap':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Ettercap.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Giant Spider':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Giant Spider.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)   
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Giant Squid':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Giant Squid.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)    
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Gorgon':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Gorgon.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Grick':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Grick.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Griffon':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Griffon.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Guardian Naga':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Guardian Naga.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Gynosphinx':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Gynosphinx.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Harpy':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Harpy.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Hippogriff':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Hippogriff.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Hydra':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Hydra.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Kraken':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Kraken.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Lamia':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Lamia.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Manticore':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Manticore.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Merrow':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Merrow.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)   
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Mimic':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Mimic.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)  
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Minotaur':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Minotaur.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Owlbear':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Owlbear.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Phase spider':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Phase spider.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Purple Worm':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Purple Worm.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Remorhaz':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Remorhaz.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Roc':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Roc.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Roper':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Roper.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Rust Monster':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Rust Monster.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Tarrasque':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Tarrasque.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Winter Wolf':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Winter Wolf.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)   
        if App.get_running_app().root.ids.Monstrosities.text == 'Monster: Worg':
            App.get_running_app().root.ids.MonstrosityImage.opacity = 1
            App.get_running_app().root.ids.MonstrosityImage.source = 'Monstrosities\Worg.jpg'
            App.get_running_app().root.ids.MonstrosityImage.pos = (880, 550)
            App.get_running_app().root.ids.Monstrosities.halign = 'center'
            App.get_running_app().root.ids.Monstrosities.text_size = (500, 1685)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    
#Ooze Monster Generation
    def Ooze_gen(self, *args):
        Oozes = ('Black Pudding', 'Black Pudding')        
        App.get_running_app().root.ids.Oozes.text = " ".join(['Monster:',(str(random.choice(Oozes)))])
        if App.get_running_app().root.ids.Oozes.text == 'Monster: Black Pudding':
            App.get_running_app().root.ids.OozeImage.opacity = 1
            App.get_running_app().root.ids.OozeImage.source = 'Oozes\Black Pudding.jpg'
            App.get_running_app().root.ids.OozeImage.pos = (880, 550)
            App.get_running_app().root.ids.Oozes.halign = 'center'
            App.get_running_app().root.ids.Oozes.text_size = (500, 1685)
        if App.get_running_app().root.ids.Oozes.text == 'Monster: Gelatinous Cube':
            App.get_running_app().root.ids.OozeImage.opacity = 1
            App.get_running_app().root.ids.OozeImage.source = 'Oozes\Gelatinous Cube.jpg'
            App.get_running_app().root.ids.OozeImage.pos = (880, 550)
            App.get_running_app().root.ids.Oozes.halign = 'center'
            App.get_running_app().root.ids.Oozes.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Oozes.text == 'Monster: Gray ooze':
            App.get_running_app().root.ids.OozeImage.opacity = 1
            App.get_running_app().root.ids.OozeImage.source = 'Oozes\Gray ooze.jpg'
            App.get_running_app().root.ids.OozeImage.pos = (880, 550)
            App.get_running_app().root.ids.Oozes.halign = 'center'
            App.get_running_app().root.ids.Oozes.text_size = (500, 1685)
        if App.get_running_app().root.ids.Oozes.text == 'Monster: Ochre Jelly':
            App.get_running_app().root.ids.OozeImage.opacity = 1
            App.get_running_app().root.ids.OozeImage.source = 'Oozes\Ochre Jelly.jpg'
            App.get_running_app().root.ids.OozeImage.pos = (880, 550)
            App.get_running_app().root.ids.Oozes.halign = 'center'
            App.get_running_app().root.ids.Oozes.text_size = (500, 1685)                                   
   
#Plant Monster Generation
    def Plant_gen(self, *args):
        Plants = ('Awakened Shrub', 'Awakened Shrub')        
        App.get_running_app().root.ids.Plants.text = " ".join(['Monster:',(str(random.choice(Plants)))])
        if App.get_running_app().root.ids.Plants.text == 'Monster: Awakened Shrub':
            App.get_running_app().root.ids.PlantImage.opacity = 1
            App.get_running_app().root.ids.PlantImage.source = 'Plants\Awakened Shrub.jpg'
            App.get_running_app().root.ids.PlantImage.pos = (880, 550)
            App.get_running_app().root.ids.Plants.halign = 'center'
            App.get_running_app().root.ids.Plants.text_size = (500, 1685)
        if App.get_running_app().root.ids.Plants.text == 'Monster: Awakened Tree':
            App.get_running_app().root.ids.PlantImage.opacity = 1
            App.get_running_app().root.ids.PlantImage.source = 'Plants\Awakened Tree.jpg'
            App.get_running_app().root.ids.PlantImage.pos = (880, 550)
            App.get_running_app().root.ids.Plants.halign = 'center'
            App.get_running_app().root.ids.Plants.text_size = (500, 1685)
        if App.get_running_app().root.ids.Plants.text == 'Monster: Shambling Mound':
            App.get_running_app().root.ids.PlantImage.opacity = 1
            App.get_running_app().root.ids.PlantImage.source = 'Plants\Shambling Mound.jpg'
            App.get_running_app().root.ids.PlantImage.pos = (880, 550)
            App.get_running_app().root.ids.Plants.halign = 'center'
            App.get_running_app().root.ids.Plants.text_size = (500, 1685)
        if App.get_running_app().root.ids.Plants.text == 'Monster: Shrieker':
            App.get_running_app().root.ids.PlantImage.opacity = 1
            App.get_running_app().root.ids.PlantImage.source = 'Plants\Shrieker.jpg'
            App.get_running_app().root.ids.PlantImage.pos = (880, 550)
            App.get_running_app().root.ids.Plants.halign = 'center'
            App.get_running_app().root.ids.Plants.text_size = (500, 1685)
        if App.get_running_app().root.ids.Plants.text == 'Monster: Violet Fungus':
            App.get_running_app().root.ids.PlantImage.opacity = 1
            App.get_running_app().root.ids.PlantImage.source = 'Plants\Violet Fungus.jpg'
            App.get_running_app().root.ids.PlantImage.pos = (880, 550)
            App.get_running_app().root.ids.Plants.halign = 'center'
            App.get_running_app().root.ids.Plants.text_size = (500, 1685)                                                              

#Swarm Monster Generation
    def Swarm_gen(self, *args):
        Swarms = ('Swarm of Bats', 'Swarm of Bats')
        App.get_running_app().root.ids.Swarms.text = " ".join(['Monster:',(str(random.choice(Swarms)))])
        if App.get_running_app().root.ids.Swarms.text == 'Monster: Swarm of Bats':
            App.get_running_app().root.ids.SwarmImage.opacity = 1
            App.get_running_app().root.ids.SwarmImage.source = 'Swarms\Swarm of Bats.jpg'
            App.get_running_app().root.ids.SwarmImage.pos = (880, 550)
            App.get_running_app().root.ids.Swarms.halign = 'center'
            App.get_running_app().root.ids.Swarms.text_size = (500, 1685)
        if App.get_running_app().root.ids.Swarms.text == 'Monster: Swarm of Insects':
            App.get_running_app().root.ids.SwarmImage.opacity = 1
            App.get_running_app().root.ids.SwarmImage.source = 'Swarms\Swarm of Insects.jpg'
            App.get_running_app().root.ids.SwarmImage.pos = (880, 550)
            App.get_running_app().root.ids.Swarms.halign = 'center'
            App.get_running_app().root.ids.Swarms.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Swarms.text == 'Monster: Swarm of Poisonous Snakes':
            App.get_running_app().root.ids.SwarmImage.opacity = 1
            App.get_running_app().root.ids.SwarmImage.source = 'Swarms\Swarm of Poisonous Snakes.jpg'
            App.get_running_app().root.ids.SwarmImage.pos = (880, 550)
            App.get_running_app().root.ids.Swarms.halign = 'center'
            App.get_running_app().root.ids.Swarms.text_size = (500, 1685)
        if App.get_running_app().root.ids.Swarms.text == 'Monster: Swarm of Quippers':
            App.get_running_app().root.ids.SwarmImage.opacity = 1
            App.get_running_app().root.ids.SwarmImage.source = 'Swarms\Swarm of Quippers.jpg'
            App.get_running_app().root.ids.SwarmImage.pos = (880, 550)
            App.get_running_app().root.ids.Swarms.halign = 'center'
            App.get_running_app().root.ids.Swarms.text_size = (500, 1685)
        if App.get_running_app().root.ids.Swarms.text == 'Monster: Swarm of Rats':
            App.get_running_app().root.ids.SwarmImage.opacity = 1
            App.get_running_app().root.ids.SwarmImage.source = 'Swarms\Swarm of Rats.jpg'
            App.get_running_app().root.ids.SwarmImage.pos = (880, 550)
            App.get_running_app().root.ids.Swarms.halign = 'center'
            App.get_running_app().root.ids.Swarms.text_size = (500, 1685)
        if App.get_running_app().root.ids.Swarms.text == 'Monster: Swarm of Ravens':
            App.get_running_app().root.ids.SwarmImage.opacity = 1
            App.get_running_app().root.ids.SwarmImage.source = 'Swarms\Swarm of Ravens.jpg'
            App.get_running_app().root.ids.SwarmImage.pos = (880, 550)
            App.get_running_app().root.ids.Swarms.halign = 'center'
            App.get_running_app().root.ids.Swarms.text_size = (500, 1685)                                                             

#Undead Monster Generation
    def Undead_gen(self, *args):
        Undead = ('Ghast', 'Ghast')
        App.get_running_app().root.ids.Undead.text = " ".join(['Monster:',(str(random.choice(Undead)))])
        if App.get_running_app().root.ids.Undead.text == 'Monster: Ghast':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Ghast.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Ghost':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Ghost.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Undead.text == 'Monster: Ghoul':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Ghoul.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Lich':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Lich.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Lich':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Lich.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Minotaur Skeleton':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Minotaur Skeleton.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Undead.text == 'Monster: Mummy':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Mummy.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Mummy Lord':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Mummy Lord.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Ogre Zombie':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Ogre Zombie.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Undead.text == 'Monster: Shadow':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Shadow.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Skeleton':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Skeleton.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Specter':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Specter.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Undead.text == 'Monster: Vampire':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Vampire.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Vampire Spawn':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Vampire Spawn.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Warhorse Skeleton':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Warhorse Skeleton.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Wight':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Wight.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Will-o-wisp':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Will-o-wisp.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)
        if App.get_running_app().root.ids.Undead.text == 'Monster: Wraith':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Wraith.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685) 
        if App.get_running_app().root.ids.Undead.text == 'Monster: Zombie':
            App.get_running_app().root.ids.UndeadImage.opacity = 1
            App.get_running_app().root.ids.UndeadImage.source = 'Undead\Zombie.jpg'
            App.get_running_app().root.ids.UndeadImage.pos = (880, 550)
            App.get_running_app().root.ids.Undead.halign = 'center'
            App.get_running_app().root.ids.Undead.text_size = (500, 1685)   
            
                


            
class DCCGenerator(GridLayout):  
    # Generator for creating Dungeon Crawl Classic characters
    def DCCCharacterGenerator(self):
        App.get_running_app().root.ids.select_level.pos = (500, 980) #Positioning the select level spinner
        App.get_running_app().root.ids.select_level.opacity = 1      #Changing opacity so the select level spinner appears

        
    def set_level(self): 
        DCCCharacterLevel = App.get_running_app().root.ids.select_level.text #Creating the DCCCharacterLevel variable to hold the current level selected 

        if DCCCharacterLevel == '0th': 
            self.DCCZeroLevel_Gen()     #Calling the zero level generator when our level is 0th
        if DCCCharacterLevel != '0th':
            self.DCCClassLevel_Gen()    #Calling the class level generator when our level is 1st or higher
            
    def set_class(self):
        DCCCharacterClass = App.get_running_app().root.ids.select_class.text #Creating the DCCCharacterClass variable to hold the current class selected
        
        
#NEED TO WORK ON THE SUBMIT BUTTON AND GENERATOR OUTPUT            
    def DCCZeroLevel_Gen(self):
        App.get_running_app().root.ids.select_class.opacity = 0     #Changing opacity so the select class spinner disappears if 0th level is selected
    
    def DCCClassLevel_Gen(self):
        App.get_running_app().root.ids.select_class.pos = (500, 880) #Positioning the select class spinner
        App.get_running_app().root.ids.select_class.opacity = 1      #Changing opacity so the select class spinner appears
        
        
        
        
class app1(App):
    Name_Variable = NameGenOriginal()  
    Louche_Variable = Louche()  
    Monster_Variable = MonsterGenerator()
    DCC_Variable = DCCGenerator()
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