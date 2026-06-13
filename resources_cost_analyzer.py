
import json
import csv

try:
    with open("resources.json", "r") as file:
        content = json.load(file)

    servers = content.get("resources", [])
    
#---------------------------------------------------------------------------------
    with open("cost_history.csv", "r") as file:
        csv_reader = csv.reader(file)

        header = next(csv_reader)
    index = 0
    final_csv = ""
        

#----------------------------------------------------------------------------------
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m" 
    YELLOW = "\033[33m"

#-----------------------------------------------------------------------------------
    def view_servers():
        if len(servers) == 0:
            print(f"\n{RED}There are no servers saved yet{RESET}")
        else:
            print()
            print(f"{YELLOW}======= SERVER LIST ======={RESET}")
            print("-" * 23)
            for s in servers:
                if s.get("type") == "VirtualMachine":
                    print(f"{YELLOW}Server Type: {s.get("type")}")
                    print(f"Server Name: {s.get("name")}")
                    print(f"Region: {s.get("region")}")
                    print(f"Owner: {s.get("owner")}")
                    print(f"CPU(cores): {s.get("cpu")}")
                    print(f"RAM(gb): {s.get("ram")}")
                    print(f"Storage(gb): {s.get("storage_gb")}{RESET}")
                    print("-" * 23)
                elif s.get("type") == "Database":
                    print(f"{YELLOW}Server Type: {s.get("type")}")
                    print(f"Server Name: {s.get("name")}")
                    print(f"Region: {s.get("region")}")
                    print(f"Owner: {s.get("owner")}")
                    print(f"DB Type: {s.get("db_type")}")
                    print(f"Storage(gb): {s.get("storage_gb")}")
                    print(f"Backup Enabled: {s.get("backup_enabled")}{RESET}")
                    print("-" * 23)
                elif s.get("type") == "ServerlessFunction":
                    print(f"{YELLOW}Server Type: {s.get("type")}")
                    print(f"Server Name: {s.get("name")}")
                    print(f"Region: {s.get("region")}")
                    print(f"Owner: {s.get("owner")}")
                    print(f"Monthly Invocations: {s.get("monthly_invocations")}")
                    print(f"Average Duration(ms): {s.get("avg_duration_ms")}{RESET}")
                    print("-" * 23)
#----------------------------------------------------------------------------------                    

    def add_resource():
        while True:
            r_type = input("""\nWhat type of resource do you want to add?
1. VirtualMachine
2. Database
3. ServerlessFunction :\t""").strip()
            if len(r_type) == 0:
                print(f"\n{RED}Please provide a valid input{RESET}")
            else:      
                if r_type == "1":
                    add_virtualmachine()
                    break
                elif r_type == "2":
                    add_database()
                    break
                elif r_type == "3":
                    add_serverless()
                    break
                    
#---------------------------------------------------------------------------------                   
#This is a common code excerpt that shows up while adding any of the three type of resources

    def excerpt_all():
        while True:   
            r_name = input("\nWhat name should the Server have?:\t").strip().lower()
            if len(r_name) == 0:
                print(f"\n{RED}Kindly enter a valid input for the name{RESET}")
            else:
                break

        while True: 
            r_region_0 = region_display()
            if len(r_region_0) == 0:
                print(f"\n{RED}Kindly enter a valid input{RESET}")
            else:
                if r_region_0 == "1":
                    r_region = "us-east-1"
                    break
                elif r_region_0 == "2":
                    r_region = "us-west-2"
                    break
                elif r_region_0 == "3":
                    r_region = "eu-west-2"
                    break
                elif r_region_0 == "4":
                    r_region = "ap-south-1"
                    break
                else:
                    print(f"\n{RED}Enter the correct option from the menu{RESET}")
                    continue

        while True:
            r_owner = input(f"\nWhat Team owns '{r_name}':\t").strip()
            if len(r_owner) == 0:
                print(f"\n{RED}Kindly enter a valid input{RESET}")
            else:
                break
        return r_name, r_region, r_owner
        
