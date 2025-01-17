from pyspark.sql import SparkSession

from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("appName").getOrCreate()

schema = StructType(
    [StructField("id", IntegerType(), True), StructField("name", StringType(), True)]
)
data = []
df = spark.creteDataFrame(data, schema)

data_size = df.rdd.map(lambda row: len(str(row))).sum()  # Approximate size in bytes
partition_size = 128 * 1024 * 1024  # Partition size: 128 MB

# Calculate number of partitions
num_partitions = (data_size // partition_size) + 1
print(f"Number of partitions: {num_partitions}")

# Repartition the DataFrame
df_repartitioned = df.repartition(num_partitions)
