course={
         'python':{'duration':'2 month','fees':8000},
         'java':{'duration':'4 month','fees':10000},
         'c++':{'duration':'3 month','fees':6000},
      }
course['java']['fees']=20000

for a,b in course.items():
  print(a,b)
