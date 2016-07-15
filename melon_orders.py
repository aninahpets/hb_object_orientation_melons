from random import randint

class TooManyMelonsError(ValueError):
    """Raise error when someone attempts to create an order over 100"""
    pass


class AbstractMelonOrder(object): 
    """Parent class for all melon orders"""
# parent class has three methods shared by both domestic and international 
#   melon orders
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.tax = 0.08
        if self.qty > 100:
            raise TooManyMelonsError("No more than 100 melons! You ordered {} melons.\
                ".format(self.qty))

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_base_price(self):
        return randint(5, 9)

    def get_total(self): 
        """Calculate price."""

        base_price = self.get_base_price()
        # base_price = float(5)
        if self.species == "Christmas":
            base_price *= float(1.5)
        total = (float(1) + self.tax) * float(self.qty) * float(base_price)
        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order. 

    Inheriting attributes from AbstractMelonOrder Class"""
# Super used to initialize domestic melons; other methods inherited from parent class
    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, "USA")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order.    

    Inheriting attributes from AbstractMelonOrder Class"""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, country_code)
# override default tax value for international orders
        self.tax = 0.17

    def get_total(self):
        #if qty less than 10 then increase total by 3 dollars because international

        new_total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            return new_total + 3
        return new_total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order.    

    Inheriting attributes from AbstractMelonOrder Class"""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(GovernmentMelonOrder, self).__init__(species, qty, country_code)
        self.tax = 0

        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Set passed_inspection to True if passed."""
        self.passed_inspection = passed


