from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("SparkKafkaExample") \
    .getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Define Kafka source and sink topics
input_topic = "sales_topic_electronics"
output_topic = "processed_sales_topic"

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", input_topic) \
    .option("startingOffsets", "earliest") \
    .load()

# Process data
# Assuming the value is a JSON string, you may need to adjust based on your actual data format
processed_df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Write to Kafka
query = processed_df.writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("topic", output_topic) \
    .option("checkpointLocation", "/tmp/kafka-to-kafka-checkpoint") \
    .start()

# Await termination
query.awaitTermination()
