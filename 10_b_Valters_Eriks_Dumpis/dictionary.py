contacts = [
    {
        'name': 'Anna',
         'age': 17,
         'phone': '2600823',
        'cars': [
            {
                'brand': 'Audi',
                'year': 2020,
                'color': 'red',
                'engine': 2.0
            },
            {
                'brand': 'Tesla',
                'year': 2022,
                'color': 'black',
                'engine': 50
            }
        ]
    },
    {
        'name': 'Oskars',
        'phone': '2213321',
        'cars': [
            'brand': 'BMW',
            'year': 2018,
            'color': 'blue',
            'engine': 2.5
        ]
    },
    {
        'name': 'Janka',
        'age': 12,
        'phone': '1299921',
        'cars': []
    }
]

for contact in contacts:
    print(contact['name'])
    for car in contact['cars']
    print(car['brand'])