def myfilter(function, iterable):
    # Create an empty list to hold the filtered results
    filtered_results = []

    # Loop through each item in the iterable
    for item in iterable:
        # If the function returns True for this item, add it to the results
        if function(item):
            filtered_results.append(item)

    return filtered_results


def canvote(x):
    if x < 18:
        return False
    else:
        return True


numbers = [1, 2, 33, 4, 25, 16, 7, 18, 19, 10]
filtered_result = myfilter(canvote, numbers)

print("Filtered result:", filtered_result)
