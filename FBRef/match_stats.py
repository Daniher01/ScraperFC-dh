import ScraperFC as sfc
import traceback
import pandas as pd
from io import StringIO

# Initialize the FBRef scraper
scraper = sfc.FBRef()
try:
    # Scrape the match using the FBRef match link
    link = 'https://fbref.com/en/matches/ed48c4b3/Univ-Chile-Huachipato-January-23-2023-Primera-Division'
    match = scraper.scrape_match(link=link)
    
    # Local
    stats_home = match['Home Player Stats'].values[0]['Summary'][0]
    # Visitante
    stats_away = match['Away Player Stats'].values[0]['Summary'][0]
    # Guardar la data en csv
    stats_home.to_csv(f'data/FBRef/match_home.csv', index=False, sep=';', encoding='utf-8')
    stats_away.to_csv(f'data/FBRef/match_away.csv', index=False, sep=';', encoding='utf-8')
except:
    # Catch and print any exceptions.
    traceback.print_exc()
finally:
    # Again, make sure to close the scraper when you're done
    scraper.close()