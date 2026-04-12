

infrastructure = {"us-east-1": {}, "eu-west-2": {}, "ap-south-1": {}}

sub_dict_us = {}
sub_dict_eu = {}
sub_dict_ap = {}

name_request = ""

add_us = 0
add_eu = 0
add_ap = 0

server_name_us = ""
server_name_eu = ""
server_name_ap = ""

def find_server(infrastructure):
    global name_request
    for region, servers in infrastructure.items():
        if len(servers) != 0:
            for number, content in servers.items():
                for k, v in content.items():
                    if k == "name" and v == name_request:
                        return region, name_request, number
    return None, None, None
                   

def after_region_choice_us():
    global server_name_us
    global add_us
    add_us += 1
    global sub_dict_us
    server_name_us = input("\nAlright, what name should be assigned to the server?:\t")
    server_cpu = int(input("How many CPU core should be added?:\t"))
    server_ram = int(input("How much Ram should be added?:\t"))
    sub_dict_us[add_us] = {"name": server_name_us, "cpu": server_cpu, "ram": server_ram, "status": "running"}
    return sub_dict_us, add_us, server_name_us

def after_region_choice_eu():
    global server_name_eu
    global add_eu
    add_eu += 1
    global sub_dict_eu
    server_name_eu = input("\nAlright, what name should be assigned to the server?:\t")
    server_cpu = int(input("How many CPU core should be added?:\t"))
    server_ram = int(input("How much Ram should be added?:\t"))
    sub_dict_eu[add_eu] = {"name": server_name_eu, "cpu": server_cpu, "ram": server_ram, "status": "running"}
    return sub_dict_eu, add_eu, server_name_eu


def after_region_choice_ap():
    global server_name_ap
    global add_ap
    add_ap += 1
    global sub_dict_ap
    server_name_ap = input("\nAlright, what name should be assigned to the server?:\t")
    server_cpu = int(input("How many CPU core should be added?:\t"))
    server_ram = int(input("How much Ram(GB) should be added?:\t"))
    sub_dict_ap[add_ap] = {"name": server_name_ap, "cpu": server_cpu, "ram": server_ram, "status": "running"}
    return sub_dict_ap, add_ap, server_name_ap


def calculate_resources(infrastructure):
    total_cpu = 0
    total_ram = 0
    for region, servers, in infrastructure.items():    
        if len(servers) != 0:
            for index, content in servers.items():
                for k, v in content.items():
                    if k == "cpu":
                        total_cpu += v
                    if k == "ram":
                        total_ram += v
        else:
            continue
    return total_ram, total_cpu
    
while True:
    print("\n---- MULTI-CLOUD INFRASTRUCTURE MANAGER ----")
    print("Enter 1 to Add a Server")
    print("Enter 2 to View all Servers")
    print("Enter 3 to Find Server")
    print("Enter 4 to Update Server status")
    print("Enter 5 to Delete Server")
    print("Enter 6 for a Regional Summary")
    print("Enter 7 to Exit the manager")
    choice = input("Enter choice:\t")
    if choice == "1":
        print("\nThe regions available are:")
        for keys in infrastructure.keys():
            print(keys, end="    ")
        region_choice = input("\n\nWhat region do you want to add the server to?:\t")
        if region_choice == "us-east-1":
            after_region_choice_us()
            infrastructure["us-east-1"] = sub_dict_us
            print(f"\nThe server: {server_name_us} has been deployed to us-east-1.")
        elif region_choice == "eu-west-2":
            after_region_choice_eu()
            infrastructure["eu-west-2"] = sub_dict_eu
            print(f"\nThe server:  {server_name_eu} has been deployed to eu-west-2.")
        elif region_choice == "ap-south-1":
            after_region_choice_ap()
            infrastructure["ap-south-1"] = sub_dict_ap
            print(f"\nThe server:  {server_name_ap} has been deployed to ap-south-1.")
        
        else:
            print("\nInvalid Input, retry and enter the correct region. ")

    elif choice == "2":
        print("\n===== ALL SERVERS ====")
        for region, servers, in infrastructure.items():
            print(f"\n Region: {region}")
            print( "-" * 25)
            if len(servers) != 0:
                for k, v in servers.items():
                    print(f"{k}.")
                    for x, y in v.items():
                        print(f"{x.upper()}: {y}")
                    print()
            else:
                print("\nThere are no servers saved here yet")

    elif choice == "3":
        name_request = input("\nWhat is the name of the server you are looking for?:\t")
        region, name_request, number = find_server(infrastructure)
        if name_request ==  None:
            print("\nNo server with that name was found")
        else:
            print(f"\nFound: {name_request} in {region} as server number {number}")

    elif choice == "4":
        name_request = input("\nWhat is the name of the server you want to update?:\t")
        region, name_request, number = find_server(infrastructure)
        if name_request == None:
            print("\nThere is no such server here.")
        else:
            status_update = input("\nWhat status do you want to update the server to?:\t")
            infrastructure[region][number].update({"status": status_update})
            print(f"The server: {name_request} has been updated to {status_update}")

    elif choice == "5":
        name_request = input("\nWhat is the name of the server you want to delete?:\t")
        region, name_request, number = find_server(infrastructure)
        if name_request == None:
            print("\nThere is no such server in the list")
        else:
            confirmation = input(f"""\nAre you sure you want to delete the server: {name_request}?
Enter y for Yes and n for No:\t""") 
            if confirmation == "y":
                del infrastructure[region][number]
                print(f"\nThe server {name_request} has been deleted successfully")
            elif confirmation == "n":
                print(f"\nAlright, server: {name_request} was not deleted")
            else:
                print("\nInvalid response, enter either y or n to confirm")
            
    elif choice == "6":
        total_ram,  total_cpu = calculate_resources(infrastructure)
        print("\n===== REGIONAL SUMMARY =====")
        for region, servers, in infrastructure.items():
            print(f"\n{region}: ", end=" ")
            print(len(servers),"server(s)", end="")
        print("\n" + ("-" * 25))
        if total_cpu == 0 and total_ram == 0:
            print("\nTotal Resources: 0 CPUs, 0 GB RAM")
            print("=" * 25)
        else:
            print(f"\nTotal Resources: {total_cpu} CPUs, {total_ram} GB RAM")
            print("=" * 25)
             
    elif choice == "7":
        print("\nShutting down the manager..........")
        break

    else:
        print("\nWrong input, kindly enter the correct input.")
        
