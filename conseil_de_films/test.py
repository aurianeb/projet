def conv_list(chaine):
  length = len(chaine)
  L = []
  k=0
  while k<length:
    if str(chaine[k])=="-":
      k = k+1
    else :
      j = k
      while (j<length) and (not str(chaine[j])=="-"):
        j = j+1
      print(k)
      print(j)
      L.append(chaine[k:j])
      k=j
  return L

conv_list("bonj-test-a--765")
chaine="00-01"
#print(str(chaine[2])=="-")
