import random
class Merc:
	def __init__(self, name, profession, archetype, background, age, attributes, characteristics, skills, inventory):
		self.name = name
		self.ancestry = roll_ancestry()
		self.profession = profession
		self.archetype = archetype
		self.background = background
		self.age = age
		self.attributes = attributes
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

driven = Ancestry(
	"Driven",
	ancestries["driven"]["size"],
	ancestries["driven"]["attributes"],
)

keen = Ancestry(
	"Keen",
	ancestries["keen"]["size"],
	ancestries["keen"]["attributes"]
)

mighty = Ancestry(
	"Mighty",
	ancestries["mighty"]["size"],
	ancestries["mighty"]["attributes"]
)

strange = Ancestry(
	"Strange",
	ancestries["strange"]["size"],
	ancestries["strange"]["attributes"]
)

ancestry_objs = [clever, driven, keen, mighty, strange]
for ancestry in ancestry_objs:
	print(ancestry)
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
#rolled_ancestry = roll_ancestry()
#initiative = prowess + intelligence
luck = {
	"D4": 12,
	"D6": 10,
	"D8": 8,
	"D10": 6,
	"D12": 4
}

skills = {
        "general_skills" : {
		    "acrobatics" : {
			    "attribute" : "vig",
			    "rank" : 0,
            },
                   "awareness" : {
		        "attribute": "INT",
			    "rank" : 0,
            },
		    "determination" : {
                           "attribute": "COM",
			    "rank" :0,
            },
            "physique" : {
			    "attribute": "VIG",
			    "rank": 0,
            },

            "skullduggery": {
                           "attribute": "VIG",
			    "rank": 0,
            },
                "steering": {
                    "attribute": "VIG",
                    "rank": 0
            },
        },
		"Intellect Skills": {
            "Barber-Surgery": {
				"attribute" : "INT",
				"rank": 0
            },
			"Comprehension": {
				"attribute": "INT",
				"rank": 0,
			},
			"Survival": {
				"attribute": "INT",
                "rank": 0,
            },
            "Tinkering": {
				"attribute": "INT",
                "rank": 0
			},
		},
        "Social Skills": {
			"Haggle": {
				"attribute": "COM",
				"rank": 0
            },
			"Insight": {
				"attribute": "COM",
                "rank": 0
            },
			"Presence": {
                "attribute": "COM",
                "rank": 0
            },
			"Performance": {
                "attribute": "COM",
                "rank": 0
            },
        },
        "Combat Skills": {
			"Brawl": {
                "attribute": "VIG",
                "rank": 0
            },
			"Dual": {
                "attribute": "PRO",
                "rank": 0
            },
			"One-Handed": {
                "attribute": "PRO",
                "rank": 0
            },
			"Ranged": {
                "attribute": "PRO",
                "rank": 0
            },
			"Shielded": {
                "attribute": "PRO",
                "rank": 0
            },
            "Two-Handed": {
                "attribute": "PRO",
                "rank": 0
            }
        },
}
