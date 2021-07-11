
"""Implementation Bubble sort"""

def bubble_sort(data_list):
    data_length = len(data_list)

    for i in range(data_length):
        for j in range(data_length-i-1):
            if data_list[j] > data_list[j+1]:
                # swap
                result = data_list[j]
                data_list[j] = data_list[j+1]
                data_list[j+1] = result


if __name__ == "__main__":
    data_list = [12, 45, 2, 36, 54, 30, 50]
    bubble_sort(data_list)
    print("Bubble sort is: ", data_list)



"""Eifficient Bubble sort"""

def bubble_sort(list_item):
    list_lenght = len(list_item)

    for i in range(list_lenght):
        swap = False

        for j in range(list_lenght-i-1):
            if list_item[j] > list_item[j+1]:

                result = list_item[j]
                list_item[j] = list_item[j+1]
                list_item[j+1] = result
                swap = True
        
        if swap == False:
            break

if __name__ == "__main__":
    list_item = [12, 45, 2, 36, 54, 30, 50]
    bubble_sort(list_item)
    print("Bubble sorted: ", list_item)