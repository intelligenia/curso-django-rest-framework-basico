# -*- coding: utf-8 -*-

from django.db import connection

def lock_tables(tables_locks):
	"""
	Bloqueo de tablas.
	No se van a realizar comprobaciones. Se supone que lo que se introduce es
	correcto.
	
	Formato:
	{
		"tabla": ["READ"]
		"tabla2": ["READ", ["alias", "READ"], ["alias2", "WRITE"]]
	
	}
	"""
	#~ LOCK TABLES
	#~ tbl_name [AS alias] {READ [LOCAL] | [LOW_PRIORITY] WRITE}
	#~ [, tbl_name [AS alias] {READ [LOCAL] | [LOW_PRIORITY] WRITE}] ...
	
	#~ // http://dev.mysql.com/doc/refman/5.5/en/lock-tables.html
	#~ // You cannot refer to a locked table multiple times in a single query
	#~ // using the same name. Use aliases instead, and obtain a separate lock
	#~ // for the table and each alias.

	sql = ""
	
	for table, locks in tables_locks.items():
		for lock in locks:
			if sql != "":
				sql += ","
			
			if isinstance(lock, list):
				sql += "{table} AS {alias} {lock}".format(table=table, alias=lock[0], lock=lock[1])
			else:
				sql += "{table} {lock}".format(table=table, lock=lock)

	cursor = connection.cursor()
	cursor.execute('LOCK TABLES {sql};'.format(sql=sql))

def unlock_tables():
	"""
	Desbloqueo de tablas previamente bloquedas
	"""
	
	cursor = connection.cursor()
	cursor.execute("UNLOCK TABLES;")

def start_transaction():
	"""
	Inicio de una transacción
	"""
	
	cursor = connection.cursor()
	cursor.execute("START TRANSACTION;")
