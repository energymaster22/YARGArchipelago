from collections.abc import Mapping
from typing import Any
from BaseClasses import Region, MultiWorld

from worlds.AutoWorld import World

from . import items, locations, options, regions, rules, web_world

from .songinfo import Songs

class YARG(World):
    """
    YARG is an Open-Source plastic band rhythm game! 
    Play through the YARG Official Setlist for the crowd,
    and maybe get some free items from your fans!
    """

    game = "YARG"

    web = web_world.YARGWebWorld()

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.goal_song = ""


    
    def generate_early(self) -> None:
        starting_song_index = self.random.randint(0,(len(Songs)))
        tempindex = self.random.randint(0,(len(Songs)))
        if tempindex == starting_song_index:
            if tempindex == 0:
                tempindex = tempindex + 1
            else:
                tempindex = tempindex - 1
        goal_song_index = tempindex
        songlist = list(Songs.keys())
        startingsong = self.create_item(str(songlist[starting_song_index]))
        self.push_precollected(startingsong)
        self.goal_song = str(songlist[goal_song_index])
        self.multiworld.completion_condition[self.player] = lambda state: state.has((songlist[goal_song_index]), self.player)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {}
        slot_data["Goal Song"] = self.goal_song

        return slot_data

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    def create_regions(self):
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.YARGItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)