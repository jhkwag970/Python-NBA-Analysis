from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster


def getAllPlayersInTeam(t_id, season):
    roster = commonteamroster.CommonTeamRoster(team_id=t_id, season=season)
    return roster.get_data_frames()[0]["PLAYER"].tolist()
    
#getAllPlayersInTeam("Atlanta Hawks", "2022-23")