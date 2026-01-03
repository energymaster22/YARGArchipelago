from typing import NamedTuple, Optional, Dict

class SongMeta(NamedTuple):
    """Contains difficulty information, Use None for unsupported intsruments"""

    group: str
    source: str
    guitar5F: Optional[int]
    bass5F: Optional[int]
    drums: Optional[int]
    drumsElite: Optional[int]
    keys5F: Optional[int]
    keysPro: Optional[int]
    vocals: Optional[int]
    harmony2: Optional[int]
    harmony3: Optional[int]
    rhythm5F: Optional[int]

Songs: Dict[str, SongMeta] = {
    "106": SongMeta("YARG Official Setlist", "yarg", 5, 4, 4, 4, None, None, 2, 2, 2, None),
    "1nput This 2 Y0ur Spine": SongMeta("YARG Official Setlist", "yarg", 6, 4, 6, 6, 6, 6, 0, None, None, None),
    "322": SongMeta("YARG Official Setlist", "yarg", 4, 4, 5, None, 3, 3, 0, None, None, None),
    "A Visitant (feat. Victor Borba)": SongMeta("YARG Official Setlist", "yarg", 3, 1, 5, None, 6, 6, 4, 4, None, None),
    "About the Author": SongMeta("YARG Official Setlist", "yarg", 3, 2, 2, None, 1, 1, 5, 5, 5, None),
    "The Afterparty": SongMeta("YARG Official Setlist", "yarg", 3, 1, 2, None, 2, 3, 3, 3, 3, None),
    "Al Gore Rhythm": SongMeta("YARG Official Setlist", "yarg", 5, 4, 5, None, None, None, 5, 5, 5, None),
    "Alibi": SongMeta("YARG Official Setlist", "yarg", 3, 3, 6, None, 0, 0, 4, 4, 4, None),
    "All of a Sudden": SongMeta("YARG Official Setlist", "yarg", 3, 3, 4, None, 2, 3, 1, 1, None, None),
    "Allure": SongMeta("YARG Official Setlist", "yarg", 5, 5, 6, None, 0, 0, 2, 2, 2, None),
    "Avatar the Last Cakebender": SongMeta("YARG Official Setlist", "yarg", 4, 3, 5, None, 4, 4, 4, 4, 4, None),
    "Avatara": SongMeta("YARG Official Setlist", "yarg", 2, 2, 4, 4, 2, 2, 0, 0, None, None),
    "Bathe in Blood": SongMeta("YARG Official Setlist", "yarg", 6, 2, 6, None, None, None, 0, None, None, None),
    "Bedroom Community": SongMeta("YARG Official Setlist", "yarg", 3, 3, 3, 3, 5, 5, 3, 3, 3, None),
    "Beverly": SongMeta("YARG Official Setlist", "yarg", 2, 2, 2, None, None, None, 2, 2, 2, None),
    "Blue (feat. Miori Celesta)": SongMeta("YARG Official Setlist", "yarg", 3, 5, 4, None, 5, 5, 5, 5, 5, None),
    "Boom Slayer (feat. Scott Foster Harris)": SongMeta("YARG Official Setlist", "yarg", 3, 3, 4, None, 2, 2, 3, 3, None, None),
    "Bottleneck": SongMeta("YARG Official Setlist", "yarg", 5, 5, 5, None, None, None, 3, 3, None, None),
    "Buds": SongMeta("YARG Official Setlist", "yarg", 2, 1, 2, None, None, None, 2, 2, 2, None),
    "Butterflies": SongMeta("YARG Official Setlist", "yarg", 3, 3, 4, 4, None, None, 1, 1, 1, None),
    "Choked Up": SongMeta("YARG Official Setlist", "yarg", 3, 1, 2, 2, 3, 4, 4, 4, 4, None),
    "Circles": SongMeta("YARG Official Setlist", "yarg", 3, 3, 3, None, 0, 0, 3, 3, 3, None),
    "Cowboy Tanaka": SongMeta("YARG Official Setlist", "yarg", 4, 3, 5, None, 5, 5, 4, 4, 4, None),
    "Cruisin'": SongMeta("YARG Official Setlist", "yarg", 5, 3, 4, None, 3, 3, None, None, None, None),
    "Discipline": SongMeta("YARG Official Setlist", "yarg", 3, 2, 2, 2, 2, 2, 3, 3, 3, None),
    "Do": SongMeta("YARG Official Setlist", "yarg", 3, 4, 5, None, 4, 4, 6, 6, None, None),
    "Don't Look!": SongMeta("YARG Official Setlist", "yarg", 2, 3, 4, None, 6, 6, 1, 1, 1, None),
    "Don't Spook the Owl": SongMeta("YARG Official Setlist", "yarg", 3, 3, 4, None, None, None, 4, 4, 4, None),
    "Dreamweaver": SongMeta("YARG Official Setlist", "yarg", 3, 3, 4, 4, None, None, 0, 0, 0, None),
    "Duvet Thief": SongMeta("YARG Official Setlist", "yarg", 2, 2, 4, None, 1, 2, 3, 3, 3, None),
    "Eleven": SongMeta("YARG Official Setlist", "yarg", 2, 2, 3, None, 0, 0, 2, 2, 2, None),
    "Emperor Rising": SongMeta("YARG Official Setlist", "yarg", 5, 5, 6, None, None, None, 4, 4, 4, None),
    "Empires": SongMeta("YARG Official Setlist", "yarg", 2, 1, 4, None, 4, 4, 4, 4, 4, None),
    "Everybody Do the Flop": SongMeta("YARG Official Setlist", "yarg", 4, 3, 5, None, 4, 4, 5, 5, 5, None),
    "Exeter": SongMeta("YARG Official Setlist", "yarg", 3, 4, 4, None, 0, 0, 2, 2, 2, None),
    "Fine": SongMeta("YARG Official Setlist", "yarg", 4, 2, 4, 4, 2, 2, 4, 4, 4, None),
    "Flight of the Bumblebee": SongMeta("YARG Official Setlist", "yarg", 6, 3, 6, None, None, None, None, None, None, None),
    "Formless Collective": SongMeta("YARG Official Setlist", "yarg", 6, 5, 8, None, None, None, 0, 0, 0, None),
    "Frank Scored a Video Game": SongMeta("YARG Official Setlist", "yarg", 6, 5, 5, None, None, None, None, None, None, None),
    "Front Row Seats (To Watching Your World Burn)": SongMeta("YARG Official Setlist", "yarg", 2, 2, 5, None, 1, 1, 3, 3, 3, None),
    "The Game": SongMeta("YARG Official Setlist", "yarg", 4, 2, 4, 4, 2, 2, 3, 3, 3, None),
    "God Only Knows (feat. Kasane Teto)": SongMeta("YARG Official Setlist", "yarg", 5, 5, 5, None, 4, 4, 3, 3, 3, None),
    "Guess I'll Never Know": SongMeta("YARG Official Setlist", "yarg", 1, 0, 3, None, 0, 0, 2, 2, 2, None),
    "Half Measures": SongMeta("YARG Official Setlist", "yarg", 0, 0, 1, None, 0, 1, 6, 6, 6, None),
    "I Don't Wanna Talk": SongMeta("YARG Official Setlist", "yarg", 3, 3, 3, None, 2, 2, 2, 2, 2, None),
    "I Wish That I Could Fall (feat. GUMI)": SongMeta("YARG Official Setlist", "yarg", 3, 5, 1, None, 5, 5, 5, 5, 5, None),
    "I'm a Bug": SongMeta("YARG Official Setlist", "yarg", 1, 1, 3, None, 5, 5, 2, 2, 2, None),
    "Igowallah": SongMeta("YARG Official Setlist", "yarg", 0, 2, 5, None, 0, 0, 4, 4, 4, None),
    "In My Head": SongMeta("YARG Official Setlist", "yarg", 1, 1, 2, None, None, None, 2, 2, 2, None),
    "Is This What You Wanted": SongMeta("YARG Official Setlist", "yarg", 4, 1, 2, None, 2, 2, 5, 5, 5, None),
    "It Kills Me": SongMeta("YARG Official Setlist", "yarg", 2, 2, 4, None, 1, 2, 3, 3, 3, None),
    "Jenny B": SongMeta("YARG Official Setlist", "yarg", 7, 4, 2, 2, None, None, 5, None, None, None),
    "John, Take Me with You": SongMeta("YARG Official Setlist", "yarg", 2, 2, 2, None, None, None, 2, 2, 2, None),
    "Join the Club": SongMeta("YARG Official Setlist", "yarg", 3, 2, 2, None, 3, 3, 3, 3, 3, None),
    "Languish": SongMeta("YARG Official Setlist", "yarg", 4, 3, 5, 5, 2, 2, 0, 0, 0, None),
    "Long in the Tooth": SongMeta("YARG Official Setlist", "yarg", 5, 3, 5, 5, 3, 3, 2, 2, 2, None),
    "Luminaire": SongMeta("YARG Official Setlist", "yarg", 3, 3, 7, None, 5, 5, None, None, None, None),
    "Marlboro Mountain": SongMeta("YARG Official Setlist", "yarg", 3, 3, 3, None, 0, 0, 3, 3, 3, None),
    "The Masquerade": SongMeta("YARG Official Setlist", "yarg", 4, 4, 4, None, 5, 5, 2, 2, 2, None),
    "Mass Gap": SongMeta("YARG Official Setlist", "yarg", 6, 6, 6, None, 6, 7, None, None, None, None),
    "Moonlight Sonata 3rd Mvt (Big Band Version)": SongMeta("YARG Official Setlist", "yarg", 3, 5, 7, None, 6, 6, None, None, None, None),
    "Need 2": SongMeta("YARG Official Setlist", "yarg", 3, 0, 0, None, 2, 2, 1, 1, 1, None),
    "The New World Disorder": SongMeta("YARG Official Setlist", "yarg", 7, 7, 6, 6, None, None, 3, 3, 3, None),
    "No Nations": SongMeta("YARG Official Setlist", "yarg", 0, 1, 0, None, 0, 0, 1, 1, 1, None),
    "No Remedy": SongMeta("YARG Official Setlist", "yarg", 1, 1, 3, None, 3, 3, 2, 2, 2, None),
    "Nomu": SongMeta("YARG Official Setlist", "yarg", 3, 2, 3, None, None, None, 5, 5, 5, None),
    "Numb the Mind": SongMeta("YARG Official Setlist", "yarg", 1, 0, 2, None, 0, 0, 2, None, None, None),
    "Oh, Krissy Baby!": SongMeta("YARG Official Setlist", "yarg", 3, 2, 2, None, 3, 3, 4, 4, 4, None),
    "Oopsie Daisy": SongMeta("YARG Official Setlist", "yarg", 1, 3, 2, None, 2, 2, 3, 3, 3, None),
    "Over Again": SongMeta("YARG Official Setlist", "yarg", 2, 1, 2, None, 1, 1, 5, 5, 5, None),
    "Overdrive": SongMeta("YARG Official Setlist", "yarg", 3, 2, 3, None, None, None, 3, None, None, None),
    "Oxygen": SongMeta("YARG Official Setlist", "yarg", 2, 1, 2, None, 2, 2, 2, 2, 2, None),
    "Participation Trophy Wife": SongMeta("YARG Official Setlist", "yarg", 4, 3, 3, None, None, None, 3, 3, None, None),
    "Pixel Galaxy": SongMeta("YARG Official Setlist", "yarg", 6, 2, 4, None, 3, 3, None, None, None, None),
    "Pizza Rolls": SongMeta("YARG Official Setlist", "yarg", 5, 1, 2, 2, None, None, 2, 2, 2, None),
    "Plastic Boogie": SongMeta("YARG Official Setlist", "yarg", 3, 3, 1, None, 1, 1, 2, 2, 2, None),
    "Poser": SongMeta("YARG Official Setlist", "yarg", 4, 3, 3, None, None, None, 4, 4, 4, None),
    "Positively Clark Street": SongMeta("YARG Official Setlist", "yarg", 4, 2, 2, None, 2, 2, 4, 4, 4, None),
    "Queen of the Night": SongMeta("YARG Official Setlist", "yarg", 3, 4, 3, None, 3, 3, 4, 4, 4, None),
    "Runnin Man": SongMeta("YARG Official Setlist", "yarg", 3, 3, 5, 5, None, None, 0, 0, 0, None),
    "Sadness (feat. Sapphire Noel)": SongMeta("YARG Official Setlist", "yarg", 2, 2, 5, None, 2, 2, 2, 2, None, None),
    "Seasons (feat. Shiki Miyoshino)": SongMeta("YARG Official Setlist", "yarg", 2, 1, 0, None, 1, 2, 3, 3, None, None),
    "Show Ya": SongMeta("YARG Official Setlist", "yarg", 2, 0, 2, None, 2, 2, 3, 3, 3, None),
    "Smile for Me": SongMeta("YARG Official Setlist", "yarg", 4, 2, 4, None, None, None, 3, 3, 3, None),
    "Song of November": SongMeta("YARG Official Setlist", "yarg", 4, 4, 4, None, 1, 1, 3, 3, 3, None),
    "Spirit": SongMeta("YARG Official Setlist", "yarg", 2, 1, 1, None, 2, 2, 3, 3, 3, None),
    "Splinter": SongMeta("YARG Official Setlist", "yarg", 2, 0, 1, None, 2, 3, 3, 3, 3, None),
    "Stowaway Ants": SongMeta("YARG Official Setlist", "yarg", 3, 2, 4, None, 4, 4, 3, 3, 3, None),
    "Strangers Once Again (feat. Treb and Ofir Tabakov)": SongMeta("YARG Official Setlist", "yarg", 4, 3, 6, None, 4, 6, 5, 5, 5, None),
    "Sweet Victory": SongMeta("YARG Official Setlist", "yarg", 3, 1, 2, None, 3, 3, 3, 3, 3, None),
    "Synthespian": SongMeta("YARG Official Setlist", "yarg", 5, 5, 6, None, None, None, 2, 2, None, None),
    "They Call": SongMeta("YARG Official Setlist", "yarg", 4, 4, 4, None, None, None, 2, 2, 2, None),
    "Time": SongMeta("YARG Official Setlist", "yarg", 3, 2, 4, 4, 0, 0, 3, 3, 3, None),
    "To Let Go": SongMeta("YARG Official Setlist", "yarg", 3, 3, 4, None, 1, 1, 4, 4, 4, None),
    "Vehemence": SongMeta("YARG Official Setlist", "yarg", 6, 4, 6, None, None, None, None, None, None, None),
    "Voidwalker": SongMeta("YARG Official Setlist", "yarg", 4, 3, 5, None, 0, 0, 0, 0, 0, None),
    "We All Float Down Here": SongMeta("YARG Official Setlist", "yarg", 6, 4, 5, None, None, None, 2, 2, None, None),
    "Burn": SongMeta("Assorted Rock 1", "yarg dlc", 1, 0, 1, None, None, None, 1, 1, 1, None),
    "Dunken Monday (Freeway Mix)": SongMeta("Assorted Rock 1", "yarg dlc", 3, 2, 1, 2, None, None, 3, 3, 3, 3),
    "Middle of the City Road": SongMeta("Assorted Rock 1", "yarg dlc", 3, 3, 2, 2, 1, 1, None, None, None, 1),
    "Moonlight": SongMeta("Assorted Rock 1", "yarg dlc", 2, 0, None, None, 1, 1, 1, None, None, None),
    "Rock Thing": SongMeta("Assorted Rock 1", "yarg dlc", 3, 1, 3, None, 4, 4, None, None, None, None),
    "Simplicity": SongMeta("Assorted Rock 1", "yarg dlc", 1, 0, 1, None, 2, 2, None, None, None, None),
    "Turtleneck": SongMeta("Assorted Rock 1", "yarg dlc", 3, 1, 3, None, 2, 2, None, None, None, None),
    "By the Seaside (feat. Kitsui Akira)": SongMeta("Assorted Electronic 1", "yarg dlc", 3, 1, 6, None, 3, 3, 3, 3, None, None),
    "Feel Good": SongMeta("Assorted Electronic 1", "yarg dlc", 2, 1, 1, None, 2, 3, 2, 2, None, None),
    "Ghost": SongMeta("Assorted Electronic 1", "yarg dlc", 3, 1, 2, None, 2, 2, 4, 4, None, None),
    "Radioactive": SongMeta("Assorted Electronic 1", "yarg dlc", 2, 6, 5, 5, 4, 5, 0, None, None, 2),
    "Rot for Clout (feat. Kasane Teto)": SongMeta("Assorted Electronic 1", "yarg dlc", 3, 4, 4, None, 4, 5, 6, 6, None, 3),
    "Say It Back": SongMeta("Assorted Electronic 1", "yarg dlc", 4, 2, 4, None, 4, 5, 5, 5, None, None),
    "Space and Time! (feat. Jelly Hoshiumi)": SongMeta("Assorted Electronic 1", "yarg dlc", 7, 2, 0, None, 4, 5, 3, 3, 3, None),
    "Angel in Disguise (feat. Kitsui Akira)": SongMeta("SUMMERTIDE", "yarg dlc", 2, 2, 2, None, 3, 3, 5, 5, None, None),
    "Cinnamon (feat. Miori Celesta and Yuuna Nini)": SongMeta("SUMMERTIDE", "yarg dlc", 2, 1, 3, None, 2, 2, 6, 6, 6, None),
    "Embrace (feat. Kiyon)": SongMeta("SUMMERTIDE", "yarg dlc", 5, 3, 2, None, 3, 3, 4, 4, 4, 4),
    "Heart of Glass (feat. Rachie)": SongMeta("SUMMERTIDE", "yarg dlc", 2, 3, 4, None, 3, 3, 6, 6, None, None),
    "Hopeless Romantic (feat. JubyPhonic)": SongMeta("SUMMERTIDE", "yarg dlc", 0, 0, 2, None, 2, 3, 3, 3, 3, None),
    "Love Me Not (feat. Tofie)": SongMeta("SUMMERTIDE", "yarg dlc", 4, 0, 1, None, 2, 2, 4, 4, 4, None),
    "Magazines (feat. Nia Suzune)": SongMeta("SUMMERTIDE", "yarg dlc", 3, 2, 2, None, 1, 3, 5, 5, 5, None),
    "One Step at a Time (feat. Miori Celesta)": SongMeta("SUMMERTIDE", "yarg dlc", 3, 2, 3, None, 2, 2, 3, 3, 3, 6),
    "Rose (feat. Ember Amane)": SongMeta("SUMMERTIDE", "yarg dlc", 2, 1, 1, None, 2, 2, 3, 3, 3, None),
    "Through the Night (feat. Yuuka Bear)": SongMeta("SUMMERTIDE", "yarg dlc", 5, 4, 2, None, 2, 2, 4, 4, 4, 4)
}

#Example on using the Songs Dictionary
#
#for name, data in Songs.items():
#    print("Song Name: " + name)
#    print("5 Fret Guitar Diff: " + str(data.guitar5F))
#    print("5 Fret Bass Diff: " + str(data.bass5F))
#
#If you want to use the Songs Dict in other file add to top of file
#
#from .songinfo import Songs
    
    