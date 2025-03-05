import random
# 文本数据
text = """
20 1.5 160
P Px Py
0.03% 123 691
0.23% 150 669
0.81% 180 639
1.60% 261 739
2.75% 306 658
4.60% 390 697
8.30% 423 594
15.71% 390 438
20.79% 438 390
16.39% 594 423
11.41% 697 390
7.41% 685 306
4.87% 739 261
3.27% 639 180
1.49% 669 150
0.31% 691 123
0.03% 746 105
100.00%
"""
n = None 
e = None
b = None

def parse_first_line(text):
    global n 
    global e 
    global num
    first_line = text.strip().split('\n')[0]
    parts1 = first_line.split()
    n = int(parts1[0])
    e = float(parts1[1])
    num = int(parts1[2])

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
   

   if (e >= n+n-1):
        num_singles = random.randint(0, n+n-1)
        num_pairs = e - num_singles
        return num_pairs, num_singles
   else:
        num_pairs = random.randint(0, e)   
        num_singles = e - num_pairs


        return num_pairs, num_singles

def generate_resistors(e, resistor_value):
 
    num_pairs, num_singles = split_e_into_pairs_and_singles(e)
    
   
    pairs = [(resistor_value, resistor_value) for _ in range(num_pairs)]
   
    singles = [(resistor_value, resistor_value)for _ in range(num_singles)]

    print(len(pairs))
    print(len(singles))
    return pairs, singles,num_pairs, num_singles

def main(text):
  
    n_squared = parse_first_line(text)
    resistor_pairs, weights = parse_text_to_resistor_pairs_and_probabilities(text)
    pairs, singles_from_generate,num_pairs1, num_singles1 = generate_resistors(num, e) 
   
    resistors_list = generate_weighted_resistor_pairs(resistor_pairs, weights, n_squared-num_pairs1)
    singles_list = generate_weighted_resistor_pairs(resistor_pairs, weights, 2*n-1-num_singles1)
    print(len(singles_list))
    print(len(resistors_list))

    for item in pairs:
  
        random_index = random.randint(0, len(resistors_list))
   
        resistors_list.insert(random_index, item)


    for item in singles_from_generate:
   
        random_index = random.randint(0, len(singles_list))
  
        singles_list.insert(random_index, item)
    singles_list1=  [t[0] for t in singles_list]
    singles_list2 =  [t[1] for t in singles_list]
    # print(singles_list)
    print(len(singles_list))
    print(len(resistors_list))

    return  resistors_list,singles_list1,singles_list2



resistor_pairs,singlessssss,singles_list1=main(text)
x_count = n
y_count = n

chosen_pair = random.sample(resistor_pairs, 1)[0]
chosen_single = random.sample(singlessssss, 1)[0]
print(singlessssss)

def generate_componentsy(x_count, y_count, start_x, start_y, step, resistor_pairs,singlessssss):
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

                    components.append(f"r {next_x} {start_y} {next_x - step} {start_y} 0 {chosen_single:.1f}")
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
                    components.append(f"r {x} {y} {next_x} {y} 0 {chosen_single:.1f}")
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

    print(singlessssss)
    return components


def generate_componentsx(x_count, y_count, start_x, start_y, step, resistor_pairs,singlessssss):

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
                    components.append(f"r {next_x} {next_y } {next_x} {next_y +step} 0 {chosen_single:.1f} ")
                    index+=1
                    next_x += step
                    print(2) 


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
                    components.append(f"r {x} {y} {x} {next_y} 0 {chosen_single:.1f} ")
                    index+=1
                    print(index)
                    
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






extra_lines = [
    "$ 1 0.000005 6.450009306485578 65 5 43",
    "w 384 656 384 592 1",
    "g 384 592 384 528 0"

    
]
extra_lines.append(f"R {start_x} {start_y+x_count*step} {start_x-step} {start_y+x_count*step} 0 0 40 20 0 0 0.5")
components = generate_componentsx(x_count, y_count, start_x, start_y, step, resistor_pairs,singlessssss)
output_filename = 'componentsx.txt'
save_to_file(output_filename, components, extra_lines)
print(f"Components have been saved to {output_filename}")




first_part = singles_list1[n-1::-1]
second_part = singles_list1[:n-1:-1]
singlessssss = first_part + second_part
extra_lines = [
    "$ 1 0.000005 6.450009306485578 65 5 43",
    "R 384 784 336 784 0 0 40 20 0 0 0.5"
   


]
extra_lines.append(f"w {start_x+x_count*step} 784 {start_x+(x_count+1)*step} 784 1")
extra_lines.append(f"g {start_x+(x_count+1)*step} 784 {start_x+(x_count+2)*step} 784 0")
components = generate_componentsy(x_count, y_count, start_x, start_y, step, resistor_pairs,singlessssss)
output_filename1 = 'componentsy.txt'
save_to_file(output_filename1, components, extra_lines)
print(f"Components have been saved to {output_filename1}")


