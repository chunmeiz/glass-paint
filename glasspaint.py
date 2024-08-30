import csv
import json

with open("nozzle_config.json") as f:
  nozzle_flows = json.load(f)

def rgb_to_cmyk(red, green, blue):
  # Roughly convert RGB values to CMYK values for printing.
  # Return a dictionary with the keys 'cyan', 'magenta', 'yellow', 'black'.
  # convert values to 0-1 range
  red, green, blue = map(lambda x: x / 255, (red, green, blue))
  black = 1 - max(red, green, blue)
  cyan = ((1 - red - black) / (1 - black)) if black != 1 else 0
  magenta = ((1 - green - black) / (1 - black)) if black != 1 else 0
  yellow = ((1 - blue - black) / (1 - black)) if black != 1 else 0
  # represent each of the colour values as an integer 'ink unit' out of 100
  cyan, magenta, yellow, black = map(lambda x: int(x * 100), (cyan, magenta, yellow, black))
  return { "cyan": cyan, "magenta": magenta, "yellow": yellow, "black": black }

# complete your code here

filename = input('Input file: ')
all_rgb = []
with open(filename) as csvfile:
  csvreader = csv.reader(csvfile)
  next(csvreader)
  for line in csvreader:
    new_line = [int(val) for val in line]
    all_rgb.append(new_line)
    
  

def check_rgb_valid(all_rgb):
  i=0
  for line in all_rgb:
    i+=1
    for num in line:
      if num < 0 or num > 255:
        invalid = i
        print(f'Invalid ink value on tile {invalid}.')
        line =[0,0,0]
        
    
count = 0   
sort_record = {}
for line in all_rgb:
      red,green,blue =  line[0],line[1],line[2]
     
      CMYK = rgb_to_cmyk(red, green, blue)
      if (red, green, blue)==(0,0,0):
        CMYK["black"] =0

      initial = []
      nozzle = []
      for key, val in CMYK.items():
        initial.append(val)
      for key, val in nozzle_flows.items():
        nozzle.append(val)
      sorting_val = max(initial[0] * nozzle[0], initial[1] * nozzle[1], initial[2] * nozzle[2], initial[3] * nozzle[3])
      
      count += 1
      sort_record[count] = sorting_val
print(sort_record)
sorted_val = dict(sorted(sort_record.items(), key=lambda item: item[1]))
print(sorted_val)
for key, val in sorted_val.items():
  print(key)


