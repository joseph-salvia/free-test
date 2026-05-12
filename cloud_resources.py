class Cloudserver:
    def __init__(self, name, region, cpu, ram, instance_type):
        self.name =  name
        self.region = region
        self.cpu = int(cpu)
        self.ram = int(ram)
        self.attribute = instance_type
        self.status = "running"

    def start(self):
        self.status = "running"
        print(f"Starting server '{self.name}' in {self.region}...")

    def stop(self):
        self.status = "stopped"
        print(f"Stopping {self.name}...")

    def display_info(self):
        print(f"""Server: {self.name}
Region: {self.region}
Type: {self.attribute}
Resources: {self.cpu} CPUs, {self.ram}GB RAM
Status: {self.status}""")

    def calculate_monthly_cost(self):
        calculated_cost = (self.cpu * 15) + (self.ram * 8)
        print(f"The monthly cost for server: '{self.name}' is ${calculated_cost}.")

    def upgrade_resources(self, new_cpu, new_ram):
        self.cpu = new_cpu
        self.ram = new_ram
        print(f"Server: '{self.name}', now has {self.cpu} CPUs and {self.ram}GB RAM.")


server1 = Cloudserver("web-01", "us-east", "12", "36", "t2.micro")
server2 = Cloudserver("db-01", "eu-west-2", "4", "8", "t3.large")
server3 = Cloudserver("app-server", "ap-south-1", "8", "16", "t1.mini") 
       
server1.start()
print()
print("-" * 25)
server1.display_info()
print("-" * 25)
server2.display_info()
print("-" * 25)
server3.display_info()
print("-" * 25)

print()
server2.calculate_monthly_cost()
print()
server3.upgrade_resources("4", "12")
print()

server3.display_info()
print("-" * 25)


