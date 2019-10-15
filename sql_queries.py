# DROP TABLES

#user_table_drop = "DROP TABLE IF EXISTS songplays"
users_table_drop = "DROP TABLE IF EXISTS users"
orders_table_drop = "DROP TABLE IF EXISTS orders"
#artist_table_drop = "DROP TABLE IF EXISTS artists"
#time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

#songplays_table_create = ("""CREATE TABLE IF NOT EXISTS songplays \
#(songplay_id SERIAL PRIMARY KEY, \
#start_time bigint NOT NULL, user_id int NOT NULL, level varchar, song_id varchar, \
#artist_id varchar, session_id int, location varchar, user_agent varchar);
#"")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users \
(user_id int PRIMARY KEY, contact_email varchar NOT NULL, phone int NOT NULL, \
browser_ip varchar, order_number int NOT NULL);
""")

orders_table_create = ("""CREATE TABLE IF NOT EXISTS orders \
(id varchar PRIMARY KEY, total_price numeric NOT NULL, name varchar NOT NULL, \
order_number int NOT NULL, order_status_url varchar NOT NULL);
""")

# artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists \
# (artist_id varchar PRIMARY KEY, name varchar NOT NULL, location varchar, \
# lattitude numeric, longitude numeric);
# """)
#
# time_table_create = ("""CREATE TABLE IF NOT EXISTS time \
# (start_time bigint PRIMARY KEY, hour int NOT NULL, day int NOT NULL, \
# week int NOT NULL, month int NOT NULL, year int NOT NULL, weekday int NOT NULL);
# """)

# INSERT RECORDS

# songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, \
# artist_id, session_id, location, user_agent) \
# VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
# """)

user_table_insert = ("""INSERT INTO users (user_id, contact_email, phone, browser_ip, order_number) \
VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (user_id)\
DO UPDATE SET level = EXCLUDED.level;""")

orders_table_insert = ("""INSERT INTO orders (id, total_price, name, order_number, order_status_url) \
VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (id)\
DO NOTHING;""")

# artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, lattitude, longitude) \
# VALUES (%s, %s, %s, %s, %s)
# ON CONFLICT (artist_id)\
# DO NOTHING;""")
#
# time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, \
# year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) \
# ON CONFLICT (start_time)\
# DO NOTHING;""")

# FIND SONGS

orders_select = ("""SELECT id, orders.id FROM orders \
JOIN users ON orders.order_number = users.order_number \
WHERE orders.id = %s AND users.id = %s AND orders.total_price = %s\
;""")

# QUERY LISTS

# create_table_queries = [songplay_table_create, user_table_create,
#                         song_table_create, artist_table_create, time_table_create]
# drop_table_queries = [songplay_table_drop, user_table_drop,
#                       song_table_drop, artist_table_drop, time_table_drop]

create_table_queries = [user_table_create, orders_table_create]
drop_table_queries = [users_table_drop, orders_table_drop]
