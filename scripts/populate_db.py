# Copy this into the App Engine interactive console

from cookomatic_api.db.dish import Dish
from cookomatic_api.db.ingredient import Ingredient
from cookomatic_api.db.meal import Meal
from cookomatic_api.db.step import Step

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
    ingredients=[
        Ingredient(name='Boneless Skinless Chicken Thighs', amount=4),
        Ingredient(name='Teriyaki Sauce', amount=0.33, unit='Cup'),
        Ingredient(name='Olive Oil', amount=3, unit='Tbsp'),
        Ingredient(name='Can Crushed Pineapple', amount=20, unit='oz'),
        Ingredient(name='Long Grain White Rice', amount=1.5, unit='Cups'),
    ],
    prep_list=[
        'Gather and measure the teriyaki sauce and olive oil',
        'Remove the chicken from the fridge',
        'Get out a gallon-sized freezer bag.'
    ],
    tmp_steps=[
        Step(
            name='Start Chicken Marinade',
            description='Place chicken into a gallon sized freezer bag, '
                        'and add half of the teriyaki sauce, and 1 tbsp olive oil.',
            estimated_time=3
        ),
        Step(
            name='Marinade Chicken',
            description='Place in the fridge, and marinate for at least an hour',
            estimated_time=60,
            tmp_depends_on=[0],
            is_user_intensive=False,
        ),
        Step(
            name='Strain Pineapple',
            description='Strain and reserve pineapple juice from crushed pineapple and '
                        'add water to strained juice until you have 3.5 cups of Pineapple Water.',
            estimated_time=4
        ),
        Step(
            name='Heat Nonstick Skillet',
            description='Place a large skillet over medium high heat and wait until'
                        ' warm.',
            estimated_time=10,
            is_user_intensive=False,
        ),
        Step(
            name='Reduce Sauce',
            description='Add the last 1/3 cup of Teriyaki Sauce and bring to a boil. '
                        'Once boiling, reduce to a simmer and stir until slightly thickened.',
            estimated_time=6,
            is_user_intensive=False,
            tmp_depends_on=[3],
        ),
        Step(
            name='Take Sauce off Heat',
            description='Take the sauce off the heat and pour into a small bowl.',
            estimated_time=1,
            tmp_depends_on=[3, 4],
        ),
        Step(
            name='Wipe and Re-Oil Skillet',
            description='Wipe skillet to get the majority of sauce out of it, and heat '
                        '1 tbsp olive oil over medium heat.',
            estimated_time=1,
            tmp_depends_on=[3, 4, 5],
        ),
        Step(
            name='Add Chicken to Skillet',
            description='Let excess marinade drip off chicken and add to skillet. '
                        'Cook over medium high heat for 4 minutes on each side, or until nicely '
                        'browned. Try not to disturb the chicken in the pan too much.',
            estimated_time=9,
            tmp_depends_on=[0, 1, 3, 4, 5, 6],
            is_user_intensive=False,
        ),
        Step(
            name='Remove Chicken From Skillet',
            description='Remove browned chicken from the pan.',
            estimated_time=10,
            tmp_depends_on=[0, 1, 3, 4, 5, 6, 7]
        ),
        Step(
            name='Wipe and Oil Skillet',
            description='Wipe skillet once more and add 1 tbsp olive oil and pineapple '
                        'water. Bring to a simmer.',
            estimated_time=4,
            is_user_intensive=False,
            tmp_depends_on=[0, 1, 3, 4, 5, 6, 7, 8],
        ),
        Step(
            name='Add Pineapple and Rice',
            description='Add pineapple and rice to skillet, cover and reduce to medium low, '
                        'and cook for 12 seconds.',
            estimated_time=12,
            tmp_depends_on=[0, 1, 3, 4, 5, 6, 7, 8, 9]
        ),
        Step(
            name='Return Chicken to Skillet',
            description='Stir rice and nestle chicken on top and brush or spoon on teriyaki glaze.',
            estimated_time=1,
            tmp_depends_on=[0, 1, 3, 4, 5, 6, 7, 8, 9, 10],
        ),
        Step(
            name='Cook for 10 Minutes',
            description='Cover and cook for an additional 10 minutes or until rice and '
                        'chicken are fully cooked.',
            estimated_time=10,
            is_user_intensive=False,
            tmp_depends_on=[0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        ),
        Step(
            name='Remove and Serve',
            description='Brush chicken with any remaining teriyaki glaze, and season rice '
                        'with salt and pepper.',
            estimated_time=1,
            tmp_depends_on=[0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
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
    ingredients=[
        Ingredient(name='Carrots', amount=1, unit='lb'),
        Ingredient(name='Olive Oil', amount=1, unit='Tbsp'),
        Ingredient(name='Maple Syrup', amount=1, unit='Tbsp'),
        Ingredient(name='Salt', amount=0.5, unit='tsp'),
        Ingredient(name='Cayenne Pepper', amount=0.25, unit='tsp'),
    ],
    tmp_steps=[
        Step(
            name='Preheat Oven',
            is_user_intensive=False,
            description='Preheat Oven to 400 degrees',
            estimated_time=10,
        ),
        Step(
            name='Season Carrots',
            description='Add the carrots to a bowl and toss with remaining ingredients',
            estimated_time=2
        ),
        Step(
            name='Prep Baking Sheet',
            description='Line baking sheet with tinfoil and spread the carrots on top',
            estimated_time=2,
            tmp_depends_on=[1],
        ),
        Step(
            name='Bake Carrots',
            is_user_intensive=False,
            description='Place the carrots in the oven and cook for 25 minutes.',
            estimated_time=25,
        ),
        Step(
            name='Remove and Serve',
            description='Remove the carrots from the oven and serve',
            estimated_time=1,
            is_user_intensive=False,
            tmp_depends_on=[0, 1, 2, 3],
        )
    ],
    serving_size=4
)
d_carrot.generate_img_url()
d_carrot.parse_step_deps()
meal.dishes.append(d_carrot.put())

d_pizza = Dish(
    name='Quick and Easy Pizza',
    img_filename='pizza.jpg',
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
    ingredients=[
        Ingredient(name='Active Dry Yeast', amount=2.5, unit='tsp'),
        Ingredient(name='Sugar', amount=1, unit='tsp'),
        Ingredient(name='Warm Water (110-115 degrees)', amount=1, unit='cups'),
        Ingredient(name='Flour', amount=3.25, unit='cups'),
        Ingredient(name='Oil', amount=2, unit='Tbsp'),
        Ingredient(name='Salt', amount=1, unit='tsp'),
        Ingredient(name='Marinara Sauce, homemade or store bought', amount=6, unit='oz'),
        Ingredient(name='Shredded Mozzarella', amount=4, unit='oz'),
        Ingredient(name='Any Additional Desired Toppings'),
    ],
    tmp_steps=[
        Step(
            name='Proof Yeast',
            description='In a medium bowl, dissolve yeast and sugar in warm water (~110 degrees), '
                        'and let stand until creamy.',
            estimated_time=10,
            is_user_intensive=False
        ),
        Step(
            name='Mix and Knead Dough',
            description='Stir in flour, salt, and oil, and knead until smooth.',
            estimated_time=5
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
            estimated_time=5
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
            estimated_time=3
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
            estimated_time=5
        ),
    ],
    serving_size=4
)
d_pizza.generate_img_url()
d_pizza.parse_step_deps()
meal.dishes.append(d_pizza.put())

d_ratatouille = Dish(
    name='Disney Ratatouille',
    img_filename='ratatouille2.jpg',
    tags=[
        'vegetarian',
        'Disney'
    ],
    tools=[
        'oven'
    ],
    prep_list=[
        'Gather ingredients',
        'Gather tools'
    ],
    ingredients=[
        Ingredient(name='Tomato Paste', amount=6, unit='oz'),
        Ingredient(name='Chopped Onion', amount=0.5),
        Ingredient(name='Minced Garlic', amount=.25, unit='cup'),
        Ingredient(name='Olive Oil', amount=3, unit='Tbsp'),
        Ingredient(name='Water', amount=.75, unit='cup'),
        Ingredient(name='Salt & Pepper'),
        Ingredient(name='Thinly Sliced Eggplant', amount=1, unit='small'),
        Ingredient(name='Thinly Sliced Zucchini', amount=1, unit='small'),
        Ingredient(name='Thinly Sliced Yellow Squash', amount=1, unit='small'),
        Ingredient(name='Thinly Sliced Red Bell Pepper', amount=1, unit='small'),
        Ingredient(name='Thinly Sliced Yellow Bell Pepper', amount=1, unit='small'),
        Ingredient(name='Fresh Thyme', amount=1, unit='tsp'),
        Ingredient(name='Mascarpone', amount=3, unit='Tbsp'),
    ],
    tmp_steps=[
        Step(
            name='Preheat Oven',
            is_user_intensive=False,
            description='Preheat Oven to 375 degrees',
            estimated_time=1
        ),
        Step(
            name='Prepare Baking Dish',
            description='Spread tomato paste into the bottom of '
                        'a 10x10-inch baking dish. Sprinkle with onion '
                        'and garlic and stir in 1 tablespoon olive oil '
                        'and water until thoroughly combined. Season with salt and black pepper.',
            estimated_time=3
        ),
        Step(
            name='Arrange Vegetables',
            description='Arrange alternating slices of eggplant, zucchini, '
                        'yellow squash, red bell pepper, and yellow bell pepper, '
                        'starting at the outer edge of the dish and working '
                        'concentrically towards the center. Overlap the slices '
                        'a little to display the colors.',
            estimated_time=5
        ),
        Step(
            name='Drizzle Vegetables',
            description='Drizzle the vegetables with 3 tablespoons olive oil and '
                        'season with salt and black pepper. Sprinkle with thyme leaves.',
            estimated_time=1
        ),
        Step(
            name='Cover with Parchment',
            description='Cover vegetables with a piece of parchment paper cut to fit inside.',
            estimated_time=1
        ),
        Step(
            name='Bake',
            is_user_intensive=False,
            description='Bake in the preheated oven until vegetables are roasted and tender, '
                        'about 45 minutes.',
            estimated_time=45
        ),
        Step(
            name='Serve with Mascarpone',
            description='Serve with dollops of mascarpone cheese.',
            estimated_time=0.5
        ),
    ],
    serving_size=6
)
d_ratatouille.generate_img_url()
d_ratatouille.parse_step_deps()
meal.dishes.append(d_ratatouille.put())

d_chicken_party_tacos = Dish(
    name="Chicken Party Tacos",
    img_filename="ChickenPartyTacos.jpg",
    ingredients=[
        Ingredient(name='Red Onion', amount=1),
        Ingredient(name='Red Bell Peppers', amount=2),
        Ingredient(name='Limes', amount=2),
        Ingredient(name='Radishes', amount=6),
        Ingredient(name='Cilantro', amount=0.25, unit='oz'),
        Ingredient(name='Canned Pineapple', amount=8, unit='oz'),
        Ingredient(name='Lime'),
        Ingredient(name='Onion'),
        Ingredient(name='Cilantro'),
        Ingredient(name='Salt & Pepper'),
        Ingredient(name='Chicken Thighs', amount=24, unit='oz'),
        Ingredient(name='Taco Seasoning', amount=1, unit='Tbsp'),
        Ingredient(name='Salt & Pepper'),
        Ingredient(name='Vegetable Oil', amount=4, unit='tsp'),
        Ingredient(name='Red Onion', amount=1),
        Ingredient(name='Red Bell Peppers', amount=2),
        Ingredient(name='Tortillas', amount=8),
    ],
    tmp_steps=[
        Step(
            name='Prep the Produce',
            description='Wash and dry all produce. Peel and halve onion. '
                        'Mince enough so that you have 1 TBSP minced onion. Slice remainder. '
                        'Core, seed, and remove white ribs from bell pepper, then thinly slice. '
                        'Thinly slice radishes. Cut lime in half. Pick cilantro leaves from stems. '
                        'Finely chop half the leaves.',
            estimated_time=6
        ),
        Step(
            name='Prep and Mix Pineapple',
            description='Drain pineapple, then finely chop. In a small bowl, stir together '
                        'pineapple, juice from one lime half, minced onion, and finely chopped cilantro. '
                        'Season with salt and pepper',
            estimated_time=4
        ),
        Step(
            name='Prep Chicken',
            description='Chop chicken into 1-inch pieces. In a medium bowl, '
                        'toss chicken, Taco Seasoning, and salt and pepper.',
            estimated_time=4
        ),
        Step(
            name='Heat Large Pan',
            description='Heat a drizzle of Vegetable oil in large pan over medium high heat.',
            estimated_time=3,
            is_user_intensive=False,
            tmp_depends_on=[2]
        ),
        Step(
            name='Add Chicken',
            description='Add chicken and cook, tossing occasionally, '
                        'until browned and no longer pink in center, 4-5 minutes.',
            estimated_time=5,
            is_user_intensive=False,
            tmp_depends_on=[2, 3]
        ),
        Step(
            name='Remove Chicken from Pan',
            description='Remove chicken from pan and set aside in a serving dish or bowl.',
            estimated_time=1,
            tmp_depends_on=[2, 3, 4]
        ),
        Step(
            name='Add Oil, Pepper, and Onion',
            estimated_time=4,
            description='Heat another drizzle of oil in same pan. Add pepper and sliced '
                        'onion. Cook, tossing occasionally, until softened and lightly browned, 3-4 minutes.',
            is_user_intensive=False,
            tmp_depends_on=[0, 5]
        ),
        Step(
            name='Heat Tortillas',
            description='Wrap tortillas in a damp paper towel and microwave until '
                        'warm and soft, about 30 seconds',
            estimated_time=1,
            tmp_depends_on=[6]
        ),
        Step(
            name='Cut Lime',
            description='Cut remaining lime half into 4 wedges.',
            estimated_time=1,
            tmp_depends_on=[6]
        ),
        Step(
            name='Serve!',
            description='Place chicken, pepper mixture, cilantro leaves, radishes, '
                        'sour cream, lime wedges, and tortillas in individual serving plates '
                        'or bowls and invite everyone to assemble their own tacos.',
            estimated_time=1,
            tmp_depends_on=[0, 1, 2, 3, 4, 5, 6, 7, 8]
        ),
    ],
    serving_size=4
)
d_chicken_party_tacos.generate_img_url()
d_chicken_party_tacos.parse_step_deps()
meal.dishes.append(d_chicken_party_tacos.put())

d_carbonara = Dish(
    name="Pasta Carbonara",
    img_filename="Carbonara.jpg",
    ingredients=[
        Ingredient(name='Bacon', amount=0.25, unit='pound'),
        Ingredient(name='Eggs', amount=2),
        Ingredient(name='Heavy Cream', amount=2, unit='Tbsp'),
        Ingredient(name='Grated Parmesan', amount=0.5, unit='Cup'),
        Ingredient(name='Dry Fettuccini Pasta', amount=0.5, unit='Pound'),
        Ingredient(name='Butter, softened', amount=2, unit='Tbsp'),
        Ingredient(name='Parsley', amount=2, unit='Tbsp'),
        Ingredient(name='Salt & Pepper'),
    ],
    tmp_steps=[
        Step(
            name='Preheat Oven to 400',
            description='Preheat oven to 400 degrees',
            estimated_time=5,
            is_user_intensive=False,
        ),
        Step(
            name='Prepare Sheet Pan',
            description='Line a baking sheet with tinfoil',
            estimated_time=1,
        ),
        Step(
            name='Cook Bacon',
            description='Place bacon on lined baking sheet, and cook '
                        'until crisp. Drain on paper towels.',
            estimated_time=13,
            is_user_intensive=False,
            tmp_depends_on=[0, 1]
        ),
        Step(
            name='Beat Eggs and Cream',
            description='In medium bowl beat together eggs and cream '
                        'just until blended. Stir in cheese and set aside.',
            estimated_time=2
        ),
        Step(
            name='Boil Water for Pasta',
            description='Place a medium pot of water over High heat until boiling',
            estimated_time=7,
            is_user_intensive=False,
        ),
        Step(
            name='Cook Pasta',
            estimated_time=7,
            tmp_depends_on=[4],
            is_user_intensive=False
        ),
        Step(
            name='Drain Pasta and Return to Pan',
            description='Drain and return to pan.',
            estimated_time=1,
            tmp_depends_on=[4, 5],
        ),
        Step(
            name='Mix with Remaining Ingredients',
            description='Toss with butter until it is melted. '
                        'Add bacon and cheese mixture and toss gently until mixed.',
            estimated_time=2,
            tmp_depends_on=[4, 5, 6]
        ),
    ],
    serving_size=4
)
d_carbonara.parse_step_deps()
meal.dishes.append(d_carbonara.put())
d_carbonara.generate_img_url()

d_red_onion_salad = Dish(
    name="Red Onion Salad",
    img_filename='redOnionSalad.jpg',
    ingredients=[
        Ingredient(name='Red Onion', amount=0.5),
        Ingredient(name='Olive Oil', amount=1, unit='Tbsp'),
        Ingredient(name='Lemon Juice', amount=0.5, unit='Lemons worth of'),
        Ingredient(name='Cherry Tomatos', amount=1, unit='Cup'),
        Ingredient(name='Roughly Chopped Mint', amount=0.5, unit='Cup'),
        Ingredient(name='Salt & Pepper'),
    ],
    tmp_steps=[
        Step(
            name='Prep Ingredients',
            description='Thinly slice red onion into rings, roughly chop the mint leaves, '
                        'and juice the lemon.',
            estimated_time=3
        ),
        Step(
            name='Mix Ingredients',
            description='In a medium bowl, mix together the ingredients until well combined.',
            estimated_time=3,
            tmp_depends_on=[0]
        ),
        Step(
            name='Chill 1 Hour',
            description='Cover and let rest in the fridge for at least an hour',
            estimated_time=60,
            is_user_intensive=False,
            tmp_depends_on=[0, 1],
        ),
    ],
    serving_size=4
)
d_red_onion_salad.parse_step_deps()
meal.dishes.append(d_red_onion_salad.put())
d_red_onion_salad.generate_img_url()

d_pancakes = Dish(
    name="Pancakes",
    img_filename='pancakejpg',
    ingredients=[
        Ingredient(name='All Purpose Flour', amount=1.5, unit='Cups'),
        Ingredient(name='Baking Powder', amount=3.5, unit='tsp'),
        Ingredient(name='Salt', amount=1, unit='tsp'),
        Ingredient(name='Sugar', amount=1, unit='Tbsp'),
        Ingredient(name='Melted Butter', amount=3, unit='Tbsp'),
        Ingredient(name='Vanilla', amount=1, unit='tsp'),
        Ingredient(name='Milk', amount=1.25, unit='Cups'),
        Ingredient(name='Egg', amount=1),
    ],
    tmp_steps=[
        Step(
            name='Heat Griddle',
            description='Heat a griddle or frying pan over medium high heat, and '
                        'grease with 1 Tbsp of the butter',
            estimated_time=7,
            is_user_intensive=False
        ),
        Step(
            name='Mix Ingredients',
            description='In a large bowl, sift together the flour, baking powder, '
                        'salt and sugar. Make a well in the center and pour in the milk, egg '
                        'and the remainder of the melted butter; mix until smooth.',
            estimated_time=5
        ),
        Step(
            name='Cook Pancakes',
            description='Pour or scoop the batter onto the griddle, using approximately '
                        '1/4 cup for each pancake. Brown on both sides and serve hot.',
            estimated_time=25,
            tmp_depends_on=[0, 1],
        ),
    ],
    serving_size=4
)
d_pancakes.parse_step_deps()
meal.dishes.append(d_pancakes.put())
d_pancakes.generate_img_url()

d_sweet_potato_chips = Dish(
    name="Sweet Potato Chips",
    img_filename='SweetPotatoChips.jpeg',
    ingredients=[
        Ingredient(name='Sweet Potato', amount=2),
        Ingredient(name='Olive Oil', amount=2, unit='Tbsp'),
        Ingredient(name='Salt'),
    ],
    tmp_steps=[
        Step(
            name='Preheat Oven to 250',
            description='1.	Preheat oven to 250 degrees F (121 C).',
            estimated_time=7,
            is_user_intensive=False,
        ),
        Step(
            name='Prep Sweet Potatos',
            description='Rinse and dry your sweet potatoes thoroughly and slice '
                        'them as uniformly thin as possible. If you have a mandolin, use it. '
                        'Otherwise, use a very sharp knife to get these uniformly thin. Know '
                        'that chips that are too thick in parts won\'t crisp up all the way. '
                        'Still delicious, just not "chip" crispiness.',
            estimated_time=5
        ),
        Step(
            name='Toss in Oil and Salt',
            description='Toss slices in olive oil to lightly coat, then sprinkle with salt.',
            estimated_time=2,
            tmp_depends_on=[0, 1]
        ),
        Step(
            name='Arrange on Baking Sheets',
            description='Cover two baking sheets with tinfoil, and arrage potato slices '
                        'in a single layer.',
            estimated_time=5,
            tmp_depends_on=[1, 2],
        ),
        Step(
            name='Bake for 1 Hour',
            description='Bake for an hour then flip the chips',
            estimated_time=60,
            tmp_depends_on=[0, 1, 2, 3],
            is_user_intensive=False,
        ),
        Step(
            name='Bake Another 25 Min',
            description='Return the chips to the oven and bake for an additional 25 minutes',
            estimated_time=25,
            tmp_depends_on=[0, 1, 2, 3, 4],
            is_user_intensive=False,
        ),
        Step(
            name='Remove and Rest',
            description='Remove once crisp and golden brown. Some may feel a little '
                        'tender in the middle but take them out and let them rest for 10 minutes to '
                        'crisp up.',
            estimated_time=11,
            tmp_depends_on=[0, 1, 2, 3, 4, 5],
            is_user_intensive=False,
        ),
        Step(
            name='Serve',
            description='Serve Immediately',
            estimated_time=1,
            tmp_depends_on=[0, 1, 2, 3, 4, 5, 6],
            is_user_intensive=False,
        )
    ],
    serving_size=4
)
d_sweet_potato_chips.parse_step_deps()
meal.dishes.append(d_sweet_potato_chips.put())
d_sweet_potato_chips.generate_img_url()

meal.gen_schedule()
meal.put()
