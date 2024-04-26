"""
DREW KROEGER- 
CSC240- INTRODUCTION TO PYTHON PROGRAMMING
FINAL PROJECT
5/1/2024
This file will use riskfactors.csv- and produce best_and_worst.txt if everything goes to plan
This file takes an input, which should be the file stated just above, and will take 5 columns and column headers from that file.
It will take those 5 columns, and all the values in those columns, it will then find the minimum, and maximum values, and the states associated with those values
with all those states, and headers, and values, it will output a formatted text file, indicating the column header, and the state with the highest value and the state with the lowest value for that specified column header
"""


import csv
#I LEFT THE ORIGINAL TWO PROTOTYPE FUNCTIONS HERE. I THOUGHT YOU MIGHT WANT TO SEE THEM
'''
def make_and_trim_lists(file_object):
    csv_reader = csv.reader(file_object)
    big_list = []
    state_names = []
    heart_disease = []
    motor_vehicle = []
    teen_birth = []
    adult_smoking = []
    adult_obesity = []
    teen_birth_fixed = []
    adult_smoking_fixed = []
    adult_obesity_fixed = []
    
    iteration = 0
    for line in csv_reader:
        
        if iteration < 3:
            iteration+= 1
            next(csv_reader)
            
        else:
            state_names.append(line[0])
            heart_disease.append(line[1])
            motor_vehicle.append(line[5])
            teen_birth.append(line[7])
            adult_smoking.append(line[11])
            adult_obesity.append(line[13])
            
    #print("STATE NAMES:",state_names, "\n\n\n")
    #print("HEART DISEASE:",heart_disease, "\n\n\n")
    #print("MOTOR VEHICLE:",motor_vehicle, "\n\n\n")
    #print("TEST",teen_birth, "\n\n\n")          #this and the two below it are percentages
    #print(adult_smoking, "\n\n\n")
    #print(adult_obesity, "\n\n\n")
    
    
    for element in teen_birth:
        element = element.replace("%", "")
        element = element.replace("N/A", "-1")
        teen_birth_fixed.append(element)
        
    for element in adult_smoking:
        element = element.replace("%", "")
        element = element.replace("N/A", "-1")
        adult_smoking_fixed.append(element)
        
    for element in adult_obesity:
        element = element.replace("%", "")
        element = element.replace("N/A", "-1")
        adult_obesity_fixed.append(element)
        
    #print("TEEN BIRTH FIXED:",teen_birth_fixed, "\n\n\n")
    #print("ADULT SMOKING FIXED:",adult_smoking_fixed, "\n\n\n")
    #print("ADULT OBESITY FIXED:", adult_obesity_fixed, "\n\n\n")
    #print("\n\n\n")
    
    return state_names,heart_disease,motor_vehicle,teen_birth_fixed,adult_smoking_fixed,adult_obesity_fixed

'''
"""----------------------------------------------------------------------------------------------------------
"""
 
    
'''
def get_max_and_min_of_one_list(big_list):
    minimum = 0
    maximum = 0
    
    for element in range(0, len(big_list)):
        big_list[element] = float(big_list[element])
        
        
    big_list_copy = big_list.copy()
    big_list_copy.sort()
    
    iteration = 0
    for element in big_list_copy:
        if element < 0:
            iteration+= 1
        elif element > 0:
            minimum = (big_list_copy[iteration])
            break
            
    big_list_copy.sort(reverse=True)
    
    iteration = 0
    for element in big_list_copy:
            maximum = (big_list_copy[iteration])
            break
            
    print(minimum)
    print(maximum)
    
    return minimum, maximum
'''

#---------------------------------------------------------------------------------------------------

#THIS IS WHERE THE ACTUAL USED FUNCTIONS START


def make_and_trim_one_list(file_obj,column):
    """
    this takes a csv file(with a specific format-see riskfactors.csv) and will take one of the columns, trims down information into only numbers, and inserts it into a list,
    it also will get the column header of that list- see what this means at column header declaration line
    requires: A opened file, an integer
    returns, a list of all the numbers of every row in that specified column in the file, it also returns the header of that column
    """
    csv_reader = csv.reader(file_obj)                                                    #we create csv object
    
    singular_list= []                                                                    #create two lists to take values in csv file
    singular_list_fixed = []                                                             
    column_header = " "                                                                  #this is what is displayed in the ouput file underneath indicator(Heart disease death rate, motor vehicle death rate, etc)
    
    iteration = 0                                                                        #we use this to get past the white lines in the csv file
    for line in csv_reader: 
        if iteration == 5:                                                               #when on line five we have the actual column header
            column_header = line[column]
            iteration += 1
        elif iteration > 5:                                                              #greater than five we know we are past the column header and into the actual data
            singular_list.append(line[column])
        else:                                                                            #if we are on line 1,2,3,4 we need to keep going
            iteration += 1
            
    for element in singular_list:                                                        #this gets rid of the N/A and % in the table, since we only want numbers to work with
        element = element.replace("%", "")
        element = element.replace("N/A", "-1")
        singular_list_fixed.append(element)                                              #make another list that is only numbers(although still in string form) back to main method
        
        
    #print("COLUMN Header:",column_header," LIST FIXED:", singular_list_fixed)

    
    return singular_list_fixed, column_header                                           #return a list and a column header
    
   

