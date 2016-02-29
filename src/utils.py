def flat_map(function, l, initial=()):
    """Apply a map function to each element of a list and flatten the result

    function -- map function (should return iterable)
    l        -- list to iterate over
    """
    flat_function = lambda x, y: x + tuple(function(y))
    return reduce(flat_function, l, initial)
