"""
Authored by AllAcacia on 14/10/2024 (dd/mm/yyyy)
card.py | "Card" class file, contains dictionaries for what symbols mean.
Intended to be used for in-game logic too, implemented as needed.
"""

COLOURS = {"r": (0, "red"), "o": (1, "orange"), "y": (2, "yellow"), "g": (3, "green"), "b": (4, "blue"), "p": (5, "purple")}
ELEMENTS = {"f": (0, "fire"), "w": (1, "water"), "s": (2, "snow")}
POWERED = {"n": (False, "not powered"), "y": (True, "powered")}
EFFECTS =  {"na": (0, "no effect"), "df": (1, "discard fire"), "dw": (2, "discard water"), "ds": (3, "discard snow"),
            "dr": (4, "discard red"), "do": (5, "discard orange"), "dy": (6, "discard yellow"),
            "dg": (7, "discard green"), "db": (8, "discard blue"), "dp": (9, "discard purple"),
            "dmr": (4, "discard multiple red"), "dmo": (5, "discard multiple orange"), "dmy": (6, "discard multiple yellow"),
            "dmg": (7, "discard multiple green"), "dmb": (8, "discard multiple blue"), "dmp": (9, "discard multiple purple"),
            "fs": (10, "fire to snow"), "sw": (11, "snow to water"), "wf": (12, "water to fire"),
            "bf": (13, "block fire"), "bw": (14, "block water"), "bs": (15, "block snow"),
            "pr": (16, "power reversal"), "pt": (17, "plus two (user)"), "mt": (18, "minus two (opponent)")}
RANK_MIN = 1
RANK_MAX = 804
VALUE_MIN = 2
VALUE_MAX = 12

class Card():
    name = None
    rank = None
    value = None
    colour = None
    element = None
    powered = None
    effect = None


    def __init__(self, name, rank, value, element, colour, powered, effect):
        """Initialise card object."""
        valid = self.verify_card(int(rank), int(value), element, colour, powered, effect)
        if valid:
            self.name = str(name)
            self.rank = int(rank)
            self.value = int(value)
            self.colour = colour
            self.element = element
            self.powered = powered
            if self.powered == "y":
                self.effect = effect
            else:
                self.effect = "na"
            # print(f"Created a {self.colour} {self.element} card with an ability of {self.effect} that is {self.powered}. Rank is {self.rank}.")
        else:
            raise print("At least one of the init inputs is invalid!")


    def __repr__(self):
        return f"Card({self.name}, {self.rank}, {self.value}, {ELEMENTS[self.element][1]}, {COLOURS[self.colour][1]}, {POWERED[self.powered][1]}, {EFFECTS[self.effect][1]})"
    

    def get_rank(self):
        """Returns rank as an integer."""
        return self.rank
    

    def get_colour(self):
        """Returns colour as a letter."""
        return self.colour


    def get_powered(self):
        """Returns whether the card is a power card as a letter."""
        return self.powered
    

    def get_effect(self):
        """Returns the effect of the card as a letter"""
        return self.effect
    

    def verify_card(self, rank, value, element, colour, powered, effect):
        """Returns the validity of the card's details."""
        result = True
        if (colour not in COLOURS.keys()):
            print(f"'{colour}' is an invalid colour. Must be one of {COLOURS.keys()}.")
            result = False
        if (element not in ELEMENTS.keys()):
            print(f"'{element}' is an invalid element. Must be one of {ELEMENTS.keys()}.")
            result = False
        if (powered not in POWERED.keys()):
            print(f"'{powered}' is an invalid power status. Must be one of {POWERED.keys()}.")
            result = False
        if (effect not in EFFECTS.keys()):
            print(f"'{effect}' is an invalid effect. Must be one of {EFFECTS.keys()}.")
            result = False
        if (rank < 1) and (rank > 804):
            print(f"'{rank}' is an invalid rank number. Must be between {RANK_MIN} and {RANK_MAX}.")
            result = False
        if (value < VALUE_MIN):
            print(f"A value of '{value}' is less than {VALUE_MIN}.")
            result = False
        
        return result
    

    def check_card_overlap(self, other):
        """Compares two cards. An overlap occurs if both ranks are equal."""
        overlap = False
        if self.rank == other.rank:
            overlap = True
            print(f"Both cards share the rank '{self.rank}'.")
        
        return overlap