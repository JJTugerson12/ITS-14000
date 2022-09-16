question = ""

while question != 'yes':
    print('Reboot The Computer and Try to Connect')
    question = (input('Problem Fixed?  :'))
    if question == 'no' :
        print('Reboot The Router and Try to Connect')
        
        question = (input('Problem Fixed?  :'))
        if question == 'no' :
            print('Make Sure Cables Between the Router and Modem are Properly Connected')

            question = (input('Problem Fixed?  :'))
            if question == 'no' :
                print('Move the Router to a New Location and Try to Connected')

                question = (input('Problem Fixed?  :'))
                if question == 'no' :
                    print('Get a New Router')
                    break