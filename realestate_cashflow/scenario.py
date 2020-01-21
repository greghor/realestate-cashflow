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
        self.set_downtine_payment()
        self.set_mortgage_monthly_payment()
        self.set_cash_flow() 

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
        self.mortgage_amount = self.price * self.mortgage_ratio

    def set_downtine_payment(self):
        tmp = (self.price * (1 + self.registration_tax - self.mortgage_ratio)
               + self.renovation_cost + self.oneshot_cost)
        self.downtime_payment = tmp

    def set_mortgage_monthly_payment(self):
        
        m = (self.mortgage_amount * self.interest_rate/12 *
             1/(1-(1+self.interest_rate/12)**(-self.mortgage_duration*12)))
        self.mortgage_monthly_payment = m
        self.mortgage_total_cost = m * self.mortgage_duration * 12

    def set_cash_flow(self):
        self.cash_flow = (self.monthly_rent 
                          - self.mortgage_monthly_payment 
                          - self.monthly_cost 
                          - (self.yearly_vacancy_ratio*self.monthly_rent
                             + self.yearly_cost + self.yearly_tax
                             )/12
                          )
            

##}

##{
sc = Scenario("realestate_cashflow/example.json")
print(sc.cash_flow)
print(sc.mortgage_monthly_payment)
##}


