import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object ETLJob {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("ETL Recommendation")
      .getOrCreate()

    // Load data from S3 or DB
    val userEvents = spark.read
      .option("header", "true")
      .csv("s3a://your-bucket/events.csv")

    val interactions = userEvents
      .filter(col("event_type").isin("view", "like", "comment"))
      .withColumn("event_score", when(col("event_type") === "view", 1.0)
        .when(col("event_type") === "like", 2.0)
        .when(col("event_type") === "comment", 2.5))

    // Save to Parquet
    interactions.write.mode("overwrite").parquet("s3a://your-bucket/processed/interactions.parquet")

    spark.stop()
  }
}
