use sqlx::SqlitePool;pub async fn init()->SqlitePool{
 let p=SqlitePool::connect("sqlite:locations.db").await.unwrap();
 sqlx::query("CREATE TABLE IF NOT EXISTS locations(id INTEGER PRIMARY KEY,user_id TEXT,latitude REAL,longitude REAL,timestamp TEXT)").execute(&p).await.unwrap();p}
