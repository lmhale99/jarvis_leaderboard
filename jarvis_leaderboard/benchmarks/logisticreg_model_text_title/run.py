from chemnlp.classification.scikit_class import sk_class
import time
t1=time.time()
sk_class(   csv_path='/wrk/knc6/AtomNLP/Summarize/pubchem.csv',key='label_name',value='title')
#sk_class(   csv_path='/wrk/knc6/AtomNLP/Summarize/cond_mat.csv',key='categories',value='title')
t2=time.time()
print ('Time',t2-t1)
