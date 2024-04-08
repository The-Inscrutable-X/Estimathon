with open("Estimathon/input2.txt", "r") as f:
    input_lines = f.readlines()

# CONFIG total intervals
total_intervals = 6
good_intervals = 0
increases = 0
count = 0
for i in input_lines:
    count += 1
    start, end, true = [float(i) for i in i.split(" ")]
    print(f"interval {count} is correct?", start < true < end)
    if (start < true < end):
        good_intervals += 1
        increases = int(end/start)
        print("Ratio", int(end/start))
    else:
        print("Score doubled")
    print()

print("good intervals:", good_intervals, total_intervals)
score = (10 + increases) * 2**(total_intervals-good_intervals)
print("Total score:", score)
