import time
with open("marks.txt",'r') as f:
    a = f.read().splitlines()

main_list=[]
for i in a:
    i = i.split(', ')
    main_list.append(i)

total_mark = [30,15,30,25]
weightage = [('labs',30),('midsem',15),('assignments',30),('endsem',25)]
policy = [80,65,50,40]
total_student_marks = []

for i in main_list:
    sum_ = 0
    for j in range(1,len(i)):
        sum_ += float(i[j])
    total_student_marks.append(sum_)


class course:
    def __init__(self,policy):
        self.policy = policy;
        self.grade = ['A','B','C','D','F']
    
    def percentile(self):
        percentile_list = []
        for i in range(len(main_list)):
            temp_list = 0
            for j in range(1,len(main_list[i])):
                temp_list += round((int(main_list[i][j]) / total_mark[j-1] * weightage[j-1][1]),2)
            percentile_list.append(temp_list)
        return percentile_list
    
    def cutoff_final(self):
        percentile_list = course(self.policy).percentile()
        for i in range(len(self.policy)):
            final_percentile_list = []
            temp_list = []
            for j in percentile_list:
                if j <= self.policy[i]+2 and j >= self.policy[i]-2:
                    temp_list.append(j)
            
            temp_list.sort(reverse = True)
            diff = 0
            if temp_list == []:
                pass
            else:
                for k in range(1,len(temp_list)):
                    if diff < (temp_list[k-1] - temp_list[k]):
                        diff = temp_list[k-1] - temp_list[k]
                        v1 = temp_list[k-1]
                        v2 = temp_list[k]
                try:
                    final_percentile_list.append((v1+v2)/2)
                except UnboundLocalError:
                    pass
                if final_percentile_list == []:
                    pass
                else:  
                    self.policy[i] = final_percentile_list[0]

    def grading(self):
        percentile_list = course(self.policy).percentile()
        self.final_grade = course(self.policy).percentile().copy()
        for i in range(len(percentile_list)):
            if percentile_list[i] > self.policy[0]:
                self.final_grade[i] = self.grade[0]
            
            elif percentile_list[i] > self.policy[1]:
                self.final_grade[i] = self.grade[1]

            elif percentile_list[i] > self.policy[2]:
                self.final_grade[i] = self.grade[2]
            
            elif percentile_list[i] > self.policy[3]:
                self.final_grade[i] = self.grade[3]
            
            elif percentile_list[i] <= self.policy[3]:
                self.final_grade[i] = self.grade[4]
        
        return self.final_grade
        
    
    def counter(self):
        A, B, C, D, F = 0, 0, 0, 0, 0

        for i in self.final_grade:
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


class Student:
    def __init__(self,course_name,credit,weightage,policy,grade,counter):
        self.course_name = course_name
        self.credit = credit
        self.weightage = weightage
        self.policy = policy
        self.grade = grade
        self.counter = counter

    def get_summary(self):
        print("----------------------------------------")
        print("                 SUMMARY                ")
        print("                  ",self.course_name,self.credit)
        print("Assessments -",self.weightage)
        print("          Policy -",self.policy)
        print("     A -",self.counter[0],"B -",self.counter[1],"C -",self.counter[2],"D -",self.counter[3],"F -",self.counter[4])

    def grade_in_file(self):
        with open('grade.txt','w') as f:
            for i in range(len(main_list)):
                f.write(main_list[i][0] + ', ' + str(total_student_marks[i]) + ', ' + str(self.grade[i]) + '\n')
        
        

    def student_record(self,main_list):
        rollno = str(input("Enter roll no: "))
        for i in range(len(main_list)):
            if str(main_list[i][0]) == rollno:
                print(main_list[i][1::],end=", ")
                print(total_student_marks[i],end=", ")
                print(self.grade[i])
                break

course_class = course(policy)
course_class.cutoff_final()
course_class.grading()

stu = Student('IP',"4",weightage,policy,course_class.grading(),course_class.counter())
while True:
    print("1. Generate grading summary\n2. Print grade of all students in file\n3. Search for a students record\n")
    
    choice = input("Enter choice: ")
    if choice == '1':
        stu.get_summary()
    elif choice == '2':
        stu.grade_in_file()
    elif choice == '3':
        stu.student_record(main_list)
    else:
        break
    print()