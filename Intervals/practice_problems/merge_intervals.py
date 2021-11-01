def merge(intervals):
    if len(intervals) <= 1:
        return intervals 
    
    sorted_intervals = sorted(intervals)
    output = [sorted_intervals[0]]

    for start, end in sorted_intervals[1:]:
        last_ending_value = output[-1][1]

        if start <= last_ending_value:
            output[-1][1] = max(last_ending_value, end)
        else:
            output.append([start, end])
    return output

print(merge([[1, 2], [2, 4]]))