"""
Authored by AllAcacia, on 14/10/2024 (dd/mm/yyyy)
file_rename_1.py | Used to bulk rename files, but with a non-breaking sequence number suffix (1, 2, 3, 4, ...).
"""

from os import rename, listdir, getcwd

# prefix = "Card-Jitsu_Cards_full_"
desired_prefix = "card_"
expected_prefix = "Card-Jitsu_Cards_full_"
directory = "non-power - Copy"

fnames = listdir(directory)

def bulk_rename_prefix(do_rename=False):
    idno_int = 1
    for fname in fnames:
        idno_str = str(idno_int)
        while len(idno_str) < 3:
            idno_str = '0' + idno_str
        
        # while idno[0] == '0':
        #     idno = idno[1:]
        
        new_fname = desired_prefix + idno_str + '.png'
        # print(fname + ', ' + new_fname)
        print(new_fname)
        if do_rename:
            rename(directory+'/'+fname, directory+'/'+new_fname)
        
        idno_int += 1

def main():
    bulk_rename_prefix(True)

main()