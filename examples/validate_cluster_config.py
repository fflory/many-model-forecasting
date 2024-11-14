# Databricks notebook source
# MAGIC %md
# MAGIC We recommend using a cluster with Databricks Runtime 14.3 LTS for ML or above. The cluster can be either a single-node or multi-node CPU cluster. MMF leverages Pandas UDF under the hood and utilizes all the available resource. Make sure to set the following Spark configurations before you start your cluster: spark.sql.execution.arrow.enabled true and spark.sql.adaptive.enabled false. You can do this by specifying Spark configuration in the advanced options on the cluster creation page.

# COMMAND ----------

assert(all([
  spark.conf.get("spark.sql.execution.arrow.enabled") == 'true', 
  spark.conf.get("spark.sql.adaptive.enabled") == 'false'
  ]))

# COMMAND ----------


