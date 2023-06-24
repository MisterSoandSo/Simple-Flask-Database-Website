import sqlite3
import re


database_name = 'blackmarket.db'
infile = 'input.txt'
date = ""

def _create_database() -> None:
    conn = sqlite3.connect(database_name)
    c = conn.cursor()   
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='blackmarket'")
    result = c.fetchone()
    if not result:
        c.execute('''CREATE TABLE blackmarket
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                item TEXT,
                price TEXT,
                date TEXT)''')
    else:
        print("Table already exists ...")
    conn.close()

def _insert_Table(item = None,price = None,date = None):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("INSERT INTO blackmarket (item,price,date) VALUES (?,?,?)", (item,price,date))
    conn.commit()
    conn.close()

def _extract_dates(text) -> bool:
    global date
    date_pattern = re.compile(r'\b(\d{1,2}[./-]\d{1,2}[./-]\d{2,4})\b')
    date_matches = date_pattern.findall(text)
    if len(date_matches) != 0: 
        date = date_matches[0]
        return True
    else:
        return False

def _extract_items_data(text):
    i_name = None
    item_pattern = re.compile( r'#\d+\s*-\s*([\w\s]+)\s*\(Sell Price: \$[\d.]+\)')
    i_name = item_pattern.findall(text)
       
    item_pattern = re.compile( r'\$\d+(?:\.\d{1,2})?')
    item_obj = item_pattern.findall(text)
  
    i_price = [(price) for price in item_obj]
    
    return ''.join(i_name)[:-1],''.join(i_price)

def check_line(line):
    if not _extract_dates(line):
        item, price = _extract_items_data(line)
        if len(item) != 0 and len(price) != 0:
            _insert_Table(item,price,date)


with open(infile, 'r') as file:
    # Create Database
    _create_database()
    # Iterate over each line in the file
    for line in file:
        # Process each line
        check_line(line)