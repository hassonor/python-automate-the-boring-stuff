from scapy.all import *

# SNIFFING
results = sniff(count=5)

# result=sniff(filter='tcp',count=2) # Only show first 2 TCP packets sniffing

results.nsummary()  # nsummary() function will display the summary detail of those packets captured
results[0].show()  # show() function  will show the full detail of the packet captured (in this demo the first)
