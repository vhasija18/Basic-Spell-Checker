# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:16:30 2019

@author: Vhasija
"""
import re
from difflib import get_close_matches
from collections import Counter

#Function to convert input file in dictionary and store it in the  form of list.
def form_dict(file):
    str = ' '
    print("We are making dictionary... Please wait!")
    for res in file :
        res = res.replace('\n',' ')
        str = str +res
    list1 = str.split()
    list2 = [re.sub('[^a-zA-Z]+','',_) for _ in list1]
    list2.sort()
    final_list = list(dict.fromkeys(list2))
    user_input(final_list)
 
#Function to take input from user and store the words in form of list
def user_input(final_list):
    list_of_words = []
    i = input("Enter number of words you want to test ")
    for x in range(int(i)):
        list_of_words.append(input("Please enter word number %d " %(x+1) ))
    print("\n\nOutput words are\n")
    for x in list_of_words:
        find_nearest(x,final_list)


def counter_list (l1,l2):
    return(list((Counter(l1)-Counter(l2)).elements()))

#Check if edited words and suggested word are equal or not.
def check(word_list2,match_list2):
    if(word_list2 == match_list2):
        print(''.join(word_list2))
        return(0)
    else:
        return(1)
        
#Function called when the length of suggested word and given word is equa.
def equal (word,matched_word):
    print(''.join(word))
 
# Function called when the given word is jumbled with respect to suggested word.
def rearrange(word_list,match_list):
    for x in range (0,len(word_list)):
        if (word_list[x]!=match_list[x]):
            temp = word_list[x]
            word_list[x]=word_list[x+1]
            word_list[x+1] = temp
    return(check(word_list,match_list))

# Function called when the given word has one character different from suggested word.
def replace(word_list,match_list): 
    x = counter_list(match_list,word_list)
    for y in range(0,len(word_list)):
        if(word_list[y]!=match_list[y]):
            word_list[y] = x[0]
            break
    return(check(word_list,match_list))
       
#Function called when the given word has one character less than suggested word.
def add_alpha(word_list,match_list):
    x = counter_list(match_list,word_list)
    word_list.append(word_list[-1])
    for y in range(0, len(word_list)):
        if(word_list[y] != match_list[y]):
            break
    temp = len(word_list) -1
    while temp > y:
        word_list[temp]= word_list[temp-1]
        temp = temp - 1
    word_list[y] = x[0]
    return(check(word_list,match_list))

#Function called when the given wpord has one character more than suggested word.  
def delete_alpha(word_list,match_list):
    x = counter_list(word_list,match_list)
    word_list.remove(x[0])
    return(check(word_list,match_list))

#Driver function.    
def find_nearest(word,final_list):
    flag = 0
    f = 0
    matches = get_close_matches(word,final_list,3)
    matches.sort()
    length_word = len(word)
    word_list = list(word)
    word_list_sort = list(word)
    word_list_sort.sort()
    if(len(matches) == 0):
        flag = 2
    if(flag == 2):
        print(''.join(word))
    else:
        for y in range (0,len(matches)):
            match_list = list(matches[y])
            match_list_sort = list(matches[y])
            match_list_sort.sort()
            if (word == matches[y]):
                equal(word,matches[y])
                flag = 1
                break
            elif(length_word == len(matches[y]) and word_list_sort == match_list_sort):
                f = rearrange(word_list,match_list)
                if(f==0):
                    flag=1
                    break
            elif(length_word == len(matches[y]) and len(counter_list(match_list,word_list)) == 1 and len(counter_list(word_list,match_list)) == 1):
                f = replace(word_list,match_list)
                if(f==0):
                    flag= 1
                    break
        if(flag==0 and f != 1 ):
               for y in range (0,len(matches)):
                   match_list = list(matches[y])
                   match_list_sort = list(matches[y])
                   match_list_sort.sort()
                   if (length_word +1 == len(matches[y]) and len(counter_list(match_list,word_list)) == 1 and len(counter_list(word_list,match_list)) == 0):
                       f = add_alpha(word_list,match_list)
                       if(f==0):
                           flag = 1
                           break
                   elif(length_word -1 == len(matches[y])  and len(counter_list(word_list,match_list)) == 1 and len(counter_list(match_list,word_list)) == 0):
                       f = delete_alpha(word_list,match_list)
                       if(f ==0):
                           flag = 1
                           break
        if(flag == 0):
              print(''.join(word))


file = open(r'C:/Users/hasij/OneDrive/Desktop/test.txt','r')
#file = open(r'C:/Users/hasij/OneDrive/Desktop/corpus-challenge5.txt','r')
form_dict(file)

