import requests
import time

def download_datasheet(model, cookies):
    url = f"https://mall.industry.siemens.com/teddatasheet/?format=PDF&caller=Mall&mlfbs={model}&language=en"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/pdf"
    }
    
    for attempt in range(2):
        try:
            response = requests.get(url, cookies=cookies, headers=headers)
            # response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            if 'application/pdf' in response.headers.get('Content-Type', ''):
                with open(f"{model}.pdf", "wb") as file:
                    file.write(response.content)
                print(f"Downloaded datasheet for model {model}")
                return
            else:
                print(f"Unexpected content type for model {model}: {response.headers.get('Content-Type')}")
                print("Content:", response.text[:1000])
                
        except requests.HTTPError as e:
            print(f'Failed to download datasheet for model {model}: {e}')
        
        # Wait before retrying
        # time.sleep(5)

def main():

    cookies = {
        "cookie_name_1": "cookie_value_1",
        "cookie_name_2": "cookie_value_2",
        # Add more cookies as needed
    }

    models = ["6ES7590-1AE80-0AA0","6EP1333-4BA00","6ES7513-1AM03-0AB0","6ES7954-8LF03-0AA0","6ES7131-6BH01-0BA0","6ES7132-6BH01-0BA0","6ES7134-6FF00-0AA1","6ES7135-6HD00-0BA1","6ES5710-8MA11","6ES7155-6AU01-0BN0","6ES7193-6AR00-0AA0","6ES7193-6BP00-0DA0","6ES7193-6BP20-0DA0","6XV1850-2GH10","6ES7193-6BP00-0DA0","6ES7137-6AA01-0BA0","6AV2124-0QC13-0AX0"]
    
    for model in models:
        download_datasheet(model, cookies)

if __name__ == "__main__":
    main()
