import math

class Interest:

    """
    This class contains modules that help in computing financial interests
    """
    def __init__(self, principal: float, rate: float, time: int, time_unit: str) -> None:
        self.principal = principal
        self.rate = rate
        self.inflation_rate: float = None
        if time_unit=='months':
            self.time = time/12
        elif time_unit=='years':
            self.time = time
        else:
            raise ValueError('time_units can be `months` or `years`')

    def simple_interest(self) -> float:
        """
        This function returns the interest earned based on the object 
        characteristics
        """
        return self.principal*self.rate*self.time

    def real_interest_rate(self) -> float:
        """
        computing the real in interest rate by adjusting the interest rate using an inflation rate
        """
        return self.rate - self.inflation_rate
    
    def real_simple_interest(self, inflation_rate: float) -> float:
        """
        computing real simple interest using the adjusted interest rate (real interest rate)
        """
        self.inflation_rate = inflation_rate
        return self.principal*self.real_interest_rate*self.time

    def compound_interest(self, n) -> float:
        """
        Computing compund interest
        """
        return self.principal*(
            (1+(self.rate/n))**(n-self.time) - 1
            )
    
    def continous_compund_interest_amount(self) -> float:
        """
        computing continous interest
        """
        return self.principal*math.exp(self.rate*self.time)