import openai
import json
import configparser
from ginai_types import Cocktail
from config_secrets import OPENAI

openai.api_key = OPENAI['api_token']

def make_drink(user_input, client, total_ml):

    prompt = f'''
    {user_input}
    With the ingredients provided above, generate a recipe for a cocktail and return a JSON array as the result.
    You are serving the drink to {client}.
    It is a hot day.
    Only give quantities in metric units.
    Do not change the case of the ingredient_name.
    You do not need to use all of the ingredients listed.
    You may only use a maximum of 4 ingredients.
    The total must not exceed a glass size of {total_ml} mL.
    The JSON must have these fields: cocktail_name, description, inventor, matching_song, instructions and an array of ingredient_name, quantity.
    '''

    completion = openai.ChatCompletion.create( 
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are a helpful bartender.'},
            {'role': 'user', 'content': prompt},
        ],
        functions=[
            {
            'name': 'get_answer_for_user_query',
            'description': 'Get user answer in series of steps',
            'parameters': Cocktail.model_json_schema()
            }
        ],
        function_call={'name': 'get_answer_for_user_query'}
    )

    try:
        # parse JSON output from AI model
        generated_text = completion.choices[0]['message']['function_call']['arguments'] 
        return json.loads(generated_text)
    except Exception as e:
        print(f'An error occurred: {e}')
        return None


if __name__ == '__main__':
    ingredients_available = ['wine', 'beer', 'apple juice', 'water', 'gin', 'vodka', 'orange juice', 'tonic', 'white rum']
    response_dict = make_drink(ingredients_available, 'an adult who wants a traditional drink', 250)
    print(json.dumps(response_dict, indent=4))
    
