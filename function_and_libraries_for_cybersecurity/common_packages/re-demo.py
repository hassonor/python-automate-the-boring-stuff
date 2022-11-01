import re

re_string = "1/11/2022 18:10:00 OrHasson login.aspx Successful login"
result_pattern = r"Success\w*"
date_pattern = r"\d+/\d+/\d+"

r_pattern = re.compile(result_pattern)
d_pattern = re.compile(date_pattern)

print("-----------------------------------------------------")

res = r_pattern.match(re_string)
dt = d_pattern.match(re_string)
print("[*]Match the pattern 'Success' followed by alphanumeric char(s)")

if res is not None:
    print(res.string)
    print(res.pos)
    print(res.group())
else:
    print("None")

res = r_pattern.search(re_string)
dt = d_pattern.search(re_string)
print("[*]Search the pattern 'Success' followed by alphanumeric char(s)")
print(res.string)
print("result: " + res.group())
print(res.start())
print("date: " + dt.group())
print("------------------------------------------------")

res = re.split(r"\s", re_string)
print("[*]Split up string by whitespace and add each individual part to res")
print("All tokens:", res)
print("Result token: ", res[4])
print("Date token:", res[0])
print("------------------------------------------------")

res = re.findall(r"\d", re_string)
print("[*]Print all the digits in a list")
print(res)
