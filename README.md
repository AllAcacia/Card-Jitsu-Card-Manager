# Card-Jitsu-Card-Manager, author: AllAcacia (https://github.com/AllAcacia/)
Contains files that allows you to create Card-Jitsu cards. Instructions on how to use may not help, as features were developed on my needs. Download images here: (https://clubpenguin.fandom.com/wiki/List_of_Regular_Card-Jitsu_Cards_(series_1-4)), here: (https://clubpenguin.fandom.com/wiki/List_of_Regular_Card-Jitsu_Cards_(series_5-8)), and here: (https://clubpenguin.fandom.com/wiki/List_of_Card-Jitsu_Power_Cards). I won't be providing these images as I am concerned about copyright issues.

![alt text](https://github.com/AllAcacia/Card-Jitsu-Card-Manager/blob/main/page-img-1.png "Preview 1")

## access_database.py
Accesses "card_database.txt", which I have prefilled with all of the Club Penguin Card-Jitsu cards, with their details denoting: (rank, value, colour, element, power status, effect). 
### Appending
Entering "a" will append a new card where you then enter a string "x.yabcd.v", where x=rank (id) (>1), y=value (2-12), a=element (f/w/s), b=colour (roygbp), c=power status (y/n), v=card name (string can be as long as you want). This will then be appended to "card_database.txt", and will be sifted in to the appropriate line.
### Deleting
Entering "d" will prompt you to enter a rank number, and the corresponding card data will be taken out of "card_database.txt".
### Image Preview
Entering "m", then a number between 1 and the number of cards you have will grab that specific card. May rework so it grabs it based on the rank number. 

I have provided "file_rename.py" to bulk rename file prefixes in a directory. I have also provided "fil_rename_1.py" which bulk renames file suffixes to a non-breaking sequence (1, 2, 3, ...), instead of (2, 5, 12, ...). These functions are intended to be used when you bulk download the corresponding image files, and the variables may need to be left up to you to set to function properly. You can use the ".blend" files to go through all of the images and crop/mask them so they are all graphically consistent (there is one for non-power cards, and one for power cards as they are different sizes), the colour settings should be fine, and compression is 100% with minimal quality decrease.
### Exiting Program
You can exit the program by entering "." on the main terminal.
