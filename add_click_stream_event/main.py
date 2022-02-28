from google.cloud import bigquery
import json

def add_click_stream_event(request):
  print("add_click_stream_event")
  request_json = request.get_json(silent=True)
  sql = request_json["sql"]
  print("sql")
  table_id = "airy-task-342220.analytics.quickstream"
  request_json = request.get_json(silent=True)
  client = bigquery.Client.from_service_account_json('auth.json')
  query_string = f"""{sql}"""  
  query_job = client.query(query_string)
  results = query_job.result()
  
  return json.dumps({"message": "success"}), 200, {'Content-Type': 'application/json'}