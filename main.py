# main.py
from database import connect_to_mongodb, insert_user_data, insert_post_data
from api import fetch_users_data, fetch_posts_data

def main():
    # Connect to MongoDB
    client = connect_to_mongodb()
    db = client['user_post_data']  

    # Fetch Users data from API
    users_data = fetch_users_data()

    # Insert Users data into the database
    for user in users_data:
        insert_user_data(user, db)

        # Fetch and store Posts data for each user
        posts_data = fetch_posts_data(user['id'])
        for post in posts_data:
            insert_post_data(post, user['id'], db)

    # Close MongoDB connection
    client.close()

if __name__ == "__main__":
    main()
