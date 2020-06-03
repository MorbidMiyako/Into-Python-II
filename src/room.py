# Implement a class to hold room information. This should have name and
# description attributes.
from player import PlayerClass


class RoomClass(PlayerClass):
    def __init__(self, room_name, room_description):
        super().__init__(room_name)
        self.room_description = room_description
