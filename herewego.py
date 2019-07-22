cursor = db.cursor()

 cursor.execute('''PRAGMA foreign_keys = ON''')

#Create Users Table
cursor.execute('''
CREATE TABLE users (
                user_id INTEGER PRIMARY KEY, 
                first_name TEXT NOT NULL, 
                last_name TEXT NOT NULL, 
                dob date, 
                email TEXT NOT NULL, 
                user_role TEXT NOT NULL, 
                user_phone TEXT
                );
''')

#Create Events table
cursor.execute('''
CREATE TABLE events (
                event_id INTEGER PRIMARY KEY, 
                event_name TEXT NOT NULL, 
                event_city TEXT NOT NULL, 
                event_type TEXT, 
                event_start date NOT NULL,
                event_end date, 
                event_capacity INTEGER NOT NULL,
                venue_id  INTEGER NOT NULL,
                                FOREIGN KEY(venue_id) REFERENCES venue(venue_id)
                );
''')

#Create venues table
cursor.execute(''' 
CREATE TABLE  venues (
                venue_id INTEGER PRIMARY KEY,
                venue_name TEXT NOT NULL,
                venue_open date,
                venue_close date,
                zip_code TEXT NOT NULL,
                city TEXT,
                address TEXT NOT NULL
				);
''')

 #Create user_events table
 cursor.execute(''' 
 CREATE TABLE user_events(
                user_id INTEGER NOT NULL REFERENCES users(user_id),
                event_id INTEGER NOT NULL REFERENCES events(event_id),
                PRIMARY KEY(user_id,event_id)
                );
 ''')                   

 db.commit()