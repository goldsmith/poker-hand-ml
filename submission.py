from pdb import set_trace

import numpy as np
import pandas as pd
import pylab
from sklearn.naive_bayes import GaussianNB


data = {
  'train': pd.read_csv('data/train.csv'),
  'test': pd.read_csv('data/test.csv')
}

def main():
	set_trace()

if __name__ == '__main__': main()