#--------------------------------------------------------------------------------

    def region_display():
        r_region = input("""\nChoose one of the available servers
1. us-east-1
2. us-west-2
3. eu-west-1
4. ap-south-1: \t""").strip().lower()
        return r_region

#--------------------------------------------------------------------------------    
               
    def add_virtualmachine():
        r_name, r_region, r_owner = excerpt_all()
        while True:
            try:
                r_cpu = int(input(f"\nHow many CPU cores should be allocated to '{r_name}'? :\t").strip())
                if r_cpu <= 0:
                    print(f"\n{RED}Enter a value greater than 0{RESET}")
                else:
                    break
            except ValueError:
                print(f"\n{RED}Error with the input, kindly enter a number please{RESET}")

        while True:
            try:
                r_ram = int(input(f"\nHow much RAM(gb) should be allocated to '{r_name}'? :\t").strip())
                if r_ram <= 0:
                    print(f"\n{RED}Enter a valid number greater than 0{RESET}")
                else:
                    break           
            except ValueError:
                print(f"\n{RED}Error with the input, kindly enter a number please{RESET}")

        while True:
            try:
                r_storage = int(input(f"\nHow much Storage(gb) should be allocated to '{r_name}'? :\t").strip())
                if r_storage < 0:
                    print(f"\n{RED}Enter a value greater than or equal to 0{RESET}")
                else:
                    r_dict = {
                        "type": "VirtualMachine",
                        "name": r_name,
                        "region": r_region,
                        "owner": r_owner,
                        "cpu": r_cpu,
                        "ram": r_ram,
                        "storage_gb": r_storage
                    }
                    servers.append(r_dict)
                    print()
                    print("-" * 56)
                    print(f"{GREEN}Server '{r_name}' has been saved successfully{RESET}")
                    print("-" * 56)
                    break
            except ValueError:
                print(f"\n{RED}Error with the input, kindly enter a number please{RESET}")

#---------------------------------------------------------------------------------

    def add_database():
        r_name, r_region, r_owner = excerpt_all()
        while True:   
            r_db_type_0 = input("""\nWhat database type should be applied?:\t
1. MySQL
2. PostgreSQL
3. Oracle:\t""").strip()
            if len(r_db_type_0) == 0:
                print(f"\n{RED}Kindly enter a valid input and try again{RESET}")
            else:
                if r_db_type_0 == "1":
                    r_db_type = "MySQL"
                    break
                elif r_db_type_0 == "2":
                    r_db_type = "PostgreSQL"
                    break
                elif r_db_type_0 == "3":
                    r_db_type = "Oracle"
                    break
                else:
                    print(f"\n{RED}Invalid input, choose from the menu and try again{RESET}")
                    continue
        
        while True:
            try:
                r_storage = int(input(f"\nHow much Storage(gb) should be allocated to '{r_name}'? :\t").strip())
                if r_storage < 0:
                    print(f"\n{RED}Enter a value greater than or equal to 0{RESET}")
                else:
                    break
            except ValueError:
                print(f"\n{RED}Error with the input, kindly enter a number please{RESET}")

        while True:
            r_backup = input(f"""\nShould the backup be enabled for '{r_name}'
1. Yes
2. No:\t""").strip()
            if len(r_backup) == 0:
                print(f"\n{RED}Invalid Input, choose an option and try again{RESET}")
            else:
                if r_backup == "1":
                    r_backup_enabled = True
                    break
                elif r_backup == "2":
                    r_backup_enabled = False
                    break
                else:
                    print(f"\n{RED}Kindly make the correct input and try again{RESET}")
                    continue
                    
        r_dict = {
            "type": "Database",
            "name": r_name,
            "region": r_region,
            "owner": r_owner,
            "db_type": r_db_type,
            "storage_gb": r_storage,
            "backup_enabled": r_backup_enabled
        }
        servers.append(r_dict)
        print()
        print("-" * 56)
        print(f"{GREEN}Server '{r_name}' has been saved successfully{RESET}")
        print("-" * 56)

