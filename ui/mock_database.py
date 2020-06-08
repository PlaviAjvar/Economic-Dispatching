from datetime import datetime

# exports solution to output database
def export_solution(ID, Name, P, P_low, P_high, cost):
    # overwrite old solution
    with open("mock_database/results.txt", "w") as outfile:
        num_generators = len(ID)
        # output everything to output folder
        for gi in range(num_generators):
            outfile.write(str(ID[gi]) + " " + str(Name[gi]) + " " + str(P[gi]) + " " +
            str(P_low[gi]) + " " + str(P_high[gi]) + " " + cost(P[gi]))


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
    
    # numbers obtained by adding up load and loss powers for all components
    # from database of components
    P_load = 0
    P_loss = 0

    # pull lines from file and make arrays
    with open("mock_database/generators.txt", "r") as genfile:
        for line in genfile:
            id, name, P_minv, P_maxv, av, bv, cv, date, time = tuple(line.split())
            ID.append(id)
            Name.append(name)
            P_min.append(float(P_minv))
            P_max.append(float(P_maxv))
            A.append(float(av))
            B.append(float(bv))
            C.append(float(cv))

    with open("mock_database/network.txt", "r") as netfile:
        for line in netfile:
            id, name, P_loadv, P_lossv, date, time = tuple(line.split())
            P_load += float(P_loadv)
            P_loss += float(P_lossv)

    return (ID, Name, P_min, P_max, P_load, P_loss, A, B, C)



# add generator to database
def add_generator(name, p_min, p_max, a, b, c):
    # if name is empty immediatly raise exception
    if not name:
        raise Exception("Failed to add generator to database. Name of generator empty.")

    # count number of lines in file
    # also check if generator has already been added (raise exception)
    with open("mock_database/generators.txt","r") as peek:
        line_count = 0
        
        for line in peek:
            # read data for the current line
            idv, namev, P_minv, P_maxv, av, bv, cv, date, time = line.split()
            if namev == name:
                raise Exception("Failed to add generator to database, matching file names.")

            line_count += 1

    # set the id to the line_count (0 - indexed)
    id = str(line_count)

    # the setting "a" appends to end of file, which we want
    with open("mock_database/generators.txt","a") as genfile:
        # get current date and time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # add generator at end of file
        genfile.write(id + " " + name + " " + str(p_min) + " " + str(p_max) + " " 
        + str(a) + " " + str(b) + " " + str(c) + " " + dt_string)


# remove generator from database
def remove_generator(id):
    # go through the database and find the line with the given id
    # if the id doesn't exist raise exception
    with open("mock_database/generators.txt","r+") as genfile:
        found_id = False
        # read all lines first
        file_lines = genfile.readlines()
        # set cursor back to the beggining
        genfile.seek(0)

        for line in file_lines:
            idv, namev, P_minv, P_maxv, av, bv, cv, date, time = line.split()
            
            if id == idv:
                found_id = True
            else:
                # write the line to the new file
                genfile.write(line)
        
        # remove excess lines <-> effectively we have removed a row
        genfile.truncate()

        if not found_id:
            raise Exception("Failed to remove generator from database, no matching id.")


# add element to network database
def add_element(name, p_load, p_loss):
    # if name is empty immediatly raise exception
    if not name:
        raise Exception("Failed to add element to database. Name of element empty.")

    # count number of lines in file
    # also check if element has already been added (raise exception)
    with open("mock_database/network.txt","r") as peek:
        line_count = 0
        
        for line in peek:
            # read data for the current line
            idv, namev, p_loadv, p_lossv, date, time = line.split()
            if namev == name:
                raise Exception("Failed to add element to database, matching file names.")

            line_count += 1

    # set the id to the line_count (0 - indexed)
    id = str(line_count)

    # the setting "a" appends to end of file, which we want
    with open("mock_database/network.txt","a") as netfile:
        # get current date and time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # add element at end of file
        netfile.write(id + " " + name + " " + str(p_load) + " " + str(p_loss) + " "  + dt_string)


# remove element from network database
def remove_element(id):
    # go through the database and find the line with the given id
    # if the id doesn't exist raise exception
    with open("mock_database/network.txt","r+") as netfile:
        found_id = False
        # read all lines first
        file_lines = netfile.readlines()
        # set cursor back to the beggining
        netfile.seek(0)

        for line in file_lines:
            idv, namev, p_loadv, p_lossv, date, time = line.split()
            
            if id == idv:
                found_id = True
            else:
                # write the line to the new file
                netfile.write(line)
        
        # remove excess lines <-> effectively we have removed a row
        netfile.truncate()

        if not found_id:
            raise Exception("Failed to remove element from database, no matching id.")


# helper function for obtaining data from database in form of table
def get_data(database):
    return [line.split() for line in database]


# returns generator data in form of 9 x n_g table
def generator_data():
    with open("mock_database/generators.txt","r") as genfile:
        return get_data(genfile)

# returns network data in form of 6 x n_g table
def network_data():
    with open("mock_database/network.txt","r") as netfile:
        return get_data(netfile)

# returns current solution in form of 6 x n_g table
def solution_data():
    with open("mock_database/results.txt","r") as resfile:
        return get_data(resfile)