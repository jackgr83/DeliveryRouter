class Package:
    def __init__(self, pid, address, city, state, zcode, deadline, weight, notes, status):
        self.id = int(pid)
        self.address = address
        self.city = city
        self.state = state
        self.zip = zcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def set_status(self, status):
        self.status = status

    def set_address(self, address):
        self.address = address

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip,
                                                       self.deadline, self.weight, self.notes, self.status)


