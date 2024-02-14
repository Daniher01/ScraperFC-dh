import ScraperFC as sfc
import traceback


# Initialize the FBRef scraper
scraper = sfc.FBRef()
try:
    # Scrape the match using the FBRef match link
    YEAR = 2023
    LEAGUE = 'Chile Campeonato Profesional'
    squad_stats, opponent_stats, player_stats = scraper.scrape_stats(year=YEAR, league=LEAGUE, stat_category='standard', normalize=True)
    filename_pre = f'data/FBRef/stats_{YEAR}_{LEAGUE}_'
    player_stats.to_csv(path_or_buf=f'{filename_pre}.csv', index=False)
    
except:
    # Catch and print any exceptions.
    traceback.print_exc()
finally:
    # Again, make sure to close the scraper when you're done
    scraper.close()