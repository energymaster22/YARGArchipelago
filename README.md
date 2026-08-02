This is an Archipelago implementation for the open source, plastic band rhythm game, YARG!

# Setup
1. Download the YARC Launcher from https://yarg.in/
2. Inside the YARC Launcher download "YARG Nightly" and the "YARG Official Setlist"
3. Download the YARGAPClient from https://github.com/energymaster22/YARGAPClient/releases/latest
4. Download Archipelago from https://github.com/ArchipelagoMW/Archipelago/releases/latest
5. Set up Archipelago
6. Download the YARG.apworld from https://github.com/energymaster22/YARGArchipelago/releases/latest
7. Double click yarg.apworld to install it into Archipelago
8. Select "Generate Template Options" from within Archipelago to get a default YAML
9. Edit YARG.yaml to your liking and put it in your "Players" folder (should be one folder up from the "Templates" folder the previous step opened)
10. Select "Generate" from within Archipelago
11. Host your outputed multiworld either on https://archipelago.gg/ or locally
> [!NOTE]
> ## Mac Users
> You will have to perform some extra steps to make the YARGAPClient launch.
> 1. Navigate to the `YARGAPClient_x.y.z_Mac` folder where the YARGAPClient is downloaded
> 2. Right click on the `YARGAPClient_x.y.z_Mac` folder
> 3. Select `New Terminal at Folder`
> - This may be under a `Services` Sub Menu
> 4. Run the following commands in the terminal
> ```
> xattr -cr ~/YARG*
> chmod -R +x ~/YARG*
> ```
> 5. Drag the `YARGAPClient_x.y.z_Mac` Application to the `Applications` folder
> 
> Thank you to vast2 and dengr1065 for figuring out how to get the Mac version running!
12. Launch the YARGAPClient
13. Click "Archipelago" on the main menu to open the login screen
14. Input the host address, port and slot name and press connect! (Game ID should be left blank if not playing on a fork) (Leave blank if unsure)

# Gameplay
1. Your goal in YARG AP is to find and complete your goal song!
2. The goal song may or may not be known depending on yaml settings.
3. Go into "Quickplay"
4. All of your collected songs will appear at the top in an "AP Songs" catagory
5. Play the songs that appear there to get checks for your multiworld!
6. When you get your goal song it will appear in an "AP Goal Song" catagory along with details on what you still need.
7. Collect the rest of the YARG Gems in the multiworld to fully unlock the goal song.
7. Play that song to finish the seed!

# Instrument Shuffle
This mode shuffles the various instruments into the multiworld, and ties each song to one of said instruments.

## Changes from normal gameplay:

+ The "AP Songs" catagory will be split into multiple categories, seperated by instrument.
+ The instrument named in the catagory will be listed in red if you are still missing it and will turn green when you recieve it.
+ You will always start with one song and it's connected instrument.
+ To send a check, you need to:
  + Have the song from the multiworld.
  + Have the instrument item from the multiworld.
  + Have the required instrument in your band while playing. (Multiplayer does work for this!)
+ The above also apply to your goal song, in addition to any "YARG Gem" requirement.
 
## Instrument Shuffle YAML Option Notes

+ You need at least 2 instruments selected to enable instrument shuffle.
+ If you do not select 2 or more, the mode will automatically disable at generation, regardless of instrument shuffle's setting.
+ Make sure your enabled setlists have a decent amount of songs that contain your instruments of choice.
+ Generation will check for at least 2 compatible songs for each instrument.
+ It is recommended to have more compatible songs to ensure successful generation.
  + "Failed generation" in this context will be an option error before proper AP gen.

# Current Notes
"Star Power Bonus" items grant 25% Star Power upon collection\
\
If a song does not support your current instrument, or you otherwise cannot complete the song, you can use a bot player to clear it

# Common Problems
## My songs are not loading!

+ This can be caused by a few things. First make sure that you have downloaded the setlists from the YARC launcher.

+ Sometimes YARG needs to rescan of your library, to do so, go to Settings> Songs and click "Scan songs" up at the top

+ Other times YARG forks do not find the YARC setlists automatically. This is a slightly more involved fix:

1. Open the YARC Launcher
2. Scroll all the way down the left panel
3. Click the Settings button on the bottom left
4. Note the directory under "File Management"
5. In the YARGAPClient go to Settings> Songs
6. Click "Add New Folder" 
7. Click "Browse" on the new entry
8. Navigate to the folder you saw in the YARC Launcher settings
9. Within the YARC install folder selct the "Setlists" folder
10. Click "Scan Songs"