#---------------------------------------------------------------------------------

    def add_serverless():
        r_name, r_region, r_owner = excerpt_all()
        while True:
            try:
                r_monthly_invocations = int(input("\nEnter estimated monthly invocations:\t").strip())
                if r_monthly_invocations <= 0:
                    print(f"\n{RED}Kindly enter a valid value!{RESET}")
                else:
                    break
            except ValueError:
                print(f"\n{RED}Error with the input, kindly enter a number please{RESET}")

        while True:
            try:
                r_avg_duration_ms = int(input("\nEnter average duration (milliseconds):\t").strip())
                if r_avg_duration_ms <= 0:
                    print(f"\n{RED}Kindly enter a valid value!{RESET}")
                else:
                    break
            except ValueError:
                print(f"\n{RED}Error with the input, kindly enter a number please{RESET}")

        r_dict = {
                    "type": "ServerlessFunction",
                    "name": r_name,
                    "region": r_region,
                    "owner": r_owner,
                    "monthly_invocations": r_monthly_invocations,
                    "avg_duration_ms": r_avg_duration_ms
                }
        servers.append(r_dict)
        print()
        print("-" * 56)
        print(f"{GREEN}Server '{r_name}' has been saved successfully{RESET}")
        print("-" * 56)

#--------------------------------------------------------------------------------
    def find_server():
        while True:
            user_input = input("\nWhat is the name of the server?:\t").strip().lower()
            if len(user_input) == 0:
                print(f"\n{RED}Kindly enter the name of the server to continue{RESET}")
            else:
                return [s for s in servers if s.get("name") == user_input]
                break 

#-------------------------------------------------------------------------------
    def region_filter():
        while True: 
            r_region_0 = region_display()
            if len(r_region_0) == 0:
                print(f"\n{RED}Error, Make sure you enter an input{RESET}")
            else:
                if r_region_0 == "1":
                    r_region = "us-east-1"
                    break
                elif r_region_0 == "2":
                    r_region = "us-west-2"
                    break
                elif r_region_0 == "3":
                    r_region = "eu-west-2"
                    break
                elif r_region_0 == "4":
                    r_region = "ap-south-1"
                    break
                else:
                    print(f"\n{RED}Enter the correct option from the menu{RESET}")
                    continue
        return [s for s in servers if s.get("region") == r_region]

#------------------------------------------------------------------------------
    def calculate_cost():
        v_machine = 0
        database = 0
        serverless = 0
        for s in servers:
            if s.get("type") == "VirtualMachine":
                v_machine_0 = VirtualMachine(s.get("name"), s.get("region"), s.get("owner"), s.get("cpu"), s.get("ram"), s.get("storage_gb"))
                v_machine += v_machine_0.get_monthly_cost()
            elif s.get("type") == "Database":
                database_0 = Database(s.get("name"), s.get("region"), s.get("owner"), s.get("db_type"), s.get("storage_gb"), s.get("backup_enabled"))
                database += database_0.get_monthly_cost()
            elif s.get("type") == "ServerlessFunction":
                serverless_0 = Serverless(s.get("name"), s.get("region"), s.get("owner"), s.get("monthly_invocations"), s.get("avg_duration_ms"))              
                serverless += serverless_0.get_monthly_cost()
        return v_machine, database, serverless 

#-------------------------------------------------------------------------------
    def v_machine_list():
        return [s for s in servers if s.get("type") == "VirtualMachine"]   

#-------------------------------------------------------------------------------
    def database_list():
        return [s for s in servers if s.get("type") == "Database"]

#-------------------------------------------------------------------------------
    def serverless_list():
        return [s for s in servers if s.get("type") == "ServerlessFunction"]

