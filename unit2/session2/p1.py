def most_endangered(species_list):
    # minPopulation = species_list[0]
    population = float('inf')
    name = " "
    
    for species in species_list:
        if species.get("population") < population:
           population = species.get("population")
           name = species.get("name")

    
    return name


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
