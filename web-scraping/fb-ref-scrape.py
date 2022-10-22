import pandas as pd
from bs4 import BeautifulSoup
import ScraperFC as sfc
import requests
import regex as re


def team_stats(team): 
    dict = {'Arsenal': '18bb7c10', 'Tottenham Hotspur': '361ca564'} #Can create full list by scraping team IDs
    tm_id = dict[str(team)]
    url = 'https://fbref.com/en/squads/{}'.format(tm_id)
    df = pd.read_html(url)[0]

    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    id_tags = soup.find_all('a', href=re.compile('/matchlogs/2022-2023/misc/'))

    id_tags_col = []
    for tag in id_tags: 
        info = tag.get('href')
        info = info[12:20]
        id_tags_col.append(info)
    df['ID'] = pd.Series(id_tags_col)

    return df

team_stats('Arsenal')

def scouting_report(player): 
    url = player
    df_s = pd.read_html(url)[0]
    df_s = df_s.dropna()
    print(df_s)
    return df_s


scouting_report('https://fbref.com/en/players/67ac5bb8/scout/11566')
