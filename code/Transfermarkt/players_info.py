import ScraperFC as sfc
import traceback

# Initialize the FBRef scraper
scraper = sfc.Transfermarkt()
try:
    YEAR = 2023
    LEAGUE = 'EPL' #'Chile Campeonato Profesional'
    # Scrape the table
    lg_table = scraper.get_players(year=YEAR, league=LEAGUE)
    
    # Guardar la data en csv
    lg_table.to_csv(f'data/Transfermarkt/players_{LEAGUE}_{YEAR}.csv', index=False, sep=';', encoding='utf-8')
except:
    # Catch and print any exceptions. This allows us to still close the
    # scraper below, even if an exception occurs.
    traceback.print_exc()
finally:
    # It's important to close the scraper when you're done with it. Otherwise,
    # you'll have a bunch of webdrivers open and running in the background.
    scraper.close()