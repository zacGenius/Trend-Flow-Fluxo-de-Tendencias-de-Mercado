from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *


# 0. Start SparkSession
spark = SparkSession.builder.appName('TransformProductsJson').getOrCreate()

# 1. Bronze Layer reading
df_bronze = spark.read.json('data/bronze/*.json')

# 2. Extract
df_silver = df_bronze.select(F.explode('products').alias("p")).select(
    F.col('p.id').alias('id'),
    F.col('p.title').alias('title'),
    F.col('p.description').alias('description'),
    F.col('p.category').alias('category'),
    
)











