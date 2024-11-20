from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    pokemon_data = None
    error_message = None

    if request.method == "POST":
        name_or_id = request.form.get("name_or_id").lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{name_or_id}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Ensure the response is valid
            data = response.json()

            pokemon_data = {
                "name": data["name"].capitalize(),
                "image": data["sprites"]["front_default"],
                "types": [t["type"]["name"] for t in data["types"]],
                "abilities": [a["ability"]["name"] for a in data["abilities"]],
                "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
            }
        except requests.exceptions.RequestException as e:
            error_message = f"Pokémon not found! Please try another name or ID. Error: {e}"

    return render_template("home.html", pokemon=pokemon_data, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
