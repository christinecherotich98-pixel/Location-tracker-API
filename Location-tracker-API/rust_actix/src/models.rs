use serde::Serialize;#[derive(Serialize,sqlx::FromRow)]
pub struct Location{pub id:i64,pub user_id:String,pub latitude:f64,pub longitude:f64,pub timestamp:String}