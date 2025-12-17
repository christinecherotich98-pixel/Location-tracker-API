const r=require('express').Router();const db=require('./state');
r.post('/locations',(req,res)=>{db.prepare('INSERT INTO locations(user_id,latitude,longitude,timestamp) VALUES (?,?,?,?)')
.run(req.body.user_id,req.body.latitude,req.body.longitude,new Date().toISOString());res.status(201).json({status:'stored'});});
r.get('/locations',(req,res)=>{res.json(db.prepare(`SELECT * FROM locations l WHERE timestamp=(SELECT MAX(timestamp) FROM locations WHERE user_id=l.user_id)`).all());});
r.get('/locations/:id',(req,res)=>{res.json(db.prepare('SELECT * FROM locations WHERE user_id=? ORDER BY timestamp DESC LIMIT 1').get(req.params.id)||{});});
r.get('/locations/:id/history',(req,res)=>{res.json(db.prepare('SELECT * FROM locations WHERE user_id=?').all(req.params.id));});
module.exports=r;