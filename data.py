import random
from random import choice


class Characteristics:
    def __init__(self, initiative: int = 0, luck: int = 0, resolve: int = 0, size: int = 0, wounds: int = 0):
        self.initiative = initiative
        self.luck = luck
        self.resolve = resolve
        self.size = size
        self.wounds = wounds

    def __repr__(self) -> str:
        return (
            f"Characteristics(initiative={self.initiative}, luck={self.luck}, "
            f"resolve={self.resolve}, size={self.size}, wounds={self.wounds})"
        )

    def __str__(self) -> str:
        return (
            f"Characteristics:\n"
            f"  Initiative: {self.initiative}\n"
            f"  Luck: {self.luck}\n"
            f"  Resolve: {self.resolve}\n"
            f"  Size: {self.size}\n"
            f"  Wounds: {self.wounds}"
        )


class Ancestry:
    def __init__(self, name: str, size: tuple, attribute_caps: dict[str, int]):
        self.name = name
        self.size = size
        self.attribute_caps = attribute_caps

    def __repr__(self) -> str:
        return f"Ancestry(name='{self.name}', size={self.size}, attribute_caps={self.attribute_caps})"

    def __str__(self) -> str:
        return f"Ancestry: {self.name}\nSize: {self.size}\nAttribute Caps: {self.attribute_caps}"


ancestries = {
    "clever": {
        "name": "Clever",
        "size": (0,),
        "attribute_caps": {
            "composure": 6,
            "intellect": 7,
            "prowess": 4,
            "vigor": 4,
        },
    },

    "driven": {
        "name": "Driven",
        "size": (0, 1),
        "attribute_caps": {
            "composure": 5,
            "intellect": 5,
            "prowess": 5,
            "vigor": 5,
        },
    },

    "keen": {
        "name": "Keen",
        "size": (1,),
        "attribute_caps": {
            "composure": 6,
            "intellect": 6,
            "prowess": 6,
            "vigor": 3,
        },
    },

    "mighty": {
        "name": "Mighty",
        "size": (2,),
        "attribute_caps": {
            "composure": 4,
            "intellect": 4,
            "prowess": 6,
            "vigor": 7,
        },
    },

    "strange": {
        "name": "Strange",
        "size": (-1, 2),
        "attribute_caps": {
            "composure": 7,
            "intellect": 6,
            "prowess": 3,
            "vigor": 5,
        },
    },
}

class Background:
    def __init__(
        self,
        name: str,
        skill_improvements: dict = None,
        arsenal: list = None,
        downtime_activity: str = "",
    ):
        self.name = name
        self.skill_improvements = skill_improvements or {
            "general skills": {},
            "combat skills": {},
            "intellect skills": {},
            "social skills": {},
        }
        self.arsenal = arsenal if arsenal is not None else []
        self.downtime_activity = downtime_activity

    def __repr__(self) -> str:
        return (
            f"Background(name='{self.name}', skill_improvements={self.skill_improvements}, "
            f"arsenal={self.arsenal}, downtime_activity='{self.downtime_activity}')"
        )

    def __str__(self) -> str:
        return (
            f"Background: {self.name}\n"
            f"Skill Improvements: {self.skill_improvements}\n"
            f"Arsenal: {self.arsenal}\n"
            f"Downtime Activity: {self.downtime_activity}"
        )


academic = Background(
    name="Academic",
    skill_improvements={
        "general skills": {
            "novice": 1,
        },
        "combat skills": {
            "novice": 1,
        },
        "intellect skills": {
            "novice": 1,
            "trained": 3,
        },
        "social skills": {
            "novice": 2,
            "trained": 2,
        },
    },
    arsenal=[
        "A cudgel or dagger",
    ],
    downtime_activity="Research (Academic): You scour your books, local libraries and temples for any scrap of useful lore. Gain an additional Grit.",
)

