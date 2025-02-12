import requests
import json


CAT_API = "https://catfact.ninja/"

def get_cats_facts(number):
    for i in range(number):
        response = requests.get(f"{CAT_API}fact")
        new_response = json.loads(response.text)
        list_of_facts = []
        list_of_facts.append(new_response["fact"])

        for idx, value in enumerate(list_of_facts):
            print(f"{i+1}.\t{value}")


num_facts = 3
get_cats_facts(num_facts)