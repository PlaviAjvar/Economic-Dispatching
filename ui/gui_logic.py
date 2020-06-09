# dirty imports messing with path

"""
import os
import sys
top_level = os.path.abspath("..")
sys.path.append(top_level)
"""

import algorithm, database
# sys.path.append("/ui")
import dispatching, gendata, generators, grid, gridata, optimize, solution
from PyQt5 import QtCore, QtGui, QtWidgets

# default number of maximum iterations
default_iter = 10000

# helper function for loading generator database into table widget
def gen_load():
    global ui_gdata, gdata_col
    # load data from database
    data = database.generator_data()
    ui_gdata.tableWidget.setRowCount(0)
    gdata_col = 10
    ui_gdata.tableWidget.setColumnCount(gdata_col)

    # add a row
    ui_gdata.tableWidget.insertRow(0)
    offset = 1

    # add row with labels for better readibility of database
    ui_gdata.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Database ID"))
    ui_gdata.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("ID"))
    ui_gdata.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Name"))
    ui_gdata.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem("P_low [MW]"))
    ui_gdata.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem("P_high [MW]"))
    ui_gdata.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem("a [$/h]"))
    ui_gdata.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem("b [$/h]"))
    ui_gdata.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem("c [$/h]"))
    ui_gdata.tableWidget.setItem(0, 8, QtWidgets.QTableWidgetItem("Date"))
    ui_gdata.tableWidget.setItem(0, 9, QtWidgets.QTableWidgetItem("Time"))

    for table_row_number, row in enumerate(data):
        # because we add some rows before
        row_number = table_row_number + offset
        ui_gdata.tableWidget.insertRow(row_number)
        for col_number, entry in enumerate(row):       
            ui_gdata.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(entry)))

# helper function for loading network database into table widget
def net_load():
    global ui_ndata, ndata_col
    # load data from database
    data = database.network_data()
    ui_ndata.tableWidget.setRowCount(0)
    ndata_col = 7
    ui_ndata.tableWidget.setColumnCount(ndata_col)

    # add a row
    ui_ndata.tableWidget.insertRow(0)
    offset = 1

    # add row with labels for readibility
    ui_ndata.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Database ID"))
    ui_ndata.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("ID"))
    ui_ndata.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Name"))
    ui_ndata.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem("P_load [MW]"))
    ui_ndata.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem("P_loss [MW]"))
    ui_ndata.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem("Date"))
    ui_ndata.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem("Time"))

    for table_row_number, row in enumerate(data):
        row_number = table_row_number + offset
        ui_ndata.tableWidget.insertRow(row_number)
        for col_number, entry in enumerate(row):
            ui_ndata.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(entry)))

# helper function for loading solution database into table widget
def sol_load():
    global ui_sol, sol_col
    # load data from database
    data = database.solution_data()
    ui_sol.tableWidget.setRowCount(0)
    # label, name, P_low, P_high, P, cost
    sol_col = 7
    ui_sol.tableWidget.setColumnCount(sol_col)

    # calculate total power and total cost
    P_total = 0
    cost_total = 0

    # add two rows
    ui_sol.tableWidget.insertRow(0)
    offset = 1

    # add row with labels for readibility
    ui_sol.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Database ID"))
    ui_sol.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("ID"))
    ui_sol.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Name"))
    ui_sol.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem("Power [MW]"))
    ui_sol.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem("P_low [MW]"))
    ui_sol.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem("P_high [MW]"))
    ui_sol.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem("Cost [$]"))


    for table_row_number, row in enumerate(data):
        row_number = table_row_number + offset
        ui_sol.tableWidget.insertRow(row_number)
        for col_number, entry in enumerate(row):
            ui_sol.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(entry)))
            if col_number == sol_col - 4:
                P_total += float(entry)
            elif col_number == sol_col - 1:
                cost_total += float(entry)
    
    ui_sol.total_cost = "The total cost of electrical production is " + str(cost_total)
    ui_sol.supplied_power = "The total supplied power from the generators is " + str(P_total)


