# -*- coding: utf-8 -*-
import room_1, room_2


print('В комнате room_1 живут:', *room_1.folks)
print('В комнате room_2 живут:', *room_2.folks)

delimiter = ', '
people = room_1.folks + room_2.folks
print('На неизвестном улице живут:', delimiter.join(people))