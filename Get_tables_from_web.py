

'''
GRABING THE LINK FROM WEB AND STORING IT IN A VARIABLE CALLED table_here USING .read_html IN PANDAS
'''

import pandas as pd

table_here = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Flash_episodes")

print(len(table_here))

print(table_here[2])

