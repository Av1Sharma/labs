"""
The class definition for the class lab

The class Length should meet the specification outlined below. It has two 
(hidden) attributes accessible behind getters.  It has a __str__ method for 
object representation and a method for converting from one unit to another.

Initial skeleton by W. White (wmw2)

YOUR NAME AND NETID HERE
THE DATE COMPLETED HERE
"""


class Length(object):
    """
    A class representing a measurement of length.
    
    Length is defined as a numerical value plus a unit of measurement.
    """

    # MUTABLE ATTRIBUTES
    # Attribute _value: The measured length
    # Invariant: _value is a float
    #
    # IMMUTABLE ATTRIBUTES
    # Attribute _unit: The unit of measurement
    # Invariant: _unit is a string and either 'ft' or 'm'
    
    # GETTERS AND SETTERS GO HERE
        
    # INITIALIZER
    def __init__(self, value, unit='ft'):
        """
        Initializes a new Length object with the given value and unit.
        
        Parameter value: The measured length
        Precondition: value is a float
        
        Parameter unit: The unit of measurement (default 'ft')
        Precondition: unit is a string and either 'ft' or 'm'
        """
        assert isinstance(value, float), 'value must be a float'
        assert isinstance(unit, str), 'unit must be a string'
        assert unit in ['ft', 'm'], "unit must be either 'ft' or 'm'"
        
        self._value = value
        self._unit = unit
    def getUnit(self):
        return self._unit
    # __str__ METHOD
    def __str__(self):
        """
        Returns: A readable string representation of this length.
        """
        return str(self._value) + ' ' + self._unit

    # Method measure
