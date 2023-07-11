def odd_even(type, data, mode):
    if type == 'S':
        data_n = data
    elif type == 'L':
        data_n = []
        for i in data :
            data_n.append(i)

    if mode == 'Odd':
        for index in range(len(data)):
            if(index % 2 == 0):
                print(data[index],end='')
    elif mode == 'Even':
        for index in range(len(data)):
            if(index % 2 != 0):
                print(data[index],end='')

print("*** Odd Even ***")
type,data,mode = input("Enter Input : ").split(",")
printout = odd_even(type, data, mode)


    
        
