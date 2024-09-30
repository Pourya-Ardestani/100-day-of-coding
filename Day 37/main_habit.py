import requests
import datetime

USERNAME = "pouryaarde"
TOKEN = "pixela_token"
GRAPH_ID = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# TODO create account in pixela
# response = requests.post(url=pixela_endpoint,json = user_params)
# print(response.text)

graf_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    "id": GRAPH_ID,
    "name": "Book Reader Graph",
    "unit": "page",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# TODO create graph
# response = requests.post(url=graf_endpoint, json=graph_config, headers=headers)
# print(response.text)
#TODO POST PIXEL
date = datetime.datetime(year=2024, month=9, day=18)
quantity = input("how many pages do you read today:")
print(date)
formatted_date = date.strftime('%Y%m%d')
point_params = {
    'date': formatted_date,
    'quantity': quantity,
}
point_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=point_endpoint, json=point_params, headers=headers)
print(response.text)

#TODO UPDATE WITH PUT
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
# point_update ={
# 'quantity': quantity
# }
# response = requests.put(url=update_endpoint,json=point_update,headers=headers)
# print(response.text)

 #TODO DELETE

# delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}'
# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)