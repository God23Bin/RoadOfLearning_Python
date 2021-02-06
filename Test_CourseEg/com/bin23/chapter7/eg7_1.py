import struct

# 等待存储的数据
# values = (8, b'abc', 9.9, True)
values = (8, bytes('abc', encoding="UTF-8"), 9.9, True)

# 创建Struct对象
s = struct.Struct('I3sf?')
# 使用Struct对象的pack方法将数据转换成二进制字节串
packed_data = s.pack(* values)
f = open('eg7_1.dat', 'wb')
# 文件对象写入二进制字节串数据
f.write(packed_data)
f.close()