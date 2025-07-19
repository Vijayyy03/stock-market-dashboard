import pandas as pd
import sqlite3

# Load CSV data
csv_file = 'mock_stock_data.csv'
df = pd.read_csv(csv_file)

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect('stocks.db')
c = conn.cursor()

# Create companies table
c.execute('''
CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
''')

# Create stock_prices table
c.execute('''
CREATE TABLE IF NOT EXISTS stock_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    date TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    FOREIGN KEY(company_id) REFERENCES companies(id)
)
''')

# Insert companies and get their IDs
df_companies = pd.DataFrame({'name': df['company'].unique()})
for name in df_companies['name']:
    c.execute('INSERT OR IGNORE INTO companies (name) VALUES (?)', (name,))
conn.commit()

# Get company name to id mapping
c.execute('SELECT id, name FROM companies')
company_map = {name: cid for cid, name in c.fetchall()}

# Insert stock prices
for _, row in df.iterrows():
    c.execute('''
        INSERT INTO stock_prices (company_id, date, open, high, low, close, volume)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        company_map[row['company']],
        row['date'],
        row['open'],
        row['high'],
        row['low'],
        row['close'],
        row['volume']
    ))
conn.commit()

print('Data loaded successfully!')
conn.close() 