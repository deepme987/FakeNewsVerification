'''
DO NOT RUN MORE THAN ONCE!!!
HIGH RISK OF DUPLICATE DATA
'''

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
print(myclient.list_database_names())

FakeNews = mydb["Fake_News"]

FakeNews.insert_many([{'Title':"Weak, Exhausted Nancy Pelosi Given Saline Drip Following Hours-Long Attempt To Stand Firm In Convictions", 'Domain': 'theonion.com'},
{'Title': "Resistance Democrat Racking Brain For Way To Sexualize Anonymous Whistleblower", 'Domain': 'theonion.com'},
{'Title': "A Piece Of History: The Beautiful Velvet Ribbon That Made JFK’s Head Fall Off When It Was Untied Is Coming To The Smithsonian", 'Domain': 'clickhole.com'},
{'Title': "Something For The Foot Fetish Crowd: This Foot Wants To Have Sex With You!", 'Domain': 'clickhole.com'},
{'Title': "Chiefs Trainer Squirts Bottle Of KC Masterpiece Into Andy Reid's Mouth", 'Domain': "theonion.com"},
{'Title': "Awesome: Home Depot Is Now Selling An Incredibly Weak Pepper Spray You Can Use On People Who Are Annoying But Not Dangerous", 'Domain': 'clickhole.com'},
{'Title': "Pompeo To Increase Bombing In Afghanistan After Figuring They’ll Miss And Hit Iran At Some Point", 'Domain': 'theonion.com'},
{'Title': "Stunning Intelligence: For The First Time Ever, Scientists Have Observed A Chimpanzee Blow Up A Human Child With Its Mind", 'Domain': "clickhole.com"}])

print(*FakeNews.find(), sep = "\n")
