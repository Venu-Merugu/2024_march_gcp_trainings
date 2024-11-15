from google.cloud import bigquery

import os

os.environ["GOOGLE-CLOUD-CREDENTIALS"] = "C:/Users/VENU GOPAL/2024_march_gcp_trainings/march2024gcptrainings"

client = bigquery.Client()

tabl_path = "march2024gcptrainings.test_practice_march_ptdh.emp"

schema =[
    bigquery.SchemaField("eid","INTEGER"),
    bigquery.SchemaField("ename","STRING"),
    bigquery.SchemaField("edesg","STRING")
]

tble=bigquery.Table(tabl_path,schema)

table = client.create_table(tble)

print(f"{table} is created and it's dataset id is {table.dataset_id}")