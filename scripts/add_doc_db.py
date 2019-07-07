import csv
import os


with open('Doctors_DB.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        os.system(f'ssh wp -C "wp post create --post_type=page --comment_status=open --post_status=publish --post_title=\\"{row["Name"]}\\" --post_content=\\"Address: {row["Address"]}, {row["City"]} {row["ZIP"]} Phone: {row["Phone"]} Public Insurance: {row["Public"]} Private Insurance: {row["Private"]} {row["Contant"]}\\"')

