from read import *
from rapidfuzz import *
def fuzzy_query(input_str):
    my_index=scenic_dict
    scenic_title=[]
    for k,v in my_index.items():
        scenic_title.append(v)  #scenic_title存储景点名称的列表
    result=process.extract(input_str, scenic_title,scorer=fuzz.ratio,score_cutoff=20)#相似度阈值设为20%
    if result[0][1]>=90:#如果有高度相似的结果（>=90%）,则只输出这条结果
       result=list(result[0])
    return result
if __name__=="__main__":
    input_str=input()
    print(fuzzy_query(input_str))

