"""
Authored by AllAcacia, on 14/10/2024 (dd/mm/yyyy)
file_rename_1.py | Used to bulk rename files. Swaps out the prefixes.
"""

from os import rename, listdir, getcwd

# prefix = "Card-Jitsu_Cards_full_"
desired_prefix = "Card-Jitsu_Cards_full_"
expected_prefix = "card_"
directory = "power"

fnames = listdir(directory)

def bulk_rename_prefix(do_rename=False):
    for fname in fnames:
        idno = str(fname[len(expected_prefix):-4])
        while len(idno) < 3:
            idno = '0' + str(idno)
        
        # while idno[0] == '0':
        #     idno = idno[1:]
        
        new_fname = desired_prefix + idno + '.png'
        # print(fname + ', ' + new_fname)
        print(new_fname)
        if do_rename:
            # rename(directory+'/'+fname, directory+'/'+new_fname)

def main():
    bulk_rename_prefix(False)