aristocrat = Background(
    name="Aristocrat",
    skill_improvements={
        "choice": {
            "novice": 5,
            "trained": 5,
        },
    },
    arsenal=[
        "Any set of light, medium or heavy armour",
        "Any 2 scarce weapons of choice",
    ],
    downtime_activity=(
        "Everything and Nothing (Aristocrat): You do whatever you fancy at the moment. "
        "Roll a D6 and partake in another background activity (Combat Discipline, Ease-Up, Pray, Research, Scout Ahead, Found It)."
    ),
)

clergy = Background(
    name="Clergy",
    skill_improvements={
        "general skills": {
            "novice": 1,
            "trained": 2,
        },
        "combat skills": {
            "novice": 1,
        },
        "intellect skills": {
            "novice": 2,
        },
        "social skills": {
            "novice": 1,
            "trained": 2,
        },
        "intellect or combat skills": {
            "trained": 1,
        },
    },
    arsenal=[
        "Any set of light or medium armour",
        "A common melee weapon",
    ],
    downtime_activity="Pray (Clergy): You ask the gods to watch over you and to grant you their blessing. Gain an additional luck die (Can bring you above your maximum).",
)

commoner = Background(
    name="Commoner",
    skill_improvements={
        "general skills": {
            "novice": 2,
            "trained": 3,
        },
        "combat skills": {
            "novice": 1,
        },
        "intellect skills": {
            "novice": 1,
        },
        "social skills": {
            "novice": 1,
            "trained": 2,
        },
    },
    arsenal=[
        "Any set of light armour",
        "2 plentiful weapons or a common weapon",
    ],
    downtime_activity="Ease-Up (Commoner): You enjoy your time-off like there’s no tomorrow. Recover D6 wounds.",
)

criminal = Background(
    name="Criminal",
    skill_improvements={
        "general skills": {
            "novice": 2,
            "trained": 2,
        },
        "combat skills": {
            "novice": 2,
            "trained": 1,
        },
        "social or intellect skills": {
            "novice": 1,
        },
        "social skills": {
            "trained": 2,
        },
    },
    arsenal=[
        "Leather jerkins or thick furs",
        "A plentiful and a common brawling or small arms weapon",
    ],
    downtime_activity=(
        "Found It (Criminal): You hustle up something extra with less than savory activities. "
        "Acquire an additional rumour or piece of gear of your choice for free with relevant test (GM’s discretion, "
        "but the scarcer the item, harder the test). On failure, suffer relevant consequence."
    ),
)

fighter = Background(
    name="Fighter",
    skill_improvements={
        "general skills": {
            "novice": 2,
            "trained": 2,
        },
        "combat skills": {
            "novice": 1,
            "trained": 3,
        },
        "social skills": {
            "novice": 2,
        },
    },
    arsenal=[
        "Any set of medium armour",
        "A scarce weapon and common weapon",
    ],
    downtime_activity="Combat Discipline (Fighter): You steel yourself for the next conflict. Recover D4 resolve.",
)

outlander = Background(
    name="Outlander",
    skill_improvements={
        "general skills": {
            "novice": 2,
            "trained": 3,
        },
        "combat skills": {
            "novice": 1,
            "trained": 2,
        },
        "intellect skills": {
            "novice": 1,
        },
        "social skills": {
            "novice": 1,
        },
    },
    arsenal=[
        "Thick furs",
        "A plentiful and a common archery or brawling weapon",
    ],
    downtime_activity="Scout Ahead (Outlander): You prepare for your travels. At the end of downtime, improve supply die by 1.",
)
roguish_tricks = {
        "Backstabber": "If you target an opponent with a stealth strike, whether you succeed or not, they suffer damage (Ignoring AB) equal to your rank.",
        "Contortionist": "Add your rank to any test to resist or end the grappled and prone condition.",
        "Critical Opportunity": "When you press as a critical manoeuvre, add your rank to your next test in the round in addition to advantage. ",
        "Evasive": "Ranged strikes targeting you suffer -your rank to hit.",
        "Light Step": "Subtract your rank from any wounds lost by collision or falling.",
        "Poisoner": "At the start of each encounter, you start with your rank’s worth of supply cost of poisons (See crafting chapter).",
        "Quick Reflexes": "At the start of the round, spend an action to increase your Initiative by your rank until the start of the next round.",
        "Scoundrels Luck": """Per encounter, you can re-roll a number of dice equal to your rank, but must accept the second result (No additional luck or resolve!). 
        If your re-roll is a 1, you count as critically failing and you can no longer use this ability until the start of your next encounter. 
        A critical failure means the opponent critical succeeds against you or something terrible happens to you in additional to failing (GMs discretion): 
        Your weapon breaks, you suffer an injury, you fall prone, etc…,""",
        "Silver-Tongued": "Add your rank to haggle and insight tests.",
        "Thief": "Add your rank to acrobatics and skullduggery tests."
    }
