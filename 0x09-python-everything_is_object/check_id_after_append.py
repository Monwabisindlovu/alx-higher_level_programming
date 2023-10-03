#!/usr/bin/python3

a = [1, 2, 3, 4]
id_before = id(a)
a = a + [5]
id_after = id(a)
print(id_after == 139926795932424)

