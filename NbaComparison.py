from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
from tkinter import *
from tkinter import ttk



def check_player1(*args):
    for button in mainframe.grid_slaves():
         if int(button.grid_info()["row"]) > 2 and int(button.grid_info()["column"]) < 3:
              button.grid_remove()



    found = False
    full_name = str(player1.get())
    x = players.find_players_by_full_name(full_name)

    duplicates_id = []
    duplicate_buttons = []
    games_played = 0


    for dictionary in x:
        if full_name.lower() == dictionary['full_name'].lower():
                duplicates_id.append(dictionary['id'])
                found = True
                
    if len(duplicates_id) == 1:
        valid_player1.set('')
        player1_id = dictionary['id']
        categories = ['PTS', 'AST', 'BLK', 'STL', 'REB', 'FG_PCT', 'FG3_PCT', 'FT_PCT']
        curr_row = 3
        curr_col = 1

        for c in categories:
            ttk.Label(mainframe, text = c).grid(column=curr_col, row=curr_row, sticky=W)
            career_stats = playercareerstats.PlayerCareerStats(per_mode36 = 'PerGame',player_id=player1_id).get_data_frames()[1].loc[:,c][0]
            
            career_avg = round(career_stats, 2)
             
                      
            ttk.Label(mainframe, text = str(career_avg)).grid(column=curr_col+1, row=curr_row, sticky=W)
            curr_row += 1

    if len(duplicates_id) > 1:
         valid_player1.set("There are multiple players with this name. Please choose one based on their player IDs below.")
         curr_row = 3
         data_start = 3+len(duplicates_id)
         for id in duplicates_id:
            ttk.Button(mainframe, text=id, command=lambda id=id: duplicate_player1(id, data_start)).grid(column=1, row=curr_row, sticky = W)

            duplicate_buttons.append(ttk.Button(mainframe, text=id, command=lambda id=id: duplicate_player1(id, data_start)))

            curr_row+=1
    
         
    if found == False:
        valid_player1.set("Invalid entry. Please type the player's full name.")

def duplicate_player1(id, data_start):
    for button in mainframe.grid_slaves():
         if int(button.grid_info()["row"]) > 2 and int(button.grid_info()["column"]) < 3:
              button.grid_remove()
         
    valid_player1.set('')
    #player_id = id
    categories = ['PTS', 'AST', 'BLK', 'STL', 'REB', 'FG_PCT', 'FG3_PCT', 'FT_PCT']
    curr_row = 3
    curr_col = 1

    for c in categories:
        ttk.Label(mainframe, text = c).grid(column=curr_col, row=curr_row, sticky=W)
        career_stats = playercareerstats.PlayerCareerStats(per_mode36 = 'PerGame',player_id=id).get_data_frames()[1].loc[:,c][0]
        
        career_avg = round(career_stats, 2)
             
        ttk.Label(mainframe, text = str(career_avg)).grid(column=curr_col+1, row=curr_row, sticky=W)
        curr_row += 1               
    

def duplicate_player2(id, data_start):
    for button in mainframe.grid_slaves():
         if int(button.grid_info()["row"]) > 2 and int(button.grid_info()["column"]) >= 3:
              button.grid_remove()
         
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
     

def check_player2(*args):

    for button in mainframe.grid_slaves():
         if int(button.grid_info()["row"]) > 2 and int(button.grid_info()["column"]) >= 3:
              button.grid_remove()

    found = False
    full_name = str(player2.get())
    x = players.find_players_by_full_name(full_name)

    duplicates_id = []
    duplicate_buttons = []
    games_played = 0


    for dictionary in x:
        if full_name.lower() == dictionary['full_name'].lower():
                duplicates_id.append(dictionary['id'])
                found = True
                
    if len(duplicates_id) == 1:
        valid_player1.set('')
        player2_id = dictionary['id']
        categories = ['PTS', 'AST', 'BLK', 'STL', 'REB', 'FG_PCT', 'FG3_PCT', 'FT_PCT']
        curr_row = 3
        curr_col = 3

        for c in categories:
            ttk.Label(mainframe, text = c).grid(column=curr_col, row=curr_row, sticky=W)
            career_stats = playercareerstats.PlayerCareerStats(per_mode36 = 'PerGame',player_id=player2_id).get_data_frames()[1].loc[:,c][0]
            
            career_avg = round(career_stats, 2)
             
                      
            ttk.Label(mainframe, text = str(career_avg)).grid(column=curr_col+1, row=curr_row, sticky=W)
            curr_row += 1

    if len(duplicates_id) > 1:
         valid_player2.set("There are multiple players with this name. Please choose one based on their player IDs below.")
         curr_row = 3
         data_start = 3+len(duplicates_id)
         for id in duplicates_id:
            ttk.Button(mainframe, text=id, command=lambda id=id: duplicate_player2(id, data_start)).grid(column=3, row=curr_row, sticky = W)

            duplicate_buttons.append(ttk.Button(mainframe, text=id, command=lambda id=id: duplicate_player2(id, data_start)))

            curr_row+=1
         
                
        
    if found == False:
        valid_player2.set("Invalid entry. Please type the player's full name.")
    

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


