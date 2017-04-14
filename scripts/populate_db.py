# Copy this into the App Engine interactive console

from cookomatic_api.db.dish import Dish
from cookomatic_api.db.meal import Meal
from cookomatic_api.db.step import Step, Ingredient

meal = Meal(name='My awesome dish')

# CHICKEN DISH
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
    prep_list=[
        'Gather and measure the teriyaki sauce and olive oil',
        'Remove the chicken from the fridge',
        'Get out a gallon-sized freezer bag.'
    ],
    tmp_steps=[
        Step(
            name='Marinate Chicken',
            description='Place chicken and seasonings into a gallon sized bag.',
            estimated_time=10,
            ingredients=[
                Ingredient(name='Chicken'),
                Ingredient(name='Seasonings'),
            ]
        ),
        Step(
            name='Heat Nonstick Skillet',
            description='Place a large skillet over medium high heat and wait until'
                        ' warm.',
            estimated_time=10,
            tmp_depends_on=[0]
        ),
        Step(
            name='Add Chicken to Skillet',
            description='Add chicken to skillet and cook over medium heat for 30 seconds.',
            estimated_time=10,
            ingredients=[
                Ingredient(name='Chicken'),
            ]
        ),
        Step(
            name='Flip Chicken',
            description='Flip the chicken and cook for an additional 30 seconds',
            estimated_time=10,
            ingredients=[
                Ingredient(name='Chicken'),
            ]
        ),
        Step(
            name='Remove Chicken From Skillet',
            description='Remove browned chicken from the pan.',
            estimated_time=10,
            ingredients=[
                Ingredient(name='Chicken'),
            ]
        ),
        Step(
            name='Add Pineapple and Rice',
            description='Add pineapple and rice to skillet, cover and reduce to medium low, '
                        'and cook for 45 seconds.',
            estimated_time=10,
            ingredients=[
                Ingredient(name='Pineapple'),
                Ingredient(name='Rice'),
            ]
        ),
        Step(
            name='Return Chicken to Skillet',
            description='Stir rice and nestle chicken on top and cook for an additional '
                        'minute.',
            estimated_time=1,
            ingredients=[
                Ingredient(name='Chicken'),
                Ingredient(name='Rice'),
            ]
        ),
    ],
    serving_size=4
)
d_chick.generate_img_url()
d_chick.parse_step_deps()
meal.dishes.append(d_chick.put())
# CARROT DISH

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
    prep_list=[
        'Gather ingredients',
        'Gather tools'
    ],
    tmp_steps=[
        Step(
            name='Preheat Oven',
            is_user_intensive=False,
            description='Preheat Oven to 400 degrees',
            estimated_time=1
        ),
        Step(
            name='Season Carrots',
            description='Add the carrots to a bowl and toss with remaining seasonings',
            estimated_time=3,
            ingredients=[
                Ingredient(name='Carrots'),
                Ingredient(name='Seasonings'),
            ]
        ),
        Step(
            name='Bake Carrots',
            is_user_intensive=False,
            description='Place the carrots on a baking tray and put in oven. Cook for 1 '
                        'minute.',
            estimated_time=3,
            ingredients=[
                Ingredient(name='Carrots'),
            ]
        ),
    ],
    serving_size=4
)
d_carrot.generate_img_url()
d_carrot.parse_step_deps()
meal.dishes.append(d_carrot.put())

d_pizza = Dish(
    name='Quick and Easy Pizza',
    img_filename='carrots.jpg',
    tags=[
        'entree',
        'bread',
        'pizza'
    ],
    tools=[
        'oven',
        'pizza pan or baking sheet',
        'medium bowl',
        'measuring cup and spoons',
        'dish cloth'
    ],
    prep_list=[
        'Heat 1 cup of water to 110 - 115 degrees F.',
        'Gather and measure remaining ingredients.'
    ],
    tmp_steps=[
        Step(
            name='Proof Yeast',
            description='In a medium bowl, dissolve yeast and sugar in warm water (~110 degrees), '
                        'and let stand until creamy.',
            estimated_time=10,
            is_user_intensive=False,
            ingredients=[
                Ingredient(name='Active Dry Yeast', amount=2.5, unit='tsp'),
                Ingredient(name='Sugar', amount=1, unit='tsp'),
                Ingredient(name='Warm Water (110-115 degrees)', amount=1, unit='cups'),
            ]
        ),
        Step(
            name='Mix and Knead Dough',
            description='Stir in flour, salt, and oil, and knead until smooth.',
            estimated_time=5,
            ingredients=[
                Ingredient(name='Flour', amount=3.25, unit='cups'),
                Ingredient(name='Oil', amount=2, unit='Tbsp'),
                Ingredient(name='Salt', amount=1, unit='tsp'),
            ]
        ),
        Step(
            name='Let the Dough Rest',
            is_user_intensive=False,
            description='Place a dish cloth on top of the bowl, and let rest in a warm place '
                        'for 20 minutes',
            estimated_time=20
        ),
        Step(
            name='Preheat Oven to 425',
            is_user_intensive=False,
            description='Preheat your oven to 425 degrees',
            estimated_time=10
        ),
        Step(
            name='Shape Dough',
            description='Lightly flour a clean surface, and turn dough out onto it and pat or '
                        'roll the dough into a circle',
            estimated_time=5,
            ingredients=[
                Ingredient(name='Flour'),
            ]
        ),
        Step(
            name='Grease Pizza Pan',
            description='Lightly grease a pizza pan or baking sheet with olive oil, or dust '
                        'with cornmeal.',
            estimated_time=1
        ),
        Step(
            name='Add Toppings',
            description='Transfer crust to greased pizza pan, and spread with the desired amount '
                        'of marinara sauce, and top with cheese and any additional desired '
                        'ingredients.',
            estimated_time=3,
            ingredients=[
                Ingredient(name='Marinara Sauce, homemade or store bought', amount=6, unit='oz'),
                Ingredient(name='Shredded Mozzarella', amount=4, unit='oz'),
                Ingredient(name='Any Additional Desired Toppings'),
            ]
        ),
        Step(
            name='Bake',
            is_user_intensive=False,
            description='Place in oven, and bake for 18 minutes, or until the bottom is golden '
                        'brown.',
            estimated_time=18
        ),
        Step(
            name='Let Cool',
            is_user_intensive=False,
            description='Let pizza cool for 5 minutes before cutting and serving',
            estimated_time=5,
            ingredients=[
                Ingredient(name='Flour'),
            ]
        ),
    ],
    serving_size=4
)
d_pizza.generate_img_url()
d_pizza.parse_step_deps()
meal.dishes.append(d_pizza.put())

meal.gen_schedule()
meal.put()
