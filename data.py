import random
class Merc:
	def __init__(self, name, profession, archetype, background, age, attributes, characteristics, skills, inventory):
		self.name = name
		self.ancestry = roll_ancestry()
		self.profession = profession
		self.archetype = archetype
		self.background = background
		self.age = age
		self.characteristics = characteristics
		self.skills = skills
		self.inventory = []
	
class Characteristics:
	def __init__(self, initiative, luck, resolve, size, wounds):
		self.initiative = initiative
		self.luck = luck
		self.resolve = resolve
		self.size = size
		self.wounds = wounds

class Ancestry:
	def __init__(self, name, size, attributes):
		self.name = name
		self.size = size
		self.attributes = attributes

	def __str__(self):
		return f"Ancestry:{self.name}\nSize:{self.size}\nAttributes: {self.attributes}"

#Characteristics

ancestries = {
    "clever": {
        "name": "Clever",
        "size": (0,),
        "attributes": {
            "composure": 6,
            "intellect": 7,
            "prowess": 4,
            "vigor": 4,
        },
    },

    "driven": {
        "name": "Driven",
        "size": (0, 1),
        "attributes": {
            "composure": 5,
            "intellect": 5,
            "prowess": 5,
            "vigor": 5,
        },
    },

    "keen": {
        "name": "Keen",
        "size": (1,),
        "attributes": {
            "composure": 6,
            "intellect": 6,
            "prowess": 6,
            "vigor": 3,
        },
    },

    "mighty": {
        "name": "Mighty",
        "size": (2,),
        "attributes": {
            "composure": 4,
            "intellect": 4,
            "prowess": 6,
            "vigor": 7,
        },
    },

    "strange": {
        "name": "Strange",
        "size": (-1, 2),
        "attributes": {
            "composure": 7,
            "intellect": 6,
            "prowess": 3,
            "vigor": 5,
        },
    },
}
clever = Ancestry(
	"Clever",
	ancestries["clever"]["size"],
	ancestries["clever"]["attributes"],
)
print (clever)
def roll_ancestry():
	roll = random.randint(1, 10)
	if roll ==1 or roll ==2:
		chosen_ancestry = ancestries["clever"]
	elif roll ==3 or roll ==4:
		chosen_ancestry =ancestries["driven"]
	elif roll ==5 or roll ==6:
		chosen_ancestry = ancestries["keen"]
	elif roll ==7 or roll ==8:
		chosen_ancestry = ancestries["mighty"]
	else:
		chosen_ancestry = ancestries["strange"]
	print(f"You rolled {chosen_ancestry['name']}!")
	return chosen_ancestry
rolled_ancestry = roll_ancestry()
#initiative = prowess + intelligence
#luck = ['D4', 'D6', 'D8', 'D10', 'D12']
#skills
'''General Skills
Acrobatics (VIG))
Awareness (INT)
Determination (COM)
Physique (VIG)
Skullduggery (VIG)
Steering (VIG)
Intellect Skills
Barber-Surgery (INT)
Comprehension (INT)
Survival (INT)
Tinkering (INT)
Social Skills
Haggle (COM)
Insight (COM)
Presence (COM)
Performance (COM)
Combat Skills
Brawl (VIG) 
Dual (PRO)
One-Handed (PRO)  
Ranged (PRO) 
Shielded (PRO) 
Two-Handed (PRO)
'''