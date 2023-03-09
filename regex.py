import re
import pandas as pd 

#r = re.compile('^[m]. [A-Z][a-z]{1,10} \([0-9]{1,2} (min from metro)\)$')
#s = 'm. Smolenskaya (9 min from metro)'

# r1 = re.compile('^[м]. [ЁёА-я]{1,10} \([0-9]{1,2} (мин пешком)\)$')
# s1 = 'м. Смоленская ( мин пешком)'
# print(r1.match(s1))


df = pd.read_csv('_data.csv')
price = df['Цена']

price = price.apply(lambda x: re.sub(r'[0-9]+', '', x).split(','))
uniq = price.explode().unique()

print(uniq)