# opens generator editting window
def open_editgen():
    global MainWindowGen, ui_gen
    MainWindowGen = QtWidgets.QMainWindow()
    ui_gen = generators.Ui_MainWindow()
    ui_gen.setupUi(MainWindowGen)
    editgen_ui_bindings()
    MainWindowGen.show()

# opens network editting window
def open_editnetwork():
    global MainWindowNet, ui_net
    MainWindowNet = QtWidgets.QMainWindow()
    ui_net = grid.Ui_MainWindow()
    ui_net.setupUi(MainWindowNet)
    editnet_ui_bindings()
    MainWindowNet.show()

# opens main window
def open_main():
    global MainWindow, ui
    MainWindow = QtWidgets.QMainWindow()
    ui = dispatching.Ui_MainWindow()
    ui.setupUi(MainWindow)
    main_ui_bindings()
    MainWindow.show()

# display solution data
def open_solution():
    global MainWindowSol, ui_sol
    MainWindowSol = QtWidgets.QMainWindow()
    ui_sol = solution.Ui_MainWindow()
    ui_sol.setupUi(MainWindowSol)
    sol_ui_bindings()
    MainWindowSol.show()
    sol_load()

# display generator data
def open_generator_data():
    global MainWindowGendat, ui_gdata
    MainWindowGendat = QtWidgets.QMainWindow()
    ui_gdata = gendata.Ui_MainWindow()
    ui_gdata.setupUi(MainWindowGendat)
    gdata_ui_bindings()
    MainWindowGendat.show()
    gen_load()

# open and display the network database
def open_network_data():
    global MainWindowNetdat, ui_ndata
    MainWindowNetdat = QtWidgets.QMainWindow()
    ui_ndata = gridata.Ui_MainWindow()
    ui_ndata.setupUi(MainWindowNetdat)
    ndata_ui_bindings()
    MainWindowNetdat.show()
    net_load()

# opens optimization window
def open_optimize():
    global MainWindowOpt, ui_opt
    MainWindowOpt = QtWidgets.QMainWindow()
    ui_opt = optimize.Ui_MainWindow()
    ui_opt.setupUi(MainWindowOpt)
    MainWindowOpt.show()

    # get number of iterations
    text_box = ui.max_iter_txt.toPlainText()
    if text_box == "":
        max_iter = default_iter
    else:
        max_iter = int(text_box)
    # clear the textbox
    ui.max_iter_txt.clear()
    
    # run algorithm
    (ID, Key, Name, P_min, P_max, p_load, p_loss, A, B, C) = database.load_data()
    try:
        (P, iter_count, total_price, total_power, total_power_loss) = algorithm.run_algorithm(P_min, 
        P_max, p_load, p_loss, A, B, C, max_iter)

        # export solution to database
        database.export_solution(ID, Key, Name, P, P_min, P_max, algorithm.cost_vector(P, A, B, C))

        # change textbook to display information about the solution
        _translate = QtCore.QCoreApplication.translate
        ui_opt.textEdit.setText("Number of iterations: " + str(iter_count) + "\nTotal price: " + str(total_price) + 
                        " [$]\nTotal power: " + str(total_power) + " [MW]\nTotal power loss: " + str(total_power_loss) + " [MW]")
    except Exception as e:
        # display error message
        show_fail(str(e))    

        # then change the textbox to error has occured
        ui_opt.textEdit.setText("No information. Error has occured.")
    

# bind everything in solution showing panel
def sol_ui_bindings():
    global ui_sol
    # bind buttons
    ui_sol.refresh_btn.clicked.connect(sol_load)

# bind everything in the generator showing pannel
def gdata_ui_bindings():
    global ui_gdata
    # bind buttons
    ui_gdata.refresh_btn.clicked.connect(gen_load)

