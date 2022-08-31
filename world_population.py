import json
import pygal
from country_codes import get_country_code
filename = "data/population_data.json"

with open(filename) as f:
    pop_data = json.load(f)
cc_population = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "2011":
        population = int(float(pop_dict["Value"]))
        code = get_country_code(pop_dict["Country Name"])
        if code:
            cc_population[code] = population

# print(cc_population)

world_pop_chart = pygal.maps.world.World()
world_pop_chart.title = "2011 world population"
world_pop_chart.add('2010',cc_population)
world_pop_chart.render_to_file("world_population.svg")
            
            