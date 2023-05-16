import PySimpleGUI as sg
import matplotlib.pyplot as plt
import stats 

start_layout = [[sg.Text('League of Stats')],
          [],
          [sg.DropDown(stats.champion_list, 'Champion')],
          [sg.DropDown(['Winrate', 'Pickrate'], 'Statistik'), sg.DropDown(['Blå', 'Röd', 'Båda'], 'Lag')],
          [sg.Button('Submit')]]  


layout = start_layout


window = sg.Window('League of Stats', layout, element_justification='l', size=(500, 500))    
while True:
    event, values = window.read()
    if values[2] in 'Blå': team = 1
    elif values[2] in 'Röd': team = 2
    elif values[2] in 'Båda': team = 3
    else: team = None
    print(event, values)


    if event in (None, 'Cancel'):
        break

    if event in 'Submit':
        if values[1] in 'Pickrate':
            sg.popup(f'{values[0]} har en pickrate av {stats.pickrate(team, values[0].replace(" ",""))}%')
        

        elif values[1] in 'Winrate':
            plt.plot(1,2,3,4)
            sg.popup(f'{values[0]} har en winrate av {stats.winrate(team, values[0].replace(" ",""))}%')
            plt.show()
            
            
            
    
    



