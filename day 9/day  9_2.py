
travel_log = [
    {"country":"France" ,"visits" : 12,"cities" : ["occa","paris","MBAPE"]},
    {"country":"Germany","visits":20,"cities": ["Berlin","Govanda","salamatAbad"],},
    {"country":"Iran","visits" : 20,"visits":["Esfehan","Tehran","Shahre_kord"]},
]

#
def add_new_country(country_name,time_visited,cities ):
    travel_log.append({"country": country_name ,"visits":time_visited ,"cities":cities , })
    
add_new_country("Russia",2,["MOscow","saint petersborg"])
print(travel_log)