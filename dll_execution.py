from ctypes import *

print(windll.msvcrt.time(None))

windll.msvcrt.puts(b"print this!")

new_str = create_string_buffer(10)
print(new_str.raw)

new_str.value = b"AAAAA"
print(new_str.raw)

windll.msvcrt.memset(new_str, c_char(b"X"), 5)
windll.msvcrt.puts(new_str)

print(new_str.raw)
