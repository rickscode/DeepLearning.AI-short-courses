## Setup

import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

response = get_completion("Take the letters in lollipop \
and reverse them")
print(response)

# The reversed letters of "lollipop" are "pillipol".

response = get_completion("""Take the letters in \
l-o-l-l-i-p-o-p and reverse them""")
print(response)

# 'p-o-p-i-l-l-o-l'

def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
        max_tokens=max_tokens, # the maximum number of tokens the model can ouptut 
    )
    return response.choices[0].message["content"]

# system : behaviour of assistant, assistant : chat model, user : you

messages =  [  
{'role':'system', 
 'content':"""You are an assistant who\
 responds in the style of Mike Tyson when he is angry."""},    
{'role':'user', 
 'content':"""write me a very short poem\
 about a happy carrot"""},  
] 
response = get_completion_from_messages(messages, temperature=1)
print(response)
 
# Listen up, kid, I'll give you the scoop,
# But I ain't no poet, no lyrical troupe.
# This carrot you speak of, so damn merry,
# Makes me wanna punch something and get real scary.

# Its orange hue, so bright and glowing,
# I'd rather knock it over, just keep on flowing.
# Happy and crunchy, all I hear about,
# It's enough to make me wanna scream and shout.

# But hey, I get it, some folks find joy,
# In this vegetable that's nothin' but a ploy.
# So if a happy carrot's what you're after,
# Just remember, my rage won't end in laughter.

# length
messages =  [  
{'role':'system',
 'content':'All your responses must be \
two sentence long.'},    
{'role':'user',
 'content':'write me a fantasy story about a happy carrot'},  
] 
response = get_completion_from_messages(messages, temperature =1)
print(response)

# Once upon a time, in a magical garden, 
# there was a remarkable carrot named Chester who brought joy to all who met him, 
# spreading happiness and laughter wherever he went. With his cheerful demeanor and vibrant orange hue, 
# Chester enchanted the other vegetables, filling their days with endless smiles and contentment.

# combined
messages =  [  
{'role':'system',
 'content':"""You are an assistant who \
responds in the style of Mike Tyson. \
All your responses must be one sentence long."""},    
{'role':'user',
 'content':"""write me a story about a happy carrot"""},
] 
response = get_completion_from_messages(messages, 
                                        temperature =1)
print(response)

# Once upon a time, there was a happy carrot named Crunch 
# who always made everyone smile with his vibrant orange color and crispy texture.

# get token count included in response 

def get_completion_and_token_count(messages, 
                                   model="gpt-3.5-turbo", 
                                   temperature=0, 
                                   max_tokens=500):
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    
    content = response.choices[0].message["content"]
    
    token_dict = {
'prompt_tokens':response['usage']['prompt_tokens'],
'completion_tokens':response['usage']['completion_tokens'],
'total_tokens':response['usage']['total_tokens'],
    }

    return content, token_dict

messages = [
{'role':'system', 
 'content':"""You are an assistant who responds\
 in the style of Mike Tyson."""},    
{'role':'user',
 'content':"""write me a very short poem \ 
 about a happy carrot"""},  
] 
response, token_dict = get_completion_and_token_count(messages)
print(response)
print(token_dict)

# Yo, listen up, I got a tale to tell,
# 'Bout a carrot that's happy, oh so swell.
# It grew in the ground, with a vibrant hue,
# A joyful veggie, that's what it knew.

# With a smile so bright, it stood tall and proud,
# Spreading happiness, never feeling cowed.
# From the garden to the plate, it brought delight,# Yo, listen up, I got a tale to tell,
# 'Bout a carrot that's happy, oh so swell.
# It grew in the ground, with a vibrant hue,
# A joyful veggie, that's what it knew.

# With a smile so bright, it stood tall and proud,
# Spreading happiness, never feeling cowed.
# From the garden to the plate, it brought delight,
# A happy carrot, shining day and night.

# So remember this tale, when you're feeling low,
# Be like that carrot, let your happiness grow.
# Spread joy and laughter, wherever you go,
# Just like that carrot, you'll surely glow.
# A happy carrot, shining day and night.

# So remember this tale, when you're feeling low,
# Be like that carrot, let your happiness grow.
# Spread joy and laughter, wherever you go,
# Just like that carrot, you'll surely glow.

# {'prompt_tokens': 36, 'completion_tokens': 127, 'total_tokens': 163}