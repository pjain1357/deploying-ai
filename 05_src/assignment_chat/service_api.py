from langchain.tools import tool
import json
import requests


@tool
def get_metropolitan_museum_facts(n:int=1):
    """
    Returns facts from Metropolitan Museum of Art.
    """
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
    params = {
        "count": n
    }
    response = requests.get(url, params=params)
    resp_dict = json.loads(response.text)
    facts_list = resp_dict.get("data", [])
    facts = "\n".join([f"{i+1}. {fact}\n" for i, fact in enumerate(facts_list)])
    return facts

@tool
def get_art_institute_facts(n:int=1):
    """
    Returns Art Institute of Chicago facts.
    """
    url = "https://api.artic.edu/api/v1/artworks"
    params = {
        "limit": n
    }
    response = requests.get(url, params=params)
    resp_dict = json.loads(response.text)
    facts_list = resp_dict.get("data", [])
    facts = "\n".join([
                f"{i+1}. {fact['attributes']['body']}\n" 
                for i, fact in enumerate(facts_list)    
                if isinstance(fact, dict) and 'attributes' in fact
            ])
    return facts