#------------------------------------------------------------------------------
    def display_cost(final_csv):
        virtualmachine_cost, database_cost, serverless_cost = calculate_cost()
        v_machine_len = len(v_machine_list())
        database_len = len(database_list())
        serverless_len = len(serverless_list())
        total_len = v_machine_len + database_len + serverless_len
        total_cost = virtualmachine_cost + database_cost + serverless_cost
        print()
        print(f"{YELLOW}===== MONTHLY COST REPORT =====")
        print(f"VirtualMachine: {v_machine_len} resource(s), ${virtualmachine_cost:.2f}")
        print(f"Database: {database_len} resource(s), ${database_cost:.2f}")
        print(f"Serverless Function: {serverless_len} resource(s), ${serverless_cost:.2f}")
        print("-" * 56)
        print()
        print(f"Total: {total_len} Resources, ${total_cost:.2f}{RESET}")
        while True:
            save_cost = input("""\nDo you want to save this cost output to a CSV for later monitoring?
1. Yes
2. No:\t""").strip()
            if save_cost == "1":
                cost_history = f"""\nVirtualMachine, {v_machine_len} resource(s), ${virtualmachine_cost:.2f}
Database, {database_len} resource(s), ${database_cost:.2f}
Serverless Function, {serverless_len} resource(s), ${serverless_cost:.2f}
Total, {total_len} Resources, ${total_cost:.2f}"""
                final_csv += cost_history
                print(final_csv)
                break
            elif save_cost == "2":
                print(f"\n{GREEN}Alright, the cost output was not saved{RESET}")
                break
            else:
                print(f"\n{RED}Enter the correct option from the menu{RESET}")
                continue
                
#-------------------------------------------------------------------------------
    def group_by_type():
        v_sub_cost = 0
        d_sub_cost = 0
        s_sub_cost = 0
        print()
        print(f"{YELLOW}=== COST REPORT (GROUPED BY TYPE) ===")
        print()
        print("VIRTUAL MACHINES")
        for s in servers:
            if s.get("type") == "VirtualMachine":
                v_cost = 0
                v_machine_0 = VirtualMachine(s.get("name"), s.get("region"), s.get("owner"), s.get("cpu"), s.get("ram"), s.get("storage_gb"))
                v_cost += v_machine_0.get_monthly_cost()
                print(f"  - {s.get("name")} [{s.get("region")}, {s.get("owner")}]: ${v_cost:.2f}/month")
                v_sub_cost += v_cost
        v_machine_len = len(v_machine_list())
        print(f"  Subtotal: {v_machine_len} Resources, ${v_sub_cost:.2f}/month")
            
        print()
        print("DATABASES")
        for s in servers:
            if s.get("type") == "Database":
                d_cost = 0
                database_0 = Database(s.get("name"), s.get("region"), s.get("owner"), s.get("db_type"), s.get("storage_gb"), s.get("backup_enabled"))
                d_cost += database_0.get_monthly_cost()
                print(f"  - {s.get("name")} [{s.get("region")}, {s.get("owner")}]: ${d_cost:.2f}/month")
                d_sub_cost += d_cost
        database_len = len(database_list())
        print(f"  Subtotal: {database_len} Resources, ${d_sub_cost:.2f}/month")

        print()
        print("SERVERLESS FUNCTIONS")
        for s in servers: 
            if s.get("type") == "ServerlessFunction":
                s_cost = 0
                serverless_0 = Serverless(s.get("name"), s.get("region"), s.get("owner"), s.get("monthly_invocations"), s.get("avg_duration_ms"))              
                s_cost += serverless_0.get_monthly_cost()
                print(f"  - {s.get("name")} [{s.get("region")}, {s.get("owner")}]: ${s_cost:.2f}/month")
                s_sub_cost += s_cost
        serverless_len = len(serverless_list())
        print(f"  Subtotal: {serverless_len} Resources, ${s_sub_cost:.2f}/month")
        total_len = v_machine_len + database_len + serverless_len
        total_cost = v_sub_cost + d_sub_cost + s_sub_cost
        print()
        print("_" * 35)
        print(f"TOTAL: {total_len} Resource(s), ${total_cost:.2f}/month{RESET}")
                
             
            
            
