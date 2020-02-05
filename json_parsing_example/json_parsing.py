import json

json_file_path = 'rectangle_glasses.json'
with open(json_file_path, 'rb') as f:
  data = json.load(f)

if data['lens']['type'] == "rectangle":
   height = data['lens']['height']
   width = data['lens']['width']
   bridge_w = data['bridge_w']
   bridge_h = data['bridge_h']
   temple_holder_h = data['temple_holder_h']
   temple_holder_w = data['temple_holder_w']
   frame_color = data['color']['frame']
   lens_color = data['color']['lens']

   print('Rectangle glasses properties:')
   print(height)
   print(width)
   print(bridge_w)
   print(bridge_h)
   print(temple_holder_h)
   print(temple_holder_w)
   print(frame_color)
   print(lens_color)



json_file_path = 'round_glasses.json'
with open(json_file_path, 'rb') as f:
  data = json.load(f)

if data['lens']['type'] == "round":
   diameter = data['lens']['diameter']
   bridge_w = data['bridge_w']
   bridge_h = data['bridge_h']
   temple_holder_h = data['temple_holder_h']
   temple_holder_w = data['temple_holder_w']
   frame_color = data['color']['frame']
   lens_color = data['color']['lens']

   print('Round glasses properties:')
   print(diameter)
   print(bridge_w)
   print(bridge_h)
   print(temple_holder_h)
   print(temple_holder_w)
   print(frame_color)
   print(lens_color)
