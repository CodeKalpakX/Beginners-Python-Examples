def ips_between(start, end):
    start_lst = start.split('.')
    end_lst = end.split('.')
    diff = 0
    for i in range(len(start_lst)):
        diff += (int(end_lst[i])-int(start_lst[i]))*(256**(3-i))
    return diff
    

print(ips_between('192.168.1.1','192.168.2.1'))
