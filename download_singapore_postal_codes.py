import requests
import csv
import json
import os
from pathlib import Path

def download_singapore_postal_codes():
    """Download Singapore postal codes with lat/long"""
    print("Downloading Singapore postal codes...")
    
    output_file = "postal_codes_singapore.csv"
    
    # Using OneMap API (Singapore's official mapping platform)
    search_api = "https://www.onemap.gov.sg/api/common/elastic/search"
    
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['postal_code', 'latitude', 'longitude', 'address', 'block', 'road_name'])
            
            # Singapore postal codes range from 1 to 999999
            # Generate all valid postal codes
            postal_codes = []
            for i in range(1, 999999):
                postal_codes.append(f"{i:06d}")
            
            print(f"Found {len(postal_codes)} Singapore postal codes to process...")
            
            count = 0
            for idx, postal in enumerate(postal_codes):
                try:
                    # Query OneMap API for postal code
                    params = {
                        'searchVal': postal,
                        'returnGeom': 'Y',
                        'getAddrDetails': 'Y',
                        'pageNum': 1
                    }

                    headers = {
                        'Authorization': ''
                    }
                    
                    response = requests.get(search_api, params=params, headers=headers, timeout=10)
                    response.raise_for_status()
                    
                    data = response.json()
                    if data.get('results') and len(data['results']) > 0:
                        result = data['results'][0]
                        writer.writerow([
                            postal,
                            result.get('LATITUDE', ''),
                            result.get('LONGITUDE', ''),
                            result.get('ADDRESS', ''),
                            result.get('BLK_NO', ''),
                            result.get('ROAD_NAME', '')
                        ])
                        count += 1
                        
                        if (idx + 1) % 100 == 0:
                            print(f"  Processed {idx + 1}/{len(postal_codes)} postal codes ({count} found)")
                    
                except Exception as e:
                    pass  # Skip postal codes that don't exist
                
            print(f"✓ Singapore postal codes saved to {output_file}")
            print(f"  Total postal codes found: {count}")
            return output_file
    
    except Exception as e:
        print(f"✗ Error downloading Singapore postal codes: {e}")
        return None

def main():
    """Main function to download Singapore postal codes"""
    print("=== Singapore Postal Code Downloader ===\n")
    
    download_singapore_postal_codes()
    
    print("\n=== Download Complete ===")
    print("Files saved in current directory")

if __name__ == "__main__":
    main()
