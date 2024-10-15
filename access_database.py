"""
Authored by AllAcacia, on 14/10/2024 (dd/mm/yyyy)
access_database.py | Used to access a .txt file, laid out like a .csv file.
"""

from Card import Card
from Match import Match
from PIL import Image

FILENAME = "card_database.txt"
HEADER_SIZE = 11
LEGAL_COMMANDS = ("r", "a", "d", ".", "m", "s", "b") # m for meme
COLOURS = ("r", "o", "y", "g", "b", "p")
ELEMENTS = ("f", "w", "s")
POWERED = ("n", "y")
EFFECTS = ('na', 'df', 'dw', 'ds', 'dr', 'do', 'dy', 'dg', 'db', 'dp', 'dmr', 'dmo', 'dmy', 'dmg', 'dmb', 'dmp', 'fs', 'sw', 'wf', 'bf', 'bw', 'bs', 'pt', 'mt', 'pr')


DATABASE_HEADER = """# id#, rank#, element, colour, is-power-card, side-effect\n# colours = {"r": (0, "red"), "o": (1, "orange"), "y": (2, "yellow"), "g": (3, "green"), "b": (4, "blue"), "p": (5, "purple")}\n# elements = {"f": (0, "fire"), "w": (1, "water"), "s": (2, "snow")}\n# power = {"n": (False, "not powered"), "y": (True, "powered")}\n# side_effect = {"na": (0, "no effect"), "df": (1, "discard fire"), "dw": (2, "discard water"), "ds": (3, "discard snow"),\n                 "dr": (4, "discard red"), "do": (5, "discard orange"), "dy": (6, "discard yellow"),\n                 "dg": (7, "discard green"), "db": (8, "discard blue"), "dp": (9, "discard purple"),\n                 "fs": (10, "fire to snow"), "sw": (11, "snow to water"), "wf": (12, "water to fire"),\n                 "bf": (13, "block fire"), "bw": (14, "block water"), "bs": (15, "block snow")}\n------------------------------------------------------------\n"""


def read_database():
    """Prints out contents of the database."""
    print("Accessing database!")
    file = open(FILENAME, "r")

    contents = file.read().splitlines()
    cards = []
    ranks = []

    if len(contents) > HEADER_SIZE:
        for i in range(HEADER_SIZE, len(contents)):
            try:
                line_list = contents[i].split(',')
                rank, value, element, colour, powered, effect, name = line_list
                aCard = Card(name, rank, value, element, colour, powered, effect)

                if not (aCard.verify_card(aCard.rank, aCard.value, aCard.element, aCard.colour, aCard.powered, aCard.effect)):
                    print("Invalid card!")
                elif aCard.get_rank() in ranks:
                    print(f"Rank '{aCard.rank}' is already taken.")
                    # Handle this by writing them out of the file
                else:
                    cards.append(aCard)
                    ranks.append(int(aCard.rank))
                    print(aCard)
            except ValueError:
                if i == HEADER_SIZE:
                    print("Nothing in database...")
                else:
                    print("Invalid card...")
            
    
    else:
        print("Nothing is in database!")

    file.close()
    return cards, ranks


def append_database(cards, ranks):
    """Appends Card-Jitsu card data to the database!"""
    append_details_message = f"Enter card details in a string with no spaces in order of: (rank),(colour),(element),(is powered),(symbol of effect),(name)\nEffects are: {EFFECTS}, enter <.> to exit:\n"
    file = open(FILENAME, "a+")

    input_str = input(append_details_message)
    while input_str != LEGAL_COMMANDS[3]:
        input_list = list(input_str)
        print(input_list)
        while len(input_list) <= 5 and input_str != '.':
            input(append_details_message)
            input_list = list(input_str)
            print(input_list)
            if input_str == LEGAL_COMMANDS[3]:
                exit_program()

        try:
            valid = True
            cursor1 = input_list.index('.')
            
            rank = int(''.join(input_list[0:cursor1]))
            
            cursor2 = cursor1+1
            while input_list[cursor2].isnumeric():
                cursor2 += 1
            
            cursor3 = cursor2+6
            while input_list[cursor3] != '.':
                cursor3 += 1

            value = int(''.join(input_list[cursor1+1:cursor2]))

            element = input_list[1+cursor2-1]
            colour = input_list[2+cursor2-1]
            powered = input_list[3+cursor2-1]
            effect = ''.join(input_list[4+cursor2-1:cursor3])
            name = ''.join(input_list[cursor3+1:])
            print(f"Create card '{name}' of:\nRank = {rank}\nValue = {value}\nElement = {element}\nColour = {colour}\nPower = {powered}\nEffect = {effect}")

            aCard = Card(name, rank, value, element, colour, powered, effect)
            print(aCard)

            for card in cards:
                if aCard.check_card_overlap(card):
                    valid = False
                    break

            if valid:
                aCard_strline = f"{aCard.rank},{aCard.value},{aCard.element},{aCard.colour},{aCard.powered},{aCard.effect}, {aCard.name}\n"
                file.write(aCard_strline)
                print("Card appended to database!\n")
        except ValueError():
            exit_program()

        input_str = input(append_details_message)
    
    file.close()
    return None


