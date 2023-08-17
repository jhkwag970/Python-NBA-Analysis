import pandas as pd
import matplotlib.pyplot as plt
from nba_api.stats.endpoints import playercareerstats
from nbaId import findPlayerId

player_name="Trae Young"
p_id = findPlayerId(player_name)
career_stats_df = playercareerstats.PlayerCareerStats(player_id=p_id).get_data_frames()[0]
seasonList = career_stats_df.SEASON_ID.values.tolist()

team_name = "Atlanta Hawks"
team_usg_df_list=[]
for season in seasonList:
    team_usg_df_list.append(pd.read_csv("resources/"+season+"_"+team_name+"_usg_bygame.csv"))

player_usg_dict={}
for season, team_usg in zip(seasonList, team_usg_df_list):
    player_usg_dict[season] = team_usg[player_name.replace(' ', '')].where(team_usg[player_name.replace(' ', '')] > 0.0).mean()

fig_name = "Trae Young Overall USG Change"
plt.figure(figsize=(20,5))
plt.title(fig_name)
plt.xlabel("season number", labelpad=10)
plt.ylabel("usg (%)", labelpad=10)
plt.plot(seasonList, player_usg_dict.values() ,label="TRAE YOUNG")
plt.grid(True)
plt.legend()
plt.savefig("resources/picture/"+fig_name+".png")
plt.show()
