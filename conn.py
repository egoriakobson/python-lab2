class DatabaseConnection:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

db = DatabaseConnection("localhost", 5432, "student", "1234")

print(db.hostname)
print(db.port)
print(db.username)
print(db.password)

