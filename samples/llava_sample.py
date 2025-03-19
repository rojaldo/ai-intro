import httpx
from ollama import generate

raw = httpx.get('https://static.wikia.nocookie.net/villains/images/4/43/Bender.png')
raw.raise_for_status()

for response in generate('llava', 'tell me wich objects is holding the character:', images=[raw.content], stream=True):
  print(response['response'], end='', flush=True)

print()