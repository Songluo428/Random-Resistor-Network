import random
# 文本数据
text = """
20 0.089 0 16 16 24 16 16 24 16 16 24 16 0
P Px Py
0.01% 1.3 7.33
0.08% 1.27 5.67
0.52% 1.55 5.52
1.60% 1.56 4.4
2.75% 1.55 3.47
5.16% 1.65 2.93
9.68% 1.76 2.48
15.50% 2.9 3.26
17.70% 3.26 2.9
16.13% 2.48 1.76
12.46% 2.93 1.65
9.16% 3.47 1.55
5.00% 4.4 1.56
2.96% 5.52 1.55
1.10% 5.67 1.27
0.16% 7.33 1.3
0.03% 8.17 1.26
100.00%
"""
n = None 
e = None
b = None
num1 =None
num2 =None 
num3 =None 
num4 =None  
def parse_first_line(text):
    global n 
    global e 
    global num
    global num1
    global num2
    global num3
    global num4
    global num5
    global num6
    global num7
    global num8
    global num9
    global num10
    global num11


    first_line = text.strip().split('\n')[0]
    parts1 = first_line.split()
    n = int(parts1[0])
    e = float(parts1[1])
    num = int(parts1[2])
    num1 = int(parts1[3])
    num2 = int(parts1[4])
    num3 = int(parts1[5])
    num4 = int(parts1[6])
    num5 = int(parts1[7])
    num6 = int(parts1[8])
    num7 = int(parts1[9])
    num8 = int(parts1[10])
    num9 = int(parts1[11])
    num10 = int(parts1[12])
    num11 = int(parts1[13])
    

    return (int(n)-1)**2 


def parse_text_to_resistor_pairs_and_probabilities(text):
    lines = text.strip().split('\n')
    resistor_pairs = []
    probabilities = []


    for line in lines[2:]:
        parts = line.split()
        if len(parts) == 3:
         
            percentage = float(parts[0].strip('%'))
        
            px = float(parts[1])
            py = float(parts[2])
         
            resistor_pairs.append((px, py))
            probabilities.append(percentage)





    total_probability = sum(probabilities)
    weights = [p / total_probability for p in probabilities]


    return resistor_pairs, weights



def generate_weighted_resistor_pairs(resistor_pairs, weights, count):
    return random.choices(resistor_pairs, weights=weights, k=count)


def generate_weighted_single_resistor(resistor_pairs, weights, count):
    
 
    first_resistors = [pair[0] for pair in resistor_pairs]
  
    return random.choices(first_resistors, weights=weights, k=count)



def split_e_into_pairs_and_singles(e):




    if( e == 40 ):
        return 38,2

    
    if(num11 == 1):
        return e,0
        
    


    if(e == 0 ):
        return 0,0
    # print(e)


    if(e >=2 ):

        num_singles = random.randint(0, 2)
        num_pairs = e -num_singles

        print(num_pairs,num_singles)
        return num_pairs, num_singles
        
    else:
        num_singles = random.randint(0, e)
        num_pairs = e -num_singles
        print(num_pairs,num_singles)
        return num_pairs, num_singles
   



def split_e_into_pairs_and_singles10(e):
    if(e == 0 ):
        return 0,0
    # print(e)

    # print("-----------------------------------------------------")

    if(e >= 19):
        T = True
        while(T):
            num_pairs = random.randint(0, 19)
            num_singles = e -num_pairs
            if(num_singles<21):
                T =False
                
            


            
        print(num_pairs,num_singles)
        return num_pairs, num_singles
        
    else:
        num_singles = random.randint(0, e)
        num_pairs = e -num_singles
        print(num_pairs,num_singles)
        return num_pairs, num_singles




# 测试函数


def generate_resistors(e, resistor_value):
 
    num_pairs, num_singles = split_e_into_pairs_and_singles(e)
    
   
    pairs = [(resistor_value, resistor_value) for _ in range(num_pairs)]
   
    singles = [(resistor_value, resistor_value) for _ in range(num_singles)]

    # print(len(pairs))
    # print(len(singles))
    return pairs, singles,num_pairs, num_singles
