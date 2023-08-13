import jsonschema
import simplejson as json
import sys
import jsonpath_rw
from pprint import pprint

if len(sys.argv)!=2:
  print("%s <schema.json>" % (sys.argv[0]))
  sys.exit(1)


json_schema = sys.argv[1]
with open(json_schema, 'r') as f:
    schema_data = f.read()
    schema = json.loads(schema_data)

for i in jsonpath_rw.parse("$..* where properties").find(schema):
    i.value['additionalProperties'] = False

# Don't forget to add it at the root level
schema['additionalProperties'] = False

print(json.dumps(schema, sort_keys=True, indent=2))
