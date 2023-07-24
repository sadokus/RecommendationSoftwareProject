from graph_search import bfs, dfs
from restaurant_choices import restaurant_choices
from restaurantData import types, restaurant_data
from queue import Queue
from node import DoublyLinkedList

restaurant_string = ""

for letter, choice in restaurant_choices.items():
    if choice.find("No styles"):
        restaurant_string += ("{0} -- {1}\n".format(letter, choice))

def greet():
    print("Welcome to Charles' Restaurant Recommendation Software!\nThis is to determine whether he knows how to handle database(s) and user input, as well as write a program from start - to - finish.")
    print("There are so many different restaurants to explore:\n" + restaurant_string)

def gather_info(inp):
    if inp is None:
        choice = input("What would you like to choose? You can enter any letter from the list to get a selection of choice(s). ")
        if choice.lower() == 'a':
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('a')
        elif choice.lower() == 'b':
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('b')
        elif choice.lower() == 'c':
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('c')
        elif choice.lower() == 'f':
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('f')
        elif choice.lower() == 'g':
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('g')
        elif choice.lower() == 'i':
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('i')
        elif choice.lower() == "j":
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('j')
        elif choice.lower() == "m":
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('m')
        elif choice.lower() == 't':
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('t')
        elif choice.lower() == 'v':
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('v')
        elif choice.lower() == 'p':
            for letter, v in restaurant_choices.items():
                if choice.lower() == letter:
                    print(v)
            get_style('p')
        else:
            print("Oops, looks like that wasn't any correct input! Try again.")
            gather_info(inp)

def bubble_sort(arr):
    for i in range(len(arr)):
        for idx in range(len(arr) - i - 1):
            if arr[idx][2] and arr[idx][3] < arr[idx+1][2] and arr[idx+1][3]:
                #print("bubble sort: {0} and {1}".format(arr[idx], arr[idx+1]))
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
    return arr

def handle_restaurant_choice(restas):
    ##this function will be the one that lists the selected genre of restaurant from highest rating to lowest rating
    #
    restas_string = ""
    #resta_dict = {}
    resta_list = []
    restas_list = DoublyLinkedList()
    lowerednp = restas.lower()
    for i in range(len(restaurant_data)):
        if restaurant_data[i][0] == lowerednp:
            add_list = []
            rd = restaurant_data[i]
            ##unsorted find, just get any matches of correct data
            """
            print("-------------------------------------------------")
            print(restaurant_data[i][0] + " --- type of restaurant!")
            print(restaurant_data[i][1] + " --- name of restaurant!")
            print(restaurant_data[i][2] + " --- price of restaurant!")
            print(restaurant_data[i][3] + " --- rating of restaurant!")
            print(restaurant_data[i][4] + " --- location of restaurant!")
            print("-------------------------------------------------")
            """
            
            add_list.append(rd[0])
            add_list.append(rd[1])
            add_list.append(rd[2])
            add_list.append(rd[3])
            add_list.append(rd[4])
            #resta_dict[rd[1]] = add_list
            resta_list.append(add_list)
    print(restas + " listed here") 
    #print(list(resta_dict))
    bs = bubble_sort(resta_list)
    #sorted = bubble_sort(list(resta_dict))
    #print(resta_list)
    #print(bs)
    for x in range(len(bs)):
        print("name: {0} -- cost: {1} -- rating: {2} -- location: {3}".format(bs[x][1], bs[x][2], bs[x][3], bs[x][4]))

    pass

def get_style(letter):
    display_text = ""
    resta_choice = None
    for i in restaurant_choices.keys():
        if i == letter:
            display_text += restaurant_choices[i]


    res_letter = input("What type would you like to choose?: ")
    ##find if the letters, regardless of if it is the full string or not matches the same string sequence, if it does, go on.
    if res_letter.lower() in types:
        resta_choice = res_letter
        print(resta_choice + ", what a nice choice!")
        print("Here is our list of restaurants of your choice: " + resta_choice + "!")
        handle_restaurant_choice(resta_choice)
    else:
        print("Sorry, that was not any type we have data on. Let's try again.")
        get_style(None)
    return resta_choice

def new_restaurant(np = None):
    np = gather_info(None)
    

def program():
    greet()
    var1 = gather_info(None)
    np = input("Would you like to have another session? (y/n) ")
    if np.lower() == 'y':
        greet()
        gather_info(None)
    elif np.lower() == 'n':
        print("Goodbye!")

program()


