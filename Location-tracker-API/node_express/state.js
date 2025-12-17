const DB=require('better-sqlite3');const db=new DB('locations.db');
db.prepare(`CREATE TABLE IF NOT EXISTS locations(id INTEGER PRIMARY KEY,user_id TEXT,latitude REAL,longitude REAL,timestamp TEXT)`).run();
module.exports=db;