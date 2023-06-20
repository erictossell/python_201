from ctypes import *
from ctypes import wintypes

SIZE_T = c_size_t
NTSTATUS = wintypes.DWORD

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40

"""
move r10, rcx
move eax, 18h, 
syscall
ret
"""

def verify(x):
    if not x:
        raise WinError()
    
buf = create_string_buffer(b"\xb8\x05\x00\x00\x00\xc3")
buf_addr = addressof(buf)
buf_len = len(buf)
print(hex(buf_addr))

VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, POINTER(wintypes.DWORD))
VirtualProtect.restype = wintypes.INT


protect = VirtualProtect(buf_addr, buf_len, PAGE_EXECUTE_READWRITE, byref(wintypes.DWORD(0)))
verify(protect)

asm_type = CFUNCTYPE(c_int)
asm_function = asm_type(buf_addr)

r = asm_function()
print(hex(r))

buf2 = create_string_buffer(b"\x4c\x8b\xda\xb8\x18\x00\x00\x00\x0f\x05\xc3")
buf2_addr = addressof(buf2)
buf2_len = len(buf2)

print(hex(buf2_addr))

protect = VirtualProtect(buf2_addr, buf2_len, PAGE_EXECUTE_READWRITE, byref(wintypes.DWORD(0)))
verify(protect)

syscall_type = CFUNCTYPE(NTSTATUS, wintypes.HANDLE, POINTER(wintypes.LPVOID), wintypes.ULONG, POINTER(SIZE_T), wintypes.ULONG, wintypes.ULONG)
syscall_function = syscall_type(buf2_addr)

handle = 0xffffffffffffffff

base_address = wintypes.LPVOID(0x0)
zero_bits = wintypes.ULONG(0)
region_size = c_ulonglong(1024 * 12)

ptr2 = syscall_function(handle, byref(base_address), zero_bits, byref(region_size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

print(ptr2)


input()
