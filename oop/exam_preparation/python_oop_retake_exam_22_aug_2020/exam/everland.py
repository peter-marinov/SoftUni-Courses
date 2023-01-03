from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        expenses = 0
        for room in self.rooms:
            expenses += room.expenses + room.room_cost

        return f"Monthly consumption: {expenses:.2f}$."

    def pay(self):
        output_str = []
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if room.budget >= total_expenses:
                room.budget -= total_expenses
                output_str.append(f"{room.family_name} paid {total_expenses}$ and have {room.budget}$ left.")
            else:
                self.rooms.remove(room)
                output_str.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(output_str)


    def status(self):
        all_people_in_the_hotel = sum([room.members_count for room in self.rooms])
        output_str = [f"Total population: {all_people_in_the_hotel}"]
        for room in self.rooms:
            child_exp = sum([c.cost for c in room.children]) * 30
            if not child_exp:
                child_exp = 0
            output_str.append(f"{room.family_name} with {room.members_count} members. "
                              f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            child_num = 1
            for child in room.children:
                output_str.append(f"--- Child {child_num} monthly cost: {(child.cost * 30):.2f}$")
                child_num += 1

            output_str.append(f"--- Appliances monthly cost: {(room.expenses - child_exp):.2f}$")

        return '\n'.join(output_str)
