def get_user_input():
    """Ask the user for the season and plant type."""
    season = input("Enter the season: ").lower().strip()
    plant_type = input("Enter the plant type: ").lower().strip()
    return season, plant_type


def get_season_advice(season):
    """Return gardening advice based on the season."""
    if season == "spring":
        return "Prepare the soil and start planting new seeds.\n"
    elif season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "autumn":
        return "Clear fallen leaves and prepare plants for colder weather.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """Return gardening advice based on the plant type."""
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    """Run the gardening advice program."""

    # Get the season and plant type from the user
    season, plant_type = get_user_input()

    # Build the gardening advice from the user's choices
    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)

    # Display the completed advice
    print(advice)


main()