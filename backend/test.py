from agent import generate_query
from drive_tool import search_drive

user_input = input("Ask something: ")

query = generate_query(user_input)

print("\nGenerated Query:")
print(query)

files = search_drive(query)

print("\nFiles Found:\n")

for file in files:
    print(file["name"])