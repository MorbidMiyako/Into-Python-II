# Implement a class to hold room information. This should have name and
# description attributes.

class RoomClass:
    def __init__(self, room_name, room_description, room_item=None, n_to=None, s_to=None, e_to=None, w_to=None):
        self.room_name = room_name
        self.room_description = room_description
        self.connections = {
            "north": n_to,
            "east": e_to,
            "south": s_to,
            "west": w_to
        }
        self.room_items = [room_item]

    def searchRoom(self, player_name):
        print(f"{player_name} looks trough the room. He finds: ")
        if None in self.room_items:
            print("No items")
            print("")
        elif len(self.room_items) > 0:
            for item in self.room_items:
                print(item.item_name)
                print(item.item_description)
                print("")
        else:
            print(len(self.room_items))
