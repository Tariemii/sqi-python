"""
create a ussd code compiler for purchase of data plan
if i press 1 create what is there (*312#)
it should show daily, weekly and monthly 
until it shows that you have purchased data
"""
code = input('Enter your code:')
if code == '*321#':
    operations = input ("""1.Data plans\n2.Enjoy 3Gb for N1000\n3.Social Bundles\n4.Business Plans\n5.Roaming/Int'l\n6.Borrow Credit/Recharge\n7.Gift Data\n8.Video Packs\n""")
    if operations == '1':
        dataplans = input("""1.Daily\n2.Weekly\n3.Monthly\n4.2-3Month\n5.Always ON\n6.Broadband\n""")
        if dataplans == '1':
            daily = input("""1.N50 for 40mb\n2.N100 for 100mb\n3.N100 for 350mb\n4.N200 for 200mb\n5.N300 for 1GB\n""")
            if daily == '1' or daily == '2' or daily == '3':
                  daily_plans = input("""
You will be charged for this data purchase. To proceed, select:
1. Auto-Renew\n2.One-off\n3.Buy for a Friend\n4. Redeem Promo Code\n 0.Back 
               """)
                  if daily_plans == '1' or daily_plans == '2' or daily_plans == '3' or daily_plans == '4':
                        print('You have successfully purchased data')
        elif dataplans == '2':
            weekly = input("""1.N300 for 350mb\n2.N200 for 1GB\n3.N500 for 1.5GB\n4.N500 for 740mb\n5.N500 for 1GB\n""")         
            if weekly == '1' or weekly == '2' or weekly == '3':
                 daily_plans = input("""
You will be charged for this data purchase. To proceed, select:
1. Auto-Renew\n2.One-off\n3.Buy for a Friend\n4. Redeem Promo Code\n 0.Back 
               """)
                 if daily_plans == '1' or daily_plans == '2' or daily_plans == '3' or daily_plans == '4':
                        print('You have successfully purchased data')
        elif dataplans == '3':
             monthly= input("""1.1000 for 1.5GB\n2.N1200 for 2GB\n3.N1500 for 3GB\n4.N2000 for 4.5GB\n5.N2500 for 6GB""")     
             if monthly == '1'or monthly == '2' or monthly == '3':
                 daily_plans = input("""
You will be charged for this data purchase. To proceed, select:
1. Auto-Renew\n 2.One-off\n 3.Buy for a Friend\n 4. Redeem Promo Code\n 0.Back 
               """)
                 if daily_plans == '1' or daily_plans == '2' or daily_plans == '3' or daily_plans == '4':
                        print('You have successfully purchased data')
else:
    print('invalid')