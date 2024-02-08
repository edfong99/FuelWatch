#for comments
#print('hello world and here is a number', 1+1)

""" wk1.1
import feedparser
import requests

response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale', headers={'user-agent': ''})

#wk1 print(response.content)

feed1 = feedparser.parse(response.content)
print(feed1)


import feedparser
import requests
from pprint import pprint

response = requests.get('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale', headers={'user-agent': ''})

#wk1 print(response.content)

feed1 = feedparser.parse(response.content)
#wk1.2 print(feed1)


pprint(feed1)
"""
"""------------------------------------------------------------------------------
WEEK2 - Data Backbones of Python: List and Dictionaries

and FUNCTIOnS


import feedparser
import json

feed1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Bentley&Surrounding=no')

print(json.dumps(feed1, indent=2))
"""
"""---------------------------------------------------------------------------------
WEEK3 notes

3 ways to join strings

first_name = 'James'
last_name = 'Bond'

1.. using + , sentece = 'My name is' + last_name + first_name + 'whatever u wanna write'
a. use %s , sentece1 'My name is %s %s' %(lastname,firstname)// old python way
2. sentece 2 = 'my name is {} {} {}' .format(lastname, firstname, lastname)
   //specify array index//  2b = 'my name is {1} {0} {1}'.format(firstname, lastname)
   // specify key// 2c = my name is {lname} {fname} {lname}.format(fname=firstname, lname = lastname)

   keyword argument example:
function example
  def minus(a,b)a;
  return a-b

minus(4,3)
minus(a =4, b=3)
minus (b = 3, a=4) -- providing keyword argument

3. fstring// sentence3 = f'my name is {first_name} {last_name} etc'

curly braces in 2,3 cannot take in variables like the fstring

// In python most things are object, so we can use .method for most

looking at JSON dump:
"string" is a list of dictionaries with:
	entries - list of dictionaries
		title - string value
		title detail - list of dictionaries
			type 

HTML CODE

Generate table HTML: https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro
Colouring elements: https://www.w3schools.com/html/html_styles.asp
Styling with CSS: https://developer.mozilla.org/en-US/docs/Web/CSS/Class_selectors

<html>
  <head>
    <style>
      table {
        border-collapse: collapse;
      }
      td {
        border: 1px red solid;
      }
    </style>
  </head>
  <body>
    <table>
      <tr>
        <td>one</td>
        <td>two</td>
      </tr>
      <tr>
        <td>one</td>
        <td>two</td>
      </tr>
    </table>
  </body>
</html>

l = ['one', 'two', 'three']

my_html_list = ''
for word in l:
    #my_list += '<li>' + word + '</li>'
    #my_list += '<li>{}</li>'.format(word)
    my_html_list += f'<li>{word}</li>'

my_html = f'''
<h1>Heading 1</h1>
<p>paragraph</p>
<ol>
    <li>one</li>
    <li>two</li>
</ol>

<ul>
    {my_html_list}
</ul>
'''
"""

#setup variables

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

item_1 = u_prices[0] #THIS is taking from a list
address1 = item_1['address']  #THIS is taking from a dictionary

#pprint(address1)
#print(item_1.values())
#for item in item_1.values()
	#print(item)
# use TYPE()
#

fullString = ''
for item in u_prices:
	fullString += f' <tr>'
	for item2 in item.keys():
	#print(item['location'])
	#fullString += f' <tr> <td>{item["location"]}</td> <td>{item["address"]}</td> <td>{item["brand"]}</td> <td>{item["brand"]}</td></tr>'
		#if item2 != ()
		fullString += f' <td>{item[item2]}</td>'
	fullString += f' </tr>'

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

"""
Create a Folder with all code inside with version control
WK 4 learning GIT

git init - creat git branch, folder is now version control

list in content and you will see .git folder
OR use git status

git status - ** USEFUL

untracked files --> not version
"""
print("HelloWorld")
