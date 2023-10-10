import argparse
import json
import datetime
import rgb_util
import time
from ginai_types import Cocktail
from pump_util import run_pumps_from_instructions
from openai_util import make_drink
from cast_audio import tts_say


ingredients_available = ['gin', 'vodka', 'tonic', 'white rum']

def speak_making(cocktail, pump_time):
    pump_time = round(pump_time)
    msg = f'Making a {cocktail.cocktail_name}. {cocktail.description}. Ready in {pump_time} seconds.'
    print(msg)
    tts_say(msg)

def speak_done(cocktail):
    msg = f'Enjoy your {cocktail.cocktail_name}. How about I play {cocktail.matching_song}'
    print(msg)
    tts_say(msg)


def map_ingredients(response_dict):
    cocktail = Cocktail(**response_dict)
    my_ingredients_list = cocktail.ingredients

    pump_instructions_ml = [0,0,0,0]

    for drink_dict in my_ingredients_list:
        this_ingredient = drink_dict.ingredient_name
        this_quantity = drink_dict.quantity_ml

        try:
            ingredients_available_idx = ingredients_available.index(this_ingredient)
            print(f'Ingredients {this_ingredient} at index {ingredients_available_idx} pour {this_quantity}')
            pump_instructions_ml[ingredients_available_idx] = this_quantity

        except ValueError as ve:
            print(f'Unable to find ingrediant {this_ingredient}')

    print(pump_instructions_ml)

    pump_time = run_pumps_from_instructions(pump_instructions_ml, ingredients_available)
    speak_making(cocktail, pump_time)
    rgb_util.thread_run(rgb_util.effect_theater_chase_rainbow, pump_time)
    speak_done(cocktail)
    rgb_util.thread_run(rgb_util.effect_green_wipe, 8)

def doAI(file):
    response_dict = make_drink(ingredients_available, 'an adult who wants a traditional drink', 80)
    print(json.dumps(response_dict, indent=4))
    map_ingredients(response_dict)

    # Serializing json
    json_object = json.dumps(response_dict, indent=4)

    # Write json
    with open(file, 'w') as outfile:
        outfile.write(json_object)


def readJSON(file):
    # Opening JSON file
    with open(file) as json_file:
        response_dict = json.load(json_file)
    
        # Print the type of data variable
        print("Type:", type(response_dict))
        print(response_dict)

        map_ingredients(response_dict)

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
        '--enablePump',
        help='Whether to enable pumps',
        action='store_true',
        required=False,
        default=False)

    parser.add_argument(
        '--readJSON', 
        help='Read from JSON', 
        type=str, 
        required=False)

    parser.add_argument(
        '--writeJSON', 
        help='Write JSON', 
        type=str, 
        required=False)
    
    parser.add_argument(
        '--creative',
        help='Creative drink creation',
        action='store_true',
        required=False,
        default=False)
    
    args = parser.parse_args()

    if (args.creative):
        now = datetime.datetime.now()
        file_dated = './recipes/' + now.strftime("%Y%m%d_%H%M%S") + '.json'
        doAI(file_dated)

    if (args.readJSON):
        print(f'Read {args.readJSON}')
        readJSON(args.readJSON)

    if (args.writeJSON):
        print(f'Write {args.writeJSON}')
        doAI(args.writeJSON)

if __name__ == '__main__':
    main()