# bind everything in the circuit element showing pannel
def ndata_ui_bindings():
    global ui_ndata
    # bind buttons
    ui_ndata.refresh_btn.clicked.connect(net_load)

# bind everything in edit generator pannel
def editgen_ui_bindings():
    # bind buttons
    global ui_gen
    ui_gen.addgen_btn.clicked.connect(add_generator)
    ui_gen.remgen_btn.clicked.connect(remove_generator)
    ui_gen.disp_dat_btn.clicked.connect(open_generator_data)

# bind everything in edit network panel
def editnet_ui_bindings():
    # bind buttons
    global ui_net
    ui_net.add_ele_btn.clicked.connect(add_element)
    ui_net.rem_ele_btn.clicked.connect(remove_element)
    ui_net.disp_data_btn.clicked.connect(open_network_data)


# bind everything in main pannel
def main_ui_bindings():
    # bind buttons
    global ui
    ui.editgen_btn.clicked.connect(open_editgen)
    ui.editnetwork_btn.clicked.connect(open_editnetwork)
    ui.optimize_btn.clicked.connect(open_optimize)
    ui.resultHistory.clicked.connect(open_solution)

# add generator to database
def add_generator():
    global MainWindowGen, ui_gen
    
    # get data from textboxes
    # just add zero so that "" is defined as zero :P
    key = ui_gen.iDLineEditin.displayText()
    name = ui_gen.nameLineEdit_add.displayText()
    P_min = float("0" + ui_gen.pminLineEdit.displayText())
    P_max = float("0" + ui_gen.pmaxLineEdit_2.displayText())
    a = float("0" + ui_gen.aLineEdit.displayText())
    b = float("0" + ui_gen.bLineEdit.displayText())
    c = float("0" + ui_gen.cLineEdit.displayText())

    # add to database
    try:
        database.add_generator(key, name, P_min, P_max, a, b, c)
    except Exception as e:
        show_fail(str(e))

    # clear textboxes
    ui_gen.iDLineEditin.clear()
    ui_gen.nameLineEdit_add.clear()
    ui_gen.pminLineEdit.clear()
    ui_gen.pmaxLineEdit_2.clear()
    ui_gen.aLineEdit.clear()
    ui_gen.bLineEdit.clear()
    ui_gen.cLineEdit.clear()

# add generator to database
def remove_generator():
    global MainWindowGen, ui_gen
    
    # get data from textboxes
    key = ui_gen.idLineEdit.displayText()

    # add to database
    try:
        database.remove_generator(key)
    except Exception as e:
        show_fail(str(e))
    
    # clear textboxes
    ui_gen.idLineEdit.clear()
        

# helper function which gives popup when failing to add or remove to db
def show_fail(text):
    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Error")
    msg.setText(text)
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.exec_()

# add element to database
def add_element():
    global ui_net

    # read input parameters
    # just add zero so that "" is defined as zero :P
    key = ui_net.iDLineEditin.displayText()
    name = ui_net.nameLineEdit.displayText()
    P_load = float("0" + ui_net.PowerUsageLineEdit.displayText())
    P_loss = float("0" + ui_net.powerLossLineEdit.displayText())

    # add to database
    try:
        database.add_element(key, name, P_load, P_loss)
    except Exception as e:
        show_fail(str(e))
    
    # clear the textboxes
    ui_net.iDLineEditin.clear()
    ui_net.nameLineEdit.clear()
    ui_net.PowerUsageLineEdit.clear()
    ui_net.powerLossLineEdit.clear()


# remove element from database
def remove_element():
    global ui_net

    # read input parameters
    key = ui_net.iDLineEdit.displayText()

    # remove from database
    try:
        database.remove_element(key)
    except Exception as e:
        show_fail(str(e))
    
    # clear the textbox
    ui_net.iDLineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    open_main()
    sys.exit(app.exec_())