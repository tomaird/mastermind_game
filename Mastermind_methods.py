#library imports
from random import randint

#Generates a pattern for a given length and number range
def gen_pattern(p_range=4,length=4):
    pattern = []
    for i in range(0,length):
        pattern.append(randint(1,p_range))
    print("Generated pattern: ",pattern)
    return pattern

#compares a guess to a pattern and returns the correctness of each item
def analyse_guess(guess,pattern):
    #print("Analysing guess: "+str(guess))
    correctness = [0 for i in pattern]
    temp_pattern = pattern[:] #copy to temp
    i = 0
    #check for exact match - correctness = 2
    for guess_item in guess:
        if guess_item == pattern[i]:
            correctness[i] = 2
            temp_pattern[i] = 0
            #print("Item "+str(i)+" correctness 2")
        i = i+1
    i = 0
    #check for inexact match - correctness = 1
    for guess_item in guess:
        if correctness[i] != 2:
            if guess_item in temp_pattern:
                correctness[i] = 1
                temp_pattern[temp_pattern.index(guess_item)] = 0
                #print("Item "+str(i)+" correctness 1")
        i = i+1
    #print("Final correctness: "+str(correctness))
    return correctness

#Checks a guess is valid for a given input range and length
def guess_is_valid(guess_input,p_range=4,p_length=4):
    #check valid range of numbers
    guess_range = list(range(1,p_range+1))
    guess_range_str = [str(guess_range[i]) for i in range(0,len(guess_range))]
    for item in guess_input:
        if item not in guess_range_str:
            print("Invalid guess item. valid guess items are: ",guess_range)
            return False
    #check valid length
    if len(guess_input)!=p_length:
        print("Invalid guess length. Length is: ",p_length)
        return False
    return True

#parses a guess from str to list of int
def parse_guess(guess_input):
    temp_list = [int(guess_input[i]) for i in range(len(guess_input))]
    return temp_list