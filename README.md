## Overview
This project consists of two main components: the "Soda Data Scraper" and the "Soda Data Analyzer." The first script extracts soda names and ingredients from the Safeway website and stores them in a CSV file. The second script, using Python's `pandas` and `matplotlib` libraries, analyzes this data to identify the most common soda ingredients and visualizes these findings in a bar chart.

## Features
- **Data Scraping**: Retrieves soda names and ingredients from the Safeway website.
- **Data Cleaning**: Cleans and formats the scraped data for analysis.
- **Data Analysis**: Analyzes the frequency of ingredients across various sodas.
- **Visualization**: Creates a bar chart visualizing the most common ingredients in sodas.

## Requirements
- Python 3.x
- `requests` and `BeautifulSoup` libraries for the scraper.
- `pandas`, `numpy`, and `matplotlib` libraries for the analyzer.
- Internet connection.

## Installation
1. Ensure Python 3.x is installed on your system.
2. Install the required libraries:
   ```
   pip install requests beautifulsoup4 pandas matplotlib
   ```
3. Download both scripts (`soda_data_scraper.py` and `soda_data_analyzer.py`) to your preferred directory.

## Usage
### Soda Data Scraper
1. Navigate to the script's directory.
2. Run the scraper script:
   ```
   python soda_data_scraper.py
   ```
3. The script will scrape data and store it in `soda_data.csv`.

### Soda Data Analyzer
1. Ensure `soda_data.csv` is in the same directory as the analyzer script.
2. Run the analyzer script:
   ```
   python soda_data_analyzer.py
   ```
3. The script will read the data, analyze the ingredient frequencies, and display a bar chart.

## Configuration
- **Scraper Script**:
  - `num_pages_to_scrape`: Number of pages to scrape.
  - `int_soda_id`: Initial soda ID for scraping. Safeway.com uses a sequential system for numbers their sodas. By default this value is set to the lowest number that represents a soda that I could find.
- **Analyzer Script**:
  - Modify the `plt.rcParams` and `colors` variables to change the visual appearance of the bar chart.

## Notes
- The scraper is configured for Safeway's website structure as of the latest update. Changes to the website may require script modifications.
- Use the scraper responsibly to avoid server overload or potential IP blocking. The scraper does contain random sleep periods to protect the service from automatic server blocking.
- The analyzer script assumes the data format provided by the scraper. Changes in the scraper's output format may require updates in the analyzer.
