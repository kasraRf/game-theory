from fractions import Fraction


#get probability function
def get_probability():
    inp=input("Enter man good probability")
    numerator, denominator = inp.split('/')
    if numerator>denominator:
       print('probability should between 0,1')
       get_probability()
    else:
       man_good_prob = Fraction(int(numerator), int(denominator))
   
    inp=input("Enter woman good probability")
    numerator, denominator = inp.split('/')
    if numerator>denominator:
        print('probability should between 0,1')
        get_probability()
    else:
        woman_good_prob = Fraction(int(numerator), int(denominator))
    man_bad_prob=1-man_good_prob
    woman_bad_prob=1-woman_good_prob  
    return man_good_prob,man_bad_prob,woman_good_prob,woman_bad_prob

#get matrix function
def get_matrix(type):
    matrix=[]
    for i in range (2):
        row=[]
        for j in range(2):
            value=int(input(""+type+" matrix[{}][{}]:".format(i,j)))
            row.append(value)
        matrix.append(row)    
    return matrix

#calculate man payoff function
def create_man_payoff(matrix,good_prob,bad_prob):
    payoff_matrix=[]
    for i in range (2):
        value1=(matrix[i][0]*good_prob)+(matrix[i][0]*bad_prob)
        value2=(matrix[i][0]*good_prob)+(matrix[i][1]*bad_prob)
        value3=(matrix[i][1]*good_prob)+(matrix[i][0]*bad_prob)
        value4=(matrix[i][1]*good_prob)+(matrix[i][1]*bad_prob)
        payoff_matrix.append([value1,value2,value3,value4])
    return payoff_matrix

#calculate woman payoff function
def create_woman_payoff(matrix,good_prob,bad_prob):
    payoff_matrix=[]
    index_1=[0,0,1,1]
    index_2=[0,1,0,1]    
    for i in range (4):
        value1=(matrix[index_1[i]][0]*good_prob)+(matrix[index_2[i]][0]*bad_prob)
        value2=(matrix[index_1[i]][1]*good_prob)+(matrix[index_2[i]][1]*bad_prob)
        payoff_matrix.append([value1,value2])
    return payoff_matrix

#find horizontal man best response
def horizontal_man_best_response(pay_off_matrix):
    best_response_matrix=[]
    for i in range(4):
        if pay_off_matrix[0][i]>pay_off_matrix[1][i]:
            best_response_matrix.append(['B'])
        elif pay_off_matrix[0][i]<pay_off_matrix[1][i]:     
            best_response_matrix.append(['S'])
        elif pay_off_matrix[0][i]==pay_off_matrix[1][i]: 
            best_response_matrix.append(['B','S'])
    return best_response_matrix
      
#find horizontal woman best response
def horizontal_woman_best_response(woman_good_matrix,woman_bad_matrix):
     best_response_matrix=[]
     for i in range(2):
            if woman_good_matrix[i][0]>woman_good_matrix[i][1]:
                if woman_bad_matrix[i][0]>woman_bad_matrix[i][1]:
                    best_response_matrix.append(['BB'])
                elif woman_bad_matrix[i][0]<woman_bad_matrix[i][1]:
                    best_response_matrix.append(['BS'])
                else:    
                    best_response_matrix.append(['BB','BS'])
            elif woman_good_matrix[i][0]<woman_good_matrix[i][1]:
                if woman_bad_matrix[i][0]>woman_bad_matrix[i][1]:
                    best_response_matrix.append(['SB']) 
                elif woman_bad_matrix[i][0]<woman_bad_matrix[i][1]:
                    best_response_matrix.append(['SS'])         
                else :
                    best_response_matrix.append(['SB','SS'])   
            else:
                if woman_bad_matrix[i][0]>woman_bad_matrix[i][1]:
                    best_response_matrix.append(['BB','SB'])
                elif woman_bad_matrix[i][0]<woman_bad_matrix[i][1]:
                    best_response_matrix.append(['BS','SS'])
                else:
                    best_response_matrix.append(['BB','BS','SB','SS'])
     return best_response_matrix    
      
#find vertical man best response
def vertical_man_best_response(man_good_matrix,man_bad_matrix):
     best_response_matrix=[]
     for i in range(2):
            if man_good_matrix[0][i]>man_good_matrix[1][i]:
                if man_bad_matrix[0][i]>man_bad_matrix[1][i]:
                    best_response_matrix.append(['BB'])
                elif man_bad_matrix[0][i]<man_bad_matrix[1][i]:
                    best_response_matrix.append(['BS'])
                else:    
                    best_response_matrix.append(['BB','BS'])
            elif man_good_matrix[0][i]<man_good_matrix[1][i]:
                if man_bad_matrix[0][i]>man_bad_matrix[1][i]:
                    best_response_matrix.append(['SB']) 
                elif man_bad_matrix[0][i]<man_bad_matrix[1][i]:
                    best_response_matrix.append(['SS'])         
                else :
                    best_response_matrix.append(['SB','SS'])   
            else:
                if man_bad_matrix[0][i]>man_bad_matrix[1][i]:
                    best_response_matrix.append(['BB','SB'])
                elif man_bad_matrix[0][i]<man_bad_matrix[1][i]:
                    best_response_matrix.append(['BS','SS'])
                else:
                    best_response_matrix.append(['BB','BS','SB','SS'])
     return best_response_matrix    

