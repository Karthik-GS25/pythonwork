"""60. Validate an integer and insert it into a NumPy sensor array."""


def insert_sensor(position, element):
    try:
        import numpy as np
    except ImportError:
        raise RuntimeError(
            "NumPy is required for question 60; install it with pip install numpy"
        )
    readings = np.array([10, 20, 30, 40, 50])
    try:
        if not str(element).isdigit():
            raise ValueError("Element must contain digits only")
        if not 0 <= position <= len(readings):
            raise IndexError("Invalid insertion position")
        return np.insert(readings, position, int(element))
    finally:
        print("Sensor insertion operation complete.")


try:
    print(insert_sensor(2, "25"))
except (ValueError, IndexError, RuntimeError) as error:
    print(error)
