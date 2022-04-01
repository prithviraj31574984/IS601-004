import math
import statistics
import scipy.stats as stat
import pandas as pd
from statistics import variance
import numpy as np
from statistics import stdev

while True:
    print('Are you Ready (yes/no)')
    ch1=input()
    if ch1=='yes' or ch1=='YES':
        print('1.Square')
        print('2.Square Root')
        while True:
            print('3.Pick 5 from below')
            print('a.Population Mean')
            print('b.Median')
            print('c.Mode')
            print('d.Population standard Deviation')
            print('e.variance of Population proportion')
            print('f.Z-Score')
            print('g.Standized score')
            print('h.Population correlation coefficient')
            print('i.Confidence Interval')
            print('j.Population variance')
            print('k.P Value')
            print('l.proportion')
            print('m.Sample mean')
            print('n.Sample Standard Deviation')
            print('o.Variance of Sample proportion')
            ch=int(input("enter the choice:"))
            if ch==1:
                n=int(input('enter the number:'))
                print('Square of the number is',n*n)

            elif ch==2:
                n=int(input('enter the number:'))
                print('the Square root of the number is {0}'.format(math.sqrt(n)))

            elif ch==3:
                ch2=input("enter the choice:")

                if ch2=='a':
                    n=(input('enter the numbers: '))
                    v=n.split(' ')
                    sum=0
                    for e in v:
                        sum=sum+int(e)
                    print("The Population Mean is {0}".format(sum/len(v)))

                elif ch2=='b':
                    n=list(map(int, input('Enter numbers: ').split()))
                    print('the medain of the numbers is {0}'.format(statistics.median(n)))

                elif ch2=='c':
                    n=list(map(int, input('Enter numbers: ').split()))
                    print("the mode of the given numbers is {0}".format(statistics.mode(n)))

                elif ch2=='d':
                    n=list(map(int, input('Enter numbers: ').split()))
                    print('The Population standard deviation is {0}'.format(statistics.stdev(n)))

                elif ch2=='e':
                    n=list(map(int, input('Enter numbers: ').split()))
                    print('The variance of Population proportion is {0}'.format(statistics.variance(v)))

                elif ch2=='f':
                    n=list(map(int, input('Enter numbers: ').split()))
                    print('The Z score is {0}'.format(stat.zscore(n)))

            #elif ch=='g':


                elif ch2=='h':
                    n=input('enter the numbers a scomma separated:')
                    df=pd.read_csv(n)
                    print("the population correlation coefficient is {0}".format(df.corr()))

                elif ch2=='i':
                    n=list(map(int, input('Enter numbers: ').split()))
                    print(stat.t.interval(alpha=0.99,df=len(n)-1,loc=np.mean(n), scale=stat.sem(n)))

                elif ch2=='j':
                    n=list(map(int, input('Enter numbers: ').split()))
                    print('The population variance is {0}'.format(variance(n)))

                elif ch2=='k':
                    p_value = stat.norm.sf(abs(-0.67))
                    print('p value is : ' + str(p_value))

                elif ch=='m':
                    n=list(map(int, input('Enter numbers: ').split()))
                    print("the sample mean is {0}".format(statistics.mean(n)))

                elif ch2=='n':
                    n=list(map(int, input('Enter numbers: ').split()))
                    print(stdev(n))

                elif ch2=='o':
                    n=list(map(int, input('Enter numbers: ').split()))
                    print("Variance of sample set is {0}".format(statistics.variance(n)))

                else:
                    break

        else:
            break
