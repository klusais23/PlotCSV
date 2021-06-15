# join()
# value = int("00000100",16)
# print(value)
# .join() with lists
numList = ['1', '2', '3', '4', "5", "6", "7", "8"]
separator = ''
print(separator.join(numList[4:8]))


# import math
# import time
#
# class measge:
#
#     def __init__(self):
#         pass
#
#
#
# bytes_as_string = "6049480e2300fefe"
# byte_as_list = list( bytes_as_string[i:i+2] for i in range(0, len(bytes_as_string),2))
# bite_list = list("{0:08b}".format(int(byte_as_list[i], 16)) for i in range(0, len(byte_as_list), 1))
#
# # res = "{0:08b}".format(int(byte_as_list[0], 16))
# a=0
# while 1:
#     byte_as_list = list(bytes_as_string[i:i + 2] for i in range(0, len(bytes_as_string), 2))
#     byte_as_list[0]=str(hex(a))
#     a = a + 1
#     if a ==255:
#         a=0
#     bite_list = list("{0:08b}".format(int(byte_as_list[i], 16)) for i in range(0, len(byte_as_list), 1))
#     time.sleep(0.05)
#     printable = str(byte_as_list) + "  " + str(bite_list)
#     print(printable, end="\r")