def makeok(x,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,pairsss):   
    size = 19 * 19
    resistor_pairs_list = [() for _ in range(size)]
    # for i in range(0, size, 19):
    #     print(resistor_pairs_list[i:i+19])


    elements_to_insert = [(x, x) for i in range(1, n1+1)]
    layer_range = (0, 37)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element
    # for i in range(0, size, 19):
    #     print(resistor_pairs_list[i:i+19])         
    
    elements_to_insert = [(x, x) for i in range(1, n2+1)]
    layer_range = (38, 75)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 

    elements_to_insert = [(x, x) for i in range(1, n3+1)]
    layer_range = (76, 113)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 

    elements_to_insert = [(x, x) for i in range(1, n4+1)]
    layer_range = (114, 151)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))

    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element
   

    elements_to_insert = [(x, x) for i in range(1, n5+1)]
    layer_range = (152, 189)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element


    elements_to_insert = [(x, x) for i in range(1, n6+1)]
    layer_range = (190, 227)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element


    elements_to_insert = [(x, x) for i in range(1, n7+1)]
    layer_range = (228, 265)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element

    elements_to_insert = [(x, x) for i in range(1, n8+1)]
    layer_range = (266, 303)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element

    elements_to_insert = [(x, x) for i in range(1, n9+1)]
    layer_range = (304, 341)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element



    elements_to_insert = [(x, x) for i in range(1, n10+1)]
    layer_range = (342, 360)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element
    
    additional_elements = pairsss
    # print(pairsss)
    additional_index = 0
    for i in range(size):
        if resistor_pairs_list[i] == ():
            resistor_pairs_list[i] = additional_elements[additional_index]
            additional_index += 1

    # for i in range(0, size, 19):
    #     print(resistor_pairs_list[i:i+19]) 

    print("----------------------")
    original_list  = resistor_pairs_list
    # original_list1 = [1,2,3,4,5,6,7,8,9,0]
    original_list1 = resistor_pairs_list
    second_part = original_list1[:342]
    first_part = original_list1[342:]
    rearranged_list =  first_part+second_part
    # print(rearranged_list)


    # for i in range(0, size, 19):
    #     print(rearranged_list[i:i+19]) 
    
    n = 19

    column_major_order = [original_list[i*n + j] for j in range(n) for i in range(n)]
    rearranged_list1 = [rearranged_list[i*n + j] for j in range(n) for i in range(n)] 

    return column_major_order,rearranged_list1
    # for i in range(0, size, 19):
    #     print(resistor_pairs_list[i:i+19])

    
def makeok1(x,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,pairsss):   
    size = 39
    resistor_pairs_list = [() for _ in range(size)]

    elements_to_insert = [(x,x) for i in range(1, n1+1)]
    layer_range = (20, 21)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element     
    
    elements_to_insert = [(x,x) for i in range(1, n2+1)]
    layer_range = (22, 23)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 

    elements_to_insert = [(x,x) for i in range(1, n3+1)]
    layer_range = (24, 25)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 

    elements_to_insert = [(x,x) for i in range(1, n4+1)]
    layer_range = (26, 27)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 


    elements_to_insert = [(x,x) for i in range(1, n5+1)]
    layer_range = (28, 29)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 

    elements_to_insert = [(x,x) for i in range(1, n6+1)]
    layer_range = (30, 31)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 


    elements_to_insert = [(x,x) for i in range(1, n7+1)]
    layer_range = (32, 33)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 

    elements_to_insert = [(x,x) for i in range(1, n8+1)]
    layer_range = (34, 35)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 

    elements_to_insert = [(x,x) for i in range(1, n9+1)]
    layer_range = (36, 37)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 

    elements_to_insert = [(x,x) for i in range(1, n10+1)]
    layer_range = (0,19)
    possible_indices = list(range(layer_range[0], layer_range[1] + 1))
    possible_indices.append(38)
    random.shuffle(possible_indices)
    for i, element in zip(possible_indices, elements_to_insert):
        resistor_pairs_list[i] = element 

    
    
    additional_elements = pairsss
    # print(pairsss)
    additional_index = 0
    for i in range(size):
        if resistor_pairs_list[i] == ():
            resistor_pairs_list[i] = additional_elements[additional_index]
            additional_index += 1
    resistor_pairs_list1 = [t[0] for t in resistor_pairs_list]
    print(resistor_pairs_list1)
    resistor_pairs_list2 = [t[1] for t in resistor_pairs_list]
    print(resistor_pairs_list2)

    return resistor_pairs_list1,resistor_pairs_list2




