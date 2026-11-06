# Google Maps scraper web app and local business data extraction Python maps project

This Python maps project extracts business names, categories, ratings, phone numbers, addresses, and URLs from Google Maps searches and exports the records to spreadsheet files.

The Google Maps scraper web app extracts structured geographic business data for local business data extraction workflows. The system runs through a desktop graphical interface or through headless browser automation scripts. Users supply a search query, and the application extracts search results directly into Excel XLSX or CSV formats.

## Architecture

The codebase contains five main components:

- Desktop application in `rapidapi/`: A desktop interface built with CustomTkinter (`gui.py`) that queries the RapidAPI Maps Data endpoint (`map_data.py`). The script sends search terms to `https://maps-data.p.rapidapi.com/searchmaps.php`, formats business status flags, and saves records to an Excel workbook with Pandas. The application triggers desktop status notifications through Plyer.
- Single-process browser scraper in `PYTHON maps/`: Selenium automation scripts using Firefox. The script `map_result.py` scrolls the Google Maps results container until the end-of-list marker appears, extracts details from each place card, and writes rows to a CSV file.
- Multiprocess browser scraper in `test multiprocessing/`: Parallel scraper architecture using Python multiprocessing and Selenium. The script `map_result.py` initializes a headless Firefox instance to collect place URLs, splits work evenly across CPU cores with `multiprocessing.cpu_count()`, launches worker processes, and stores records in a shared `multiprocessing.Manager().list()` before writing a CSV file.
- Offline parser in `short address/`: Scripts (`lxml_parser.py` and `soup_test.py`) that parse saved Google Maps HTML snapshots using `lxml.etree` XPath expressions.
- API prototypes in `attempt-3/` and `attempt-4/`: Experimental parsers that evaluate internal JSON responses and Apify client crawler integration.

## Setup

1. Install Python 3.10 or higher.
2. Install Mozilla Firefox and geckodriver, then verify that geckodriver exists in PATH.
3. Install required Python packages:

```bash
pip install customtkinter pillow requests pandas plyer selenium openpyxl lxml apify-client
```

## Usage

### Desktop application

Run the CustomTkinter desktop interface:

```bash
python "rapidapi/gui.py"
```

Type a query such as `Gift Shop In Chennai` into the text box and press Enter. The script queries the API, sends a system notification, and saves the output file `{query}.xlsx` in the current working directory.

### Browser scraper

Run the single-process Selenium scraper:

```bash
python "PYTHON maps/map_result.py"
```

The script launches Firefox, searches Google Maps, iterates over matching place elements, and writes `results_in_{location}.csv`.

### Multiprocess scraper

Run the parallel scraper:

```bash
python "test multiprocessing/map_result.py"
```

Enter a search query at the prompt. The script collects listing links, distributes links among worker processes across CPU cores, and writes `results in {location}.csv`.

## Configuration

- RapidAPI settings: `rapidapi/map_data.py` contains the endpoint URL, RapidAPI host header, and API key.
- Headless execution: `test multiprocessing/map_result.py` passes the `--headless` flag to `FirefoxOptions`.
- Timeouts: Selenium scripts configure explicit and implicit timeouts at 30 seconds using `WebDriverWait` and `driver.implicitly_wait(30)`.
- Apify token: `attempt-4/test ctrl-v.py` sets the Apify client API token and actor ID.
