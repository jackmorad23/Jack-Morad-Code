# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:08:07 2023

@author: jackm
"""

# Importing modules
from flask import Flask, request, render_template
import wikipediaapi
import sqlite3

# Create a Flask application instance
app = Flask(__name__)

# SQLite database setup
# Use the 'with' statement for a safer connection that automatically closes
with sqlite3.connect('presidents_data.db') as conn:
    # Create a cursor to interact with the database
    cursor = conn.cursor()
    # Create a 'presidents_data' table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS presidents_data (id INTEGER PRIMARY KEY, president_name TEXT, president_biography TEXT)''')
    # Commit the changes to the database
    conn.commit()

# Wikipedia API setup
# Create a Wikipedia API object with the specified user-agent policy URL
wiki_wiki = wikipediaapi.Wikipedia('https://meta.wikimedia.org/wiki/User-Agent_policy')

# Define a route for the main page, supporting both GET and POST requests
@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if the request method is POST
    if request.method == 'POST':
        # Extract and clean up the names from the submitted form data
        president_names = [name.strip() for name in request.form['president_names'].split(',')]
        # Fetch biographies from Wikipedia API
        president_biographies = get_biographies(president_names)
        # Save names and biographies to the database
        save_to_database(president_names, president_biographies)
        # Render the index.html template with the obtained data
        return render_template('index.html', president_names=president_names, president_biographies=president_biographies)
    # Render the index.html template for GET requests
    return render_template('index.html')

# Function to fetch biographies from Wikipedia API
def get_biographies(president_names):
    # Use the 'with' statement for a safer connection that automatically closes
    with sqlite3.connect('presidents_data.db') as conn:
        # Create a cursor to interact with the database
        cursor = conn.cursor()
        # Initialize a list to store biographies
        president_biographies = []
        # Iterate through each president name
        for president_name in president_names:
            try:
                # Fetch the Wikipedia page for the given president name
                page_py = wiki_wiki.page(president_name)
                # Append the summary to the biographies list
                president_biographies.append(page_py.summary)
            except wikipediaapi.exceptions.PageError as e:
                # Handle errors when loading the Wikipedia page
                president_biographies.append("Error while loading page.")
        # Return the list of biographies
        return president_biographies

# Function to save names and biographies to the database
def save_to_database(president_names, president_biographies):
    # Use the 'with' statement for a safer connection that automatically closes
    with sqlite3.connect('presidents_data.db') as conn:
        # Create a cursor to interact with the database
        cursor = conn.cursor()
        # Iterate through each president name and biography
        data = [(name, bio) for name, bio in zip(president_names, president_biographies)]
        # Execute a single SQL query to insert all data into the 'presidents_data' table
        cursor.executemany('INSERT INTO presidents_data (president_name, president_biography) VALUES (?, ?)', data)
        # Commit the changes to the database
        conn.commit()

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
