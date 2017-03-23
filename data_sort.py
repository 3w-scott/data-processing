file_object1 = open("D:\study\python\工程\data_processing\hydrophobic.txt")
file_object2 = open('arranged_hydrophobic.txt', 'w')
lines = file_object1.readlines()
total_list = []  # 第一次分割后的结果 62
total_list2 = []  # 第二次分割后的结果 62*4

for i in range(62):  # 子数组的编号是0到61
    total_list.append([])
for i in range(248):
    total_list2.append([])

for i in range(0, len(lines)):  # 第一次分割
    first_cha = lines[i][0]
    if ord(first_cha) in range(65, 90):  # 对于第一个字符为大写字母的行，分布在第0-25子数组
        total_list[ord(first_cha) - 65].append(lines[i])
    if ord(first_cha) in range(97, 122):  # 对于第一个字符为小写字母的行，分布在第26-51子数组
        total_list[ord(first_cha) - 71].append(lines[i])
    if ord(first_cha) in range(48, 57):  # 对于第一个字符为小写字母的行，分布在第52-61子数组
        total_list[ord(first_cha) - 4].append(lines[i])

for i in range(0, len(total_list)):  # 第二次分割
    for j in total_list[i]:
        if j[2] == 'A':
            total_list2[4 * i].append(j)
        if j[2] == 'C':
            total_list2[4 * i + 1].append(j)
        if j[2] == 'G':
            total_list2[4 * i + 2].append(j)
        if j[2] == 'U':
            total_list2[4 * i + 3].append(j)

for i in range(0, len(total_list2) - 1):
    total_list2[i].sort
print(total_list2)
for i in range(0, len(total_list2)):
    file_object2.writelines(total_list2[i])

file_object1.close()
file_object2.close()

file_object1 = open("D:\study\python\工程\data_processing\hbond.txt")
file_object2 = open('arranged_hbond.txt', 'w')
lines = file_object1.readlines()
total_list3 = []  # 第一次分割后的结果 62
total_list4 = []  # 第二次分割后的结果 62*4

for i in range(62):  # 子数组的编号是0到61
    total_list3.append([])
for i in range(248):
    total_list4.append([])

for i in range(0, len(lines)):  # 第一次分割
    first_cha = lines[i][0]
    if ord(first_cha) in range(65, 90):  # 对于第一个字符为大写字母的行，分布在第0-25子数组
        total_list3[ord(first_cha) - 65].append(lines[i])
    if ord(first_cha) in range(97, 122):  # 对于第一个字符为小写字母的行，分布在第26-51子数组
        total_list3[ord(first_cha) - 71].append(lines[i])
    if ord(first_cha) in range(48, 57):  # 对于第一个字符为小写字母的行，分布在第52-61子数组
        total_list3[ord(first_cha) - 4].append(lines[i])

for i in range(0, len(total_list3)):  # 第二次分割
    for j in total_list3[i]:
        if j[2] == 'A':
            total_list4[4 * i].append(j)
        if j[2] == 'C':
            total_list4[4 * i + 1].append(j)
        if j[2] == 'G':
            total_list4[4 * i + 2].append(j)
        if j[2] == 'U':
            total_list4[4 * i + 3].append(j)

for i in range(0, len(total_list4) - 1):
    total_list4[i].sort
print(total_list4)
for i in range(0, len(total_list4)):
    file_object2.writelines(total_list4[i])

file_object1.close()
file_object2.close()
