# ChefGPT - Your Personal Chef

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <p>ChefGPT is an AI-powered personal chef assistant built using LangChain and Streamlit. This interactive chatbot can help you find recipes based on ingredients or dietary preferences, suggest recipes that cater to specific allergies, and even recommend hotels serving your desired dishes in a specified city.</p>

  <h2>Features</h2>
    <ul>
        <li><strong>Recipe Suggestions</strong>: Get recipes based on specific ingredients or dish names.</li>
        <li><strong>Allergy-Friendly Recipes</strong>: Filter recipes to include or exclude certain ingredients.</li>
        <li><strong>Hotel Recommendations</strong>: Find hotels that serve specific recipes in your desired city.</li>
        <li><strong>Continuous Conversation</strong>: Maintain context throughout the conversation for a seamless user experience.</li>
    </ul>

  <h2>Technology Stack</h2>
    <ul>
        <li><strong>LangChain</strong>: For implementing the language model and managing tools.</li>
        <li><strong>Streamlit</strong>: For creating the interactive user interface.</li>
        <li><strong>Spoonacular API</strong>: For fetching recipes and related data.</li>
        <li><strong>SerpAPI</strong>: For retrieving hotel recommendations.</li>
        <li><strong>Model used</strong>: "llama3-70b-8192"(Groq)</li>
    </ul>

  <h2>Getting Started</h2>
    <ol>
        <li>Clone the repository.</li>
        <li>Install the required packages using <code>pip install -r requirements.txt</code>.</li>
        <li>Set up your environment variables in a <code>.env</code> file.</li>
        <li>Run the Streamlit app with <code>streamlit run main.py</code>.</li>
    </ol>
    ![img1](<Screenshot 2024-06-29 203923.png>)
    ![img2](<Screenshot 2024-06-29 204020.png>)
    ![img3](<Screenshot 2024-06-29 204050.png>)
</body>
</html>
