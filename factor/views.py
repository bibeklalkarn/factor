from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import numpy as np

def index(request):
    template = loader.get_template('index.html')
    N = int(request.POST.get('N', '1'))
    t = int(request.POST.get('t','1'))
    n = int(request.POST.get('n', '0'))

    expns = []
    for j in range(N,t+1):
        d = j
        k=[]
        m=[]

        for i in range(1,d+1):
            if d%i==0:
                k.append(i)
            c = 0
            a = k
            np.random.shuffle(a)

            for i in k:
                if [int(i),int(a[c]+d/a[c]),int(a[c]-d/a[c]), int(-a[c]+d/a[c]), int(d/i) ] in m:
                    continue
                else:
                    if i == 1:
                        # print('x^2 + {}x + {} '.format(int(a[c]+d/a[c]),int(d/i)))
                        expns.append('x^2 + {}x + {} '.format(int(a[c]+d/a[c]),int(d/i)))
                        if a[c]-d/a[c] > 0:
                            # print('x^2 + {}x - {} '.format(int(a[c]-d/a[c]),int(d/i)))
                            expns.append('x^2 + {}x - {} '.format(int(a[c]-d/a[c]),int(d/i)))
                        elif a[c]-d/a[c] < 0:
                            # print('x^2 - {}x - {} '.format(int(-a[c]+d/a[c]),int(d/i)))
                            expns.append('x^2 - {}x - {} '.format(int(-a[c]+d/a[c]),int(d/i)))
                        else:
                            # print('x^2 - {} '.format(int(d/i)))
                            expns.append('x^2 - {} '.format(int(d/i)))
                        # print('x^2 - {}x + {} '.format(int(a[c]+d/a[c]),int(d/i)))
                        expns.append('x^2 - {}x + {} '.format(int(a[c]+d/a[c]),int(d/i)))
                    else:
                        # print('{}x^2 + {}x + {} '.format(int(i),int(a[c]+d/a[c]),int(d/i)))
                        expns.append('{}x^2 + {}x + {} '.format(int(i),int(a[c]+d/a[c]),int(d/i)))
                        if a[c]-d/a[c] > 0:
                            # print('{}x^2 + {}x - {} '.format(int(i),int(a[c]-d/a[c]),int(d/i)))
                            expns.append('{}x^2 + {}x - {} '.format(int(i),int(a[c]-d/a[c]),int(d/i)))
                        elif a[c]-d/a[c] < 0:
                            # print('{}x^2 - {}x - {} '.format(int(i),int(-a[c]+d/a[c]),int(d/i)))
                            expns.append('{}x^2 - {}x - {} '.format(int(i),int(-a[c]+d/a[c]),int(d/i)))
                        else:
                            # print('{}x^2 - {} '.format(int(i),int(d/i)))
                            expns.append('{}x^2 - {} '.format(int(i),int(d/i)))


                            # print('{}x^2 - {}x + {} '.format(int(i),int(a[c]+d/a[c]),int(d/i)))
                            expns.append('{}x^2 - {}x + {} '.format(int(i),int(a[c]+d/a[c]),int(d/i)))
                    m.append([int(i),int(a[c]+d/a[c]),int(a[c]-d/a[c]), int(-a[c]+d/a[c]), int(d/i) ])

                    c+=1
    np.random.shuffle(expns)
    list_n = expns[:n]
    context = {}
    pl = []
    for i in range(len(list_n)):
        pl.append({"vals":list_n[i]})
        
    context = {"values": pl}
        
        
    # for i in range(n):
    #     print(str(expns[i]))    
    
    print(context)
    # return render(request, 'index.html', {'list':list_n})
    return HttpResponse(template.render(context, request))

# def factor_combi(request):
#     N = int(request.POST.get('N'))
#     t = int(request.POST.get('t'))
#     n = int(request.POST.get('n'))
#     for i in range(5):
#         print(N*2)
#     expns = []
#     for j in range(N,t+1):
#         d = j
#         k=[]
#         m=[]

#         for i in range(1,d+1):
#             if d%i==0:
#                 k.append(i)
#             c = 0
#             a = k
#             np.random.shuffle(a)

#             for i in k:
#                 if [int(i),int(a[c]+d/a[c]),int(a[c]-d/a[c]), int(-a[c]+d/a[c]), int(d/i) ] in m:
#                     continue
#                 else:
#                     if i == 1:
#                         # print('x^2 + {}x + {}\\\\'.format(int(a[c]+d/a[c]),int(d/i)))
#                         expns.append('x^2 + {}x + {}\\\\'.format(int(a[c]+d/a[c]),int(d/i)))
#                         if a[c]-d/a[c] > 0:
#                             # print('x^2 + {}x - {}\\\\'.format(int(a[c]-d/a[c]),int(d/i)))
#                             expns.append('x^2 + {}x - {}\\\\'.format(int(a[c]-d/a[c]),int(d/i)))
#                         elif a[c]-d/a[c] < 0:
#                             # print('x^2 - {}x - {}\\\\'.format(int(-a[c]+d/a[c]),int(d/i)))
#                             expns.append('x^2 - {}x - {}\\\\'.format(int(-a[c]+d/a[c]),int(d/i)))
#                         else:
#                             # print('x^2 - {}\\\\'.format(int(d/i)))
#                             expns.append('x^2 - {}\\\\'.format(int(d/i)))
#                         # print('x^2 - {}x + {}\\\\'.format(int(a[c]+d/a[c]),int(d/i)))
#                         expns.append('x^2 - {}x + {}\\\\'.format(int(a[c]+d/a[c]),int(d/i)))
#                     else:
#                         # print('{}x^2 + {}x + {}\\\\'.format(int(i),int(a[c]+d/a[c]),int(d/i)))
#                         expns.append('{}x^2 + {}x + {}\\\\'.format(int(i),int(a[c]+d/a[c]),int(d/i)))
#                         if a[c]-d/a[c] > 0:
#                             # print('{}x^2 + {}x - {}\\\\'.format(int(i),int(a[c]-d/a[c]),int(d/i)))
#                             expns.append('{}x^2 + {}x - {}\\\\'.format(int(i),int(a[c]-d/a[c]),int(d/i)))
#                         elif a[c]-d/a[c] < 0:
#                             # print('{}x^2 - {}x - {}\\\\'.format(int(i),int(-a[c]+d/a[c]),int(d/i)))
#                             expns.append('{}x^2 - {}x - {}\\\\'.format(int(i),int(-a[c]+d/a[c]),int(d/i)))
#                         else:
#                             # print('{}x^2 - {}\\\\'.format(int(i),int(d/i)))
#                             expns.append('{}x^2 - {}\\\\'.format(int(i),int(d/i)))


#                             # print('{}x^2 - {}x + {}\\\\'.format(int(i),int(a[c]+d/a[c]),int(d/i)))
#                             expns.append('{}x^2 - {}x + {}\\\\'.format(int(i),int(a[c]+d/a[c]),int(d/i)))
#                     m.append([int(i),int(a[c]+d/a[c]),int(a[c]-d/a[c]), int(-a[c]+d/a[c]), int(d/i) ])

#                     c+=1
#     np.random.shuffle(expns)
#     for i in range(n):
#         print(str(expns[i]))
#     # return render(request, 'index.html')
#     return HttpResponse(template.render(context, request))
    