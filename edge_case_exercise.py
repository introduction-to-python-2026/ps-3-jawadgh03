
def move(my_list, direction):
    index_of_one = my_list.index(1)
  
    if direction == 'right':
         if my_list[index_of_one] ==1:
          my_list[index_of_one +1] = 1
          return my_list
          if index_of_one[-1]:
              return my_list



    elif direction == 'left':
       if index_of_one > 0:
           if index_of_one[0]:
              return my_list
           elif my_list[index_of_one] == 1:
            my_list[index_of_one] = 0
            my_list[index_of_one -1] = 1
            return my_list
        
    return my_list
      

