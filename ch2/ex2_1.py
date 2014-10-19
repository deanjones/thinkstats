import pandas as pd
    
def pumpkin():
    data = [1, 1, 1, 3, 3, 591]
    s = pd.Series(data)
    print 'mean =', s.mean()
    print 's.d. =', s.std()
    print 'variance =', s.var()
    
if __name__ == '__main__':
    pumpkin()