def main(text):
  
    n_squared = parse_first_line(text)
    resistor_pairs, weights = parse_text_to_resistor_pairs_and_probabilities(text)
    pairs, singles_from_generate,num_pairs1, num_singles1 = generate_resistors(num, e)
    print( pairs, singles_from_generate,num_pairs1, num_singles1)

    pairs1, singles_from_generate1,num_pairs11, num_singles11 = generate_resistors(num1, e)

    print(num_pairs11, num_singles11) 
    pairs2, singles_from_generate2,num_pairs12, num_singles12 = generate_resistors(num2, e)
    print(num_pairs12, num_singles12)
    pairs3, singles_from_generate3,num_pairs13, num_singles13 = generate_resistors(num3, e)
    print(num_pairs13, num_singles13)
    pairs4, singles_from_generate4,num_pairs14, num_singles14 = generate_resistors(num4, e)  
    print(num_pairs14, num_singles14)




    pairs5, singles_from_generate5,num_pairs15, num_singles15 = generate_resistors(num5, e)
    print(num_pairs15, num_singles15) 

    pairs6, singles_from_generate6,num_pairs16, num_singles16 = generate_resistors(num6, e)
    print(num_pairs16, num_singles16)

    pairs7, singles_from_generate7,num_pairs17, num_singles17 = generate_resistors(num7, e)
    print(num_pairs17, num_singles17)

        
    pairs8, singles_from_generate8,num_pairs18, num_singles18 = generate_resistors(num8, e)
    print(num_pairs18, num_singles18)

    pairs9, singles_from_generate9,num_pairs19, num_singles19 = generate_resistors(num9, e)
    print(num_pairs19, num_singles19)

    num_pairs110, num_singles110 = split_e_into_pairs_and_singles10(num10)

    print(num_pairs110, num_singles110 )




    allnum1  = num_pairs1+num_pairs11+num_pairs12+num_pairs13+num_pairs14+num_pairs15+num_pairs16+num_pairs17+num_pairs18+num_pairs19+num_pairs110
    allnum2 = num_singles11+num_singles12+num_singles13+num_singles14+num_singles15+num_singles16+num_singles17+num_singles18+num_singles19+num_singles110




    # pairs, singles_from_generate,num_pairs1, num_singles1 = generate_resistors(num, e)
    # print( pairs, singles_from_generate,num_pairs1, num_singles1)



    resistors_list = generate_weighted_resistor_pairs(resistor_pairs, weights, n_squared-allnum1)
    singles_list = generate_weighted_resistor_pairs(resistor_pairs, weights, 2*n-1-allnum2)
 

    resistors_list,resistors_list1=makeok(e,num_pairs11,num_pairs12,num_pairs13,num_pairs14,num_pairs15,num_pairs16,num_pairs17,num_pairs18,num_pairs19,num_pairs110,resistors_list)
    singles_list,singles_list1 = makeok1 (e,num_singles11 ,num_singles12,num_singles13,num_singles14,num_singles15,num_singles16,num_singles17,num_singles18,num_singles19,num_singles110,singles_list)



    
    print(len(singles_list))
    print(len(resistors_list))

    return  resistors_list,singles_list,resistors_list1,singles_list1



resistor_pairs,singlessssss,resistors_list1,singles_list1=main(text)
x_count = n
y_count = n

chosen_pair = random.sample(resistor_pairs, 1)[0]
chosen_single = random.sample(singlessssss, 1)[0]


def generate_components(x_count, y_count, start_x, start_y, step, resistor_pairs,singlessssss):
    # print("resistor_pairs----")
    # for i in range(0, 361, 19):
    #     print(resistor_pairs[i:i+19])
    index = 0
    components = []
    pair_index = 0 

    for i in range(x_count):
        for j in range(y_count):
           
                                              
            if j == 0 and i == 0:
               next_x = start_x
               for k in range(x_count):
                    next_x += step
                    chosen_single = singlessssss[index]

                    components.append(f"r {next_x} {start_y} {next_x - step} {start_y} 0 {chosen_single:.5f}")
                    # print(index)
                    index += 1
                    # singlessssss.remove(chosen_single)
                    # print(index)
                
            if pair_index < len(resistor_pairs) or i < x_count: 
                x = start_x + i * step
                y = start_y + j * step
                if i == 0 and j!= x_count-1:
                    next_y = y +step
                  
                    components.append(f"w {x} {y} {x} {next_y } 0")
                       
                
                if i == x_count-1 and j != x_count-1:
                    next_y = y + step
                   
                    components.append(f"w {x+step} {y} {x+step} {next_y} 0 ")
                    
                    
                if i == 0 and j != 0:
                    next_x = x+step
                    chosen_single = singlessssss[index]
                    components.append(f"r {x} {y} {next_x} {y} 0 {chosen_single:.5f}")
                    # print(2)
                    # singlessssss.remove(chosen_single)
                    # print(index)
                    index += 1
                    # singlessssss.remove(chosen_single)
                    # print(index)
                    
                if 1 <= i <= x_count-1 and j != x_count-1  :
                    next_x = x + step  
                    next_y = y + step
                    

                    components.append(f"r {x} {y} {x} {next_y} 0 {resistor_pairs[pair_index][0]}")

                if 0 <= j <= x_count-2 and i != 0: 
                    next_x = x + step
              
                    components.append(f"r {x} {next_y} { next_x} {next_y} 0 {resistor_pairs[pair_index][1]}")
                    pair_index += 1  
            else:
                break  

    # print(singlessssss)
    return components


