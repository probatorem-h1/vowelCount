def stringWithVowelCount(lst):
    count = 0
    if lst == []:
        return count
    if type(lst[0]) == list:
        count = stringWithVowelCount(lst[0])
    if type(lst[0]) == str:
        if 'a' in lst[0] or 'e' in lst[0] or 'i' in lst[0] or 'o' in lst[0] or 'u' in lst[0]:
            count = count + 1
    
    return count + stringWithVowelCount(lst[1:])


print(stringWithVowelCount([]))                               
print(stringWithVowelCount([[1,'Test',2.0,'v','other',1,2,'bbbbb',8,9,10]]))
print(stringWithVowelCount([[[[[[[[['nnnnnnnnn']]]]]]]]]))
print(stringWithVowelCount([['Anthony'],[4,[[[5,[[[6,'Bob']]]]]]]]))
print(stringWithVowelCount([[[[[[[[[10,20],'Carl']]]]]]]]))
print(stringWithVowelCount([[[[[[[[[]]]]]]]]]))
