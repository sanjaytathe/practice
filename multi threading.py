from threading import *
def show():
        for i in range(5):
            print("hii..")
t1=Thread(target=show)
t1.start()
for i in range(5):
    print("bye....")



# from threading import *
# def twice(num):
#     for i in num:
#         print(2*i)
# def display(num):
#     for x in num:
#         print(x*x)
# num=[1,2,3,4,5]
# t1=Thread(target=twice,args=(num,))
# t2=Thread(target=display,args=(num,))
# t1.start()
# t1.join()
# t2.start()


# from threading import *
# def disp(a,b):
#     print("thread running",a,b)
# for i in range(5):
#     t=Thread(target=disp,args=(10,20))
#     t.start()

#
# from threading import *
# # a=Lock()
# def show(num):
#     # a.acquire()
#     for i in range(5):
#         print(i)
#     # a.release()
# t1=Thread(target=show,args=(1,))
# t2=Thread(target=show,args=(2,))
# t3=Thread(target=show,args=(3,))
# t1.start()
# t2.start()
# t3.start()

