import pandas as pd
import numpy as np

# rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.
# rock  = A, X  
# paper = B, Y
# scissors = C, Z
#winning combinations=(A,Y) (B,Z) (C,A)

df=pd.read_csv("/home/sree/Documents/aoc/day2.txt",sep=" ")
print(df.columns)
df["Result"]= np.where(((df['opponent'] == 'A') and (df['player'] == 'Y')),"Winner","Unknown")
print(df)