def generate_components1(x_count, y_count, start_x, start_y, step, resistor_pairs,singlessssss):

    components = []
    pair_index = 0 
    index = 0

    for i in range(x_count):
        for j in range(y_count):
           
                                              
            if j == 0 and i == 0:
               next_x = start_x
               for k in range(x_count-1):
                    next_x += step
                    components.append(f"w {next_x} {start_y} {next_x - step} {start_y} 0")

            if j == 0 and i == 0:
                next_y = start_y + (x_count-1)*step
                next_x = start_x
                for k in range(x_count):
                    chosen_single = singlessssss[index]
                    components.append(f"r {next_x} {next_y } {next_x} {next_y +step} 0 {chosen_single:.5f} ")
                    index+=1
                    next_x += step
                    # print(2) 

                # chosen_single = random.sample(singlessssss, 1)[0]
                # components.append(f"r {x} {y} {x} {next_y} 0 {chosen_single:.1f} ")
                # singlessssss.remove(chosen_single)
                # print(2)                    
                
            if pair_index < len(resistor_pairs) or i < x_count: 
                x = start_x + i * step
                y = start_y + j * step
                if j == x_count-1 and i == 0 :
                    next_x = x
                    for k in range(x_count-1):
                        next_x += step
                        components.append(f"w {next_x} {y+step} {next_x - step} {y+step} 0")
                       
                
                if i == x_count-1 and j != x_count-1:
                    next_y = y + step
                    chosen_single = singlessssss[index]
                    components.append(f"r {x} {y} {x} {next_y} 0 {chosen_single:.5f} ")
                    index+=1
                    # print(index)
                    
                # if j == x_count-1 :
                #     next_y = y + step
                #     chosen_single = random.sample(singlessssss, 1)[0]
                #     components.append(f"r {x} {y} {x} {next_y} 0 {chosen_single:.1f} ")
                #     singlessssss.remove(chosen_single)
                #     print(2)
                    
                if 0 <= i <= x_count-2 and j != x_count-1 :
                    next_x = x + step  
                    next_y = y + step
                    

                    components.append(f"r {x} {y} {x} {next_y} 0 {resistor_pairs[pair_index][0]}")

                if 0 <= j <= x_count-2 and i != x_count-1:  
                    next_x = x + step
              
                    components.append(f"r {x} {next_y} { next_x} {next_y} 0 {resistor_pairs[pair_index][1]}")
                    pair_index += 1  
            else:
                break  
    return components





def save_to_file(filename, components, extra_content):
    with open(filename, 'w') as file:
      
        for line in extra_content:
            file.write(line + '\n')
       
        for component in components:
            file.write(component + '\n')





start_x = 384
start_y = 656
step = 64
components1 = generate_components1(x_count, y_count, start_x, start_y, step, resistor_pairs,singlessssss)
output_filename2 = 'components20x.txt'
extra_lines = [
    "$ 1 0.000005 6.450009306485578 65 5 43",
    "w 384 656 384 592 1",
    "g 384 592 384 528 0"    
]
extra_lines.append(f"R {start_x} {start_y+x_count*step} {start_x-step} {start_y+x_count*step} 0 0 40 20 0 0 0.5")
save_to_file(output_filename2, components1, extra_lines)
print(f"Components have been saved to {output_filename2}")

first_part = singles_list1[19::-1]
second_part = singles_list1[:19:-1]
singlessssss = first_part + second_part

extra_lines = [
    "$ 1 0.000005 6.450009306485578 65 5 43",
    "R 384 784 336 784 0 0 40 20 0 0 0.5"
   


]
extra_lines.append(f"w {start_x+x_count*step} 784 {start_x+(x_count+1)*step} 784 1")
extra_lines.append(f"g {start_x+(x_count+1)*step} 784 {start_x+(x_count+2)*step} 784 0")
components = generate_components(x_count, y_count, start_x, start_y, step, resistors_list1,singlessssss)
output_filename1 = 'components20y.txt'
save_to_file(output_filename1, components, extra_lines)
print(f"Components have been saved to {output_filename1}")

