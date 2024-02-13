import ScraperFC as sfc
import traceback
import pandas as pd
from io import StringIO

# Initialize the FBRef scraper
scraper = sfc.FBRef()
try:
    # Scrape the match using the FBRef match link
    link = 'https://fbref.com/en/matches/967efd56/Southampton-Tottenham-Hotspur-September-20-2020-Premier-League'
    match = scraper.scrape_match(link=link)
    stats_home = match['Home Player Stats'].values[0]['Summary'][0]
    # Guardar la data en csv
    stats_home.to_csv(f'data/FBRef/match_home.csv', index=False, sep=';', encoding='utf-8')
except:
    # Catch and print any exceptions.
    traceback.print_exc()
finally:
    # Again, make sure to close the scraper when you're done
    scraper.close()