# -*- coding: utf-8 -*-
import room_1, room_2


delimiter = ', '
people = room_1.folks + room_2.folks
print('На районе живут:', delimiter.join(people))