class Profession:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability


class Archetype:
    def __init__(self, name, profession, ability):
        self.name = name
        self.profession = profession
        self.ability = ability
alchemist = Profession("Alchemist", "Perfected Craft:\nAdd your rank to tinkering tests and at the start of each encounter you start with double your rank's worth of supply cost of the following items:\nBombardier: You start with double your rank worth of engineer devices(Weapons, bombs, upgrades and gadgets.\nElixerist: You start with double your rank worth of alchemical concoctions.")
bombardier = Archetype("Bombardier", alchemist, "Blackpowder Savant: When you strike with a blackpowder or engineering device, add your rank to the damage. In addition, regardless of background, you start with a rifle or pistol.")
elixirist = Archetype("Elixerist", alchemist, "Improved Concoctions: Add your rank to any test required to use or apply alchemical concoctions (GM’s discretion).")
rogue = Profession("Rogue", f"Rogueish Tricks:\n Choose a number of tricks equal to your rank(Maximum of 5, gain one when you rank up).{roguish_tricks}")
charlatan = Archetype("Charlatan", rogue, "Distracting Exploit: In combat, you can use the Exploit (1) reaction against a visible opponent: The next test or instance of damage against them in the round gains your rank or the next instance of damage they deal is lowered by your rank  (You choose).\nThe same target cannot be targeted more than once in the same round (Unless they are really gullible!). ")
cutpurse = Archetype("Cutpurse", rogue, "Opportunist: Add your rank to any test for executing manoeuvres.")
cutthroat = Archetype("Cutthroat", rogue, "Gutter-Cutter: If you strike an opponent with a stealth strike or that is suffering from a condition, you add your rank to hit and to the damage.")





#background_objs = [academic, aristocrat, clergy, commoner, criminal, fighter, outlander]
background_instances = {
    "academic": academic,
    "aristocrat": aristocrat,
    "clergy": clergy,
    "commoner": commoner,
    "criminal": criminal,
    "fighter": fighter,
    "outlander": outlander,
}

clever = Ancestry(
    ancestries["clever"]["name"],
    ancestries["clever"]["size"],
    ancestries["clever"]["attribute_caps"],
)

driven = Ancestry(
    ancestries["driven"]["name"],
    ancestries["driven"]["size"],
    ancestries["driven"]["attribute_caps"],
)

keen = Ancestry(
    ancestries["keen"]["name"],
    ancestries["keen"]["size"],
    ancestries["keen"]["attribute_caps"],
)

mighty = Ancestry(
    ancestries["mighty"]["name"],
    ancestries["mighty"]["size"],
    ancestries["mighty"]["attribute_caps"],
)

strange = Ancestry(
    ancestries["strange"]["name"],
    ancestries["strange"]["size"],
    ancestries["strange"]["attribute_caps"],
)

