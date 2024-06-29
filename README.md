# ChefGPT - Your Personal Chef

ChefGPT is an AI-powered personal chef assistant built using LangChain and Streamlit. This interactive chatbot can help you find recipes based on ingredients or dietary preferences, suggest recipes that cater to specific allergies, and even recommend hotels serving your desired dishes in a specified city.

## Features

- **Recipe Suggestions**: Get recipes based on specific ingredients or dish names.
- **Allergy-Friendly Recipes**: Filter recipes to include or exclude certain ingredients.
- **Hotel Recommendations**: Find hotels that serve specific recipes in your desired city.
- **Continuous Conversation**: Maintain context throughout the conversation for a seamless user experience.

## Technology Stack

- **LangChain**: For implementing the language model and managing tools.
- **Streamlit**: For creating the interactive user interface.
- **Spoonacular API**: For fetching recipes and related data.
- **SerpAPI**: For retrieving hotel recommendations.
- **Model used**: "llama3-70b-8192" (Groq)

## Getting Started

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Set up your environment variables in a `.env` file.
4. Run the Streamlit app with `streamlit run main.py`.

## Demo Screenshots

![Screenshot 1](Screenshot2024-06-29_203923.png)
![Screenshot 2](Screenshot2024-06-29_204020.png)
![Screenshot 3](Screenshot2024-06-29_204050.png)
