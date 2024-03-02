#Week 4 catch up main code for fuelwatch.py
#use pdb for breakpoint

import feedparser
from pprint import pprint

def get_fuel(product_id):
    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb=Cloverdale'
    data = feedparser.parse(url)
    return data['entries']
  
unleaded = 1
premium_unleaded = 2

u_prices = get_fuel(unleaded)
pu_prices = get_fuel(premium_unleaded)

#pprint(u_prices)


item_1 = u_prices[0] #THIS is taking from a list of parameters with unleaded

print(str(type(u_prices)) + "Length  of entries " + str(len(u_prices)))
#pprint(item_1) #print out the first1

address1 = item_1['address']  #THIS is taking from a dictionary

#pprint(address1)
#print(item_1.values())
#for item in item_1.values()
	#print(item)
# use TYPE()
#

print(item_1.keys())
#print(str(type(item_1.keys())))
### looping

fullString = '<tr>' #is this necessary

for labels in item_1.keys():
    fullString += f' <td>{labels}</td>'

fullString += f'</tr>'

for item in u_prices:
    fullString += f' <tr>'
    for item2 in item.keys():
	  #print(item['location'])
	    #fullString += f' <tr> <td>{item["title"]}</td> <td>{item["title_detail"]}</td> <td>{item["summary"]}</td> <td>{item["summary_detail"]}</td> </tr>'
		    fullString += f'<td>{item[str(item2)]}</td>' #get string value of key and put in 
        #fullString += f' </tr>'
        #if item2 != ()
		  #fullString += f' <td>{item[item2]}</td>'
    fullString += f' </tr>'

##html related
my_html = f'''
<!DOCTYPE html>
<html>
  <head>
    <style>
      table {{
        border-collapse: collapse;
      }}
      td {{
        border: 0px red solid;
      }}
    </style>
  </head>
  <body>
    <table>
      <tr>
        <td>LOCATION</td>
        <td>ADDRESS</td>
        <td>BRAND</td>
      </tr>
     {fullString}
    </table>
  </body>
</html>
'''
f = open('render.html', 'w')
f.write(my_html)
f.close()