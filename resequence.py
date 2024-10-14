from os import rename, listdir, getcwd

dir_to_change = "non-power-format"
dir_to_follow = "non-power"

prefix_change = "0"
prefix_follow = "Card-Jitsu_Cards_full_"
prefix_wanted = "card_"

def resequence():
    if len(listdir(dir_to_change)) != len(listdir(dir_to_follow)):
        print(f"Reference directory has {len(listdir(dir_to_follow))} files compared to the changing one with {len(listdir(dir_to_change))}")
    dir_size = len(listdir(dir_to_change))
    print("Size of directories match!")

    fnames_follow = listdir(dir_to_follow)
    fnames_change = listdir(dir_to_change)
    for i in range(len(fnames_follow)):
        if fnames_change[i][0:len(prefix_change)] == prefix_change:
            fname = fnames_follow[i]
            # print(fnames_follow[i] + ', ' + listdir(dir_to_follow)[i])
            idno = fname[len(prefix_follow):-4]
            new_fname = prefix_wanted + idno + ".png"
            print(fnames_change[i] + ", " + new_fname)

            rename(dir_to_change+"/"+fnames_change[i], dir_to_change+"/"+new_fname)
        else:
            print("File does not conform to naming format!")

def main():
    resequence()

main()