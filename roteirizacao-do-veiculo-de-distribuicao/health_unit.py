class Health_unit:
    next_id = 0
    next_visit_order = 0

    def __init__(self, name, coordinate):
        self.id = Health_unit.next_id
        Health_unit.next_id += 1

        self.name = name
        self.coordinate = coordinate
        self.was_visited = False
        self.visit_order = None

    def __str__(self):
        return "Health Unit: %s | name: %s | coordinate: %s | was_visited: %s | visit_order: %s" % (self.id, self.name, self.coordinate.__str__(), self.was_visited, self.visit_order)

    def visit(self):
        self.was_visited = True
        self.visit_order = Health_unit.next_visit_order
        Health_unit.next_visit_order += 1
