from ctypes import windll, byref, create_string_buffer, GetLastError, Structure, sizeof, POINTER
from ctypes.wintypes import HWND, LPCSTR, UINT, INT, LPSTR, LPDWORD, DWORD, HANDLE, BOOL

MessageBoxA = windll.user32.MessageBoxA # MessageBoxA is a function pointer

MessageBoxA.argtypes = (HWND, LPCSTR, LPCSTR, UINT) # argtypes is a tuple
MessageBoxA.restype = INT # restype is a type

print(MessageBoxA)

lpText = LPCSTR(b"Hello World!")
lpCaption = LPCSTR(b"Hello")
MB_OK = 0x00000000
MB_OKCANCEL = 0x00000001

#MessageBoxA(0, lpText, lpCaption, MB_OKCANCEL)

GetUserNameA = windll.advapi32.GetUserNameA
GetUserNameA.argtypes = (LPSTR, LPDWORD)
GetUserNameA.restype = INT

buffer_size = DWORD(32)
buffer = create_string_buffer(buffer_size.value)

GetUserNameA(buffer, byref(buffer_size))
print(buffer.value)

error = GetLastError()

if error != 0:
    print("Error code: {0}".format(error))  
    
class RECT(Structure):
    _fields_  = [("left", INT),
                 ('top', INT),
                 ('right', INT),
                 ('bottom', INT)]
rect = RECT()
    
print("Size of RECT is {0}".format(sizeof(RECT)))
print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)

rect.left = 1 

print(rect.left)

GetWindowRect = windll.user32.GetWindowRect
GetWindowRect.argtypes = (HWND, POINTER(RECT))
GetWindowRect.restype = BOOL

hwnd = windll.user32.GetForegroundWindow()
GetWindowRect(hwnd, byref(rect))

print(rect.left)
print(rect.top)
print(rect.right)
print(rect.bottom)
