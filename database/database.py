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

    # get current date and time ymd format
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
    date, time = dt_string.split()

    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # check if order with the same ID has been added
    cur.execute("SELECT * FROM results WHERE order_id=?", (Order,))
    search_res = cur.fetchone()

    # if result is not empty raise exception
    if search_res:
        raise Exception("Failed to add result to database. Matching order ID.")

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
    # if some fields are empty empty immediatly raise exception
    if not key:
        raise Exception("Failed to add generator to database. ID is empty.")
    if not name:
        raise Exception("Failed to add generator to database. Name of generator empty.")
    if not p_min or not p_max or not a or not b or not c:
        raise Exception("Failed to add generator to database. Some fields are empty.")
    
    # convert strings to floats
    p_min, p_max, a, b, c = map(float, (p_min, p_max, a, b, c))

    if p_min > p_max:
        raise Exception("Failed to add generator to database. P_min cannot be larger than P_max.")

    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # check if generator with the same ID has already been added
    cur.execute("SELECT * FROM generators WHERE key=?", (key,))
    search_res = cur.fetchone()

    # if result is not empty raise exception
    if search_res:
        raise Exception("Failed to add generator to database. Matching IDs.")

    # get current date and time ymd format
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
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
    if not p_load and not p_loss:
        raise Exception("Failed to add element to database. Both P_load and P_loss fields empty.")

    # hacky way to make float default to zero
    p_load = float("0" + p_load)
    p_loss = float("0" + p_loss)

    # convert string -> float
    p_load, p_loss = float(p_load), float(p_loss)

    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # check if generator with the same ID has already been added
    cur.execute("SELECT * FROM network WHERE key=?", (key,))
    search_res = cur.fetchone()

    # if result is not empty raise exception
    if search_res:
        raise Exception("Failed to add element to database. Matching IDs.")

    # get current date and time ymd format
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
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



# returns generator data in form of 10 x n_g table

def generator_data(gen_id, gen_name, date_after, date_before):
    # form query from input data
    query_list = []
    var_list = []

    if gen_id:
        query_list.append("key = ?")
        var_list.append(gen_id)
    
    if gen_name:
        query_list.append("name = ?")
        var_list.append(gen_name)
    
    if date_after:
        query_list.append("date >= ?")
        var_list.append(date_after)
    
    if date_before:
        query_list.append("date <= ?")
        var_list.append(date_before)

    return fetch_data("generators", query_list, var_list)



# returns network data in form of 7 x n_g table

def network_data(elem_id, elem_name, date_after, date_before):
    # form query from input data
    query_list = []
    var_list = []

    if elem_id:
        query_list.append("key = ?")
        var_list.append(elem_id)
    
    if elem_name:
        query_list.append("name = ?")
        var_list.append(elem_name)
    
    if date_after:
        query_list.append("date >= ?")
        var_list.append(date_after)
    
    if date_before:
        query_list.append("date <= ?")
        var_list.append(date_before)

    return fetch_data("network", query_list, var_list)



# returns current solution in form of 7 x n_g table

def solution_data(order_id, generator_id, generator_name, date_after, date_before,
                                        power_low, power_high, cost_low, cost_high):
    # form query from input data
    query_list = []
    var_list = []

    if order_id:
        query_list.append("order_id = ?")
        var_list.append(order_id)
    
    if generator_id:
        query_list.append("key = ?")
        var_list.append(generator_id)
    
    if generator_name:
        query_list.append("name = ?")
        var_list.append(generator_name)
    
    if date_after:
        query_list.append("date >= ?")
        var_list.append(date_after)
    
    if date_before:
        query_list.append("date <= ?")
        var_list.append(date_before)

    if power_low:
        query_list.append("p >= ?")
        var_list.append(float(power_low))
    
    if power_high:
        query_list.append("p <= ?")
        var_list.append(float(power_high))
    
    if cost_low:
        query_list.append("cost >= ?")
        var_list.append(float(cost_low))
    
    if cost_high:
        query_list.append("cost <= ?")
        var_list.append(float(cost_high))

    return fetch_data("results", query_list, var_list)



# helper function for fetching data from database

def fetch_data(table, query_list, var_list):
    # create db cursor
    conn = sqlite3.connect("database/dispatching.db")
    cur = conn.cursor()

    # join all queries with AND inbetween
    query = " AND ".join(query_list)
    
    # pull all results where query is satisfied
    if query_list:
        cur.execute("SELECT * FROM " + table + " WHERE " + query, tuple(var_list))

    # if there is no query pull all data
    else:
        cur.execute("SELECT * FROM " + table)

    return cur.fetchall()


# function which fixes date formatting from y/m/d to d/m/y
def fix_date(date):
    # if empty return empty string
    if not date:
        return ""

    y, m, d = date.split("/")
    return "/".join([d, m, y])