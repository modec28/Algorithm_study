number_of_room = int(input())

if number_of_room ==1:
    print(1)
else:
    k_factor = int((number_of_room-2)/6)*2
    #k_factor = k(k+1)

    distance = 0
    #print("k_factor : ", k_factor)
    while True:
        prev_dist = distance*(distance+1)
        next_dist = (distance+1)*(distance+2)

        if prev_dist <= k_factor and k_factor < next_dist:
            print(distance+2)
            break
        else:
            distance += 1
