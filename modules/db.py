#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2019 by Keno "docplay" Hummel.
# All rights reserved. Do not distribute!
# This file is part of the database Project.

import sqlite3
import modules

def generate():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE  TABLE IF NOT EXISTS "guilds" ("guild_id"	INTEGER UNIQUE,"guild_prefix"	TEXT DEFAULT '!',"guild_invite"	TEXT,"guild_cid_wlcm"	INTEGER,"guild_cid_cntrl"	INTEGER,"guild_cid_spprt"	INTEGER,"guild_rules"	TEXT DEFAULT 'n/a',"guild_owner"	INTEGER,PRIMARY KEY("guild_id"))""")
    connection.commit()
    connection.close()

def addGuild(guild):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(f""""INSERT INTO "guilds" ("guild_id","guild_owner") VALUES ({guild.id},{guild.owner_id}); """)
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS "{guild.id}_user" ("user_id"	INTEGER NOT NULL UNIQUE,"user_valid"	BOOLEAN DEFAULT 0,"user_joindate"	TEXT NOT NULL,"user_xp"	INTEGER DEFAULT 0,"user_msg"	INTEGER DEFAULT 0,"user_tickets"	INTEGER DEFAULT 0,"user_warns"	INTEGER DEFAULT 0,"user_kicks"	INTEGER DEFAULT 0,"user_bans"	INTEGER DEFAULT 0,PRIMARY KEY("user_id")))""")
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS "{guild.id}_modactions" ("case_id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,"mod_id"	INTEGER,"target_id"	INTEGER,"action"	TEXT,"reason"	TEXT)""")
    connection.commit()
    connection.close()



def execute(command):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(command)
    connection.commit()
    connection.close()

def getXp(id):
     connection = sqlite3.connect("database.db")
     cursor = connection.cursor()
     cursor.execute("SELECT xp FROM user WHERE id = " + str(id))
     return int(cursor.fetchall()[0][0])
     connection.commit()
     connection.close()

def addXp(id, xp):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE user SET xp =" + str(xp) + " WHERE id = " + str(id))
    connection.commit()
    connection.close()

def getLvl(id):
     connection = sqlite3.connect("database.db")
     cursor = connection.cursor()
     cursor.execute("SELECT level FROM user WHERE id = " + str(id))
     return int(cursor.fetchall()[0][0])
     connection.commit()
     connection.close()

def addLvl(id, lvl):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE user SET level =" + str(lvl) + " WHERE id = " + str(id))
    connection.commit()
    connection.close()

def  getMsg(id):
     connection = sqlite3.connect("database.db")
     cursor = connection.cursor()
     cursor.execute("SELECT messages FROM user WHERE id = " + str(id))
     return int(cursor.fetchall()[0][0])
     connection.commit()
     connection.close()

def addMsg(id):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("SELECT messages FROM user WHERE id = " + str(id))
    result_msg = cursor.fetchall()
    newmsg = result_msg[0][0] + 1
    cursor.execute("UPDATE user SET messages =" + str(newmsg) + " WHERE id = " + str(id))
    connection.commit()
    connection.close()

def addUser(usr_id, usr_name,time=f"{modules.cmd.time.ctime()}", usr_xp=0):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO user ('id', 'name', 'messages', 'xp', 'level') VALUES({str(usr_id)},  '{str(usr_name)}', 0, {str(usr_xp)}, 0);")
    connection.commit()
    connection.close()


     