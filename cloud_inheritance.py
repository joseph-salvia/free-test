class CloudResource:
    def __init__(self, name, region):
        self.name = name
        self.region = region

    def start(self):
        print(f"Starting server: '{self.name}'...")

    def stop(self):
        print(f"Stopping server: '{self.name}'...")

    def calculate_cost(self):
        return 50

    def __str__(self):
        return f"{self.name} in {self.region}"

class VirtualMachine(CloudResource):
    def __init__(self, name, region, cpu, ram):
        super().__init__(name, region)
        self.cpu = cpu
        self.ram = ram

    def calculate_cost(self):
        return (self.cpu * 15) + (self.ram * 8)

    def print_cost(self):
            cost = self.calculate_cost()
            print(f"{self.name} monthly cost: ${cost}")

    def __str__(self):
        return f"VM: {self.name} ({self.cpu}CPUs, {self.ram}RAM) in {self.region}"

class Database(CloudResource):
    def __init__(self, name, region, storage_db, db_type):
        super().__init__(name, region)
        self.storage_db = storage_db
        self.db_type = db_type

    def calculate_cost(self):
        return (self.storage_db * 2) + 100

    def print_cost(self):
        cost = self.calculate_cost()
        print(f"{self.name} monthly cost: ${cost}")

    def backup(self):
        print(f"Backing up {self.db_type} database: {self.name}")

    def __str__(self):
        return f"Database: {self.name} ({self.db_type}, {self.storage_db}GB) in {self.region}"


v_machine1 = VirtualMachine("web-vm", "us-east-1", 4, 16)
db1 = Database("prod-db", "eu-west-1", 500, "PostgreSql")

v_machine1.start()
print()
db1.start()
print()
print(v_machine1)
print(db1)        

v_machine1.print_cost()
print()
db1.print_cost()
print()
db1.backup()

