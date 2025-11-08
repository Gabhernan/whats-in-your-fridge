from SearchRecipes_Flask import app, forms, main_functions
from flask import request, render_template
import requests


@app.route('/', methods=["GET", "POST"])
@app.route('/search', methods=["GET", "POST"])
def quiz():
    form = forms.RecipeQuiz()

    if request.method == "POST" and form.validate_on_submit():
        ingredients = form.ingredients.data
        allergies = form.allergies.data
        diet = form.diet.data

        api_key_dict = main_functions.read_from_file('SearchRecipes_Flask/JSON_Files/api_key.json')
        api_key = api_key_dict["api_key"]

        url = "https://api.spoonacular.com/recipes/complexSearch"

        params = {
            "apiKey": api_key,
            "includeIngredients": ingredients,
            "intolerances": allergies,
            "diet": diet,
            "instructionsRequired": True,
            "addRecipeInstructions": True,
            "addRecipeNutrition": True,
            "number": 10,
            "sort": "popularity"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        main_functions.save_to_file(data,'SearchRecipes_Flask/JSON_Files/recipes.json')

        recipes = data.get("results", [])

        clean_results = []
        for r in recipes:
            recipe_id = r.get("id")
            title = r.get("title", "")
            title_slug = title.replace(" ", "-").lower()
            spoonacular_url = f"https://spoonacular.com/recipes/{title_slug}-{recipe_id}"
            source_url = r.get("sourceUrl")

        # Check if there are instructions or a working URL
            has_instructions = bool(r.get("analyzedInstructions")) and len(r["analyzedInstructions"]) > 0
            has_url = bool(source_url or spoonacular_url)

        # Skip recipes that have neither
            if not has_instructions and not has_url:
                continue

            nutrients = r.get("nutrition", {}).get("nutrients", [])
            main_nutrients = {}
            for n in nutrients:
                if n["name"] in ["Calories", "Fat", "Protein", "Carbohydrates"]:
                    main_nutrients[n["name"]] = f"{n['amount']} {n['unit']}"

            clean_results.append({
                "title": title or "No Title",
                "image": r.get("image"),
                "readyInMinutes": r.get("readyInMinutes", "N/A"),
                "servings": r.get("servings", "N/A"),
                "rating": round(r.get("spoonacularScore", 0), 1),
                "url": source_url if source_url else spoonacular_url,
                "nutrition": main_nutrients
            })
        return render_template("recipes_results.html", recipes=clean_results)

    return render_template("quiz.html", form=form)
