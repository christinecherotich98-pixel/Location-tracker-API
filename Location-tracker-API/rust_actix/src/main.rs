use actix_web::{App,HttpServer,web};mod routes;mod state;
#[actix_web::main] async fn main()->std::io::Result<()>{
 let pool=state::init().await;
 HttpServer::new(move||App::new().app_data(web::Data::new(pool.clone())).configure(routes::config))
 .bind(("0.0.0.0",8080))?.run().await}
