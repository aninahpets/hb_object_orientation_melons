
class AbstractMelonOrder(object): 
    """Parent class for all melon orders"""
# parent class has three methods shared by both domestic and international 
#   melon orders
    def __init__(self, species, qty, country_code="USA"):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.tax = 0.08

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_total(self): 
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order. 

    Inheriting attributes from AbstractMelonOrder Class"""
# Super used to initialize domestic melons; other methods inherited from parent class
    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(self, species, qty)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order.    

    Inheriting attributes from AbstractMelonOrder Class"""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

# override default tax value for international orders
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
