from ch1.ex1_3 import *
from random import random
from statsmodels.distributions.empirical_distribution import ECDF

def get_sample(ecdf, n):
    rnd = random()
    

if __name__ == "__main__":
    preg = load_pregnancies()
    ecdf = ECDF(preg['birthwgt_oz'])
    sample = get_sample(ecdf, 1000)
