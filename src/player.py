# Write a class to hold player information, e.g. what room they are in
# currently.

class PlayerClass:
    def __init__(self, current_room, player_name, player_items=None, amount_of_moves=0, is_playing=True):
        self.current_room = current_room
        self.player_name = player_name
        self.player_inventory = [player_items]
        self.amount_of_moves = amount_of_moves
        self.is_playing = is_playing

    def move(self, direction):
        if self.current_room.connections[direction] is not None:
            self.current_room = self.current_room.connections[direction]
            print(f"{self.player_name} goes {direction}")
            print("")
        else:
            print(f"{self.player_name} goes {direction}")
            print("")
            print(f"{self.player_name} can't go that way")
            print("")

    def searchInventory(self):
        print(f"{self.player_name} looks trough his inventory. He finds: ")
        if None in self.player_inventory:
            print("No items")
            print("")
        elif len(self.player_inventory) > 0:
            for item in self.player_inventory:
                print(item.item_name)
                print(item.item_description)
                print("")
        else:
            print(len(self.player_inventory))

    def changeInventory(self, change_list):
        if change_list[0] == "drop":

            if change_list[1] in self.player_inventory and self.current_room.room_items.count(None) > 0:
                self.current_room.room_items.clear()
                self.player_inventory.remove(change_list[1])
                self.current_room.room_items.append(
                    change_list[1])
                print(
                    f"{self.player_name} drops {change_list[1].item_name}")
                if len(self.player_inventory) == 0:
                    self.player_inventory.append(None)

            elif change_list[1] in self.player_inventory:
                self.player_inventory.remove(change_list[1])
                self.current_room.room_items.append(
                    change_list[1])
                print(
                    f"{self.player_name} drops {change_list[1].item_name}")
                if len(self.player_inventory) == 0:
                    self.player_inventory.append(None)

            else:
                print(
                    f"{self.player_name} doesnt have {change_list[1].item_name} in his inventory")
        elif change_list[0] == "take":

            if self.player_inventory.count(None) > 0 and change_list[1] in self.current_room.room_items:
                self.player_inventory.clear()
                self.player_inventory.append(change_list[1])
                self.current_room.room_items.remove(change_list[1])
                print(
                    f"{self.player_name} takes {change_list[1].item_name}")
                if len(self.current_room.room_items) == 0:
                    self.current_room.room_items.append(None)
            elif change_list[1] in self.current_room.room_items:
                self.player_inventory.append(change_list[1])
                self.current_room.room_items.remove(change_list[1])
                print(
                    f"{self.player_name} takes {change_list[1].item_name}")
                if len(self.current_room.room_items) == 0:
                    self.current_room.room_items.append(None)
            else:
                print(
                    f"{self.current_room.room_name} doesnt have {change_list[1].item_name} in his inventory"
                )

    def useItem(self, change_list, treasure):
        if change_list[1].item_name == "key" and treasure in self.current_room.room_items:
            print(f"{self.player_name} opened the chest!")
            print("The chest is filled with gold!")
            print(f"{self.player_name} finished in {self.amount_of_moves} actions!")
            self.is_playing = False

        elif change_list[1].item_name == "key" and treasure in self.player_inventory:
            print(f"{self.player_name} tries to use the key on the treasure chest")
            print(
                f"{self.player_name} is unsuccessful and considers putting the treasure down first")
        else:
            print(
                f"{self.player_name} has nothing to use {change_list[1].item_name} on.")
