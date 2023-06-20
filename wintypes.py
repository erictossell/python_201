from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
SIZE_T = c_size_t

VirtualAlloc = kernel32.VirtualAlloc
VirtualAlloc.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAlloc.restype = wintypes.LPVOID

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40

ptr = VirtualAlloc(None, 100, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

error = GetLastError()

if error != 0:
    print(error)
    print(WinError(error))

print("VirtualAlloc: {0}".format(hex(ptr)))

nt = windll.ntdll
NTSTATUS = wintypes.LONG

NtAllocateVirtualMemory = nt.NtAllocateVirtualMemory
NtAllocateVirtualMemory.argtypes = (wintypes.HANDLE, wintypes.LPVOID, wintypes.ULONG, POINTER(SIZE_T), wintypes.ULONG, wintypes.ULONG)
NtAllocateVirtualMemory.restype = NTSTATUS

handle = 0xffffffffffffffff

base_address = wintypes.LPVOID(0x0)
zero_bits = wintypes.ULONG(0)
region_size = c_ulonglong(1024 * 12)

ptr2 = NtAllocateVirtualMemory(handle, byref(base_address), zero_bits, byref(region_size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)
    
if ptr2 != 0:    
    print(error)
    print(ptr2)
    
print("NtAllocateVirtualMemory: {0}".format(hex(base_address.value)))

input()