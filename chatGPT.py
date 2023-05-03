import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = "https://www.robu.in/"

# Send a GET request to the URL and retrieve its HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the categories on the website
categories = soup.find_all("li", {"class": "cat-item"})

# Iterate through each category and retrieve the product information
for category in categories:
    # Get the category name
    category_name = category.a.text
    
    # Get the URL of the category page
    category_url = category.a.get("href")
    
    # Send a GET request to the category URL and retrieve its HTML content
    category_response = requests.get(category_url)
    category_html_content = category_response.content
    
    # Parse the HTML content using BeautifulSoup
    category_soup = BeautifulSoup(category_html_content, 'html.parser')
    
    # Find all the products in the category
    products = category_soup.find_all("div", {"class": "product-inner"})
    
    # Iterate through each product and retrieve the product information
    for product in products:
        # Get the product name
        product_name = product.find("h2", {"class": "product-title"}).text.strip()
        
        # Get the product description
        product_description = product.find("div", {"class": "product-excerpt"}).text.strip()
        
        # Get the product price
        product_price = product.find("span", {"class": "woocommerce-Price-amount amount"}).text.strip()
        
        # Print the product information
        print("Category: " + category_name)
        print("Product Name: " + product_name)
        print("Product Description: " + product_description)
        print("Product Price: " + product_price)
        