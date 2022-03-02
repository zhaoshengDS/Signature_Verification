"""
Convert files from '.txt', '.dat' or other formats into '.csv' format
"""

import os
import csv
import pandas as pd
import winsound

duration = 2000  # milliseconds
freq = 440  # Hz

directory = "Test"

for root, subdirectories, files in os.walk(directory):
    for file in files:
        try:            
            data = pd.read_csv(os.path.join(root, file),
                               header = None,
                               engine = "python",
                               sep = ',| ')

            data.columns = ['x', 'y', 'z']
            
            data.to_csv(os.path.join(root, file).split('.')[0] + ".csv", 
                        index = False)
        
        except Exception as e:
            print("Type of error: " + str(e))
            print(os.path.join(root, file))

print("Mission Accomplished")
winsound.Beep(freq, duration)