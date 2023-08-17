from nba_api.stats.static import teams
from nba_api.stats.static import players

def findTeamId(team_name):
    team = teams.find_teams_by_full_name(team_name)[0]
    return team['id']
    
def findPlayerId(player_name):
    player = players.find_players_by_full_name(player_name)[0]
    return player['id']