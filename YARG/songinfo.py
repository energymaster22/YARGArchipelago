from typing import NamedTuple, Optional, Dict

class SongMeta(NamedTuple):
    """Contains difficulty information, Use None for unsupported intsruments"""

    guitar5F: Optional[int]
    bass5F: Optional[int]
    drums: Optional[int]
    drumsElite: Optional[int]
    keys5F: Optional[int]
    keysPro: Optional[int]
    vocals: Optional[int]
    harmony2: Optional[int]
    harmony3: Optional[int]

Songs: Dict[str, SongMeta] = {
    "106": SongMeta(5, 4, 4, 4, None, None, 2, 2, 2),
    "1nput This 2 Y0ur Spine": SongMeta(6, 4, 6, 6, 6, 6, 0, None, None),
    "322": SongMeta(4, 4, 5, None, 3, 3, 0, None, None),
    "A Visitant (feat. Victor Borba)": SongMeta(3, 1, 5, None, 6, 6, 4, 4, None),
    "About the Author": SongMeta(3, 2, 2, None, 1, 1, 5, 5, 5)
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
#from songinfo import Songs
    
    