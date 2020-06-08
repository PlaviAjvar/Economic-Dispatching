# database for stand in implementations using files
import mock_database


# exports solution to output database
def export_solution(ID, Name, P, P_low, P_high, cost):
    mock_database.export_solution(ID, Name, P, P_low, P_high, cost)

# load data in form apropriate for use in algorithm
def load_data():
    return mock_database.load_data()

# add generator to database
def add_generator(name, p_min, p_max, a, b, c):
    mock_database.add_generator(name, p_min, p_max, a, b, c)

# remove generator from database
def remove_generator(id):
    mock_database.remove_generator(id)

# add element to network database
def add_element(name, p_load, p_loss):
    mock_database.add_element(name, p_load, p_loss)

# remove element from network database
def remove_element(id):
    mock_database.remove_element(id)

# returns generator data in form of 9 x n_g table
def generator_data():
    return mock_database.generator_data()

# returns network data in form of 6 x n_g table
def network_data():
    return mock_database.network_data()

# returns current solution in form of 6 x n_g table
def solution_data():
    return mock_database.solution_data()
