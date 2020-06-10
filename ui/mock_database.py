from datetime import datetime

# exports solution to output database
# appends to end of file

def export_solution(Order, Key, Name, P, P_low, P_high, cost):
    # if order label is empty raise xception
    if not Order:
        raise Exception("Failed to proccess order. Order ID is empty.")

    # count number of lines in file
    with open("mock_database/results.txt","r") as peek:
        line_count = 0
        for line in peek:
            line_count += 1

    # overwrite old solution
    with open("mock_database/results.txt", "a") as outfile:
        # get current date and time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        num_generators = len(Key)
        # output everything to output folder
        for gi in range(num_generators):
            outfile.write(str(gi + line_count) + " " + Order + " " + dt_string + " " + str(Key[gi]) + " " + str(Name[gi]) + " " + 
            str(P[gi]) + " " + str(P_low[gi]) + " " + str(P_high[gi]) + " " + str(cost[gi]) + "\n")



# load data in form apropriate for use in algorithm
def load_data():
    # parameters from database of generators
    P_min = []
    P_max = []
    A = []
    B = []
    C = []
    ID = []
    Name = []
    Key = []
    
    # numbers obtained by adding up load and loss powers for all components
    # from database of components
    p_load = 0
    p_loss = 0

    # pull lines from file and make arrays
    with open("mock_database/generators.txt", "r") as genfile:
        for line in genfile:
            id, key, name, P_minv, P_maxv, av, bv, cv, date, time = tuple(line.split())
            ID.append(id)
            Name.append(name)
            Key.append(key)
            P_min.append(float(P_minv))
            P_max.append(float(P_maxv))
            A.append(float(av))
            B.append(float(bv))
            C.append(float(cv))

    with open("mock_database/network.txt", "r") as netfile:
        for line in netfile:
            id, key, name, p_loadv, p_lossv, date, time = tuple(line.split())
            p_load += float(p_loadv)
            p_loss += float(p_lossv)

    return (ID, Key, Name, P_min, P_max, p_load, p_loss, A, B, C)



# add generator to database
def add_generator(key, name, p_min, p_max, a, b, c):
    # if name or key is empty immediatly raise exception
    if not key:
        raise Exception("Failed to add generator to database. ID is empty.")
    if not name:
        raise Exception("Failed to add generator to database. Name of generator empty.")

    # count number of lines in file
    # also check if generator has already been added (raise exception)
    with open("mock_database/generators.txt","r") as peek:
        line_count = 0
        
        for line in peek:
            # read data for the current line
            idv, keyv, namev, P_minv, P_maxv, av, bv, cv, date, time = line.split()
            if keyv == key:
                raise Exception("Failed to add generator to database. Matching IDs.")

            line_count += 1

    # set the id to the line_count (0 - indexed)
    id = str(line_count)

    # the setting "a" appends to end of file, which we want
    with open("mock_database/generators.txt","a") as genfile:
        # get current date and time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # add generator at end of file
        genfile.write(id + " " + key + " " + name + " " + str(p_min) + " " + str(p_max) + " " 
        + str(a) + " " + str(b) + " " + str(c) + " " + dt_string + "\n")


# remove generator from database
def remove_generator(key):
    # if key is empty immediatly raise exception
    if not key:
        raise Exception("Failed to remove generator from database. ID is empty.")

    # go through the database and find the line with the given key
    # if the key doesn't exist raise exception
    with open("mock_database/generators.txt","r+") as genfile:
        found_key = False
        # read all lines first
        file_lines = genfile.readlines()
        # set cursor back to the beggining
        genfile.seek(0)

        for line in file_lines:
            idv, keyv, namev, P_minv, P_maxv, av, bv, cv, date, time = line.split()
            
            if key == keyv:
                found_key = True
            else:
                # write the line to the new file
                genfile.write(line)
        
        # remove excess lines <-> effectively we have removed a row
        genfile.truncate()

        if not found_key:
            raise Exception("Failed to remove generator from database. No matching ID.")


# add element to network database
def add_element(key, name, p_load, p_loss):
    # if name or key is empty immediatly raise exception
    if not key:
        raise Exception("Failed to add element to database. ID is empty.")
    if not name:
        raise Exception("Failed to add element to database. Name of element empty.")

    # count number of lines in file
    # also check if element has already been added (raise exception)
    with open("mock_database/network.txt","r") as peek:
        line_count = 0
        
        for line in peek:
            # read data for the current line
            idv, keyv, namev, p_loadv, p_lossv, date, time = line.split()
            if keyv == key:
                raise Exception("Failed to add element to database. Matching IDs.")

            line_count += 1

    # set the id to the line_count (0 - indexed)
    id = str(line_count)

    # the setting "a" appends to end of file, which we want
    with open("mock_database/network.txt","a") as netfile:
        # get current date and time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # add element at end of file
        netfile.write(id + " " + key + " " + name + " " + str(p_load) + " " + str(p_loss) + " "  + dt_string + "\n")


# remove element from network database
def remove_element(key):
    # if key is empty immediatly raise exception
    if not key:
        raise Exception("Failed to remove element from database. Key is empty.")

    # go through the database and find the line with the given id
    # if the id doesn't exist raise exception
    with open("mock_database/network.txt","r+") as netfile:
        found_key = False
        # read all lines first
        file_lines = netfile.readlines()
        # set cursor back to the beggining
        netfile.seek(0)

        for line in file_lines:
            idv, keyv, namev, p_loadv, p_lossv, date, time = line.split()
            
            if keyv == key:
                found_key = True
            else:
                # write the line to the new file
                netfile.write(line)
        
        # remove excess lines <-> effectively we have removed a row
        netfile.truncate()

        if not found_key:
            raise Exception("Failed to remove element from database. No matching id.")


# helper function for obtaining data from database in form of table
def get_data(database):
    return [line.split() for line in database]


# returns generator data in form of 10 x n_g table
def generator_data():
    with open("mock_database/generators.txt","r") as genfile:
        return get_data(genfile)

# returns network data in form of 7 x n_g table
def network_data():
    with open("mock_database/network.txt","r") as netfile:
        return get_data(netfile)

# returns current solution in form of 7 x n_g table
def solution_data():
    with open("mock_database/results.txt","r") as resfile:
        return get_data(resfile)