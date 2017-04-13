"""Generates meal schedule."""

import flask

from cookomatic_api.db.meal import Meal

api_schedule = flask.Blueprint('api_schedule', __name__)


class Schedule(object):
    """Generate cooking schedule for a meal."""
    def __init__(self, meal_id):
        # The finished schedule we are trying to generate
        self.schedule = []

        # List that contains the steps for each dish
        self.steps_by_dish = []

        # Contains total time so far for each dish, plus the next step that must be added
        self.time_step = []

        # Total number of steps in the entire meal
        self.total_steps = 0

        # The actual object containing the Meal
        self.meal = Meal.get_by_id(meal_id)

        # Wait time between steps that can be completed simultaneously
        self.wait_time = 0.5

        self._generate()

    def _generate(self):
        """Generates the schedule."""
        self.populate_steps_by_dishes()
        self.populate_time_step()
        self.add_steps()
        self.add_start_time()

    def populate_steps_by_dishes(self):
        """Creates an array of steps sorted by dish."""
        # Populates the steps_by_dish list with the steps for each dish
        for dish_key in self.meal.dishes:
            dish = dish_key.get()
            steps = []
            for step_key in dish.steps:
                steps.append(step_key.get())
                self.total_steps += 1

            self.steps_by_dish.append(steps)

    def populate_time_step(self):
        """Calculates relative time of initial step."""
        # Trying to find the number of steps in each dish and the estimated time of the last step
        for steps in self.steps_by_dish:
            num_steps = len(steps)
            self.time_step.append(steps[num_steps - 1].estimated_time)

    def add_steps(self):
        """Adds steps to the schedule based on time."""
        for _ in range(0, self.total_steps):
            # Find index of minimum value in time_step
            dish_num = self.time_step.index(min(self.time_step))

            # Add the last step for the given dish to the schedule and remove it from that
            # steps_by_dish' step list. The order of these items will be reversed later.
            self.schedule.append(self.steps_by_dish[dish_num].pop())

            # Find the index of the new last step in the steps_by_dish array
            step_num = len(self.steps_by_dish[dish_num]) - 1
            if step_num < 0:
                self.time_step[dish_num] = 10000
            else:
                # Adding new last step's estimated time to running dish time total
                self.time_step[dish_num] += self.steps_by_dish[dish_num][step_num].estimated_time

        # Reverse schedule
        self.schedule.reverse()

    def add_start_time(self):
        """Calculates start time of each step."""
        # The schedule is in order now, all that's left is to assign a start time to every step
        for i, current_step in enumerate(self.schedule):
            previous_step = self.schedule[i - 1]

            # If this is the first step, start at 0
            if i == 0:
                self.schedule[i].start_time = 0
                continue

            # If previous step is user intensive, wait until its done to start this step
            if previous_step.is_user_intensive:
                current_step.start_time = \
                    previous_step.start_time + previous_step.estimated_time

            # If the step doesn't depend on anything, wait a short period of time then start
            elif not current_step.depends_on:
                current_step.start_time = \
                    previous_step.start_time + self.wait_time

            # The previous step is not intensive, but this step may depend on it
            else:
                # Find the most recent step that current_step depends on
                for step in reversed(self.schedule[:i]):
                    if step.key in current_step.depends_on:
                        previous_time = previous_step.start_time + self.wait_time
                        found_time = step.start_time + self.wait_time
                        current_step.start_time = max(previous_time, found_time)
                        break

                else:
                    raise ValueError("Didn't find dependent step.")

            # Save back to schedule
            self.schedule[i] = current_step

        # Calculates the total estimated time for the entire meal
        self.meal.estimated_time = \
            self.schedule[-1].start_time + self.schedule[-1].estimated_time

    def serialize(self):
        """Serializes entity."""
        return [step.serialize() for step in self.schedule]


@api_schedule.route('/v1/schedule/<int:meal_id>')
def get_schedule(meal_id):
    """API method to get meal schedule."""
    sched = Schedule(meal_id)
    return flask.jsonify(sched.serialize())
