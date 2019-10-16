import os
import glob
import psycopg2
import pandas as pd
import numpy as np
from sql_queries import *


# cur parameter: actual connection to DATABASE
# filepath parameter: JSON file path
# this function receive a connection and json path parameters.
# read the information using pandas and insert into database.
def process_data_file(cur, filepath):
    # open data file
    df = pd.read_json(filepath, orient='columns')

    # insert user record
    for order in df['orders']:
        user_id = order['user_id']
        contact_email = order['contact_email']
        phone = order['phone']
        total_price = order['total_price']
        buyer_accepts_marketing = order['buyer_accepts_marketing']
        order_number = order['order_number']

    user_data = [user_id, contact_email, phone, total_price, buyer_accepts_marketing, order_number]
    cur.execute(user_table_insert, user_data)

    #insert order data
    for order in df['orders']:
        id = order['id']
        created_at = order['created_at']
        updated_at = order['updated_at']
        total_price = order['total_price']
        name = order['name']
        order_number = order['order_number']
        total_price_usd = order['total_price_usd']
        currency = order['currency']
        app_id = order['app_id']
        order_status_url = order['order_status_url']

    for line_items in df['orders'][0]['line_items']:
        quantity = line_items['quantity']
        product_id = line_items['product_id']

    orders_data = [id, created_at, updated_at, total_price, name, order_number, total_price_usd, currency, app_id, order_status_url, quantity, product_id]

    cur.execute(orders_table_insert, orders_data)

    #insert data for sales_table
    for order in df['orders']:
        id = order['id']
        total_price = order['total_price']
        created_at = order['created_at']
        order_number = order['order_number']
        currency = order['currency']
        total_price_usd = order['total_price_usd']
        financial_status = order['financial_status']

    for line_items in df['orders'][0]['line_items']:
        quantity = line_items['quantity']

    sales_data = [id, total_price, created_at, order_number, currency, total_price_usd, quantity]

    cur.execute(sales_table_insert, sales_data)

    #insert data for analytics_price_table
    for order in df['orders']:
        id = order['id']
        total_tax = order['total_tax']
        taxes_included = order['taxes_included']
        total_discounts = order['total_discounts']
        device_id = order['device_id']

    analytics_price_data = [id, total_tax, taxes_included, total_discounts, device_id]

    cur.execute(analytics_price_table_insert, analytics_price_data)



def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=data-engineering-test.dev.glossier.io dbname=shubhra_db user=shubhra password=iheartcloudpaint port=80")
    cur = conn.cursor()

    process_data(cur, conn, filepath='/Users/shubhraparadkar/Documents/data', func=process_data_file)

    conn.close()


if __name__ == "__main__":
    main()
