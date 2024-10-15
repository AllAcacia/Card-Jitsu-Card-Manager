"""
Authored by AllAcacia on 15/10/2024 (dd/mm/yyyy)
match.py | "match" class file, contains definitions of a match's outcome.
Intended to be used for in-game logic too, implemented as needed.
"""

from enum import Enum

Match = Enum('Match', ['WIN', 'LOSS', 'DRAW'])