ancestry_objs = [clever, driven, keen, mighty, strange]
ancestry_instances = {
    "clever": clever,
    "driven": driven,
    "keen": keen,
    "mighty": mighty,
    "strange": strange,
}
luck = {
    "D4": 12,
    "D6": 10,
    "D8": 8,
    "D10": 6,
    "D12": 4,
}
untrained = 0
novice = 2
trained = 4
expert = 6
master = 8
legend = 10
proficiency_ranks = [untrained, novice, trained, expert, master, legend]
skills = {
    "general_skills": {
        "acrobatics": {
            "attribute": "vigor",
            "rank": untrained,
        },
        "awareness": {
            "attribute": "intellect",
            "rank": untrained,
        },
        "determination": {
            "attribute": "composure",
            "rank": untrained,
        },
        "physique": {
            "attribute": "vigor",
            "rank": untrained,
        },
        "skullduggery": {
            "attribute": "vigor",
            "rank": untrained,
        },
        "steering": {
            "attribute": "vigor",
            "rank": untrained,
        },
    },
    "intellect_skills": {
        "barber_surgery": {
            "attribute": "intellect",
            "rank": untrained,
        },
        "comprehension": {
            "attribute": "intellect",
            "rank": untrained,
        },
        "survival": {
            "attribute": "intellect",
            "rank": untrained,
        },
        "tinkering": {
            "attribute": "intellect",
            "rank": untrained,
        },
    },
    "social_skills": {
        "haggle": {
            "attribute": "composure",
            "rank": untrained,
        },
        "insight": {
            "attribute": "composure",
            "rank": untrained,
        },
        "presence": {
            "attribute": "composure",
            "rank": untrained,
        },
        "performance": {
            "attribute": "composure",
            "rank": untrained,
        },
    },
    "combat_skills": {
        "brawl": {
            "attribute": "vigor",
            "rank": untrained,
        },
        "dual": {
            "attribute": "prowess",
            "rank": untrained,
        },
        "one_handed": {
            "attribute": "prowess",
            "rank": untrained,
        },
        "ranged": {
            "attribute": "prowess",
            "rank": untrained,
        },
        "shielded": {
            "attribute": "prowess",
            "rank": untrained,
        },
        "two_handed": {
            "attribute": "prowess",
            "rank": untrained,
        },
    },
}

def roll_ancestry() -> Ancestry:
    roll = random.randint(1, 10)
    if roll in (1, 2):
        chosen_ancestry = clever
    elif roll in (3, 4):
        chosen_ancestry = driven
    elif roll in (5, 6):
        chosen_ancestry = keen
    elif roll in (7, 8):
        chosen_ancestry = mighty
    else:
        chosen_ancestry = strange
    return chosen_ancestry


