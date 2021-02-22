"""
A collection of simple math operations
"""

def simple_add(a,b):
    """The sum of two numbers.
    
    Parameters
    ----------
    a, b : scalars
        Numbers to add.
    
    Returns
    -------
    s : scalar
        The sum of a and b.
        
    Examples
    --------
    >>> simple_math.simple_add(1,2)
    3
    >>> simple_math.simple_add(2.4,3) 
    5.4
    """
    return a+b

def simple_sub(a,b):
    """The difference between two numbers.
    
    Parameters
    ----------
    a : scalar
        Number to subtract from.
    
    b : scalar
        Number that is subtracted.
    
    Returns
    -------
    d : scalar
        The difference a-b.
    
    Examples
    --------
    >>> simple_math.simple_sub(1,2)
    -1
    >>> simple_math.simple_sub(2.4,1) 
    1.4
    """
    return a-b

def simple_mult(a,b):
    """The product of two numbers.
    
    Parameters
    ----------
    a, b : scalars
        Numbers to multiply.
    
    Returns
    -------
    p : scalar
        The product of a and b.
        
    Examples
    --------
    >>> simple_math.simple_mult(4,2)
    8
    >>> simple_math.simple_mult(-2.45,1/3)                                                                              
    -0.8166666666666667
    """
    return a*b

def simple_div(a,b):
    """The quotient of two numbers.
    
    Parameters
    ----------
    a : scalar
        Numerator.
    
    b : scalar
        Denominator.
    
    Returns
    -------
    q : scalar
        The quotient of a and b.
        
    Examples
    --------
    >>> simple_math.simple_div(6,3)
    2.0
    >>> simple_math.simple_div(-1,5)                                                                              
    -0.2
    """
    return a/b

def poly_first(x, a0, a1):
    """First order polynomial evaluation.
    
    Parameters
    ----------
    x : scalar
        Point at which to evaluate.
    
    a0 : scalar
        Offset.
    
    a1 : scalar
        Slope.
    
    Returns
    -------
    y : scalar
        The value of the polynomial at x.
    
    Examples
    --------
    >>> simple_math.poly_first(1,1,1)
    2
    >>> simple_math.poly_first(1,1/3,2/3)                                                                             
    1.0
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """Second order polynomial evaluation.
    
    Parameters
    ----------
    x : scalar
        Point at which to evaluate.
    
    a0 : scalar
        Offset.
    
    a1 : scalar
        Coefficient of x.
    
    a2 : scalar
        Coefficient of x^2.
    
    Returns
    -------
    y : scalar 
        The value of the polynomial at x. 
        
    Examples
    --------
    >>> simple_math.poly_second(1,1,1,1)
    3
    >>> simple_math.poly_second(2,1,1/2,1/4)                                                                            
    3.0
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
