# Singapore Postal Code Downloader

A Python script to download Singapore postal codes with latitude, longitude, and address information from official mapping APIs.

## Features

- 🗺️ **Comprehensive Data**: Downloads all 999,000+ Singapore postal codes
- 📍 **Geocoding Support**: Get latitude and longitude for each postal code
- 💾 **CSV Export**: Results saved in easy-to-use CSV format

## Prerequisites

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/singapore-postal-code-downloader.git
cd singapore-postal-code-downloader
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

Run the script:
```bash
python postal_downloader.py
```

### Method 1: OneMap API (Recommended)

Downloads all Singapore postal codes using the official OneMap API.

**Advantages:**
- Comprehensive coverage of all 999,000+ postal codes
- Includes block numbers and road names
- Official Singapore mapping data
- Most accurate for local addresses

**Output file:** `postal_codes_singapore.csv`

**Columns:**
- `postal_code` - 6-digit Singapore postal code
- `latitude` - Latitude coordinate
- `longitude` - Longitude coordinate
- `address` - Full address
- `block` - Block number
- `road_name` - Road name

**Example:**
```csv
postal_code,latitude,longitude,address,block,road_name
001000,1.2896,103.8503,BLK 1 RAFFLES PLACE,1,Raffles Place
001001,1.2896,103.8503,BLK 2 RAFFLES PLACE,2,Raffles Place
```

## Output

After running the script, CSV files will be generated in your working directory:

- `postal_codes_singapore.csv` - Complete dataset from OneMap API

## Performance

- **(OneMap)**: ~20-25 hours for all 999,000+ postal codes (includes API rate limiting)

## API Information

### OneMap API
- **Endpoint**: `https://www.onemap.gov.sg/api/common/elastic/search`
- **Authentication**: `https://www.onemap.gov.sg/apidocs/authentication`
- **Documentation**: `https://www.onemap.gov.sg/apidocs/maps`


## Data Quality

- OneMap API provides official Singapore postal code data
- Addresses are in English
- Data is regularly updated by OneMap

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for:
- Bug fixes
- Performance improvements
- Additional data sources
- Documentation improvements

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational and research purposes. Users are responsible for ensuring compliance with the terms of service of the respective APIs:
- OneMap API Terms: `https://www.onemap.gov.sg/legal/apitermsofservice.html`

## Author

Created for developers and researchers needing Singapore postal code data with geographic coordinates.

---

**Note**: This script makes multiple API requests. Please be respectful of API rate limits and consider caching results if running frequently.
