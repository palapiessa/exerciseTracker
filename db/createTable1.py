
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
    con = lite.connect('..\db\activity.db')
                                      
    cur = con.cursor()  
                                                
    cur.executescript("""
    DROP TABLE IF EXISTS activity ;              DROP TABLE IF EXISTS distanceUnit;
    DROP TABLE IF EXISTS activityType;
    CREATE TABLE activityType (Id INTEGER PRIMARY KEY, Name TEXT);
        INSERT INTO activityType VALUES(1,'cycling');                                            INSERT INTO activityType VALUES(2,'running');                                        CREATE TABLE unit (Id INTEGER PRIMARY KEY, Unit TEXT);                               INSERT INTO unit values (1, 'km');                                             INSERT INTO unit values (2, 'mi');
    CREATE TABLE activity (Id INTEGER PRIMARY KEY, Start TEXT, End TEXT, ActivityType INT, Distance REAL, unit INT, FOREIGN KEY(ActivityType) REFERENCES activityType(Id), FOREIGN KEY (unit) REFERENCES unit(Id));
        """)
      
    con.commit()
    
except lite.Error, e:
    
    if con:
     
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()

