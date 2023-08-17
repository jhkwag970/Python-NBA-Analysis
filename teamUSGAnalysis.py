import pandas as pd
import os
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
fileList = os.listdir("resources/")
dfList=[]
season_list=[]
for file in fileList:
    if "csv" in file:
        season = file.split(" ")[0]
        season_list.append(season)
        dfList.append(pd.read_csv("resources/"+file))

season_usg_list=[]
for current_df in dfList:
    hawks_num_play_dict = {}
    for hawk in current_df.columns:
        cnt = 0
        for usg in current_df[hawk].values.tolist():
            if usg > 0.0:
                cnt+=1        
        hawks_num_play_dict[hawk] = cnt

    hawks_top_usg_dict = {}
    for hawk in current_df.columns:
        if hawks_num_play_dict[hawk] > 50:
            hawks_top_usg_dict[hawk] = current_df[hawk].where(current_df[hawk] > 0.0).mean()
    d1 = sorted(hawks_top_usg_dict.values())     
    top=5
    hawks_top_usg_dict = dict(sorted(hawks_top_usg_dict.items(), key=lambda x:x[1], reverse=True)[:top])
    print(hawks_top_usg_dict)
    season_usg_list.append(hawks_top_usg_dict)


for cnt, season in zip(season_list, season_usg_list):
    fig_name = cnt + " ATL HAWKS TOP "+str(top)+" USG PLAYER BY GAME "
    plt.figure(figsize=(20,5))
    plt.title(fig_name)
    plt.xlabel("name", labelpad=10)
    plt.ylabel("usg (%)", labelpad=10)
    plt.bar(season.keys(), season.values(), color = ['r', 'g', 'b', 'k', 'dodgerblue'])
    plt.grid(True)
    plt.legend()
    plt.savefig("resources/picture/"+fig_name+".png")
        