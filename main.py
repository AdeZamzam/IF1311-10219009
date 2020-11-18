# a = 10, a adalah variable dengan nilai 10

#tipe data : angka satuan (integer)
data_integer = 1
print("data :", data_integer)
print("- bertype", type(data_integer))

#tipe  data : angka dan koma (float)
data_float = 1.5
print("data :", data_float)
print("- bertype", type(data_float))

#type data : kumpulan karakter (string)
data_string = "ucup"
print("data :", data_string)
print("_ bertype :", type(data_string))

#type data : type data biner true/fals (bool)
data_bool = False
print("data :", data_bool)
print("- bertype :", type (data_bool))

#type data khusus
# bilangan kompleks
data_complex = complex(5.6)
print("data ;", data_complex)
print("- bertype :", type(data_complex))

#type data dari bahasa c
from ctypes import c_double, c_char

data_c_double = c_double (10.5)
print("data :", data_c_double)
print("- bertype :", type(data_c_double))