#-------------------------------------------------------------------------------

    class CloudResource():
        def __init__(self, name, region, owner):
            self.name = name
            self.region = region
            self.owner = owner
        def get_monthly_cost(self):
            raise NotImplementedError
        def __str__(self):
            return f"'{self.name}' in {self.region} by '{self.owner}'"
    class VirtualMachine(CloudResource):
        def __init__(self, name, region, owner, cpu, ram, storage_gb):
            super().__init__(name, region, owner)
            self.cpu = cpu
            self.ram = ram
            self.storage_gb = storage_gb
        def get_monthly_cost(self):
            cpu_rate = 15
            ram_rate = 8 
            storage_gb_rate = 0.5
            return (self.cpu * cpu_rate) + (self.ram * ram_rate) + (self.storage_gb * storage_gb_rate)
    class Database(CloudResource):
        def __init__(self, name, region, owner, db_type, storage_gb, backup_enabled):
            super().__init__(name, region, owner)
            self.db_type = db_type
            self.storage_gb = storage_gb
            self.backup_enabled = backup_enabled
        def get_monthly_cost(self):
            storage_gb_rate = 2
            if self.backup_enabled:
                backup_rate = 100
            else:
                backup_rate = 0
            return (self.storage_gb * storage_gb_rate) + backup_rate + 50
    class Serverless(CloudResource):
        def __init__(self, name, region, owner, monthly_invocations, avg_duration_ms):
            super().__init__(name, region, owner)
            self.monthly_invocations = monthly_invocations
            self.avg_duration_ms = avg_duration_ms
        def get_monthly_cost(self):
            invocation_rate = 20
            duration_ms_rate = 10
            return ((self.monthly_invocations/1000000) * invocation_rate) + ((self.avg_duration_ms/1000) * duration_ms_rate)

#----------------------------------------------------------------------------------
#__main__


    while True:
        print()
        print("=" * 23 )
        print(f"CLOUD MANAGER INTERFACE")
        print("=" * 23 )
        menu_choice = input(f"""1. View all Servers
2. Add a new Resource
3. Search Server by name
4. Filter by Region
5. Calculate Total Monthly cost
6. Generate Cost Report
7. Delete a Resource
8. Save and quit:\t""").strip()
#================================================================================
        if menu_choice == "1":
            view_servers()
#=================================================================================            
        elif menu_choice == "2":
            add_resource()   
#================================================================================
        elif menu_choice == "3":
            s_find_list = find_server()
            if s_find_list:
                print()
                print(f"{GREEN}Yay, Server was found!{RESET}")
                print()
                for s in s_find_list:
                    if s.get("type") == "VirtualMachine":
                        print(f"{YELLOW}")
                        print("-" * 23)
                        print(f"Server Type: {s.get("type")}")
                        print(f"Server Name: {s.get("name")}")
                        print(f"Region: {s.get("region")}")
                        print(f"Owner: {s.get("owner")}")
                        print(f"CPU(cores): {s.get("cpu")}")
                        print(f"RAM(gb): {s.get("ram")}")
                        print(f"Storage(gb): {s.get("storage_gb")}{RESET}")
                        print("-" * 23)
                    elif s.get("type") == "Database":
                        print(f"{YELLOW}")
                        print("-" * 23)
                        print(f"Server Type: {s.get("type")}")
                        print(f"Server Name: {s.get("name")}")
                        print(f"Region: {s.get("region")}")
                        print(f"Owner: {s.get("owner")}")
                        print(f"DB Type: {s.get("db_type")}")
                        print(f"Storage(gb): {s.get("storage_gb")}")
                        print(f"Backup Enabled: {s.get("backup_enabled")}{RESET}")
                        print("-" * 23)
                    elif s.get("type") == "ServerlessFunction":
                        print(f"{YELLOW}")
                        print("-" * 23)
                        print(f"Server Type: {s.get("type")}")
                        print(f"Server Name: {s.get("name")}")
                        print(f"Region: {s.get("region")}")
                        print(f"Owner: {s.get("owner")}")
                        print(f"Monthly Invocations: {s.get("monthly_invocations")}")
                        print(f"Average Duration(ms): {s.get("avg_duration_ms")}{RESET}")
                        print("-" * 23)
            else:
                print(f"\n{RED}No server which such name has been saved yet.{RESET}")
