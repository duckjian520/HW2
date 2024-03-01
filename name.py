import pandas as pd
import numpy as np
mydata = {
'a': [21, 32, 78]
}
print(pd.Series(mydata),"\n")

a=[12, 312, 323, 41]
print(pd.Series(a),"\n")

a= [2, 4, 6, 8, 10]
b= [1, 3, 5, 7, 9]
val1=pd.Series(a)
val2=pd.Series(b)
print(val1+val2, val2/val1, val1-val2, val1*val2, "\n")

print(val1==val2, "\n", val1<val2, "\n", val1>val2)

a={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print(pd.Series(a), "\n")

a=np.array([10, 20, 30, 40, 50])
print(pd.Series(a), "\n")


b=[100, 200, "python", 300.12, 400]
b1=pd.Series(b)
b1[2]=np.NaN
print(b1.astype(float), "\n")

data={
    'col1': [1, 2, 3, 4, 7, 11],
    'col2':[4,5,6,9,5,0],
    'col3':[7,5,8,12,1,11]

}
df=pd.DataFrame(data)
print(df['col1'],"\n")

S=[100,200,"python",300.12,400]
s1=pd.Series(S)
print(s1)
s2=np.array(s1)
print(s2,"\n",type(s2),"\n")

data={
'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]
}
print(pd.DataFrame(data),"\n")

exam_data = {
'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(exam_data,index=labels)
print(df,"\n")

print("Summary of the basic information about this DataFrame and its data:")
print(df.info(),"\n")

print("first three rows of the data frame: ","\n",df.head(3),"\n")

print("Select specific columns:","\n",df[['name','score']],"\n")

print("Select specific columns:","\n",df[['score','qualify']].loc[['b','d','f','g']],"\n")

print("Number of attempts in the examination is greater than 2:","\n",df[df['attempts']>2],"\n")

tr=len(df.axes[0])
tc=len(df.axes[1])
print("Number of the row: ", tr,"\n","Number of the columns: ",tc,"\n")

print("Rows where score is missing: ","\n",df[df['score'].isnull()],"\n")

print("Rows where score is between 15 and 20: ","\n",df[df['score'].between(15,20)])