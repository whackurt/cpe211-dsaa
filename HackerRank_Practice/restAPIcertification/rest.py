import requests
def getTotalGoals(team, year):
    goals=0
    
    home = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page=1"
    visiting = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page=1"
    
    homeRes = requests.get(home).json()
    visRes = requests.get(visiting).json()
    for i in range(0,homeRes['total_pages']):
        homeRes = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={i+1}").json()
        visRes = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={i+1}").json()
        for j in homeRes['data']:
            goals+= int(j['team1goals'])
        for k in visRes['data']:
            goals+= int(k['team2goals'])
        
    return goals
    
       

print(getTotalGoals('Barcelona',2011))
print(getTotalGoals('Chelsea',2014))
