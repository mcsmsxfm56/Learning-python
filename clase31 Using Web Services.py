#formats to exchange data between sites: XML and JSON
#Sending data across the net(PHP Array, Javascript Object, Java HashMap, Python Dictionary)
{
    "name": "Chuck",
    "phone": "303-4456"
}
#XML (eXtensible Markup Language)
#primary purpose is to help information systems share structured data
#xml uses tags, attributes and serialize/de-serialize
#seriealize/de-serialize: convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner

#xml example
#<person>
#   <name>Chuck</name>
#   <phone type="intl">
#       +1 734 303 4456
#   </phone>
#   <email hide="yes"/>
#</person>

#XML Schema
#Description of the legal format of an XML document
#Expressed in terms of constraints on the structure and content of documents
#Often used to specify a "contract" between systems - "My system will only accept XML  that conforms to this particular schema"

#if a particular piece of XML Meets the specification of the schema it is say to validate

#XML Document
#<person>
#   <lastname>Severance</lastname>
#   <age>17</age>
#   <dateborn>2001-04-17</dateborn>
#</person>

#XML Schema Contract
#<xs:complexType name="person">
#   <xs:sequence>
#       <xs:element name="lastname" type="xs:string">
#       <xs:element name="age" type="xs:integer">
#       <xs:element name="dateborn" type="xs:date">
#   </xs:sequence>
#</xs:complexType>

#in this class will se XSD, elements, sequences and complexType
#<xs:complexType name="person">
#   <xs:sequence>
#       <xs:element name="lastname" type="xs:string" minOccurs="1" maxOccurs="1"> minoccurs tell how many times the tag is present
#       <xs:element name="age" type="xs:integer">
#       <xs:element name="dateborn" type="xs:date">
#   </xs:sequence>
#</xs:complexType>

#types of xml
#date 2002-09-24
#startdate 2002-05-30T09:30:10Z t is hour and z is timezone
#decimal 999.50
#integer 30

#Web Services: JSON
import json

import urllib.parse
data = '''{
"name": "Chuck",
"phone": {
"type": "intl",
"number": "+1 734 303 4456"
},
"email": {
"hide": "yes"
}
}'''

info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print('lat', lat, 'lng', lng)
location = js["results"][0]['formatted_address']
print(location)
