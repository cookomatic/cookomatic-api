# Copy this into the App Engine interactive console

from cookomatic_api.db.dish import Dish
from cookomatic_api.db.step import Step

d_chick_steps = [
    Step(name='Marinate Chicken',
         description='Place chicken and seasonings into a gallon sized bag.',
         estimated_time=1,
         ingredients=[
             'Chicken',
             'Seasonings'
         ]),

    Step(name='Heat Nonstick Skillet',
         description='Place a large skillet over medium high heat and wait until'
                     ' warm.',
         estimated_time=1),

    Step(name='Add Chicken to Skillet',
         description='Add chicken to skillet and cook over medium heat for 30 seconds.',
         estimated_time=1,
         ingredients=[
             'Chicken'
         ]),
    Step(name='Flip Chicken',
         description='Flip the chicken and cook for an additional 30 seconds',
         estimated_time=1,
         ingredients=[
             'Chicken'
         ]),
    Step(name='Remove Chicken From Skillet',
         description='Remove browned chicken from the pan.',
         estimated_time=1,
         ingredients=[
             'Chicken'
         ]),
    Step(name='Add Pineapple and Rice',
         description='Add pineapple and rice to skillet, cover and reduce to medium low, '
                     'and cook for 45 seconds.',
         estimated_time=1,
         ingredients=[
             'Pineapple',
             'Rice'
         ]),
    Step(name='Add Chicken to Skillet',
         description='Stir rice and nestle chicken on top and cook for an additional '
                     'minute.',
         estimated_time=1,
         ingredients=[
             'Chicken',
             'Rice'
         ]),
]
d_chick = Dish(
    name="Teriyaki Chicken and Pineapple Rice",
    img_filename="chicken-rice.jpg",
    tags=[
        'entree',
        'japanese',
        'dinner'
    ],
    tools=[
        'stove',
        'fridge',
        'nonstick skillet and lid',
        'measuring cups and spoons',
        'small bowl',
        'plate',
        'pastry brush or spoon',
        'gallon-sized freezer bag',
        'strainer'
    ],
    ingredients=[
        'Chicken',
        'Pineapple',
        'Rice',
        'Seasoning'
    ],
    prep_list=[
        'Gather and measure the teriyaki sauce and olive oil',
        'Remove the chicken from the fridge',
        'Get out a gallon-sized freezer bag.'
    ],
    steps=[step.put() for step in d_chick_steps],
    total_time=40,
    serving_size=4
)
d_chick.generate_img_url()
d_chick.put()

d_carrot_steps = [
    Step(name='Preheat Oven',
         description='Preheat Oven to 400 degrees',
         estimated_time=1),
    Step(name='Season Carrots',
         description='Add the carrots to a bowl and toss with remaining seasonings',
         estimated_time=1,
         ingredients=[
             'Carrots',
             'Seasonings'
         ]),
    Step(name='Bake Carrots',
         description='Place the carrots on a baking tray and put in oven. Cook for 1 '
                     'minute.',
         estimated_time=1,
         ingredients=[
             'Carrots'
         ]),
]
d_carrot = Dish(
    name='Spicy Maple Roasted Carrots',
    img_filename='carrots.jpg',
    tags=[
        'side dish',
        'southern'
    ],
    tools=[
        'medium bowl',
        'tin foil',
        'oven',
        'baking sheet',
        'measuring spoons'
    ],
    ingredients=[
        'Carrots',
        'Seasoning'
    ],
    prep_list=[
        'Gather ingredients',
        'Gather tools'
    ],
    steps=[step.put() for step in d_carrot_steps],
    total_time=30,
    serving_size=4
)
d_carrot.generate_img_url()
d_carrot.put()
