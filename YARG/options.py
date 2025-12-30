from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Range

from .songinfo import Songs

class TotalSongs(Range):
    """
    The total amount of songs in the multiworld.
    """

    display_name = "Total Songs"

    range_start = 5
    range_end = len(Songs)

    default = 10

class PercentOfGemsRequired(Range):
    """
    Percent of YARG Gems required to get the items from your goal song.
    """

    display_name = "Percent of Gems Required"

    range_start = 0
    range_end = 100

    default = 80

@dataclass
class YARGOptions(PerGameCommonOptions):
    total_songs: TotalSongs
    percent_of_gems_required: PercentOfGemsRequired

option_groups = [
    OptionGroup(
        "Song Selection Options",
        [TotalSongs, PercentOfGemsRequired],
    ),
]