import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

## Generate a marketing product description from a product fact sheet

fact_sheet_chair = """
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture, 
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100) 
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black, 
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities: 
 medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests 

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy
"""

prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Use at most 70 words and include the country of origin.

Technical specifications: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)

# Response:

# Introducing our mid-century inspired office chair, made in Italy. Part of a beautiful furniture family, 
# it comes in several shell colors and base finishes, with or without armrests. 
# Choose from plastic or full upholstery in 10 fabric and 6 leather options. 
# The chair is suitable for home or business settings and is qualified for contract use. 
# With a 5-wheel plastic coated aluminum base and pneumatic chair adjust, it's easy to raise or lower. 
# Available with soft or hard-floor casters and two seat foam densities.

## Issue 1: The text is too long 
# - Limit the number of words/sentences/characters.

prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

Use at most 50 words and include the country of origin.

Technical specifications: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)

# Response:

# Introducing our mid-century inspired office chair, made in Italy. 
# With a range of shell colors and base finishes, and the option of plastic or full upholstery in 10 fabric and 6 leather choices, 
# this chair is perfect for home or business settings. 
# The 5-wheel base and pneumatic chair adjust make it easy to use, 
# while the choice of soft or hard-floor casters and armrest options ensure maximum comfort.

## Issue 2. Text focuses on the wrong details
# - Ask it to focus on the aspects that are relevant to the intended audience.

prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers, 
so should be technical in nature and focus on the 
materials the product is constructed from.

Use at most 50 words and include the country of origin.

Technical specifications: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)

# Response:

# Introducing the mid-century inspired office chair from Italy. This chair is part of a beautiful family of furniture, including filing cabinets, 
# desks, bookcases, and meeting tables. Available in several shell colors and base finishes, with plastic or full upholstery options. 
# The chair is constructed with a 5-wheel plastic coated aluminum base and features a pneumatic chair adjust for easy raise/lower action. 
# Suitable for home or business settings and qualified for contract use.

prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers, 
so should be technical in nature and focus on the 
materials the product is constructed from.

At the end of the description, includ 7-character 
Product ID in the technical specification.

Use at most 50 words and include the country of origin.

Technical specifications: ```{fact_sheet_chair}```
"""
response = get_completion(prompt)
print(response)

# Response:

# Introducing our mid-century inspired office chair, perfect for home or business settings. 
# With a range of shell colors and base finishes, including stainless steel and matte black, this chair is available with or without armrests
# and in 10 fabric and 6 leather options. Constructed with a 5-wheel plastic coated aluminum base and HD36 foam seat, 
# it also features pneumatic chair adjust for easy raise/lower action. Product ID: SWC-100/110. Made in Italy.

## Issue 3. Description needs a table of dimensions
# - Ask it to extract information and organize it in a table.

prompt = f"""
Your task is to help a marketing team create a 
description for a retail website of a product based 
on a technical fact sheet.

Write a product 150 word description based on the information 
provided in the technical specifications delimited by 
triple backticks.

The description is intended for furniture retailers, 
so should be technical in nature and focus on the 
materials the product is constructed from.

At the end of the description, include every 7-character 
Product ID in the technical specification.

After the description, include a table that gives the 
product's dimensions. The table should have two columns.
In the first column include the name of the dimension. 
In the second column include the measurements in inches only.

Give the table the title 'Product Dimensions'.

Format everything as HTML that can be used in a website. 
Place the description in a <div> element.

Technical specifications: ```{fact_sheet_chair}```
"""

response = get_completion(prompt)
print(response)

# Response:

# <div>
# <p>The mid-century inspired office chair is a beautiful addition to any workspace. Part of a family of office furniture, 
# this chair is available in several shell color and base finish options. Choose between plastic back and front upholstery or full upholstery in a 
# variety of fabric and leather options. The chair is also available with or without armrests and is suitable for both home and business settings. </p>

# <p>The chair is constructed with a 5-wheel plastic coated aluminum base and features a pneumatic chair adjust for easy raise/lower action. 
# It is also qualified for contract use. The shell base glider is made of cast aluminum with modified nylon PA6/PA66 coating and has a shell thickness of 10mm. 
# The seat is made of HD36 foam. </p>

# <p>Choose between soft or hard-floor caster options and two choices of seat foam densities: medium (1.8 lb/ft3) or high (2.8 lb/ft3). 
# The chair also comes with the option of armless or 8 position PU armrests. </p>

# <p>Product ID: SWC-100, SWC-110</p>
# </div>

# <table>
#   <caption>Product Dimensions</caption>
#   <tr>
#     <th>Dimension</th>
#     <th>Measurement (inches)</th>
#   </tr>
#   <tr>
#     <td>Width</td>
#     <td>20.87"</td>
#   </tr>
#   <tr>
#     <td>Depth</td>
#     <td>20.08"</td>
#   </tr>
#   <tr>
#     <td>Height</td>
#     <td>31.50"</td>
#   </tr>
#   <tr>
#     <td>Seat Height</td>
#     <td>17.32"</td>
#   </tr>
#   <tr>
#     <td>Seat Depth</td>
#     <td>16.14"</td>
#   </tr>
# </table>



# The mid-century inspired office chair is a beautiful addition to any workspace. Part of a family of office furniture, 
# this chair is available in several shell color and base finish options. Choose between plastic back and front upholstery or full upholstery in a variety 
# of fabric and leather options. The chair is also available with or without armrests and is suitable for both home and business settings.

# The chair is constructed with a 5-wheel plastic coated aluminum base and features a pneumatic chair adjust for easy raise/lower action. 
# It is also qualified for contract use. The shell base glider is made of cast aluminum with modified nylon PA6/PA66 coating and has a shell 
# thickness of 10mm. The seat is made of HD36 foam.

# Choose between soft or hard-floor caster options and two choices of seat foam densities: medium (1.8 lb/ft3) or high (2.8 lb/ft3). 
# The chair also comes with the option of armless or 8 position PU armrests.

# Product ID: SWC-100, SWC-110

# Product Dimensions
# Dimension	Measurement (inches)
# Width	20.87"
# Depth	20.08"
# Height	31.50"
# Seat Height	17.32"
# Seat Depth	16.14"
