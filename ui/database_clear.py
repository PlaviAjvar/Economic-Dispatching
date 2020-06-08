import sys

# given input flags clears databases

for flag in sys.argv[1:]:
    if flag != "generators" and flag != "network" and flag != "results":
        continue
    open("mock_database/" + flag + ".txt", "w").close()