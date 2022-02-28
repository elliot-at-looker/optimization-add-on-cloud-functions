from google.cloud import bigquery
import json

def get_word_frequency(request):
  print("get_word_frequency")
  request_json = request.get_json(silent=True)
  sql = request_json["sql"]
  table_id = "airy-task-342220.word_freq.frequency"
  request_json = request.get_json(silent=True)
  client = bigquery.Client.from_service_account_json('auth.json')
  query_string = f"""{sql}"""  
  query_job = client.query(query_string)
  rows = list(query_job)
  records = [dict(row) for row in query_job]
  return json.dumps(records), 200, {'Content-Type': 'application/json'}