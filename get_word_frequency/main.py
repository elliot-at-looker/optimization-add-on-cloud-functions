from google.cloud import bigquery
import json

def get_word_frequency(request):

  request_json = request.get_json(silent=True)
  print(request_json)
  sql = request_json["sql"]
  print(sql)
  # print(request.args)
  # if request.args and 'sql' in request.args:
  #     return request.args.get('sql')
  # elif request_json and 'sql' in request_json:
  #     return request_json['sql']
  # else:
  #     return f'get_word_frequency!'

  table_id = "airy-task-342220.word_freq.frequency"
  request_json = request.get_json(silent=True)
  client = bigquery.Client.from_service_account_json('auth.json')
  # query_string = f"""SELECT * FROM `word_freq.frequency` LIMIT 10""" 
  query_string = f"""{sql}"""  
  print(query_string)
  #  
  query_job = client.query(query_string)
  # for row in query_job:
  #   print("row") 
  #   print(row) 
  #   print("row[0]")
  #   print(row[0])
  #   print("row[1]")
  #   print(row[1])
  # results = query_job.result()
  rows = list(query_job)
  print(rows)
  print("Query results loaded to the table {}".format(table_id))
  #https://stackoverflow.com/questions/55681206/how-to-convert-results-returned-from-bigquery-to-json-format-using-python
  records = [dict(row) for row in query_job]
  print(records)
  return json.dumps(records), 200, {'Content-Type': 'application/json'}