import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# MongoDB connection
try:
    client = MongoClient('mongodb://localhost:27017/books_db')  # Replace with your MongoDB connection URL
    db = client['books_db']
    collection = 'db.books_collection.find()' 
    print("Connected to MongoDB successfully!")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    # exit()

base_url = "http://books.toscrape.com/catalogue/page-{}"
total_pages = 50

for page in range(1, total_pages + 1):
    url = base_url.format(page)
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('h3')
        
        for book in books:
            title = book.a['title']
            price = float(book.find_next('p', class_='price_color').text.strip('Â£'))
            availability = book.find_next('p', class_='instock availability').text.strip()
            rating = book.find_next('p', class_='star-rating')['class'][1]
            
            # Create a book document and insert it into MongoDB
            book_doc = {
                'title': title,
                'price': price,
                'availability': availability,
                'rating': rating
            }
            collection.insert_one(book_doc)

print("Scraping and storing data in MongoDB is complete.")
