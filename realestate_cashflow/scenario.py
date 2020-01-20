##{
import numpy as np
import json
##}


##{
class Scenario():

    def __init__(self, scenario_path):

        self.scenario_path = scenario_path
        self.load_data()
        self.check_data()
        self.set_attributes()
        self.get_downtine_payment()

    def load_data(self):
        with open(self.scenario_path) as f:
            self.data = json.load(f)

    def check_data(self):
        # assert all keys are there
        # assert all values are numeric
        # assert 0 <= rate/ratio <= 1
        return None

    def set_attributes(self):
        for k, v in self.data.items():
            setattr(self, k, v)

    def get_downtine_payment(self):
        tmp = (self.price * (1 + self.registration_tax - self.mortgage_ratio)
               + self.renovation_cost + self.oneshot_cost)
        self.downtime_payment = tmp
##}

sc = Scenario("realestate_cashflow/example.json")