#-------------------------------------------------------------------------------------------------------------



def get_max_and_state_of_one_list(big_list,state_list):
    """
    this takes a list, and finds the maximum value of it, it also takes the index the maximum value was found at and gives the associated state
    requires: a list of numbers, a list of states in alphbetical order
    returns: the largest number in the list of numbers, and the state associated with the largest number
    """
    maximum = 0
    state = ""
    for element in range(0, len(big_list)):                                              #change the string elements in the list into float/numbers instead
        big_list[element] = float(big_list[element])
        
    maximum = 0                                                                          #we find the largest value in the list
    for element in big_list:
        if element > maximum:
            maximum = element
            
    index = big_list.index(maximum)                                                      #once we have the true maximum we want to find the index of it
    state = state_list[index]                                                            #with the index of the true maximum we can find the associated state with it, as the maximum's index is the same as its state is, I BUILT MY PROGRAM AROUND THIS ORIGINAL THOUGHT
    
    #print("maximum value:",maximum)
    #print("maximum value state:",state)
    
    return maximum,state





#----------------------------------------------------------------------------------------------------------




def get_min_and_state_of_one_list(big_list,state_list):
    """
    this takes a list, and finds the minimum value of it, it also takes the index the minimum value was found at and gives the associated state
    requires: a list of numbers, a list of states in alphbetical order
    returns: the smallest number in the list of numbers, and the state associated with the smallest number
    """
    minimum = 0              
    state = ""
    for element in range(0, len(big_list)):                                             #change string elements into float again
        big_list[element] = float(big_list[element])
    
    iteration = 0
    minimum = 999999                                                                    #need to find smallest value in list
    for element in big_list:
        if element < minimum and element > -1:                                          #since we havee -1 representing N/A, then we need to exclude those values, which we can do with this
            minimum = element
            
    index = big_list.index(minimum)                                                     #with true maximum we need to find index of it
    state = state_list[index]                                                           #with the index we just got, we can find the state associated with that index
    
    
    #print("minimum value:",minimum)
    #print("minimum value state:",state)
    
    return minimum,state                                                                #return the minimum and state



#---------------------------------------------------------------------------------------------------------------------


def file_output(head_list,min_state, max_state, min_value, max_value):
    """
    this takes 5 column headers, and minimum values and states associated with those values, along with maximum values and states associated with those values
    requires:a list of 5 column headers, 2 seperate state lists(each only contains 5 states), 2 seperate value lists(each only contains 5 values)
    returns: an int(specifically 1), however it actually creates and formats a file with the information stated in the 2 lines above this 
    
    """
    min_value_string = []                                                              #we already the minimum value list, and max value list into floats, but since we are printing it we need to put it back into string
    max_value_string = []
    
    for element in range(0,len(min_value)):                                            #we know that max_value_string and min_value_string will be the same length(or they should be), so only one for loop is needed, to change the values back into strings
        min_value_string.append((str(min_value[element])))
        max_value_string.append((str(max_value[element])))
    #print("MIN STATE",min_state)
    #print("MAX STATE",max_state)
    #print(min_value_string)   
    #print(max_value_string)
    
    
    output_file_obj = open("best_and_worst.txt" , 'w')                                #this is where actually writing into an output file starts, there is not a whole lot to explain here, it is a lot of formatted printing, see best_and_worst.txt(output file) for what it looks like
    print('{:<35}:{:<30}{:<5}'.format("Indicator","Min","Max"),file = output_file_obj)
    print('-------------------------------------------------------------------------------------------------------',file=output_file_obj)
    print('{:<35}:{:<20}{:>5}:    {:<20}{:>5}'.format(head_list[0],min_state[0],min_value_string[0],max_state[0],max_value_string[0]),file = output_file_obj)
    print('{:<35}:{:<20}{:>5}:    {:<20}{:>5}'.format(head_list[1],min_state[1],min_value_string[1],max_state[1],max_value_string[1]),file = output_file_obj)
    print('{:<35}:{:<20}{:>5}:    {:<20}{:>5}'.format(head_list[2],min_state[2],min_value_string[2],max_state[2],max_value_string[2]),file = output_file_obj)
    print('{:<35}:{:<20}{:>5}:    {:<20}{:>5}'.format(head_list[3],min_state[3],min_value_string[3],max_state[3],max_value_string[3]),file = output_file_obj)
    print('{:<35}:{:<20}{:>5}:    {:<20}{:>5}'.format(head_list[4],min_state[4],min_value_string[4],max_state[4],max_value_string[4]),file = output_file_obj)
    output_file_obj.close()                                                          #close the output file
    return 1