#find vertical woman best response
def vertical_woman_best_response(pay_off_matrix):
    best_response_matrix=[]
    for i in range(4):
        if pay_off_matrix[i][0]>pay_off_matrix[i][1]:
            best_response_matrix.append(['B'])
        elif pay_off_matrix[i][0]<pay_off_matrix[i][1]:     
            best_response_matrix.append(['S'])
        elif pay_off_matrix[i][0]==pay_off_matrix[i][1]: 
            best_response_matrix.append(['B','S'])
    return best_response_matrix
      

#find candidate nash
def horizontal_candidate_nash(man_best_response_matrix,woman_best_response_matrix):
     i=0     
     type=['B','S']
     candidate_nash=[]
     for exist in woman_best_response_matrix:
        for element in woman_best_response_matrix[i]:
                if element =='BB' and type[i] in man_best_response_matrix[0]:
                    candidate_nash.append([type[i],'BB'])
                elif element=='BS' and type[i] in man_best_response_matrix[1]:
                    candidate_nash.append([type[i],'BS'])
                elif element=='SB' and type[i] in man_best_response_matrix[2]:
                    candidate_nash.append([type[i],'SB'])
                elif element=='SS' and type[i] in man_best_response_matrix[3]:
                    candidate_nash.append([type[i],'SS'])
        i=i+1   
     return candidate_nash

def vertical_candidate_nash(man_best_response_matrix,woman_best_response_matrix):
     i=0     
     type=['B','S']
     candidate_nash=[]
     for exist in man_best_response_matrix:
        for element in man_best_response_matrix[i]:
                if element =='BB' and type[i] in woman_best_response_matrix[0]:
                    candidate_nash.append(['BB',type[i]])
                elif element=='BS' and type[i] in woman_best_response_matrix[1]:
                    candidate_nash.append(['BS',type[i]])
                elif element=='SB' and type[i] in woman_best_response_matrix[2]:
                    candidate_nash.append(['SB',type[i]])
                elif element=='SS' and type[i] in woman_best_response_matrix[3]:
                    candidate_nash.append(['SS',type[i]])
        i=i+1   
     return candidate_nash



#find nash
def horizontal_find_nash(candidate1_nash,candidate2_nash):
    nash=[]
    for element1 in candidate1_nash:
        for element2 in candidate2_nash:
            if element1[1]==element2[1]:
                nash.append([element1[0]+element2[0],element1[1]])
    return nash
def vertical_find_nash(candidate1_nash,candidate2_nash):
    nash=[]
    for element1 in candidate1_nash:
        for element2 in candidate2_nash:
            if element1[0]==element2[0]:
                nash.append([element1[0],element1[1]+element2[1]])
    return nash




#get probability from user
man_good_prob,man_bad_prob,woman_good_prob,woman_bad_prob=get_probability()

#get matrix from user 
man_good_matrix=get_matrix('man good') 
man_bad_matrix=get_matrix('man bad')
woman_good_matrix=get_matrix('woman good') 
woman_bad_matrix=get_matrix('woman bad')

#calculate payoff for good and bad day of man and woman
man_good_payoff=create_man_payoff(man_good_matrix,man_good_prob,man_bad_prob)
man_bad_payoff=create_man_payoff(man_bad_matrix,man_good_prob,man_bad_prob)
woman_good_payoff=create_woman_payoff(woman_good_matrix,woman_good_prob,woman_bad_prob)
woman_bad_payoff=create_woman_payoff(woman_bad_matrix,woman_good_prob,woman_bad_prob)

#find horizontal best response
horizontal_man_good_best_response=horizontal_man_best_response(man_good_payoff)
horizontal_man_bad_best_response=horizontal_man_best_response(man_bad_payoff)
woman_best_response=horizontal_woman_best_response(woman_good_matrix,woman_bad_matrix)


#find vertical best response
man_best_response=vertical_man_best_response(man_good_matrix,man_bad_matrix)
vertical_woman_good_best_response=vertical_woman_best_response(woman_good_payoff)
vertical_woman_bad_best_response=vertical_woman_best_response(woman_bad_payoff)


#find nash
candidate_nash1=horizontal_candidate_nash(horizontal_man_good_best_response,woman_best_response)
candidate_nash2=horizontal_candidate_nash(horizontal_man_bad_best_response,woman_best_response)
candidate_nash3=vertical_candidate_nash(man_best_response,vertical_woman_good_best_response)
candidate_nash4=vertical_candidate_nash(man_best_response,vertical_woman_bad_best_response)
nash1=horizontal_find_nash(candidate_nash1,candidate_nash2)
nash2=vertical_find_nash(candidate_nash3,candidate_nash4)
print(nash1)
print(nash2)