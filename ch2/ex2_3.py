from ch1.ex1_3 import *

def mode(data, dimension):
    grouped = data.groupby(dimension)
    counts =  grouped[dimension].agg(lambda x: x.value_counts())
    return counts.order(ascending=False).index[0]

if __name__=='__main__':
    preg = load_pregnancies()
    first = get_first_babies(preg)
    others = get_others(preg)
    print mode(first, 'prglength')

