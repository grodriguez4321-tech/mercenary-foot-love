import random


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
    def __init__(self, name: str, skill_improvements: list = None, arsenal: list = None, downtime_activity: str = ""):
        self.name = name
        self.skill_improvements = skill_improvements if skill_improvements is not None else []
        self.arsenal = arsenal if arsenal is not None else []
        self.downtime_activity = downtime_activity


academic = Background("Academic", [], [], "")

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
