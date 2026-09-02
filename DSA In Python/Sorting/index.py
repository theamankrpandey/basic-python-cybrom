# import json
# p_data={'x':True,'y':False,'z':None}
# j_data=json.dumps(p_data)
# print(j_data)
# print(type(j_data))
# p_data={10,20,30,40,50}
# print(json.dumps(p_data))


import json

j_data="python"
print(type(j_data))

j_data='[10,20,"python"]'
print(type(j_data))

j_data='{"x":true,"y":false,"z":null}'
print(type(j_data))

p_data = json.loads(j_data)
print(p_data)
print(type(p_data))