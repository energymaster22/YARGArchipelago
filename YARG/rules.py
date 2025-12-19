from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from .songinfo import Songs

if TYPE_CHECKING:
    from .world import YARGWorld


def set_all_rules(world: YARGWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_location_rules(world: YARGWorld) -> None:
    # Location rules work no differently from Entrance rules.
    # Most of our locations are chests that can simply be opened by walking up to them.
    # Thus, their logical requirements are covered by the Entrance rules of the Entrances that were required to
    # reach the region that the chest sits in.
    # However, our two enemies work differently.
    # Entering the room with the enemy is not enough, you also need to have enough combat items to be able to defeat it.
    # So, we need to set requirements on the Locations themselves.
    # Since combat is a bit more complicated, we'll use this chance to cover some advanced access rule concepts.

    # Sometimes, you may want to have different rules depending on the player's chosen options.
    # There is a wrong way to do this, and a right way to do this. Let's do the wrong way first.
    
    for name in Songs.keys():
        location1 = world.get_location("\"" + str(name) + "\" Item 1")
        location2 = world.get_location("\"" + str(name) + "\" Item 2")
        item = str(name)
        set_rule(location1, lambda state, x=item: state.has(x, world.player))
        
        set_rule(location2, lambda state, x=item: state.has(x, world.player))


def set_completion_condition(world: YARGWorld) -> None:
    
    world.multiworld.completion_condition[world.player] = lambda state: state.has("1nput This 2 Y0ur Spine", world.player)
