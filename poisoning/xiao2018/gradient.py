import numpy as np

import sys, os

# current workaround to support imports from top level for things above the scope of this package
# don't remember if there is a better way

if __name__ == "__main__":
    sys.path.extend([f'../../../{name}' for name in os.listdir("../..") if os.path.isdir("../../" + name)])
else:
    sys.path.extend([f'../{name}' for name in os.listdir(".") if os.path.isdir(name)])

from poisoning.utils import PoisonLogger

def r_term(weights, **kwargs):
    
    """The r-term as described in the paper in equation 4 and 5

    Parameters:
        Weights: The weights (turned into np.array)
        Arguments:
            type : (str) : type of algorithm to use ::: {'lasso', 'ridge', 'elastic'}
                default => 'lasso'
            rho : (float) : Term in the elastic net
                default => 0.5
            range_value : (float) : Range the sub-gradient returns if weight at that point is zero
                default => 0.0
    
    Raises:
        TypeError: Invalid range value (less than -1 or greater than 1)
        TypeError: Unknown parameters
        TypeError: Invalid algorithm type

    Returns:
        Vector of the same size as the weights: The derivative of Omega term with respect to the weights
    """
    
    if kwargs:
        PoisonLogger.info(f'Got arguments: {kwargs}')
    
    algorithm = kwargs.pop('type', 'lasso')
    rho = kwargs.pop('rho', 0.5)
    range_value = kwargs.pop('range_value', 0.0)
    
    if range_value < -1 or range_value > 1:
        raise TypeError('range_value cannot be greater than 1 or less than -1')
    
    if kwargs:
        raise TypeError('Unknows parameters: ' + ', '.join(kwargs.keys()))
    
    weights = np.array(weights)

    PoisonLogger.info('Finding subgradient.')

    if algorithm == 'lasso':
        return subgradient(weights, range_value)
    elif algorithm == 'ridge':
        return weights
    elif algorithm == 'elastic':
        return rho * subgradient(weights, range_value) + (1 - rho) * weights
    else:
        raise TypeError(f'Invalid algorithm type provided: {algorithm}')

def subgradient(weights, range_value=0.0):
    """Returns the subgradient as described in the paper as sub(w)

    Args:
        weights (vector): The weights
        range_value (float, optional): In between -1 and 1 inclusive. Defaults to 0.0.

    Returns:
        [type]: [description]
    """
    
    PoisonLogger.info(f'Got argument for range_value::{range_value}.')
    
    return np.array([-1 if i < 0 else 1 if i > 0 else range_value for i in weights])