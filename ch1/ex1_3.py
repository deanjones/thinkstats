import pandas as pd
import numpy as no
import numpy as np
import survey

DATA_DIR = '../data'

def load_pregnancies():
    preg = survey.Pregnancies()
    preg.ReadRecords(DATA_DIR)

    tuples = [(p.caseid, p.nbrnaliv, p.babysex, p.birthwgt_lb, p.birthwgt_oz, p.prglength, p.outcome, p.birthord, p.agepreg, p.finalwgt) for p in preg.records]
    cols = [x[0] for x in preg.GetFields()]

    preg_df = pd.DataFrame.from_records(tuples, columns=cols)

    # map 'NA' to NaN
    preg_df = preg_df.applymap(lambda x: np.nan if x=='NA' else x)

    # convert types to float
    preg_df[['nbrnaliv', 'babysex', 'birthwgt_lb', 'birthwgt_oz', 'birthord']] =  preg_df[['nbrnaliv', 'babysex', 'birthwgt_lb', 'birthwgt_oz', 'birthord']].astype(float)
    
    return preg_df

def get_first_babies(preg_df):
    return preg_df[(preg_df['birthord']==1) & (preg_df['outcome']==1)]

def get_others(preg_df):
    return preg_df[(preg_df['birthord']!=1) & (preg_df['outcome']==1)]

# calculate difference in hours between means

if __name__ == '__main__':
    data = load_pregnancies()
    first_babies = get_first_babies(data)
    others = get_others(data)
    print ((first_babies['prglength'].mean(skipna=True)) - (others['prglength'].mean(skipna=True))) * 7 * 24

