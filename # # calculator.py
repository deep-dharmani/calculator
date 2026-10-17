# # calculator
history="empty history you did'nt do any type of calculation"
no=0
while True:
    work=input('what you want to do in calculator \n (1)do calculation then enter(cal)\n (2)check history of calculation(history)\n (3)exit the calculater(exit)  :')
    work=work.strip()
    work=work.lower()
    if work=='cal':
        calculation=input('what you want to do in calculation :').lower().strip()
        if calculation=='multiplication':
            no1_multi=int(input('enter your first number:'))
            no2_multi=int(input('enter your second number:'))
            if no==0:
                history=f"{no1_multi}x{no2_multi}={no1_multi*no2_multi}"
                no+=1
                print(f"{no1_multi}x{no2_multi}={no1_multi*no2_multi}")
            else:
                history=history ,f"{no1_multi}x{no2_multi}={no1_multi*no2_multi}" 
                no+=1
                print (f"{no1_multi}x{no2_multi}={no1_multi*no2_multi}")
        elif calculation=='addition':
                    no1_add=int(input('enter your first number:'))
                    no2_add=int(input('enter your second number:'))
                    if no==0:
                        history=f"{no1_add}+{no2_add}={no1_add+no2_add}" 
                        no+=1
                        print(f"{no1_add}+{no2_add}={no1_add+no2_add}")
                    else:
                        history=history , f"{no1_add}+{no2_add}={no1_add+no2_add}" 
                        no+=1
                        print(f"{no1_add}+{no2_add}={no1_add+no2_add}")
        elif calculation=='subtraction':
                    no1_sub=int(input('enter your first number:'))
                    no2_sub=int(input('enter your second number:'))
                    if no==0:
                        history=f"{no1_sub}-{no2_sub}={no1_sub-no2_sub}" 
                        no+=1
                        print(f"{no1_sub}-{no2_sub}={no1_sub-no2_sub}")
                    else:
                        history=history , f"{no1_sub}-{no2_sub}={no1_sub-no2_sub}" 
                        no+=1
                        print( f"{no1_sub}-{no2_sub}={no1_sub-no2_sub}")
        elif calculation=='division':
                    no1_divide=int(input('enter your first number:'))
                    no2_devide=int(input('enter your second number:'))
                    if no==0:
                        history= f"{no1_divide}/{no2_devide}={no1_divide/no2_devide}" 
                        no+=1
                        print(f"{no1_divide}/{no2_devide}={no1_divide/no2_devide}")
                    else:
                        history=history ,  f"{no1_divide}/{no2_devide}={no1_divide/no2_devide}" 
                        no+=1
                        print(f"{no1_divide}/{no2_devide}={no1_divide/no2_devide}")
        elif calculation=='power':
                    no1_power=int(input('enter exponent:'))
                    no2_power=int(input('enter power   :'))
                    if no==0:
                        history= f"{no1_power} power {no2_power}={no1_power**no2_power}" 
                        no+=1
                        print(f"{no1_power} power {no2_power}={no1_power**no2_power}")
                    else:
                        history=history , f"{no1_power} power {no2_power}={no1_power**no2_power}" 
                        no+=1
                        print(f"{no1_power} power {no2_power}={no1_power**no2_power}" )
        else:
              print('unavailable calculation feature in our calculator')
    elif work=='history':
          print(history)
          print(" ")
          clr_history=input("clear history (yes/no):").lower().strip()
          if clr_history=='yes':
                history=("you cleared the history")
                print(history)
    elif work=="exit":
          exit=input("if you exit then your all work should be deleted  (cancel/ok):").lower().strip()
          if exit=='ok':
                break
    else:
          print("unvailable feature")      
    

          
                    
                        
                    