def loop(ırarr):
    d = 0 
    click = 0

    for ır in ırarr:
        if ır != 1023:
            if click == 1:
                d = 1
                click += 1

            elif click == 2:
                d = 0
                click = 0
            else:
                click += 1
        
        yield d

signal_array = [1023,1023,1023,23,23,1023,1023,23,1023,1023,23,23,1023,1023,23,1023,1023]

print(list(loop(signal_array)))
