import pandas as pd 
import numpy as np

laps_4 = {
     'lap': [1, 2, 3, 4, 5,0],
     'time(s)': [60, 62, 63, 65, 66, 64],
} 

laps_44 = {
     'lap': [1, 2, 3, 4, 5,0],
     'time(s)': [60, 62, 63, 65, 66, 66],
}

laps_33 = {
     'lap': [1, 2, 3, 4, 5,0],
     'time(s)': [61, 62, 63, 65, 66, 62],
}

list_laps = [sum(laps_4['time(s)']), sum(laps_44['time(s)']), sum(laps_33['time(s)'])]
list_laps_ordenada = sorted(list_laps)
laps = {
    'driver': [laps_4, laps_44, laps_33],
    'name': ['norris', 'hamilton', 'verstappen'],
    'total time': [np.sum(laps_4['time(s)']), np.sum(laps_44['time(s)']), np.sum(laps_33['time(s)'])],
    'laps completed': [len(laps_4['lap']), len(laps_44['lap']), len(laps_33['lap'])],
}

laps_df = pd.DataFrame(laps)
laps_df = laps_df.sort_values(by=['laps completed', 'total time'], ascending=[False, True])
laps_df['position'] = laps_df.reset_index().index + 1


def main(): 
    return print(laps_df)

if __name__ == '__main__':
    main()