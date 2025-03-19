import gradio as gr

import asyncio

import ollama
from ollama import ChatResponse

def rectangle_area(base: int, height: int) -> int:
#   cast to int to ensure the result is an integer
    base = int(base)
    height = int(height)
    return base * height

def rectangle_perimeter(base: int, height: int) -> int:
#   cast to int to ensure the result is an integer
    base = int(base)
    height = int(height)
    return 2 * (base + height)

def circle_area(radius: int) -> float:
    # cast to int to ensure the result is an integer
    radius = int(radius)
    return 3.14 * radius ** 2

def circle_perimeter(radius: int) -> float:
    # cast to int to ensure the result is an integer
    radius = int(radius)
    return 2 * 3.14 * radius

def triangle_area(base: int, height: int) -> float:
    # cast to int to ensure the result is an integer
    base = int(base)
    height = int(height)
    return 0.5 * base * height

def triangle_perimeter(side1: int, side2: int, side3: int) -> int:
    # cast to int to ensure the result is an integer
    base = int(base)
    height = int(height)
    return side1 + side2 + side3

def add_two_numbers(a: int, b: int) -> int:
  return a + b

def subtract_two_numbers(a: int, b: int) -> int:
  # check if a and b are digits
  if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
  else:
    raise ValueError('Both a and b must be integers')
  return a - b

# Tools can still be manually defined and passed into chat
subtract_two_numbers_tool = {
  'type': 'function',
  'function': {
    'name': 'subtract_two_numbers',
    'description': 'Subtract two numbers',
    'parameters': {
      'type': 'object',
      'required': ['a', 'b'],
      'properties': {
        'a': {'type': 'integer', 'description': 'The first number'},
        'b': {'type': 'integer', 'description': 'The second number'},
      },
    },
  },
}

async def main(messages, available_functions):
  client = ollama.AsyncClient()

  response: ChatResponse = await client.chat(
    'llama3.2',
    messages=messages,
    tools=[add_two_numbers, subtract_two_numbers_tool, rectangle_area, rectangle_perimeter, circle_area, circle_perimeter, triangle_area, triangle_perimeter],
  )

  if response.message.tool_calls:
    # There may be multiple tool calls in the response
    for tool in response.message.tool_calls:
      # Ensure the function is available, and then call it
      if function_to_call := available_functions.get(tool.function.name):
        print('Calling function:', tool.function.name)
        print('Arguments:', tool.function.arguments)
        output = function_to_call(**tool.function.arguments)
        print('Function output:', output)
      else:
        print('Function', tool.function.name, 'not found')

  # Only needed to chat with the model using the tool call results
  if response.message.tool_calls:
    # Add the function response to messages for the model to use
    messages.append(response.message)
    messages.append({'role': 'tool', 'content': str(output), 'name': tool.function.name})

    # Get final response from model with function outputs
    final_response = await client.chat('llama3.2', messages=messages)
    print('Final response:', final_response.message.content)

  else:
    print('No tool calls returned from model')
  return final_response.message.content


async def saludo(peticion):
    messages = [{'role': 'user', 'content': peticion}]
    print('Prompt:', messages[0]['content'])

    available_functions = {
    'add_two_numbers': add_two_numbers,
    'subtract_two_numbers': subtract_two_numbers,
    'rectangle_area': rectangle_area,
    'rectangle_perimeter': rectangle_perimeter,
    'circle_area': circle_area,
    'circle_perimeter': circle_perimeter,
    'triangle_area': triangle_area,
    'triangle_perimeter': triangle_perimeter
    }
    response = await main(messages, available_functions)
    return response

iface = gr.Interface(fn=saludo, inputs=gr.Textbox(label="Peticion", value="scalcula el area de un circulo con radio 33"), outputs="text")
iface.launch()

# calcula el area y el perimetro de un rectangulo  de la 3 y altura 4










