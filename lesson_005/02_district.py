# -*- coding: utf-8 -*-
import room_1, room_2
from district.central_street.house1 import room1 as f11
from district.central_street.house1 import room2 as f12
from district.central_street.house2 import room1 as f21
from district.central_street.house2 import room2 as f22
from district.soviet_street.house1 import room1 as f31
from district.soviet_street.house1 import room2 as f32
from district.soviet_street.house2 import room1 as f41
from district.soviet_street.house2 import room2 as f42
# о, тут молодец!
delimiter = ', '
people = room_1.folks + room_2.folks
people_central_street = f11.folks + f12.folks + f21.folks + f22.folks
people_soviet_street = f31.folks + f32.folks + f41.folks + f42.folks

print('На неизвестном улице живут:', delimiter.join(people))
print('На центральной улице живут:', delimiter.join(people_central_street))
print('На советской улице живут:', delimiter.join(people_soviet_street))

# зачет!
