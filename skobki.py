#scobka_length = len(scobka)
s=list(input("Введите сюда скобки чтобы проверить их. "))
st=[]
for i in range(len(s)):
    if s[i]=='(' or s[i]=='{' or s[i]=='[':
        st.append(s[i])
        continue
    if (s[i]==')' or s[i]=='}' or s[i]==']') and st:
        if (st[-1]+s[i]=='()') or (st[-1]+s[i]=='{}') or (st[-1]+s[i]=='[]'):
            st.pop()
        else:
            print('Никак нет')
            exit()
    else:
        print('Нет')
        exit()
if st==[]:
    print('Всё правильно')
else:
    print('Не пойдет')
#print(scobka_length)
#print(scobka)
