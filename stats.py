import pandas as pd

df = pd.read_csv('.\lol\games.csv')
champion_json = pd.read_json('.\lol\champion_info_2.json')
spell_json = pd.read_json('.\lol\summoner_spell_info.json')


champion_list = []
for i in champion_json['data']:
    champion_list.append(i['name'])

def times_picked(team, champ):
    'Returnerar hur många gånger en karaktär blivit valt. team 1: lag 1, 2: lag 2, 3: båda'
    
    #Summerar hur många gånger värdet dyker upp i kolumnerna t1_champ'1-5' och t2_champ'1-5'id 
    picks_team_1 = ((df['t1_champ1id'] == champion_json['data'][champ]['id']).sum() +
     (df['t1_champ2id'] == champion_json['data'][champ]['id']).sum() +
     (df['t1_champ3id'] == champion_json['data'][champ]['id']).sum() +
     (df['t1_champ4id'] == champion_json['data'][champ]['id']).sum() +
     (df['t1_champ5id'] == champion_json['data'][champ]['id']).sum())
    
    picks_team_2 = ((df['t1_champ1id'] == champion_json['data'][champ]['id']).sum() +
     (df['t2_champ2id'] == champion_json['data'][champ]['id']).sum() +
     (df['t2_champ3id'] == champion_json['data'][champ]['id']).sum() +
     (df['t2_champ4id'] == champion_json['data'][champ]['id']).sum() +
     (df['t2_champ5id'] == champion_json['data'][champ]['id']).sum())

    if team == 1: return(picks_team_1)
    elif team == 2: return(picks_team_2)
    elif team == 3: return(picks_team_1 + picks_team_2)


def pickrate(team, champ):
    'Returnerar hur många procent(avrundat till 2 decimaler) av alla matcher som en karaktär har valts. team 1: lag 1, 2: lag 2, 3: båda'

    return(round(times_picked(team, champ) / len(df['gameId']) * 100, 2))


def winrate(team, champ):
    'Returnerar hur många procent(avrundat till 2 decimaler) av dess spelade matcher som en karaktär har vunnit. team 1: lag 1, 2: lag 2, 3: båda'

#summerar antalet rader där     
    wins_team_1 = ((len(df[(df["t1_champ1id"] == (champion_json['data'][champ]['id'])) & (df["winner"]== 1)])) + 
                   (len(df[(df["t1_champ2id"] == (champion_json['data'][champ]['id'])) & (df["winner"]== 1)])) +
                   (len(df[(df["t1_champ3id"] == (champion_json['data'][champ]['id'])) & (df["winner"]== 1)])) +
                   (len(df[(df["t1_champ4id"] == (champion_json['data'][champ]['id'])) & (df["winner"]== 1)])) +
                   (len(df[(df["t1_champ5id"] == (champion_json['data'][champ]['id'])) & (df["winner"]== 1)])))
    
    wins_team_2 = ((len(df[(df["t2_champ1id"] == (champion_json['data'][champ]['id'])) & (df["winner"]== 1)])) + 
                   (len(df[(df["t2_champ2id"] == (champion_json['data'][champ]['id'])) & (df["winner"]== 1)])) +
                   (len(df[(df["t2_champ3id"] == (champion_json['data'][champ]['id'])) & (df["winner"]== 1)])) +
                   (len(df[(df["t2_champ4id"] == (champion_json['data'][champ]['id'])) & (df["winner"]== 1)])) +
                   (len(df[(df["t2_champ5id"] == (champion_json['data'][champ]['id'])) & (df["winner"]== 1)])))

    if team == 1: return(round(wins_team_1 / times_picked(team, champ) * 100, 2))
    if team == 2: return(round(wins_team_2 / times_picked(team, champ) * 100, 2))
    if team == 3: return(round((wins_team_1 + wins_team_2) / times_picked(team, champ) * 100, 2))




# tem = int(input('tem '))
# chap = input('champ ').title()

# print(times_picked(tem, chap))
# print(winrate(tem, chap))
# print(pickrate(tem, chap))