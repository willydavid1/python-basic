def run():
    countries_population = {
        'argentina': 44_938_712,
        'brazil': 210_147_125,
        'colombia': 50_372_424
    }
    print(countries_population) # {'argentina': 44938712, 'brazil': 210147125, 'colombia': 50372424}
    print(f'countries_population[\'argentina\']: {countries_population["argentina"]}')
    print(f'countries_population[\'brazil\']: {countries_population["brazil"]}')
    print(f'countries_population[\'colombia\']: {countries_population["colombia"]}')

    for country in countries_population.keys():
        print(f'{country}: {countries_population[country]}')

    for value in countries_population.values():
        print(value)

    # returns a tuple countries_population.items()
    for country, population in countries_population.items():
        print(country, population)

if __name__ == '__main__':
    run()
