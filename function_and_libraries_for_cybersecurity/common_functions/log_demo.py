LOG_FILE = "2022/11/01 04:12:05 OrHasson 200 success login.aspx"
PARTS = LOG_FILE.split()

date = PARTS[0]
time = PARTS[1]
user = PARTS[2]
status = PARTS[3]
result = PARTS[4]
page = PARTS[5]

new_date = date[5:] + "/" + date[:4]

print("On {}, User {} had {} on page: {}".format(new_date, user, result, page))
