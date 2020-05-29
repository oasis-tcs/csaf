import jsonschema
import simplejson as json
import sys

if len(sys.argv)!=3:
  print("<command> <schema.json> <validated.json>")
  sys.exit(1)


json_schema = sys.argv[1]
json_input = sys.argv[2]
with open(json_schema, 'r') as f:
    schema_data = f.read()
    schema = json.loads(schema_data)


with open(json_input, 'r') as f:
    input_data = f.read()
    input_obj = json.loads(input_data)

jsonschema.validate(input_obj, schema)
