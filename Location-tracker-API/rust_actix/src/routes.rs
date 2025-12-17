use actix_web::{web,HttpResponse};use sqlx::SqlitePool;use crate::models::Location;
pub fn config(cfg:&mut web::ServiceConfig){
 cfg.route("/locations",web::post().to(add))
    .route("/locations",web::get().to(latest))
    .route("/locations/{id}",web::get().to(one))
    .route("/locations/{id}/history",web::get().to(hist));}
async fn add(pool:web::Data<SqlitePool>,b:web::Json<serde_json::Value>)->HttpResponse{
 sqlx::query("INSERT INTO locations(user_id,latitude,longitude,timestamp) VALUES (?,?,?,datetime('now'))")
 .bind(&b["user_id"]).bind(&b["latitude"]).bind(&b["longitude"]).execute(pool.get_ref()).await.unwrap();
 HttpResponse::Created().finish()}
async fn latest(pool:web::Data<SqlitePool>)->HttpResponse{
 let r=sqlx::query_as::<_,Location>("SELECT * FROM locations l WHERE timestamp=(SELECT MAX(timestamp) FROM locations WHERE user_id=l.user_id)").fetch_all(pool.get_ref()).await.unwrap();
 HttpResponse::Ok().json(r)}
async fn one(pool:web::Data<SqlitePool>,id:web::Path<String>)->HttpResponse{
 let r=sqlx::query_as::<_,Location>("SELECT * FROM locations WHERE user_id=? ORDER BY timestamp DESC LIMIT 1").bind(id.into_inner()).fetch_optional(pool.get_ref()).await.unwrap();
 HttpResponse::Ok().json(r)}
async fn hist(pool:web::Data<SqlitePool>,id:web::Path<String>)->HttpResponse{
 let r=sqlx::query_as::<_,Location>("SELECT * FROM locations WHERE user_id=?").bind(id.into_inner()).fetch_all(pool.get_ref()).await.unwrap();
 HttpResponse::Ok().json(r)}
