
  
  





print("mad lib is ")


# def find_keys(formatString):
f = open('./madlib_cli/test.txt', 'r')
file_txt=f.read()
#   keys_list = []
#   end = 0
#   repetitions = file_txt.count("{)")
#   for i in range(repitions):
#     start = file_txt.find('{',end) + 1
#     end = file_txt.find('}', start)
#     key = file_txt[start : end]
#     keys_list.append(key)
#   print (keys_list)
# I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}

# for i in keys_list:
#   file_txt= file_txt.replace(i, input("add "+ i))
# print(file_txt)

# print(keys_list)
# print(new_list)
def prompt_user_input(): 
  first_user_input = input("I the --put-adjective-here-- and: ")
  new_list.append(first_user_input)
  file_txt.replace("adjective1",first_user_input)
  print(first_user_input)
  second_user_input = input("I the --adjective-- and --put-a-second-adjective-here-: ")
  new_list.append(second_user_input)
  print(second_user_input)
  third_user_input = input("I the --adjective-- and --put-a-second-adjective-here- have --past-tense-verb: ")
  new_list.append(third_user_input)
  print(third_user_input)
  fourth_user_input = input("I the --adjective-- and --put-a-second-adjective-here- have --past-tense-verb: ")
  new_list.append(fourth_user_input)
  print(fourth_user_input)
  # for i in keys_list
  #   file_txt.replace(i, input("add "+ i))

def print_user_madlib_info():

  print("I the " + new_list[0] + " and " + new_list[1] +""+ new_list[2] + " have " + new_list[3])
  
  prompt_user_input() 
  print_user_madlib_info()
   