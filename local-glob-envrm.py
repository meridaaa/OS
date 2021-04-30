# fixed and local
# p1 = ['A', 'B', 'C', 'A', 'W']
# p2 = ['E', 'O', 'A', 'H']
# q = [p1, p2]
memo = []
print("tedad process ha ra vared konid: ")
q=[]
for j in range(int(input())):
  p1=[]
  print("tedad process haye mored niaz:")
  for i in range(int(input())):
    p1.append(input("process haye morede niaz(char): "))
  q.append(p1)


def get_drive2(peocess, memo, l):
    for i in range(3):
        if not (chr(ord(peocess) + i) in memo):
            memo[l + i] = chr(ord(peocess) + i)
    return memo


def get_drive4(peocess, memo):
    for i in range(3):
        if not (chr(ord(peocess) + i in memo)):
            memo.append(chr(ord(peocess) + i))
def get_drive(peocess, memo):
     for i in range(3):
            memo.append(chr(ord(peocess) + i))
     memo.append(" ")
     memo.append(" ")
     memo.append(" ")
     return memo
def remove_memoo(memo ,l):
    memo[l] = " "
    memo[l + 1] = " "
    memo[l + 2] = " "
def remove_memo4( memo, l):
    memo[l] = " "
    memo[l + 1] = " "
    memo[l + 2] = " "
    memo[l + 3] = " "
    memo[l + 4] = " "
    memo[l + 5] = " "
    return memo
def remove_memo( memo, l):
    memo.insert(l, " ")
    memo.insert(l+1," ")
    memo.insert(l+2," ")
    memo.insert(l+3," ")
    memo.insert(l+4," ")
    memo.insert(l+5," ")
    return memo
def get_drive3(peocess, memo, l, parti):
      if len(memo) < parti:
          for i in range(parti - len(memo)+1):
            memo.insert(l+i, " ")
      for i in range(3):
          if not (chr(ord(peocess)+i in memo)):
             memo[l + i] = chr(ord(peocess)+i)
      return memo
def remove_memo2(memo, l):
    for i in range(3):
        memo[l+i] = " "
    return memo
def glob_var(q_process, memo):
    get_drive4(q_process[0][0], memo)
    page_f = 0
    for j in q_process:
        for k in j:
            if not (k in memo):
                page_f += 1
                get_drive4(k, memo)
    return memo

def fix_loc(q_process, memo):
    for i in range(2):
      if not(q_process[i][0] in memo):
        get_drive(q_process[i][0],memo)
      else:  remove_memo(memo, i*6)
    page_f = 0
    for j in q_process:
        indx = q_process.index(j)
        for u in range(2, len(q_process)):
           if j == q_process[u]:
            remove_memo4(memo, 0)
            if not (q_process[i][0] in memo):
                get_drive2(q_process[2][0], memo, 0)
        for k in j:
          for i in range(len(q_process)):
             if (k in memo):
                 break
             elif not (k in memo[i]):
                page_f += 1
                if q_process.index(j) > 1:
                    indx = q_process.index(j)-2
                if memo[indx * 6 + 3] == " ":
                    l = indx *6 + 3
                    get_drive2(k, memo, l)
                else:
                    l=q_process.index(j)*6
                    remove_memoo(memo, l)
                    get_drive2(k, memo, l)
                break
    return memo
def fix_glob(q_process, memo):
    parti = []
    for i in range(2):
     if not (q_process[i][0] in memo):
       get_drive(q_process[i][0], memo)
     else:  remove_memo(memo, i * 6)
    parti.append(6)
    parti.append(6)
    o=-1
    for j in q_process:
        o+=1
        page_f = 0
        c=0
        indx=q_process.index(j)
        if j == q_process[2:]:
            o=0
            remove_memo4(memo, 0)
            if not (q_process[i][0] in memo):
               get_drive2(q_process[2][0], memo, 0)
        for k in j:
            for i in range(len(q_process)):
             if (k in memo):
                c+=1
                if (c >= 3 and page_f == 0) or (c > 3 and page_f == 1):
                    if memo[q_process.index(j) * 6 + 3] == " " and memo[q_process.index(j) * 6 + 3 + 1] == " ":
                          if parti[o]-1 == 3:
                            memo.remove(" ")
                            parti[o] -= 1
                          elif parti[o]-2 >=3:
                            memo.remove(" ")
                            memo.remove(" ")
                            parti[o] -= 2
                    elif memo[q_process.index(j) * 6 + 3] == " " and memo[q_process.index(j) * 6 + 3 + 1] != " ":
                        if parti[o] - 1 == 3:
                            memo.remove(" ")
                            parti[o] -= 1
                        elif parti[o] - 2 >= 3:
                            memo.remove(" ")
                            memo.remove(j[0])
                            parti[o] -= 2
                    elif memo[q_process.index(j) * 6 + 3] != " " and memo[q_process.index(j) * 6 + 3 + 1] != " ":
                        if parti[o] - 1 == 3:
                            memo.remove(j[0])
                            parti[o] -= 1
                        elif parti[o] - 2 >= 3:
                            memo.remove(j[1])
                            memo.remove(j[0])
                            parti[o] -= 2
                break
             elif not (k in memo[i]):
                page_f += 1
                if o !=0:
                    l = parti[o-1]
                else: l = 0
                # if memo[3*o+3]==" ":
                #     l =3*o+3
                #     get_drive2(k, memo, l)
                if q_process.index(j) > 1:
                    indx = q_process.index(j)-2
                if memo[indx * parti[o - 1] + 3] != " ":
                    remove_memo2(memo, l)
                    if page_f > 2:
                        parti[o] += 2
                    get_drive3(k, memo, l, parti[o])
                elif memo[indx * parti[o-1] + 3] == " ":
                    l = indx * parti[o-1] + 3
                    get_drive2(k, memo, l)
                # else:
                #     remove_memo2(memo, l, parti[o])
                #     if page_f > 2:
                #       parti[o] += 2
                #     get_drive3(k, memo, l, parti[o])o
                break
    return memo

print("Baraye estefade az ravesh Local va fix '0', \n"
      "Baraye estefade az ravesh Global va Varibale '1', \n"
      "Baraye estefade az ravesh  Gobal va fix '2' ra vared konid.")
kodam = int(input())
if kodam == 0:
    print(fix_loc(q, memo))
if kodam == 1:
    print(glob_var(q, memo))
if kodam == 2:
    print(fix_glob(q, memo))