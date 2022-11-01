import sys

""" STDERR AND STDOUT DEMO
sys.stderr = open('out-err.log', 'w')
sys.stdout = open('out.log', 'w')

sys.stdout.write("Print Out - STDOUT 1\n")
sys.stderr.write("ERROR: fata error - STDERR 1\n")

sys.stdout.write("Print Out - STDOUT 2\n")
sys.stderr.write("ERROR: fata error - STDERR 2\n")

sys.stdout.write("Print Out - STDOUT 3\n")
sys.stderr.write("ERROR: fata error - STDERR 3\n")
"""

uname = input("Enter Name: ")
print("Hello " + uname)

print("Argument: " + sys.argv[0])

print("\nPath: ", sys.path[0])
print("\nFull Path: ", sys.path)
print("\nVersion of python", sys.version)
print("\nVersion_Info of python:", sys.version_info)
