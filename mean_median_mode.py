from collections import Counter 
def mean(array,places_to_round):
    return round(sum(array)/len(array),places_to_round)

def median(array):
    array = sorted(array)
    if len(array)%2==0:
        return (array[int(len(array)/2)-1],array[int(len(array)/2)])
    else:
        return array[int(len(array)/2)]
    
def mode(array):
    data = Counter(array)
    data = dict(data)
    mode = [k for k, v in data.items() if v == max(list(data.values()))] 
  
    if len(mode) == len(array):
        get_mode = "No mode found"
    else: 
        get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 

    print(get_mode) 
