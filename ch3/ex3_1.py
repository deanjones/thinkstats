import pandas as pd

obs = {'size' : ['5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49'], 'count' : [8, 8, 14, 4, 6, 12, 8, 3, 2]}

data = pd.DataFrame(obs, dtype='int')

print 'mean =', data['count'].mean()
