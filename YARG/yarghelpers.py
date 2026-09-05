def instnamechange(input):
    #Swaps between the 2 formats of intsrument names
    if input == "guitar5F":
        return "Guitar"
    if input == "bass5F":
        return "Bass"
    if input == "rhythm5F":
        return "Rhythm"
    if input == "coop5F":
        return "Co-op Guitar"
    if input == "drums":
        return "Drums"
    if input == "keys5F":
        return "Keys"
    if input == "keysPro":
        return "Pro Keys"
    if input == "vocals":
        return "Vocals"
    if input == "harmony2":
        return "2 Part Harmony"
    if input == "harmony3":
        return "3 Part Harmony"
    if input == "guitar6F":
        return "6 Fret Guitar"
    if input == "bass6F":
        return "6 Fret Bass"
    if input == "rhythm6F":
        return "6 Fret Rhythm"
    if input == "coop6F":
        return "6 Fret Co-op Guitar"
    
    
    if input == "Guitar":
        return "guitar5F"
    if input == "Bass":
        return "bass5f"
    if input == "Rhythm":
        return "rhythm5F"
    if input == "Co-op Guitar":
        return "coop5F"
    if input == "Drums":
        return "drums"
    if input == "Keys":
        return "keys5F"
    if input == "Pro Keys":
        return "keysPro"
    if input == "Vocals":
        return "vocals"
    if input == "2 Part Harmony":
        return "harmony2"
    if input == "3 Part Harmony":
        return "harmony3"
    if input == "6 Fret Guitar":
        return "guitar6F"
    if input == "6 Fret Bass":
        return "bass6F"
    if input == "6 Fret Rhythm":
        return "rhythm6F"
    if input == "6 Fret Co-op Guitar":
        return "coop6F"

def itemnamefromindex(index):
    from .songinfo import Songs
    longnames = False

    if longnames == False:
        return f'"{(Songs.get(index)).songname}" by {(Songs.get(index)).artistname}'

    if longnames == True:
        return f'"{(Songs.get(index)).songname}" by {(Songs.get(index)).artistname} from {(Songs.get(index)).source}'