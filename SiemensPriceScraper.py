import requests
from bs4 import BeautifulSoup
import csv

# Function to get the list price of a product based on its model number
def get_list_price(model_number, cookies, pricetype):
    url = f'https://mall.industry.siemens.com/mall/en/nl/Catalog/Product/{model_number}'  # URL for Siemens product page
    
    headers = {
        'User-Agent': 'Mozilla/7.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }  # Headers to mimic a browser request

    # Send the GET request with the specified headers and cookies
    response = requests.get(url, headers=headers, cookies=cookies)
    response.raise_for_status()  # Ensure the request was successful

    soup = BeautifulSoup(response.text, 'html.parser')  # Parse the response content using BeautifulSoup

    # Find the price element using the specified pricetype (e.g., Customer, List, etc.)
    price_tag = soup.select_one(f'#{pricetype}PriceCell')

    # Return the price if found, otherwise return a 'Price not found' message
    if price_tag:
        return price_tag.get_text(strip=True)
    else:
        return 'Price not found'

# Function to save the data to a CSV file
def save_to_csv(data, pricetype, filename='prices.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Model Number', f'{pricetype} Price'])  # Write header row
        for model, price in data.items():
            writer.writerow([model, price])  # Write model number and price

# Main function to retrieve prices for a list of models and save them to a CSV
def main():
    # Placeholder for cookies (replace with actual cookies)
    cookies = {
        "cookie_name_1": "cookie_value_1",
        "cookie_name_2": "cookie_value_2",
        # Add more cookies as needed
    }

    # List of model numbers to retrieve prices for
    models = [
        "6ES5710-8MA11", "6EP1332-4BA00", "6ES7515-2RM00-0AB0"
    ]
    
    prices = {}  # Dictionary to store model numbers and their corresponding prices

    # Loop through each model and retrieve the price
    for model in models:
        price = get_list_price(model, cookies, pricetype)
        prices[model] = price  # Store the price in the dictionary
        print(f"Model: {model}, {pricetype} Price: {price}")

    # Save the prices to a CSV file
    save_to_csv(prices, pricetype)

if __name__ == "__main__":
    pricetype = "Customer"  # Define the pricetype (e.g., Customer, List, etc.)
    main()  # Run the main function
