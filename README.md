# What’s In Your Fridge?

A simple yet smart recipe web app built with **Python (Flask)** + **HTML/CSS/JS** that helps you discover recipes using the ingredients you already have — perfect for when you’re staring at your fridge wondering what to cook 🍳  

This project connects to the **Spoonacular API** to fetch recipe ideas, filter by allergies and diets, and shows recipes that include instructions.

---

## Features

- **Ingredient-based Search** – Enter what’s in your fridge and instantly find recipes that use those ingredients.  
- **Allergy & Diet Filters** – Supports dietary preferences like vegetarian, vegan, keto, and gluten-free.  
- **Instruction Results** – Shows recipes that include full step-by-step instructions.  
- **Nutrition Overview** – Displays calories, fat, protein, and carbs per recipe.   
- **Modern UI** – Minimalist, responsive design inspired by real cooking apps.  
- **Start Over Button** – Quickly restart a search without reloading.

---

## Tech Stack

**Backend:**  
- Python 3  
- Flask (with Flask-WTF for forms)  
- Requests (for Spoonacular API)  

**Frontend:**  
- HTML5  
- CSS3 (custom responsive grid system)  
- JavaScript (form validation + UX tweaks)

**API:**  
- [Spoonacular API](https://spoonacular.com/food-api/docs#Search-Recipes-Complex)

---

## UI Preview

### Quiz Page (Get Started)
> Users input their ingredients, allergies, and diet preference.

add here

### Results Page
> Displays recipe cards with instructions, nutrition info, and source links.

add here

---

## Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/whats-in-your-fridge.git
   cd whats-in-your-fridge
   
2. **Create a virtual environment**
   ```bash
    python -m venv venv
   
    source venv/bin/activate  # macOS/Linux
   
    venv\Scripts\activate     # Windows

3. **Install dependencies**
   ```bash

   pip install -r requirements.txt
    
4. **Add your Spoonacular API key**
   
    Create a folder called JSON_Files

    Add a file named api_key.json:

    {
        "api_key": "YOUR_API_KEY_HERE"
    }

6. **Run the Flask app**
   ```bash
    python run.py

7. **Open browser**
   
    http://127.0.0.1:5000

## Project Structure


## Future Features/Planned Improvements

### Pre-fetch and validate recipe links

Currently, some recipe URLs returned by Spoonacular may be outdated or no longer accessible.
By pre-fetching and validating each link before it’s displayed, the app can ensure users only see recipes that lead to real, working pages.
This improvement would make the user experience smoother, more reliable, and remove the frustration of broken or expired links.

### Favorites Section

A favorites section will let users save recipes they love or plan to try later. This adds a personal touch to the app, making it feel more interactive and meaningful.
It encourages users to return, revisit saved recipes, and build a personalized library of meal ideas.

### Local database or cloud sync

Introducing a local or cloud-based database will allow the app to store user favorites, recent searches, and preferences.
This ensures that users can resume their experience exactly where they left off even after closing the app.
It also opens the door for optional sign-in features and multi-device syncing in the future.



