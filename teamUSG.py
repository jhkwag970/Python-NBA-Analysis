from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import boxscoreusagev2
from nba_api.stats.endpoints import boxscoretraditionalv2
from nba_api.stats.static import teams
from playerList import getAllPlayersInTeam
from nbaId import findTeamId
import pandas as pd
import matplotlib.pyplot as plt

team_name = "Atlanta Hawks"
t_id = findTeamId(team_name)
season = '2019-20'
season_type="Regular Season"

# Get all games for the Atlanta Hawks in the specified season
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=t_id, season_nullable=season, season_type_nullable=season_type)
games = gamefinder.get_data_frames()[0]

# Get the game IDs
game_ids = list(reversed(games['GAME_ID'].tolist()))
wl = list(reversed(games["WL"].tolist()))

box_score = boxscoreusagev2.BoxScoreUsageV2(game_id=game_ids[1])
box_score_traditional = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_ids[1])
box = box_score.get_data_frames()[0]
box_traditional = box_score_traditional.get_data_frames()[0]

hawks_list = getAllPlayersInTeam(t_id, season)

hawks_usg_dict_bygame = {}
for hawk in hawks_list:
    if hawks_usg_dict_bygame.get(hawk) == None:
        hawks_usg_dict_bygame[hawk] = []
    
for cnt ,g_id in enumerate(game_ids):
    box_usg_df = boxscoreusagev2.BoxScoreUsageV2(game_id=g_id).get_data_frames()[0]
    box_atl = box_usg_df[box_usg_df['TEAM_ID'] == t_id]
    box_usg = box_atl[["PLAYER_NAME", "USG_PCT"]].values.tolist()
    for box in box_usg:
        if hawks_usg_dict_bygame.get(box[0]) != None:
            hawks_usg_dict_bygame[box[0]].append(box[1])
    for name, usg in hawks_usg_dict_bygame.items():
        if len(usg) == cnt:
            hawks_usg_dict_bygame[name].append(0.0)
            
hawks_usg_df_bygame = pd.DataFrame({})

for name, usg in hawks_usg_dict_bygame.items():
    hawks_usg_df_bygame[name] = usg

hawks_usg_df_bygame.columns = hawks_usg_df_bygame.columns.str.replace(' ', '')
    
hawks_usg_df_bygame.to_csv("resources/"+season+"_"+team_name+"_usg_bygame.csv",index=False)
print("USG Export Done")


# plt.figure()
# plt.title("22-23 ATL HAWKS PLAYER USG BY GAME")
# plt.xlabel("game number", labelpad=10)
# plt.ylabel("usg (%)", labelpad=10)
# for name,usg in hawks_usg_dict_bygame.items():
#     plt.plot(usg, marker='o', markerfacecolor='skyblue', markersize=6, label=name)
# plt.grid(True)
# plt.legend()
# plt.show()

    
    

# for id in game_ids:
#    box_usg_df = boxscoreusagev2.BoxScoreUsageV2(game_id=id).get_data_frames()[0]
#    box_usg_ty_list = box_usg_df[box_usg_df[box_usg_df["PLAYER_ID"] == 1629027]]
#    box_usg_ty_list = box_usg_df[box_usg_df[box_usg_df["PLAYER_ID"] == 1629027]]
#    box_usg_ty_list = box_usg_df[box_usg_df[box_usg_df["PLAYER_ID"] == 1629027]]

#print(box[box['TEAM_ID'] == 1610612737])
#box_atl = box[box['TEAM_ID'] == 1610612737]
#print(box_atl[["PLAYER_NAME", "USG_PCT"]].sort_values("USG_PCT", ascending=False))
#print(box_traditional[box_traditional['TEAM_ID'] == 1610612737])

# dict={}
# if dict.get("trae young") == None:
#     dict["trae young"] = []
#     dict["trae young"].append(0.31)

# if dict.get("trae young") != None:
#     dict["trae young"].append(0.32)

# print(dict)
