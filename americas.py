import pygal
worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = "North america"
worldmap_chart.add("North America",["ca", "mx", "us"])
worldmap_chart.render_to_file("america.svg")


