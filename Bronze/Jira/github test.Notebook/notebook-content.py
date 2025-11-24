# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "bba43c31-2704-43b9-8b30-6155d551ebcb",
# META       "default_lakehouse_name": "Qualys_Vulnerability_Data_Lakehouse",
# META       "default_lakehouse_workspace_id": "06cfedbc-ad86-42d5-9c92-f8903d669987",
# META       "known_lakehouses": [
# META         {
# META           "id": "bba43c31-2704-43b9-8b30-6155d551ebcb"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!

from datetime import datetime, date, timedelta

from pyspark.sql import SparkSession, Row
from pyspark.sql import functions as F
from pyspark.sql.functions import current_timestamp, when, lit, monotonically_increasing_id, expr
from pyspark.sql.types import StructField, StructType, DateType, IntegerType, StringType

import json
import re
import requests
import time

from requests.auth import HTTPBasicAuth

from delta.tables import DeltaTable

from jira import JIRA


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