#===============================================================================
        elif menu_choice == "4":
            r_list = region_filter()
            if r_list:
                print()
                for s in r_list:
                    if s.get("type") == "VirtualMachine":
                        print(f"{YELLOW}")
                        print("-" * 23)
                        print(f"Server Type: {s.get("type")}")
                        print(f"Server Name: {s.get("name")}")
                        print(f"Region: {s.get("region")}")
                        print(f"Owner: {s.get("owner")}")
                        print(f"CPU(cores): {s.get("cpu")}")
                        print(f"RAM(gb): {s.get("ram")}")
                        print(f"Storage(gb): {s.get("storage_gb")}{RESET}")
                        print("-" * 23)
                    elif s.get("type") == "Database":
                        print(f"{YELLOW}")
                        print("-" * 23)
                        print(f"Server Type: {s.get("type")}")
                        print(f"Server Name: {s.get("name")}")
                        print(f"Region: {s.get("region")}")
                        print(f"Owner: {s.get("owner")}")
                        print(f"DB Type: {s.get("db_type")}")
                        print(f"Storage(gb): {s.get("storage_gb")}")
                        print(f"Backup Enabled: {s.get("backup_enabled")}{RESET}")
                        print("-" * 23)
                    elif s.get("type") == "ServerlessFunction":
                        print(f"{YELLOW}")
                        print("-" * 23)
                        print(f"Server Type: {s.get("type")}")
                        print(f"Server Name: {s.get("name")}")
                        print(f"Region: {s.get("region")}")
                        print(f"Owner: {s.get("owner")}")
                        print(f"Monthly Invocations: {s.get("monthly_invocations")}")
                        print(f"Average Duration(ms): {s.get("avg_duration_ms")}{RESET}")
                        print("-" * 23)
            else:
                print(f"\n{RED}No server has been saved in that region yet.{RESET}")

#===============================================================================
        elif menu_choice == "5":
            display_cost(final_csv)

#===============================================================================
        elif menu_choice == "6":
            group_by_type()

#================================================================================
        elif menu_choice == "7":
            found_server = find_server()
            if found_server:
                for f in found_server:
                    while True:
                        del_confirm = input(f"""\nAre you sure you want to delete '{f.get("name")}'?
1. Yes
2. No:\t""").strip().lower()
                        if del_confirm == "1":
                            for s in servers:
                                for f in found_server:
                                    if s.get("name") == f.get("name"):
                                        print(f"\n{GREEN}Server '{s.get("name")}' has been deleted successfully{RESET}")
                                        servers.remove(s)
                            break
                        elif del_confirm == "2":
                            for f in found_server:
                                print(f"\n{GREEN}The server '{f.get("name")}' was not deleted{RESET}")
                            break
                        else:
                            print(f"\n{RED}Invalid input. Please enter either 1 or 2 to proceed{RESET}")
                            continue
            else:
                print(f"\n{RED}No server with such name has been saved yet{RESET}")
#================================================================================             
        elif menu_choice == "8":
            final_json = {}
            final_json["resources"] = servers
            with open("resources.json", "w") as file:
                    json.dump(final_json, file, indent=2)
                    
            print(f"\n{GREEN}Session saved and Program has quitted successfully{RESET}")
            break
        else:
            print(f"\n{RED}Invalid input detected, kindly choose from the menu below{RESET}")


except FileNotFoundError:
    print("Json file 'resources.json' was not found")
    print("Make sure the file is available before running the program again")
    
except json.decoder.JSONDecodeError:
    print("Invalid Json File")
    print("Make sure the json file is setup correctly before running the program again")

except KeyboardInterrupt:
    print(f"\n{GREEN}Goodbye!!{RESET}")

#----------------------------------------------------------------------------------
