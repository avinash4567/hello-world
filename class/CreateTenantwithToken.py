


import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\r\n\t\"aaaUser\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"name\": \"admin\",\r\n\t\t\t\"pwd\": \"ciscoapic\"\r\n\t\t}\r\n\t}\r\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY29hcGlj'}

response = requests.request("POST", url, data=payload, headers=headers)

json_response = json.loads(response.text)


#print(json_response['imdata'][0]['aaaLogin']['attributes']['token'])

tokenfromlogin =(json_response['imdata'][0]['aaaLogin']['attributes']['token'])

# Next API Request

url = "http://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting.json"
payload = "{\r\n\t\"fvAp\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-acme/ap-Accounting\",\r\n\t\t\t\"name\": \"Accounting\",\r\n\t\t\t\"rn\": \"ap-Accounting\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"

cookie = {"APIC-cookie": tokenfromlogin}
response = requests.request("POST", url, data=payload, cookies=cookie)

url = "http://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting/epg-Payroll.json"
payload = "{\"fvAEPg\":{\"attributes\":{\"dn\":\"uni/tn-acme/ap-Accounting/epg-Payroll\",\"name\":\"Payroll\",\"rn\":\"epg-Payroll\",\"status\":\"created\"},\"children\":[{\"fvCrtrn\":{\"attributes\":{\"dn\":\"uni/tn-acme/ap-Accounting/epg-Payroll/crtrn\",\"name\":\"default\",\"rn\":\"crtrn\",\"status\":\"created,modified\"},\"children\":[]}}]}}\r\nresponse: {\"totalCount\":\"0\",\"imdata\":[]}"

cookie = {"APIC-cookie": tokenfromlogin}
response = requests.request("POST", url, data=payload, cookies=cookie)

url = "http://192.168.10.1/api/node/mo/uni/tn-acme/ap-Accounting/epg-Bills.json"
payload = "{\"fvAEPg\":{\"attributes\":{\"dn\":\"uni/tn-acme/ap-Accounting/epg-Bills\",\"name\":\"Bills\",\"rn\":\"epg-Bills\",\"status\":\"created\"},\"children\":[{\"fvCrtrn\":{\"attributes\":{\"dn\":\"uni/tn-acme/ap-Accounting/epg-Bills/crtrn\",\"name\":\"default\",\"rn\":\"crtrn\",\"status\":\"created,modified\"},\"children\":[]}}]}}\r\n"

cookie = {"APIC-cookie": tokenfromlogin}
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)

