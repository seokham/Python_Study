
#* [AND]
#* True  and True  -> True
#* True  and False  -> False
#* False and True  -> False
#* False and False -> False

#* [OR]
#* True	  or  True	 True
#* True	  or	False	 True
#* False  or	True	 True
#* False  or	False	 False

#* [NOT]
#* not   True    False
#* not   False   True


in_str = input("Please enter your ID.\n")
real_hoppang = "hoppang"
real_h1234 = "h1234"
if real_hoppang == in_str or real_h1234 == in_str:
  print("Hello!")
else:
  print("Who are you?")