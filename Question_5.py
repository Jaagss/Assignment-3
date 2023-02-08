with open("marks.txt",'r') as f:
    a = f.read().splitlines()

main_list=[]
for i in a:
    i = i.split(', ')
    main_list.append(i)

total_mark = [100,100,100,100]
weightage = [('labs',30),('midsem',15),('assignments',30),('endsem',25)]
policy = [80,65,50,40]
grade = ['A','B','C','D','F']

total_student_marks = []
for i in main_list:
    sum_ = 0
    for j in range(1,len(i)):
        sum_ += int(i[j])
    total_student_marks.append(sum_)


def percentage(main,total_mark,weights):
    percentile_list = []
    for i in range(len(main)):
        temp = 0
        for j in range(1,len(main[i])):
            temp += round((float(main[i][j])) / total_mark[j-1] * weights[j-1][1],2)
        percentile_list.append(temp)
    return percentile_list

def final_cutoff(policy):
    final_percentile_list = []
    percentile_list = percentage(main_list,total_mark,weightage)
    pol = policy.copy()
    for i in range(len(policy)):
        final_percentile_list = []
        temp = []
        for j in percentile_list:
                if j <= pol[i]+2 and j >= pol[i]-2:
                    temp.append(j)
        temp.sort(reverse = True)
        diff = 0
        if temp == []:
            pass
        else:
            for k in range(1,len(temp)):
                if diff < (temp[k-1] - temp[k]):
                    diff = temp[k-1] - temp[k]
                    v1 = temp[k-1]
                    v2 = temp[k]
            try:
                final_percentile_list.append((v1+v2)/2)
            except UnboundLocalError:
                pass
            if final_percentile_list == []:
                pass
            else:
                pol[i] = final_percentile_list[0]
    return pol
print(final_cutoff(policy))

def grading(pol):
    policy = final_cutoff(pol)
    percentile_list = percentage(main_list,total_mark,weightage)
    final_grade = percentage(main_list,total_mark,weightage).copy()
    for i in range(len(percentile_list)):
        if percentile_list[i] > policy[0]:
            final_grade[i] = grade[0]
        
        elif percentile_list[i] > policy[1]:
            final_grade[i] = grade[1]

        elif percentile_list[i] > policy[2]:
            final_grade[i] = grade[2]
        
        elif percentile_list[i] > policy[3]:
            final_grade[i] = grade[3]
        
        elif percentile_list[i] <= policy[3]:
            final_grade[i] = grade[4]
    
    return final_grade

def counter_1(pol):
    A, B, C, D, F = 0, 0, 0, 0, 0
    final_grade = grading(pol)
    for i in final_grade:
        if i == 'A':
            A += 1
        elif i == "B":
            B += 1
        elif i == 'C':
            C += 1
        elif i =='D':
            D += 1
        elif i == 'F':
            F += 1
    counter_list = []
    counter_list.append(A)
    counter_list.append(B)
    counter_list.append(C)
    counter_list.append(D)
    counter_list.append(F)
    return counter_list

counter = counter_1(policy)
policy = final_cutoff(policy)
def get_summary(cname, credit,policy):
    print("----------------------------------------")
    print("                 SUMMARY                ")
    print("                  ",cname,credit)
    print("Assessments -",weightage)
    print("          Policy -",policy)
    print("     A -",counter[0],"B -",counter[1],"C -",counter[2],"D -",counter[3],"F -",counter[4])


def grade_in_file(main):
    with open('grade.txt','w') as f:
        for i in range(len(main)):
            f.write(main[i][0] + ', ' + str(total_student_marks[i]) + ', ' + str(grade[i]) + '\n')


def student_record(main_list):
    rollno = str(input("Enter roll no: "))
    for i in range(len(main_list)):
        if str(main_list[i][0]) == rollno:
            print(main_list[i][1::],end=", ")
            print(total_student_marks[i],end=", ")
            print(grade[i])

while True:
    print("1. Generate grading summary\n2. Print grade of all students in file\n3. Search for a students record\n")
    
    choice = int(input("Enter choice: "))
    if choice == 1:
        cname = input("Enter course name: ")
        credit = input("Enter credits: ")
        get_summary(cname,credit,policy)
    elif choice == 2:
        grade_in_file()
    elif choice == 3:
        student_record(main_list)