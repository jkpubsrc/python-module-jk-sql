#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys

import sqlite3

from jk_sql import *





db = DBManager.createSQLiteMemoryDB()
table = db.createTable(DBTableDef("mytable", [
	DBColDef("rowidxxx", EnumDBColType.PK, False, EnumDBIndexType.NONE),
	DBColDef("mybool", EnumDBColType.BOOL, True, EnumDBIndexType.NONE),
	DBColDef("myint", EnumDBColType.INT32, True, EnumDBIndexType.NONE),
	DBColDef("myfloat", EnumDBColType.DOUBLE, True, EnumDBIndexType.NONE),
	DBColDef("mystr", EnumDBColType.STR256, True, EnumDBIndexType.NONE),
	DBColDef("myblob", EnumDBColType.BLOB, True, EnumDBIndexType.NONE),
	DBColDef("myclob", EnumDBColType.CLOB, True, EnumDBIndexType.NONE),
]))

# insert
print("---- verify the insert")

for n in range(0, 3):
	table.addRow({
		"mybool": True,
		"myint": 123 + n,
		"myfloat": 1.23,
		"mystr": "abc" + str(n),
		"myblob": b"\x00\x01\x02\x03",
		"myclob": "Lorem ipsum",
	})

print("---- verify the insert")

rows = table.getRows()
assert len(rows) == 3
print(rows[0])
assert rows[0] == (1, True, 123, 1.23, "abc0", b"\x00\x01\x02\x03", "Lorem ipsum")
print(rows[1])
assert rows[1] == (2, True, 124, 1.23, "abc1", b"\x00\x01\x02\x03", "Lorem ipsum")
print(rows[2])
assert rows[2] == (3, True, 125, 1.23, "abc2", b"\x00\x01\x02\x03", "Lorem ipsum")

print("---- verify counting")

count = table.countRows()
assert count == 3

count = table.countRows({
	"mystr": "abc1"
})
assert count == 1

count = table.countRows({
	"myint": 0
})
assert count == 0

print("---- delete")

table.deleteRows({
	"myint": 124
})

print("---- verify the delete")

rows = table.getRows()
assert len(rows) == 2
print(rows[0])
assert rows[0] == (1, True, 123, 1.23, "abc0", b"\x00\x01\x02\x03", "Lorem ipsum")
print(rows[1])
assert rows[1] == (3, True, 125, 1.23, "abc2", b"\x00\x01\x02\x03", "Lorem ipsum")

print("---- update")

table.updateRows({
	"myint": 123456789,
	"myclob": "Lorem ipsum dolor",
	"mybool": False,
	"myfloat": 1.234567,
}, {
	"myint": 125
})

print("---- verify the update")

rows = table.getRows()
assert len(rows) == 2
print(rows[0])
assert rows[0] == (1, True, 123, 1.23, "abc0", b"\x00\x01\x02\x03", "Lorem ipsum")
print(rows[1])
assert rows[1] == (3, False, 123456789, 1.234567, "abc2", b"\x00\x01\x02\x03", "Lorem ipsum dolor")

print("---- add another column")

bSuccess = -1
try:
	table.addColumn(DBColDef("myvalue", EnumDBColType.INT32, False, EnumDBIndexType.UNIQUE_INDEX))
	bSuccess = 1
except:
	# this should fail
	bSuccess = 0
assert bSuccess == 0

table.addColumn(DBColDef("myvalue", EnumDBColType.INT32, False, EnumDBIndexType.INDEX))

print("---- verify the add column operation")

rows = table.getRows()
assert len(rows) == 2
print(rows[0])
assert rows[0] == (1, True, 123, 1.23, "abc0", b"\x00\x01\x02\x03", "Lorem ipsum", 0)
print(rows[1])
assert rows[1] == (3, False, 123456789, 1.234567, "abc2", b"\x00\x01\x02\x03", "Lorem ipsum dolor", 0)

print("---- remove column")

table.removeColumn("myvalue")

print("---- verify the remove column operation")

rows = table.getRows()
assert len(rows) == 2
print(rows[0])
assert rows[0] == (1, True, 123, 1.23, "abc0", b"\x00\x01\x02\x03", "Lorem ipsum")
print(rows[1])
assert rows[1] == (3, False, 123456789, 1.234567, "abc2", b"\x00\x01\x02\x03", "Lorem ipsum dolor")

print("---- verify distinct queries")

table.addRow({
	"mybool": True,
	"myint": 123,
	"myfloat": 1.23,
	"mystr": "abc0",
	"myblob": b"\x00\x01\x02\x03",
	"myclob": "Lorem ipsum",
})

rows = table.getDistinct([ "myint" ])
assert len(rows) == 2
print(rows[0])
assert rows[0] == (123,)
print(rows[1])
assert rows[1] == (123456789,)

rows = table.getDistinct([ "myint", "mystr", "myclob" ])
assert len(rows) == 2
print(rows[0])
assert rows[0] == (123, "abc0", "Lorem ipsum")
print(rows[1])
assert rows[1] == (123456789, "abc2", "Lorem ipsum dolor")

print("--- ALL TESTS SUCCEEDED.")













