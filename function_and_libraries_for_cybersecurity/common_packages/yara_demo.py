import yara
import os

directory = '/orhme'
yara_rules = yara.compile(filepath='/orhme/yara_rules/test_rule.yar')

for filename in os.listdir(directory):
    matches = yara_rules.match(data=filename)
    if matches:
        print(filename + ": Matched and Possibly Infected :(")
    else:
        print(filename + ": Clean :)")
