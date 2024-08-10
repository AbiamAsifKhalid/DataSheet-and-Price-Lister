import requests
from time import sleep

# List of model numbers to download datasheets for
model_numbers = [
    "BMEXBP0400","BMEH584040","BMENOC0321","BMENUA0100","BMXCPS3020","BMXXEM010","490NAC0100","490NTW00002","BMEXBP0602","BMXCPS4022"
]

# List of region-specific URLs
base_urls = [
    "https://www.se.com/ww/en/product/download-pdf/",
    "https://www.se.com/us/en/product/download-pdf/",
    "https://www.se.com/uk/en/product/download-pdf/",
    "https://www.se.com/sa/en/product/download-pdf/",
    "https://www.se.com/ae/en/product/download-pdf/",
    "https://www.se.com/in/en/product/download-pdf/",
    # Add more region URLs if needed
]

def download_datasheet(model_number):
    for base_url in base_urls:
        url = f"{base_url}{model_number}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"{model_number}.pdf", 'wb') as file:
                    file.write(response.content)
                print(f"Downloaded: {model_number} from {base_url}")
                return True
            else:
                print(f"Failed to download from {base_url}{model_number} - Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading {model_number} from {base_url}: {e}")
        # Sleep to avoid hitting the server too hard
        sleep(1)
    print(f"Failed to download datasheet for model number: {model_number}")
    return False

# Download datasheets for all model numbers
for model_number in model_numbers:
    download_datasheet(model_number)
