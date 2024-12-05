#!/usr/bin/env python3

show dbs;
use ejv4pz;
show collections;

#create new collection "contacts" with five docs
db.contacts.insertMany( [
   { name: "Anila", university:"UVA", age: 19, contacts: {email: "anila.noushin@gmail.com", phone: 5793442673, status: "Friend" },
   { name: "Odin", university:"Geneva", age: 20, contacts: {email: "okulp@gmail.com", phone: 7825672345}, status: "Friend"},
   { name: "Vanessa", university:"CNU", age: 18, contacts: {email: "vjadenewman@yahoo.com", phone: 5404339876}, status: "Friend"},
   { name: "Carson", university:"UVA", age: 20, contacts: {email: "cmbarnes@gmail.com", phone: 5732132234}, status: "Friend"},
   { name: "Ally", university:"UVA", age: 19, contacts: {email: "allyson231@gmail.com", phone: 8654230098}, status: "Roommate"}
] );

db.contacts.find({"university": "UVA"})
