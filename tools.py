import requests
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.tools import tool

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('SPOONACULAR_API_KEY')
serp_api_key = os.getenv("SERPAPI_KEY")
def fetch_recipes(query):
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={api_key}"
    response = requests.get(url)
    return response.json()

def get_recipe_texts(recipes):
    recipe_texts = ""
    for recipe in recipes:
        recipe_texts += recipe['title'] 
    return recipe_texts

@tool
def retrieve_recipes(query):
    """Get relevant recipes based on the user input."""
    recipes = fetch_recipes(query)
    recipe_texts = get_recipe_texts(recipes['results'])
    return recipe_texts

def fetch_recipes_by_ingredients(ingredients):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={','.join(ingredients)}&apiKey={api_key}"
    response = requests.get(url)
    return response.json()

def get_recipe_texts_by_ingredients(recipes):
    recipe_texts = ""
    for recipe in recipes:
        recipe_texts += recipe['title']
    return recipe_texts

@tool
def retrieve_recipes_by_ingredients(ingredients):
    """Get relevant recipes based on the ingredients provided by the user. This should be used when 
    the user specifies more than one ingredients in the query or "and" is used in the query."""
    recipes = fetch_recipes_by_ingredients(ingredients)
    recipe_texts = get_recipe_texts_by_ingredients(recipes)
    return recipe_texts

def fetch_hotels(query, location):
    url = f"https://serpapi.com/search.json?q={query}+restaurants+in+{location}&hl=en&gl=us&api_key={serp_api_key}"
    response = requests.get(url)
    return response.json()

def get_hotel_texts(results):
    hotel_texts = ""
    for result in results['local_results']['places']:
        hotel_texts += f"Name: {result['title']}, Address: {result['address']}\n"
    return hotel_texts

@tool
def retrieve_hotels(query, location):
    """Get hotels serving the required recipe in a specific city."""
    results = fetch_hotels(query, location)
    hotel_texts = get_hotel_texts(results)
    return hotel_texts

if __name__ == '__main__':
    query = "chicken"
    recipes = fetch_recipes(query)
    recipe_texts = get_recipe_texts(recipes['results'])
    results = retrieve_hotels("chicken", "rajahmundry")
    print(results)
