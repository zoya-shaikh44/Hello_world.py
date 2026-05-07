#AI guess no.
low = 1
high = 100
while low <= high:
    mid = (low + high) //2
    print ("AI guess =",mid)
    feedback = input ("Is it (h)igh ,(l)ow,(c)orrect ?")
    if feedback == 'c':
        print (" AI guessed it !")
        break
    elif feedback == 'h': #number decrease 
        high = mid -1
    elif feedback == 'l':#number increase 
        low= mid +1
    else :
        print (" please select the correct number ")
