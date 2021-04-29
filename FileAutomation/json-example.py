import json
from pprint import pprint

with open('service-policy.json', 'r') as opened_file:
	policy = json.load(opened_file)
	pprint(policy)