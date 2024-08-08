import statistics

# List of marks
marks = [6, 7, 5, 7, 7, 8, 7, 6, 9, 7, 4, 10, 6, 8, 8, 9, 5, 6, 4, 8]

mean = statistics.mean(marks)
print("Mean", mean)

median = statistics.median(marks)
print("Media", median)

mode = statistics.mode(marks)
print("Mode", mode)

standard_deviation = statistics.stdev(marks)
print("Standard Deviation", standard_deviation)