#----------------------------------------------------------------------------------------------------------






def main():
    """This is the main method for final.py(this file) it will ask for a file input(should be riskfactors.csv- or something with almost exact same format) and will find minimum and maximum values and states associated with those values
    this method does not require anything, although there should be a riskfactors.csv- or other csv to be input into the first input prompt
    """
    #file_object = open("riskfactors.csv", 'r', encoding = "windows-1252")
    #state_list,heart_list,motor_list,birth_list,smoking_list,obesity_list = make_and_trim_lists(file_object)
    
    
    input_checker =True
    while input_checker == True:
        file_str = input( "Enter name of file you want to open:" )                         #this will run until an actual file matching input line name is found
        try:
            file_object = open(file_str, 'r', encoding = "windows-1252")
            input_checker = False
        except FileNotFoundError:
            print("The file", file_str ,"doesn't exist.")    
    
    
    state_list,state_header = make_and_trim_one_list(file_object,0)                       #we make and trim the five lists specified in the prompt, we also make a state list, which is used for finding the min and max values of every list, state_header is never used.
    file_object.seek(0)                                                                   #this .seek will go back to the beginning of the csv file, it is more inefficient than the other way i did(doing it all in one go), but adds way more functionality/flexibility
    heart_list,heart_header = make_and_trim_one_list(file_object,1)                       #the second number that is input is the column in which the row we want lies
    file_object.seek(0) 
    motor_list,motor_header = make_and_trim_one_list(file_object,5)
    file_object.seek(0)
    birth_list,birth_header = make_and_trim_one_list(file_object,7)
    file_object.seek(0)
    smoking_list,smoking_header = make_and_trim_one_list(file_object,11)
    file_object.seek(0)
    obesity_list,obesity_header = make_and_trim_one_list(file_object,13)                 
     #if we wanted to add all 20 values to our output file, we could, we would just need to repeat these lines above for each column, and get variables for each one, you could also just make a list to store all the varibales in
    
    
    #print("HEART ISSUES:")                                                              #we then get the minimum and maximum values, along with their associated state for the ouput file, THIS COULD ALL BE DONE IN ONE FOR LOOP, BUT I LIKE IT THE WAY IT IS,was easier to follow individual variables
    heart_min, min_heart_state = get_min_and_state_of_one_list(heart_list,state_list)
    heart_max,max_heart_state = get_max_and_state_of_one_list(heart_list,state_list)
    
    #print("MOTOR ISSUES")
    motor_min, min_motor_state = get_min_and_state_of_one_list(motor_list,state_list)
    motor_max, max_motor_state = get_max_and_state_of_one_list(motor_list,state_list)
    
    #print("BIRTH ISSUES")
    birth_min,min_birth_state = get_min_and_state_of_one_list(birth_list,state_list)
    birth_max, max_birth_state = get_max_and_state_of_one_list(birth_list,state_list)
    
    #print("SMOKING ISSUES")
    smoke_min,min_smoking_state = get_min_and_state_of_one_list(smoking_list,state_list)
    smoke_max,max_smoking_state = get_max_and_state_of_one_list(smoking_list,state_list)
    
    #print("OBESITY ISSUES")
    obesity_min,min_obesity_state = get_min_and_state_of_one_list(obesity_list,state_list)
    obesity_max,max_obesity_state = get_max_and_state_of_one_list(obesity_list,state_list)
    #once we have each minimum and maximum value we want, along with their state, we put it all into an array so we can put it into the output function much easier, i do not want 25 or so parameters, just do 5
    
    
    
    headers = [heart_header,motor_header,birth_header,smoking_header,obesity_header]     #these lists would need to add extra variables if you did all 20 values in the csv
    min_state_list = [min_heart_state,min_motor_state,min_birth_state,min_smoking_state,min_obesity_state]
    max_state_list = [max_heart_state,max_motor_state,max_birth_state,max_smoking_state,max_obesity_state]
    min_state_values = [heart_min,motor_min,birth_min,smoke_min,obesity_min]
    max_state_values = [heart_max,motor_max,birth_max,smoke_max, obesity_max]
    
    
    
    
    number= file_output(headers,min_state_list,max_state_list,min_state_values,max_state_values) # we put the lists into the output function and are then done
    print("All Done :D!(It takes a second to load sometimes)")
    file_object.close()                                                                         #close the output file
    
    
     
main()                                                                                  #actually run the main function in the script
