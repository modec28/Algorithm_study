x = int(input())


if x ==1:
    print("1/1")
else:
    k_factor = int(2*(x-1))
    #k_factor = k(k+1)

    n = 0
    #print("k_factor : ", k_factor)
    while True:
        prev_dist = n*(n+1)
        next_dist = (n+1)*(n+2)

        if prev_dist <= k_factor and k_factor < next_dist:
            k = int(1+n*(n+1)/2)

            child = 1
            mom = n+1
            for j in range(x-k):
                child +=1
                mom -= 1
            if n%2==0:
                #print("even",n,x-k, mom,"/",child)
                print(str(mom)+"/"+str(child))
            else:
                #print("odd",n,x-k, child,"/",mom)
                print(str(child)+"/"+str(mom))
            break
        else:
            n += 1
