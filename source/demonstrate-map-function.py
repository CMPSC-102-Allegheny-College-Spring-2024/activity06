"""Demonstrate the use of the map higher-order function."""

# TODO: Refer to the course slides for more details about these functions

# TODO: Add type annotations to describe the input and output of this function
def square(value):
    """Compute the square of a provided number."""
    # TODO: compute the square of the provided number and return it


# TODO: Add type annotations to describe the input and output of this function
def map(f, sequence):
    """Apply the function f to the sequence of values."""
    # TODO: apply the function f to the sequence of values and return
    # the result of the overall computation
    # TODO: note that this should work for any type of callable function f
    # TODO: return the result of this computation


# create a list of values and then square them using map
values = (2, 3, 5, 7, 11)
squared = map(square, values)
# TODO: display the output of the squaring computation
# TODO: display the result of the computation, indented by three spaces

# create a list of values using the range function
# then square the output of range with the map function
squared_range = map(square, range(10))
# TODO: display the output of the squaring computation
# TODO: display the result of the computation, indented by three spaces
print("   " + str(squared_range))