class Merc:
    MAX_ATTRIBUTE_BOOSTS: int = 7

    def __init__(
        self,
        name: str,
        ancestry: Ancestry = None,
        profession: str = "",
        archetype: str = "",
        background: str = "",
        age: int = 20,
        skills: dict = None,
        inventory: list = None,
        characteristics: Characteristics = None,
    ):
        self.name = name
        self.ancestry = ancestry if ancestry is not None else roll_ancestry()
        self.profession = profession
        self.archetype = archetype
        self.background = background
        self.age = age
        self.current_attributes = {
            "composure": 1,
            "intellect": 1,
            "prowess": 1,
            "vigor": 1,
        }
        self.characteristics = characteristics or Characteristics()
        self.skills = skills or {}
        self.inventory = inventory or []
        self.attribute_boosts = 0
        self.update_derived_characteristics()

    def increase_attribute(self, attr_name: str, amount: int = 1) -> None:
        if amount <= 0:
            raise ValueError(f"Increase amount must be positive, got {amount}")

        attr = attr_name.lower()
        if attr not in self.current_attributes:
            raise KeyError(f"Invalid attribute: '{attr_name}'")

        if self.attribute_boosts + amount > self.MAX_ATTRIBUTE_BOOSTS:
            raise ValueError(
                f"Cannot apply {amount} boost(s): would exceed total allowed boosts "
                f"({self.attribute_boosts + amount}/{self.MAX_ATTRIBUTE_BOOSTS})."
            )

        cap = self.ancestry.attribute_caps.get(attr, 0)
        new_val = self.current_attributes[attr] + amount
        if new_val > cap:
            raise ValueError(
                f"Cannot increase {attr} to {new_val}: exceeds ancestry cap of {cap} for {self.ancestry.name}."
            )

        self.current_attributes[attr] = new_val
        self.attribute_boosts += amount
        self.update_derived_characteristics()

    def calculate_initiative(self) -> int:
        return self.current_attributes["prowess"] + self.current_attributes["intellect"]

    def calculate_resolve(self) -> int:
        return self.current_attributes["composure"]

    def calculate_wounds(self) -> int:
        return self.current_attributes["vigor"]

    def update_derived_characteristics(self) -> None:
        self.characteristics.initiative = self.calculate_initiative()
        self.characteristics.resolve = self.calculate_resolve()
        self.characteristics.wounds = self.calculate_wounds()
        if self.ancestry and self.ancestry.size:
            self.characteristics.size = self.ancestry.size[0]

    def __repr__(self) -> str:
        return (
            f"Merc(name='{self.name}', ancestry={self.ancestry.name}, "
            f"attributes={self.current_attributes})"
        )

    def __str__(self) -> str:
        return (
            f"Merc: {self.name}\n"
            f"Ancestry: {self.ancestry.name}\n"
            f"Profession: {self.profession}\n"
            f"Archetype: {self.archetype}\n"
            f"Background: {self.background}\n"
            f"Age: {self.age}\n"
            f"Attributes: {self.current_attributes}\n"
            f"{self.characteristics}"
        )

    def roll_skill(self, skill_name: str) -> int | None:
        for category in self.skills:
            if skill_name in self.skills[category]:
                skill = self.skills[category][skill_name]

                attribute = skill["attribute"]
                rank = skill["rank"]
                roll_result = self.current_attributes[attribute] + rank + random.randint(1, 10)
                return roll_result
        print("That skill does not exist")
        return None

if __name__ == "__main__":
    print("=== Ancestry Rolling Demo ===")
    for _ in range(3):
        rolled = roll_ancestry()
        print(f"Rolled: {rolled.name} (Caps: {rolled.attribute_caps}, Size: {rolled.size})")

    print("\n=== Merc Character Creation & Attribute Progression ===")
    merc = Merc(name="Valen", ancestry=clever, profession="Scholar")
    print(merc)
    print(f"Initial attributes: {merc.current_attributes}")

    # Increase intellect within cap (Clever intellect cap is 7)
    merc.increase_attribute("intellect", 5)
    print(f"Intellect after +5: {merc.current_attributes['intellect']}")
    assert merc.current_attributes["intellect"] == 6
    assert merc.characteristics.initiative == merc.calculate_initiative()

    merc.increase_attribute("intellect", 1)
    print(f"Intellect at cap (7): {merc.current_attributes['intellect']}")
    assert merc.current_attributes["intellect"] == 7

    # Attempt to exceed cap
    try:
        merc.increase_attribute("intellect", 1)
        print("ERROR: Should not reach here, cap was exceeded!")
    except ValueError as e:
        print(f"Cap enforcement working as expected: {e}")

    # Increase other attributes and verify auto-synchronization of derived characteristics
    merc.increase_attribute("vigor", 1)
    assert merc.characteristics.wounds == 2
    print(f"\nFinal Attributes: {merc.current_attributes}")
    print(f"Updated Characteristics: {merc.characteristics}")

    # Attempt to exceed total boost limit (used: 5+1+1 = 7)
    try:
        merc.increase_attribute("prowess", 1)
        print("ERROR: Should not reach here, boost limit was exceeded!")
    except ValueError as e:
        print(f"Boost limit enforcement working as expected: {e}")

    print("\n=== Skills Dictionary Integrity Check ===")
    valid_attributes = set(merc.current_attributes.keys())
    for category_name, category_skills in skills.items():
        for skill_name, skill_info in category_skills.items():
            attr = skill_info["attribute"]
            assert attr in valid_attributes, f"Invalid attribute '{attr}' in skill '{skill_name}'"
    print("All skill attributes match valid core attribute keys!")
