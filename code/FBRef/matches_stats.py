import ScraperFC as sfc
import traceback


# Initialize the FBRef scraper
scraper = sfc.FBRef()
try:
    # Scrape the match using the FBRef match link
    YEAR = 2023
    LEAGUE = 'Chile Campeonato Profesional'
    matches = scraper.scrape_matches(year=YEAR, league=LEAGUE)
    filename = f'data/FBRef/{YEAR}_{LEAGUE.replace(" ","_")}_FBRef_matches.csv'
    matches.to_csv(path_or_buf=filename, index=False)
    
except:
    # Catch and print any exceptions.
    traceback.print_exc()
finally:
    # Again, make sure to close the scraper when you're done
    scraper.close()