#
# from logging import *
# s='{asctime}s ** {name} ** {message}s ** {lineno}d'
# basicConfig(filename="logfile1.log",level=DEBUG,filemode='w',style='{',format=s)
#
# logger=getLogger("sanjay")
# logger.debug("this is debug")
# logger.info("this is info")
# logger.warning("this is warning")
# error("this is error")
# critical("this is critical")
#
#
# from logging import *
# basicConfig(filename="logfile2.log",level=DEBUG,format='%(asctime)s--%(message)s')
# num1=int(input("enter the value 1 :- "))
# num2=int(input("enter the value 2 :- "))
# sum_=num1+num2
# # debug(("addition of two no is {}").format(sum_))
# debug((f"addition of two no is {sum_}"))




from logging import *
basicConfig(filename="test.log",level=DEBUG,format="%(asctime)s--%(message)s",filemode='w')
num=10
num2=30
sum=num+num2
debug(f"(sum of {sum}) ")





















