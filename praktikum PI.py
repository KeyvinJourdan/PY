# file = open('data.txt', mode = 'w', encoding = 'utf-8')
# print(file)

#close file
# file.close()

with open('data.txt', mode = 'r', encoding = 'utf-8') as file :
    #file kondisi open
    #file.write untuk menambahkan teks
    # file.write(',Halo lagi bang deh')

    #file.read untuk membaca
    # file.read()

    # print(file.read())
    # print(file.read(8)) #membaca sebanyak 8 karakter
    # print(file.readline()) #baca 1 baris sampai dengan endline (\n)

    x = file.readlines()

    # print(x[2])
    x = map(lambda i : i.replace('\n', ''),x)
    # for i in range (len(x)):
    #     x[i] = x[i].replace('\n', '')

    for kata in x:
        print(kata)

#file kondisi close

