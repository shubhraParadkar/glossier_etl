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
def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, orient='columns')
    # insert song record
    for order in df['orders']:
        user_id = order['user_id']
        contact_email = order['contact_email']
        phone = order['phone']
        browser_ip = order['browser_ip']
        order_number = order['order_number']

    user_data = [user_id, contact_email, phone, browser_ip, order_number]
    #print(user_data)
    cur.execute(user_table_insert, user_data)

    # orders_data = df[['id', 'total_price', 'name',
    #                   'order_number', 'order_status_url']].values[0].tolist()
    # cur.execute(orders_table_insert, orders_data)

# this function receive a connection and json path parameters.
# read the information using pandas and insert into database.


# def process_log_file(cur, filepath):
#     # open log file
#     df = pd.read_json(filepath, lines=True)
#
#     # filter by NextSong action
#     df = df[df['page'] == 'NextUser']
#
#     # convert timestamp column to datetime
#     t = pd.to_datetime(df['ts'], unit='ms')
#
#     # insert time data records
#     time_data = np.transpose(np.array([df['ts'].values, t.dt.hour.values, t.dt.day.values, t.dt.week.values,
#                                        t.dt.month.values, t.dt.year.values, t.dt.weekday.values]))
#     column_labels = ('ts', 'hour', 'day', 'week', 'month', 'year', 'weekday')
#     time_df = pd.DataFrame(data=time_data, columns=column_labels)
#
#     # iterate into every row and create a insert statement for every row
#     for i, row in time_df.iterrows():
#         cur.execute(time_table_insert, list(row))
#
#     # load user table
#     user_df = df[['userId', 'contact_email', 'phone', 'browser_ip', 'order_number']]
#
#     # insert user records
#     for i, row in user_df.drop_duplicates().iterrows():
#         cur.execute(user_table_insert, row)
#
#     # insert songplay records
#     for index, row in df.iterrows():
#         # get songid and artistid from song and artist tables
#         cur.execute(orders_select, (row.order.encode('utf-8'),
#                                   row.user.encode('utf-8'), row.length))
#
#         # retrieve the information by tuples
#         results = cur.fetchone()
#         # asing song_id and artist_id into variables
#         id, user_id = results if results else (None, None)
#
#         # insert songplay record
#         songplay_data = (row.ts, row.user_id, row.contact_email, id, order_number,
#                          row.sessionId, row.location, row.userAgent)
#         cur.execute(orders_table_insert, orders_data)

# iterate into every directory and retrieve json files to process data


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

    process_data(cur, conn, filepath='/Users/shubhraparadkar/Documents/data', func=process_song_file)
    #process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
