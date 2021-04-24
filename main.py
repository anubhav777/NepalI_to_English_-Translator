import pandas as pd
import numpy as np
import spacy
import nepali_roman as nr
import Levenshtein
import re
import sys
from textblob import TextBlob

dtypes_dict = {
    0: int, # geonameid
    1: str,  # name
    2: str,  # asciiname
    3: str,  # alternatenames
    4: float, # latitude
    5: float, # longitude
    6: str, # feature class
    7: str, # feature code
    8: str, # country code
    9: str, # cc2
    10: str, # admin1 code
    11: str, # admin2 code
    12: str, # admin3 code
    13: str, # admin4 code
    14: int, # population
    15: None, # elevation
    16: int, # dem (digital elevation model)
    17: str, # timezone
    18: str # modification date yyyy-MM-dd
}

data = pd.read_csv("NP.txt", sep="\t", header = None, dtype=dtypes_dict)
data.to_csv('output.txt', sep='\t')

arr = data[1].values.tolist()