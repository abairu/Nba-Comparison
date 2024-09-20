from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from tkinter import *
from tkinter import ttk


# The function that will run once the user clicks on the 'player1' button
def check_player1(*args):

    # This updates the window by removing the previous widgets in the area that we want our new information to be placed
    for button in mainframe.grid_slaves():
         if int(button.grid_info()["row"]) > 2 and int(button.grid_info()["column"]) < 3:
              button.grid_remove()


    # This will keep track of whether the string entered in our 'player1' entry is valid
    found = False
    unique = False
    id = 0
    # The 'player1' entry
    full_name = str(player1.get())
    # Calls the 'nba_api' module 'players', returns a list of dictionaries that contains 
    # a key with 'full_name' and various player information, and assigns it to variable 'x'
    x = players.find_players_by_full_name(full_name)

    # Variable to keep track of players with the same name.
    # I chose to use the duplicate players' 'player_id' to keep track of them because it is unique to every player
    duplicates_id = []

    # Search the players we found and store their 'player_id'
    if unique == False:
        for dictionary in x:
            if full_name.lower() == dictionary['full_name'].lower():
                    duplicates_id.append(dictionary['id'])
                    found = True

    if len(duplicates_id) == 1:
         unique = True
         id = duplicates_id[0]

    if len(args) > 0:
         unique = True
         id = args[0]

    # If the player name is unique, go straight to displaying their stats            
    if unique == True:
        found = True
        valid_player1.set('')
        player1_id = id
        categories = ['PTS', 'AST', 'BLK', 'STL', 'REB', 'FG_PCT', 'FG3_PCT', 'FT_PCT']
        curr_row = 3
        curr_col = 1

        # Search through the stats we want to grab from 'nba_api'
        for c in categories:
            ttk.Label(mainframe, text = c).grid(column=curr_col, row=curr_row, sticky=W)
            # Retrieve the career stat per game data frame, locate the series of values with label 'c', and get the value from the series
            career_stats = playercareerstats.PlayerCareerStats(per_mode36 = 'PerGame',player_id=player1_id).get_data_frames()[1].loc[:,c][0]
            
            career_avg = round(career_stats, 2)
             
                      
            ttk.Label(mainframe, text = str(career_avg)).grid(column=curr_col+1, row=curr_row, sticky=W)
            curr_row += 1
    # If there are players with the same name, display buttons of the players' unique 'player_id'
    else:
         valid_player1.set("There are multiple players with this name. Please choose one based on their player IDs below.")
         curr_row = 3
         for player_id in duplicates_id:
            # Clicking each duplicate player's button will execute the 'duplicate_player1' function with the 'player_id' parameter 
            ttk.Button(mainframe, text=player_id, command=lambda args=(player_id): check_player1(args)).grid(column=1, row=curr_row, sticky = W)


            curr_row+=1
    
         
    if found == False:
        valid_player1.set("Invalid entry. Please type the player's full name.")


# Same as 'check_player1', but for player2
def check_player2(*args):

    for button in mainframe.grid_slaves():
         if int(button.grid_info()["row"]) > 2 and int(button.grid_info()["column"]) >= 3:
              button.grid_remove()

    unique = False
    found = False
    id = 0

    full_name = str(player2.get())
    x = players.find_players_by_full_name(full_name)

    duplicates_id = []


    if unique == False:
        for dictionary in x:
            if full_name.lower() == dictionary['full_name'].lower():
                    duplicates_id.append(dictionary['id'])
                    found = True
    
    if len(duplicates_id) == 1:
         unique = True
         id = duplicates_id[0]

    if len(args) > 0:
         unique = True
         id = args[0]

    if unique == True:
        found = True
        valid_player2.set('')
        player2_id = id
        categories = ['PTS', 'AST', 'BLK', 'STL', 'REB', 'FG_PCT', 'FG3_PCT', 'FT_PCT']
        curr_row = 3
        curr_col = 3

        for c in categories:
            ttk.Label(mainframe, text = c).grid(column=curr_col, row=curr_row, sticky=W)
            career_stats = playercareerstats.PlayerCareerStats(per_mode36 = 'PerGame',player_id=player2_id).get_data_frames()[1].loc[:,c][0]
            
            career_avg = round(career_stats, 2)
             
                      
            ttk.Label(mainframe, text = str(career_avg)).grid(column=curr_col+1, row=curr_row, sticky=W)
            curr_row += 1

    else:
         valid_player2.set("There are multiple players with this name. Please choose one based on their player IDs below.")
         curr_row = 3
         for player_id in duplicates_id:
            ttk.Button(mainframe, text=player_id, command=lambda args=(player_id): check_player2(args)).grid(column=3, row=curr_row, sticky = W)


            curr_row+=1
         
                
    if found == False:
        valid_player2.set("Invalid entry. Please type the player's full name.")
    
# The code below is responsible for creating and formatting the application's windows and widgets
root = Tk()
root.title("NBA Comparison")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

player1 = StringVar()
player1_id = 0
player1_entry = ttk.Entry(mainframe, width=7, textvariable=player1)
player1_entry.grid(column=1, row=1, sticky = (W, E))

player2 = StringVar()
player2_id = 0
player2_entry = ttk.Entry(mainframe, width=7, textvariable=player2)
player2_entry.grid(column=3, row=1, sticky = (W, E))


valid_player1 = StringVar()
valid_player2 = StringVar()
ttk.Label(mainframe, textvariable = valid_player1).grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, textvariable = valid_player2).grid(column=3, row=2, sticky=W)
     

ttk.Button(mainframe, text="player1", command=lambda: check_player1()).grid(column=2, row=1, sticky = W)
ttk.Button(mainframe, text="player2", command=lambda: check_player2()).grid(column=4, row=1, sticky = W)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

player1_entry.focus()


root.mainloop()


