def is_number(n):
    try:
        int(n)
    except ValueError:
        return False
    return True

def precision(tp, fp, fn):
    return tp/(tp+fp)

def Recall(tp,fp,fn):
    return tp/(tp+fn)

def f1_score(tp, fp, fn):
    pre = precision(tp,fp,fn)
    recall = Recall(tp,fp,fn)
    return 2*((pre*recall)/(pre+recall))


def evaluate_classification(tp, fp, fn):
    if (is_number(tp) != True):
        print('tp must be int')
    elif (is_number(fp) != True):
        print('fp must be int')
    elif (is_number(fn) != True):
        print('fn must be int')
    else:
        tp, fp, fn = int(tp), int(fp), int(fn)
        if (tp > 0 and fp > 0 and fn > 0):
            print("precision is " + str(precision(tp, fp, fn)))
            print("recall is " + str(Recall(tp, fp,fn)))
            print("f1-score is " + str(f1_score(tp,fp,fn)))
        else:
            print("tp and fp and fn must be greater than zero")
    
tp, fp, fn = input().split() 
print(evaluate_classification(tp, fp, fn))
