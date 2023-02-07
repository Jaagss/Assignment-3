n = int(input("Enter number of files: "))

def read_file(file):
    with open(file,'r') as f:
        a = f.read().splitlines()
    return a


def F_1(file):
    a = read_file(file)
    count_total = 0
    unique_list = []
    for i in a:
        for j in i.split():
            j = j.strip(',.:; ')
            count_total += 1
            if j not in unique_list:
                unique_list.append(j)
    return len(unique_list)/count_total


def F_2(file):
    a = read_file(file)
    words_dict = {}
    word_list = []
    count_words = 0

    for i in a:
        for j in i.split():
            count_words += 1
            word_list.append(j)

    for i in word_list:
        words_dict[i] = word_list.count(i)
    words_occur = sorted(words_dict.items(), key = lambda x: x[1], reverse = True)
    count_occur = 0

    try:
        for i in range(5):
            count_occur += words_occur[i][1]
    except:
        pass
    return count_occur/count_words


def F_3(file):
    a = read_file(file)
    sentence = []
    total_sentence = []
    for i in a:
        i = i.strip(',:; ')
        i = i.split('. ')
        print(i)
        for j in i:
            words_count = j.split()
            if len(words_count) > 35 or len(words_count) < 5:
                sentence.append(j)
            total_sentence.append(j)
    print(len(sentence))
    print(len(total_sentence))
    return len(sentence)/len(total_sentence)


def F_4(file):
    a = read_file(file)
    words = []
    for i in a:
        i = i.split()
        words+=i
    no_of_words = len(words)
    count_main = 0
    for i in words:
        count_symbol = 0
        for j in i:
            if j in [',','.',';',':']:
                count_symbol += 1
        if count_symbol > 1:
            count_main += 1
    return count_main/no_of_words


def F_5(file):
    a = read_file(file)
    count = 0
    for i in a:
        i = i.split('.')
        i.remove("")
        for j in i:
            j = j.split()
            count += len(j)
    
    if count > 750:
        return 1
    else:
        return 0


for i in range(n):
    file_name = input("Enter File Name: ")
    f1 = F_1(file_name)
    f2 = F_2(file_name)
    f3 = F_3(file_name)
    f4 = F_4(file_name)
    f5 = F_5(file_name)
    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(4+f1*6+f2*6-f3-f4-f5)