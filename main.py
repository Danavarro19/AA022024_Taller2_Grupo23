import csv

from Employee import Employee
from Heap import Heap

entries = []
with open('entries.csv', 'r') as f:
    reader = csv.DictReader(f, fieldnames=['name', 'salary'])
    for row in reader:
        entries.append(Employee(row['name'], int(row['salary'])))

h = Heap(entries)
for entry in h.sort():
    print(entry)