def delete_database(file, cards, ranks, rank):
    """Deletes a card from the database."""
    if rank in ranks:
        index = int(ranks.index(rank))
        print(f"Found card: {cards[index]}")
        cards.pop(index)
        
        file = open(FILENAME, 'w')
        file.write(DATABASE_HEADER)
        file.close()
        file = open(FILENAME, "a")
        for card in cards:
            card_strline = f"{card.rank},{card.value},{card.element},{card.colour},{card.powered},{card.effect},{card.name}\n"
            file.write(card_strline)
        file.close()
    return None


def search_database_by_element(cards, element_tally):
    """Tally up them elements!"""
    for card in cards:
        element_tally[card.element] += 1
    return None


def get_card_index(rank, cards):
    """Finds a card based on its rank."""
    index = 0
    for index, card in enumerate(cards):
        if card.rank == rank:
            return index
    return None


def generate_image_preview(cards):
    """Generate a preview!"""
    the_int = int(input(f"Choose a number between 1 and {cards[-1].rank}:\n"))        
    index = get_card_index(the_int, cards)
    if index is not None:
        the_int = cards[index].rank

        print(f"Chose {the_int} as the number!")
        the_str = str(the_int)
        while len(the_str) < 3:
            the_str = "0" + the_str
            print("Adding a 0...")
        the_path = "_collated/card_"+the_str+".png"
        print(f"Showing '{the_path}' as:\n{cards[index]}")
        im = Image.open(the_path)
        im.show()
    else:
        print("Couln't find card...")


def match_cards(cards):
    """Simulate an actual Card-Jitsu battle!"""
    card1 = cards[get_card_index(int(input(f"Enter the rank of the first card to match: (<={cards[-1].rank})\n")), cards)]
    card2 = cards[get_card_index(int(input(f"Enter the rank of the second card to match: (<={cards[-1].rank})\n")), cards)]
    match_result = card1.match_two_cards(card2)
    if match_result == Match.WIN:
        print(f"Card '{card1.name}' wins against Card '{card2.name}'! ({card1.element}{card1.value} vs {card2.element}{card2.value})")
    if match_result == Match.LOSS:
        print(f"Card '{card1.name}' loses against Card '{card2.name}'... ({card1.element}{card1.value} vs {card2.element}{card2.value})")
    if match_result == Match.DRAW:
        print(f"Card '{card1.name}' draws with Card '{card2.name}'. ({card1.element}{card1.value} vs {card2.element}{card2.value})")
    return None


def reorder_contents(file, cards):
    """Reorders the file's contents."""
    file = open(FILENAME, "w")
    file.write(DATABASE_HEADER)

    if len(cards) > 0:
        cards = sorted(cards, key=lambda card: card.get_rank())
        file.mode = "a"
        for card in cards:
            card_strline = f"{card.rank},{card.value},{card.element},{card.colour},{card.powered},{card.effect},{card.name}\n"
            file.write(card_strline)
    return None


def exit_program(file):
    """Closes the program, and the file."""
    file.close()
    exit()


