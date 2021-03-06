import numpy as np
from typing import Union

def my_strict_sin(x: np.ndarray) -> Union[np.ndarray, np.scalar]:
    return np.sin(x)

def my_chill_sin(x: np.array_like) -> Union[np.ndarray, np.scalar]:
    return np.sin(x)

if __name__ == "__main__":
    a = np.arange(10)
    l = [1, 2, 3]
    my_strict_sin(a)     # Passes typecheck
    my_strict_sin(l)     # Fails typecheck
    my_chill_sin(a)      # Passes typecheck
    my_chill_sin(l)      # Passes typecheck
