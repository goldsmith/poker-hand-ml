from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
import pylab
from pdb import set_trace

data = {}

for s in ['train', 'test']:
	data[s] = pd.read_csv('data/' + s + '.csv')

def main():
	set_trace()

if __name__ == '__main__': main()