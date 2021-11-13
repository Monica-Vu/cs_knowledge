def get_itinerary(objects, start=None):
    if len(objects) == 0:
        return []
    
    trip = objects_to_dict(objects)
    return create_iternary_list(start, trip)

def objects_to_dict(objects):
    trip = {}

    for i in range(len(objects)):
        pair = objects[i].split(":")
        trip[pair[0]] = pair[1]

    return trip 

def find_next_destination(trip, next_stop):
    for source, destination in trip.items():
        if source == next_stop:
            return destination

def create_iternary_list(start, trip):
    iternary = [start]
    source = start 

    while len(trip) != 0: 
        destination = find_next_destination(trip, source)
        iternary.append(destination)
        del trip[source]
        source = destination 
    
    return iternary

print(get_itinerary(["YVR:SFO", "YYZ:NYC", "SFO:YYZ"], "YVR"))