def start_program():
    """Executes program, asks whether to read or write."""
    command_message = "Read from <r>, append to <a>, delete from <d>, <s> to line cards in order, or exit <.> the database? (<m> for memes, <b> to match cards)\n"
    file = open(FILENAME, "r")
    cards, ranks = read_database()
    element_tally = {"f": 0, "w": 0, "s": 0}
    search_database_by_element(cards, element_tally)
    print(f"There are {len(cards)} cards to choose from!\nThere are {element_tally['f']} fire cards, {element_tally['w']} water cards, and {element_tally['s']} snow cards.")

    command = input(command_message)
    # command = "w" # default command is write
    while 1 != 0:
        while command not in LEGAL_COMMANDS:
            command = input(command_message)
        
        if command == LEGAL_COMMANDS[0]: # Read from database
            print("Selected: read from database...")
            cards = read_database()
            if len(cards) == 0:
                exit_program()
        
        elif command == LEGAL_COMMANDS[1]: # Append to database
            print("Selected: append to database...")
            append_database(cards, ranks)
            cards, ranks = read_database()
            reorder_contents(file, cards)
            cards, ranks = read_database()
        
        elif command == LEGAL_COMMANDS[2]: # Delete from database
            print("Selected: deleting data from database...")
            input_rank = int(input("What is the rank of the card you want to delete?\n"))
            delete_database(file, cards, ranks, input_rank)
            reorder_contents(file, cards)
            cards, ranks = read_database()
            reorder_contents(file, cards)
            cards, ranks = read_database()
        
        elif command == LEGAL_COMMANDS[3]: # Exit
            print("Exiting program...")
            exit_program(file)
        
        elif command == LEGAL_COMMANDS[4]: # For fun
            print("Generating an image..?")
            generate_image_preview(cards)
        
        elif command == LEGAL_COMMANDS[5]: # Reorder
            print("Reordering the database...")
            reorder_contents(file, cards)
        
        elif command == LEGAL_COMMANDS[6]:
            print("Matching two cards...")
            match_cards(cards)
        
        command = input(command_message)


def extract_from_csv(filename, powered_bool):
    """Extracts data from fandom (finally, the website is useful)."""
    csv_elements = {"Fire": "f", "Water": "w", "Snow": "s"}
    csv_effect_phrases = {"CJ Discard Red Card (opponent)": "dr",
                          "CJ Discard Orange Card (opponent)": "do",
                          "CJ Discard Yellow Card (opponent)": "dy",
                          "CJ Discard Green Card (opponent)": "dg",
                          "CJ Discard Blue Card (opponent)": "db",
                          "CJ Discard Purple Card (opponent)": "dp",
                          "CJ Discard Red Cards (opponent)": "dmr",
                          "CJ Discard Orange Cards (opponent)": "dmo",
                          "CJ Discard Yellow Cards (opponent)": "dmy",
                          "CJ Discard Green Cards (opponent)": "dmg",
                          "CJ Discard Blue Cards (opponent)": "dmb",
                          "CJ Discard Purple Cards (opponent)": "dmp",
                          "CJ Block Fire (opponent)": "bf",
                          "CJ Block Water (opponent)": "bw",
                          "CJ Block Snow (opponent)": "bs",
                          "CJ Discard Fire (opponent)": "df",
                          "CJ Discard Water (opponent)": "dw",
                          "CJ Discard Snow (opponent)": "ds",
                          "CJ Change Fire to Snow (both players)": "fs",
                          "CJ Change Snow to Water (both players)": "sw",
                          "CJ Change Water to Fire (both players)": "wf",
                          "CJ Power Reversal (both players)": "pr",
                          "CJ +2 Power (user)": "pt",
                          "CJ -2 Power (opponent)": "mt"}


    file = open(filename, "r")
    for line in file.read().splitlines()[1:]:
        line = line.split(',')
        rank = int(line[0])
        value = int(''.join(list(line[5])[8:]))
        element = csv_elements[line[4]]
        colour = line[6].lower()[0]
        if powered_bool:
            powered = "y"
        else:
            powered = "n"
        if powered_bool == False:
            effect = "na"
        else:
            effect = line[7]
            if effect in csv_effect_phrases:
                effect = csv_effect_phrases[line[7]]
                
        name = line[1].title()

        format = f"{rank},{value},{element},{colour},{powered},{effect},{name}"
        print(format)


def main():
    """Main function."""
    start_program()


main()