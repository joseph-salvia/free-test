#I intentionally made the input for the cpu and ram as a string
#If they were integers and the user just considered them optional, the code will break
#If there is ever any need to make a calculation on them,  a simple int(cpu) and int(ram) will solve that

import json

with open("inventory.json", "r") as file:
    data = json.load(file)
    
servers = data.get("servers", [])
final_json = {}

def view_server():
    if len(servers) == 0:
        print("No servers saved yet")
    else:
        for server in servers:
            print("-" * 25)
            print(f"""Name:   {server.get('name')}
Region: {server.get('region')}
CPU(cores):    {server.get('cpu')}
RAM(GB):    {server.get('ram')}""")
            print("-" * 25)

def add_server():
    server_add = {}
    server_name = input("\nWhat name should the server have?\t")
    if len(server_name) == 0:
        print("\nNo input was made by user, kindly retry")
    else:
        server_add["name"] = server_name
        server_region = input("What region should the server be deployed in?\t")
        server_add["region"] = server_region
        server_cpu = (input("How many CPU cores should the server have?\t"))
        server_add["cpu"] = server_cpu
        server_ram = (input("How many GB RAM should the server have?\t"))
        server_add["ram"] = server_ram
        servers.append(server_add)
        print(f"\nServer '{server_name}' has been saved successfully")
    

def find_server():
    name_find = input("\nWhat is the name of the server?\t").strip()
    found_server = None
    for server in servers:
        if server.get("name") == name_find:
            found_server = server
            break
    return found_server, name_find

while True:
    print()
    print("=" * 25)
    print("INVENTORY MANAGER")
    print("=" * 25)
    user_input = input("""Enter 1 to  View all servers
Enter 2 to  Add a new server
Enter 3 to Search for a server by name
Enter 4 to Delete a server by name
Enter 5 to Save and quit\t""")

    if user_input == "1":
        #print(f"\n{servers}")
        view_server()
    elif user_input == "2":
        add_server()
    elif user_input == "3":
        found_server, name_find = find_server()
        if found_server:
            print(f"""\n✅ Server found!
Name:   {found_server.get('name')}
Region: {found_server.get('region')}
CPU(cores):    {found_server.get('cpu')}
RAM(GB):    {found_server.get('ram')} """)
        else:
            print(f"\n❌ No server found with the name '{name_find}'.")
    elif user_input == "4":
        found_server, name_find = find_server()
        if found_server:
            print(f"Are you sure you want to delete server '{name_find}' ?")
            confirm = input("Enter y for yes and n for no:\t")
            if confirm == "y":
                servers.remove(found_server)
                print(f"\nServer '{name_find}' has been deleted successfully.")
            elif confirm == "n":
                print(f"\nThe server '{name_find}' was not deleted.")
            else:
                print("\nInvalid input!!, Kindly try again")
        else:
            print(f"\nServer '{name_find}' not found!!")
    elif user_input == "5":
        final_json["servers"] = servers
        with open("inventory.json", "w") as file:
            json.dump(final_json, file, indent=2)
        print("\nProgram run ended, and file is saved successfully")
        break
    else:
        print("""\nInvalid Input.
Kindly enter either 1,2,3,4, or 5 to proceed""")
