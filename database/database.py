# database for stand in implementations using files
import sqlite3
from datetime import datetime

# sets up database
# executed on program start
def setup():
    # connect to db file
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()
    
    # try to create generator table
    try:
        cur.execute("""CREATE TABLE generators (
                key text,
                name text,
                p_min real,
                p_max real,
                a real,
                b real,
                c real,
                date text,
                time text
            )""")
    except Exception as e:
        # table already exists
        print(str(e))

    # try to create network table
    try:
        cur.execute("""CREATE TABLE network (
                key text,        
                name text,
                p_load real,
                p_loss real,
                date text,
                time text
            )""")
    except Exception as e:
        # table already exists
        print(str(e))

    # try to create solution table
    try:
        cur.execute("""CREATE TABLE results (
                order_id text,
                date text,
                time text,
                key text,
                name text,
                p real,
                p_low real,
                p_high real,
                cost real
            )""")
    except Exception as e:
        # table already exists
        print(str(e))



# exports solution to output database
def export_solution(Order, Key, Name, P, P_low, P_high, cost):
    # if order label is empty raise xception
    if not Order:
        raise Exception("Failed to proccess order. Order ID is empty.")

    # get current date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    date, time = dt_string.split()

    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # add results into db
    n_g = len(Key)
    for i in range(n_g):
        cur.execute("INSERT INTO results VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (Order, date, time, 
                    Key[i], Name[i], P[i], P_low[i], P_high[i], cost[i]))
        conn.commit()



# load data in form apropriate for use in algorithm
def load_data():
    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # get all generator data
    cur.execute("SELECT * FROM generators")
    generators = cur.fetchall()

    if len(generators) == 0:
        raise Exception("Can't execute algorithm. No generators in network.")
    else:
        # zip is OP
        Key, Name, P_min, P_max, A, B, C, _, _ = map(list, zip(*generators))

    # get network data
    cur.execute("SELECT * FROM network")
    network = cur.fetchall()
    
    if len(network) == 0:
        raise Exception("Can't execute algortihm. No elements in power grid.")
    else:
        _, _, P_load, P_loss, _, _ = map(list, zip(*network)) 
    
    # calculate the sum of the load and loss powers
    p_load = sum(P_load)
    p_loss = sum(P_loss)

    return (Key, Name, P_min, P_max, p_load, p_loss, A, B, C)



# add generator to database
def add_generator(key, name, p_min, p_max, a, b, c):
    # if name or key is empty immediatly raise exception
    if not key:
        raise Exception("Failed to add generator to database. ID is empty.")
    if not name:
        raise Exception("Failed to add generator to database. Name of generator empty.")

    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # check if generator with the same ID has already been added
    cur.execute("SELECT * FROM generators WHERE key=?", (key,))
    search_res = cur.fetchone()

    # if result is not empty raise exception
    if search_res:
        raise Exception("Failed to add generator to database. Matching IDs.")

    # get current date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    date, time = dt_string.split()

    # insert the generator
    cur.execute("INSERT INTO generators VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (key, name, p_min, p_max, a, b, c, date, time))
    conn.commit()



# remove generator from database
def remove_generator(key):
    # if key is empty immediatly raise exception
    if not key:
        raise Exception("Failed to remove generator from database. ID is empty.")
    
    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # if key isn't in database raise exception
    cur.execute("SELECT * FROM generators WHERE key=?", (key,))
    search_res = cur.fetchone()

    # if result is empty raise exception (no matching key)
    if not search_res:
        raise Exception("Failed to remove generator from database. No matching ID.")
    
    # otherwise remove it from DB
    cur.execute("DELETE FROM generators WHERE key=?", (key,))
    conn.commit()



# add element to network database
def add_element(key, name, p_load, p_loss):
    # if name or key is empty immediatly raise exception
    if not key:
        raise Exception("Failed to add element to database. ID is empty.")
    if not name:
        raise Exception("Failed to add element to database. Name of element empty.")

    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # check if generator with the same ID has already been added
    cur.execute("SELECT * FROM network WHERE key=?", (key,))
    search_res = cur.fetchone()

    # if result is not empty raise exception
    if search_res:
        raise Exception("Failed to add element to database. Matching IDs.")

    # get current date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    date, time = dt_string.split()

    # insert the generator
    cur.execute("INSERT INTO network VALUES (?, ?, ?, ?, ?, ?)", (key, name, p_load, p_loss, date, time))
    conn.commit()



# remove element from network database
def remove_element(key):
    # if key is empty immediatly raise exception
    if not key:
        raise Exception("Failed to remove element from database. Key is empty.")

    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # if key isn't in database raise exception
    cur.execute("SELECT * FROM network WHERE key=?", (key,))
    search_res = cur.fetchone()

    # if result is empty raise exception (no matching key)
    if not search_res:
        raise Exception("Failed to remove element from database. No matching ID.")
    
    # otherwise remove it from DB
    cur.execute("DELETE FROM network WHERE key=?", (key,))
    conn.commit()



# helper function to get data from database
def get_data(table):
    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # pull everything from table
    cur.execute("SELECT * FROM " + table)
    results = list(map(list, cur.fetchall()))
    
    return results

# returns generator data in form of 10 x n_g table
def generator_data():
    return get_data("generators")

# returns network data in form of 7 x n_g table
def network_data():
    return get_data("network")

# returns current solution in form of 7 x n_g table
def solution_data():
    return get_data("results")