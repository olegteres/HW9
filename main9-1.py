import requests

urls = [
    f'https://www.superheroapi.com/api.php/2619421814940190/search/Hulk',
    f'https://www.superheroapi.com/api.php/2619421814940190/search/Thanos',
    f'https://www.superheroapi.com/api.php/2619421814940190/search/Captain%America',
]

def requests_get(all_urls):
  result = (requests.get(url) for url in all_urls)
  return result


def find_most_intelligence():
  super_heros = []
  for item in requests_get(urls):
    intelligence = item.json()
    try:
      for power_stats in intelligence['results']:
        super_heros.append({
        'name': power_stats['name'],
        'intelligence': power_stats['powerstats']['intelligence'],
        })
    except KeyError:
      print(f"Проверте ссылки: {urls}")

  intelligence_super_hero = 0
  name = ''
  for intelligence_hero in super_heros:
    if intelligence_super_hero < int(intelligence_hero['intelligence']):
      intelligence_super_hero = int(intelligence_hero['intelligence'])
      name = intelligence_hero['name']

  print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")

find_most_intelligence()