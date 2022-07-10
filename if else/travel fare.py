while True:
 import datetime

 time = (datetime.datetime.now())

 travel = int(input('''
  WHERE YOU WANT TO GO

  1 nagpur to pune
  2 aurangabad to pune
  3 mumbai to pune   

                 '''))

 type_adult = int(input('''
     type of passanger
    1 adult (above 21 yr)
    2 kid (between 10 to 21 year)
    3 handicap
    '''))
 seat = int(input('''
    which seat would you like to prefer
     1 window seat  #### you have to pay 50rs read write for window seat
     2 corner seat'''))
 no_seat = int(input('''
 how many do you want to book
 1. for 1 seat
 2. for 2 seat
 3. for 3 seat
 you can book max 3 seat at a time
 '''))

 time1 = int(input('''
  which time would you like to prefer
  1  8.00 pm departure
  2  9.00 pm departure
  3. 10.00 pm departure '''))
 boarding = input(" enter the boarding address")
 dropping = input(" enter the droppind address")
 print('''

              ''')
 if time1 == 1:
    print("your departure time is 8.00am")
 elif time1 == 2:
    print("your departure time is 8.00am")
 elif time1 == 3:
    print("your departure time is 8.00am")
 else:
     print("please enterd correct time")
 if travel == 1:
    if type_adult == 1:
      if no_seat<=3:
        if seat == 1:
            print(("your fare is 550 * {} = ").format(no_seat), 550 * no_seat)
        elif seat == 2:
            print(("your fare is 500 * {} = ").format(no_seat), 500 * no_seat)
        else:
            print("you entered invalid seat")
      else:
        print("you entered invalid no_seat")
    elif type_adult == 2:
        if no_seat<=3:
          if seat == 1:
            print(("your fare is 400 * {} = ").format(no_seat), 400 * no_seat)
          elif seat == 2:
            print(("your fare is 350 * {} = ").format(no_seat), 350 * no_seat)
          else:
              print("you entered invalid seat")
        else:
            print("you entered invalid no_seat")
    elif type_adult == 3:
        if no_seat<=3:
          if seat == 1:
            print(("your fare is 300 * {} = ").format(no_seat), 300 * no_seat)
          elif seat == 2:
            print(("your fare is 250 * {} = ").format(no_seat), 250 * no_seat)
          else:
              print("you entered invalid seat")
        else:
            print("you entered invalid no_seat")
    else:
        print("please select correct type_adult")
 elif travel == 2:
    if type_adult == 1:
      if no_seat<=3:
        if seat == 1:

            print(("your fare is 700 * {} = ").format(no_seat), 750 * no_seat)
        elif seat == 2:
            print(("your fare is 750 * {} = ").format(no_seat), 700 * no_seat)
        else:
            print("you entered invalid seat")
      else:
          print("you entered invalid no_seat")
    elif type_adult == 2:
        if no_seat<=3:
          if seat == 1:
            print(("your fare is 550 * {} = ").format(no_seat), 550 * no_seat)
          elif seat == 2:
            print(("your fare is 500 * {} = ").format(no_seat), 500 * no_seat)
          else:
              print("you entered invalid seat")
        else:
            print("you entered invalid no_seat")
    elif type_adult == 3:
        if no_seat<=3:
          if seat == 1:
            print(("your fare is 400 * {} = ").format(no_seat), 400 * no_seat)
          elif seat == 2:
            print(("your fare is 350 * {} = ").format(no_seat), 350 * no_seat)
          else:
              print("you entered invalid seat")
        else:
            print("you entered invalid no_seat")
    else:
        print("please select correct type_adult")
 elif travel == 3:
    if type_adult == 1:
        if no_seat<=3:
          if seat == 1:

            print(("your fare is 525 * {} = ").format(no_seat), 525 * no_seat)
          elif seat == 2:
            print(("your fare is 475 * {} = ").format(no_seat), 475 * no_seat)
          else:
              print("you entered invalid seat")
        else:
            print("you entered invalid no_seat")

    elif type_adult == 2:
        if no_seat<=3:
          if seat == 1:
            print(("your fare is 440 * {} = ").format(no_seat), 440 * no_seat)
          elif seat == 2:
            print(("your fare is 390 * {} = ").format(no_seat), 390 * no_seat)
          else:
              print("you entered invalid seat")
        else:
            print("you entered invalid no_seat")
    elif type_adult == 3:
        if no_seat<=3:
          if seat == 1:
            print(("your fare is 300 * {} = ").format(no_seat), 300 * no_seat)
          elif seat == 2:
            print(("your fare is 250 * {} = ").format(no_seat), 250 * no_seat)
          else:
              print("you entered invalid seat")
        else:
            print("you entered invalid no_seat")
    else:
        print("please select correct type_adult")
 else:
    print("please select correct travel")

 print("Date :- {:%d-%m-%Y %H:%M:%S}".format(time))
 print("your boarding address  :- ", boarding)
 print("your dropping address  :- ", dropping)
 print("your ticket has booked")
 print("thank you for using service")
 rebook=int(input('''do you want to book another seat
 1 yes
 2 no'''))
 if rebook==1:
     continue
 else:
     break