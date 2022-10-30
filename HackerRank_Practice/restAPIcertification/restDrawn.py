import requests
def getNumDraws(year):
    draw_matches=0
    matches_url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&page=1"
    
    matRes = requests.get(matches_url).json()
    for i in range(0,matRes['total_pages']):
        matRes = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&page={i+1}").json()
        for eachMatch in matRes['data']:
            if(int(eachMatch['team1goals']) == int(eachMatch['team2goals'])):
                draw_matches+=1
    
    return draw_matches

print(getNumDraws(2011))