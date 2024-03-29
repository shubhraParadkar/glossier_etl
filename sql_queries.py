# DROP TABLES

users_table_drop = "DROP TABLE IF EXISTS users"
orders_table_drop = "DROP TABLE IF EXISTS orders"
sales_table_drop = "DROP TABLE IF EXISTS sales"
analytics_price_table_drop = "DROP TABLE IF EXISTS analytics_price"

# CREATE TABLES

user_table_create = ("""CREATE TABLE IF NOT EXISTS users \
(user_id int PRIMARY KEY, contact_email text NOT NULL, phone text NOT NULL, \
total_price numeric NOT NULL, buyer_accepts_marketing text, order_number numeric NOT NULL);
""")

orders_table_create = ("""CREATE TABLE IF NOT EXISTS orders \
(id numeric PRIMARY KEY, created_at text, updated_at text, total_price numeric NOT NULL, name text NOT NULL, \
order_number numeric NOT NULL, total_price_usd numeric, currency text, app_id numeric, order_status_url text NOT NULL, quantity numeric, product_id text);
""")

sales_table_create = ("""CREATE TABLE IF NOT EXISTS sales \
(id numeric PRIMARY KEY, total_price numeric, created_at text, order_number numeric NOT NULL, \
currency text, total_price_usd numeric, quantity numeric);
""")

analytics_price_table_create = ("""CREATE TABLE IF NOT EXISTS analytics_price \
(id numeric PRIMARY KEY, total_tax numeric, taxes_included text NOT NULL, \
total_discounts numeric NOT NULL, device_id text);
""")

#insert tables
user_table_insert = ("""INSERT INTO users (user_id, contact_email, phone, total_price, buyer_accepts_marketing, order_number) \
VALUES (%s, %s, %s, %s, %s, %s) \
ON CONFLICT (user_id)\
DO NOTHING;""")

orders_table_insert = ("""INSERT INTO orders (id, created_at, updated_at, total_price, name, order_number, total_price_usd, currency, app_id, order_status_url, quantity, product_id) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) \
ON CONFLICT (id)\
DO NOTHING;""")

sales_table_insert = ("""INSERT INTO sales (id, total_price, created_at, order_number, currency, total_price_usd, quantity) \
VALUES (%s, %s, %s, %s, %s, %s, %s) \
ON CONFLICT (id)\
DO NOTHING;""")

analytics_price_table_insert = ("""INSERT INTO analytics_price (id, total_tax, taxes_included, total_discounts, device_id) \
VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (id)\
DO NOTHING;""")


# QUERY LISTS
create_table_queries = [user_table_create, orders_table_create, sales_table_create, analytics_price_table_create]
drop_table_queries = [users_table_drop, orders_table_drop, sales_table_drop, analytics_price_table_drop]
