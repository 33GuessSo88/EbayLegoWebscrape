from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import date
from urllib.parse import urlparse

searchterm = ['21033',
              '75827'
              ]

df = pd.read_html('https://brickset.com/sets/query-8570')

print(df)



