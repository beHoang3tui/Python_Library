set1 = {1,4,6,3,7,9}
set2 = {4,3,1,9}

def Kiem_tra(set1, set2):
  def Tim_kiem(set1, set2):
    return(set2-set1)
  set3 = Tim_kiem(set1, set2)
  if(len(set3)==0):
    print('Tập hợp set2 là con của tập hợp set1 ')
  else:
    print('Tập hợp set2 không là con của tập hợp set1 ')
  
Kiem_tra(set1, set2)
