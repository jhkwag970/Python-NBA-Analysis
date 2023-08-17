import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
team_name = "Atlanta Hawks"
season = '2020-21'
hawks_usg_df = pd.read_csv("resources/"+season+"_"+team_name+"_usg_bygame.csv")

hawks_num_play_dict = {}
for hawk in hawks_usg_df.columns:
    cnt = 0
    for usg in hawks_usg_df[hawk].values.tolist():
        if usg > 0.0:
            cnt+=1        
    hawks_num_play_dict[hawk] = cnt

hawks_top_usg_dict = {}
for hawk in hawks_usg_df.columns:
    if hawks_num_play_dict[hawk] > 50:
        hawks_top_usg_dict[hawk] = hawks_usg_df[hawk].where(hawks_usg_df[hawk] > 0.0).mean()
d1 = sorted(hawks_top_usg_dict.values())     
top=1
hawks_top_usg_dict = dict(sorted(hawks_top_usg_dict.items(), key=lambda x:x[1], reverse=True)[:top])
fig_name = season +" ATL HAWKS TOP "+str(top)+" USG PLAYER BY GAME"
plt.figure(figsize=(20,5))
plt.title(fig_name)
plt.xlabel("game number", labelpad=10)
plt.ylabel("usg (%)", labelpad=10)
for name in hawks_top_usg_dict.keys():
    plt.plot(hawks_usg_df[name], marker='o', markerfacecolor='skyblue', markersize=6, label=name)
plt.grid(True)
plt.legend()
plt.savefig("resources/picture/"+fig_name+".png")
plt.show()
