from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import *


# 0. Start SparkSession
spark = SparkSession.builder.appName('TransformProductsJson').getOrCreate()

# 1. Bronze Layer reading
df_bronze = spark.read.option('multiLine', True).json('data/bronze/*.json')

# 2. Silver Layer (Explode + Selection + Data Types)
df_silver = df_bronze.select(F.explode('products').alias('p')).select(
    F.col('p.id').cast(IntegerType()).alias('id'),
    F.col('p.title').cast(StringType()).alias('product_name'),
    F.col('p.category').cast(StringType()).alias('category'),
    F.col('p.price').cast(FloatType()).alias('price'),
    F.col('p.discountPercentage').cast(FloatType()).alias('discount'),
    F.col('p.rating').cast(FloatType()).alias('rating'),
    F.col('p.brand').cast(StringType()).alias('brand'),
    F.col('p.warrantyInformation').cast(StringType()).alias('warranty_info'),
    F.col('p.shippingInformation').cast(StringType()).alias('shipping_info'),
    F.col('p.availabilityStatus').cast(StringType()).alias('stock_status'),
    F.size('p.reviews').alias('numReviews')
)

# 3. Save as Parquet (Standard in Silver Layer)
df_silver.write.mode('overwrite').parquet('data/silver')

