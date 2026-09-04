class Merc:
	def __init__(self, name, ancestry, profession, archetype, background, age, attributes, characteristics, skills, inventory):
		self.name = name
		self.ancestry = ancestry
		self.profession = profession
		self.archetype = archetype
		self.background = background
		self.age = age
		self.attributes = attributes
		self.characterisrics = characteristics
		self.skills = skills
		self.inventory = []
	
	
class Ancestry:
	def __init__(self, name, ancestry_attributes):
		self.name = name
		self.ancestry_attributes = ancestry_attributes
clever = Ancestry('Clever', )
clever_attributes = {
	'composure' : 6,
	'intellect' : 7,
	'prowess' : 4,
	'vigor' : 4
}
