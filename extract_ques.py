import numpy as np
import json
import sys



if __name__=="__main__":    
    data = []
    data1=[]
    array =[]
    q_file = sys.argv[1]
    with open(q_file) as f:
        for line in f:
            value = json.loads(line)
            data.append(value)
    value1 = value["questions"]
    i=0
    for row in value1:    
         value2 =value1[i]
         data1.append(value2[u'question'])
         i = i+1
    myarray = np.asarray(data1)
    np.savetxt('datasets/ques', myarray,fmt="%s")
    
    print "VQA dataset created! as ques at datasets/ques"
    
