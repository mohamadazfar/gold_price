import requests
import psycopg2
import configparser

url = "https://data-asg.goldprice.org/dbXRates/MYR"
parser = configparser.ConfigParser()
parser.read('config.ini')

connection = psycopg2.connect(host=parser['postgresql']['host'], port=parser['postgresql']['port'], database=parser['postgresql']['database'], user=parser['postgresql']['user'], password=parser['postgresql']['password'])

query = """INSERT into test (amount) VALUES (%s)"""

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.06'}

response = requests.get(url, headers=headers)

x = response.json()

amount = x['items'][0]['xauPrice']

cursor = connection.cursor()

cursor.execute(query,[amount] )

connection.commit()

connection.close()

cursor.close()