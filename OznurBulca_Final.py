# we can use PySimpleGUI to create GUI applications
import PySimpleGUI as sg      
import sqlite3
# layout is a list of GUI elements
# Text: to show information to the user
# Input: to get text input from user
# Button: to trigger functionality
con = sqlite3.connect('armut.db')
cur = con.cursor()
email=[]
password=[]
alldata=[]
allids=[]
for row in cur.execute('SELECT ID, Email, Name, Surname,Password,Phone FROM User'):
    alldata.append(row)
    allids.append(row[0])
    email.append(row[1])
    password.append(row[4])
cids=[]
for row in cur.execute('SELECT CID FROM Customer'):
    cids.append(row[0])
pids=[]
for row in cur.execute('SELECT PID FROM Provider'):
    pids.append(row[0])
aids=[]
for row in cur.execute('SELECT AID FROM Admin'):
    aids.append(row[0])
Services=[] 
count=0
for row in cur.execute('SELECT SID,SName, Price,Category,Description FROM Services'):
    Services.append(row)
    
    
# for row in cur.execute('SELECT CID, CompanyName FROM Company'):
#     companies.append((row[0],row[1]))
def startpage():
    layout = [[sg.Text('Welcome to the Service Provider System. Please enter your information')],[sg.Text('E-Mail:')], [sg.Input(key='email_input')],
              [sg.Text('Password:')], [sg.Input(key='password_input')],
              [sg.Button('Login')]]
    window = sg.Window('Service Provider System', layout)      
    event, values = window.read()
    window.close()
    return (window,event,values)
    
def providerpage(window,ind):
    layout = [[sg.Text('Hello, Please choose your work'+'\t'+str(alldata[ind][2]))],
              [sg.Button('Register')],
              [sg.Button('Applications')],
              [sg.Button('Customers')],
              [sg.Button('Log out')]]  
    window = sg.Window('Service Provider System ', layout)      
    event, values = window.read()
    window.close()
    # sg.popup('Welcome'+'\t'+str(alldata[ind][2]))
    return (window,event,values)
def bookingaceptance(pid):
    booking=[]
    con = sqlite3.connect('armut.db')
    cur = con.cursor()
    for row in cur.execute('SELECT BID, Date, CID, SID, PID, Status FROM completeBooking WHERE PID=?',(pid,) ):
        booking.append(row)
    con.commit()
    con.close()
    layout = [[sg.Text('Choose a booking to edit!:')],
          [sg.Listbox(booking, size=(100, len(booking)), key='booking')],
          [sg.Button('Confirm')],[sg.Button('Redject')],[sg.Button('Exit')]]
    window = sg.Window('Customer Bookings', layout) 
    event, values = window.read()     
    window.close()
    return (window, event, values)
# def editbooks(bookdata):
#     Status=['Rejected', 'Confirmed']
#     layout = [[sg.Text('Review the provider')],[sg.Text('Rating:')] ,[sg.Combo(Status, size=(15, len(Status)), key='status')],
#               [sg.Button('Save')]]
#     window = sg.Window('Service Provider System', layout)   
#     # con = sqlite3.connect('armut.db')
#     # cur = con.cursor()
#     # cur.execute('SELECT MAX(RID) FROM completeReview')
#     # new_id = cur.fetchone()[0] + 1
#     # con.commit()
#     # con.close()
#     event, values = window.read()
#     window.close()
    # return (window,event,values)
    # cons = sqlite3.connect('armut.db')
    # curs = cons.cursor()
    # curs.execute('UPDATE Offer SET OfferStatus=? WHERE PID=?', ('Approved',wind[2]['application'][0][7]))
    # cons.commit()
    # cons.close()
def editbookpage(data):
    layout = [
    [sg.Text('Edit Booking:')],
    [sg.Checkbox('Completed', key='completed'), sg.Text(data['all_bookings'])],
    [sg.Button('Save')],
    [sg.Button('Exit')]]
    window = sg.Window('Service Provider System', layout)      
    event, values = window.read()
    window.close()
    return (window,event,values)
def custombookinghistory(cid):
    custombookings=[]
    # confirmedbookings=[]
    con = sqlite3.connect('armut.db')
    cur = con.cursor()
    # cur.execute('SELECT MAX(BID) FROM completeBooking')
    # new_id = cur.fetchone()[0] + 1
    for row in cur.execute('SELECT BID, Date, CID, SID, PID, Status FROM completeBooking WHERE CID=?',(cid,) ):
        custombookings.append(row)
    # for row in cur.execute('SELECT BID, Date, CID, SID, PID, Status FROM completeBooking WHERE CID=? AND Status=?',(cid,'Confirmed') ):
    #     confirmedbookings.append(row)
    con.commit()
    con.close()
    
    # layout = [[sg.Text('Booking History:')],
    #       [sg.Listbox(custombookings, size=(100, len(custombookings)), key='custombookings')],
    #       [sg.Checkbox('Completed', key='compeleted')],
    #       [sg.Button('Review')],
    #       [sg.Button('Exit')]]
    layout = [
    [sg.Text('Booking History:')],
    [sg.Listbox(custombookings, size=(50, len(custombookings)), key='all_bookings')],
    [sg.Button('Edit')],
    [sg.Button('Review')],
    [sg.Button('Exit')]
    ]
    # con = sqlite3.connect('armut.db')
    # cur = con.cursor()
    
    # con.commit()
    # con.close()
    # for booking in custombookings:
    #     layout.append([sg.Checkbox('Completed', size=(100,1), key='completed'), sg.Text(booking)])
   
    # Add each confirmed booking with a parallel checkbox
    # for booking in confirmedbookings:
    #     layout.append([sg.Checkbox('Completed', size=(100,1), key='completed'), sg.Text(booking, key='booking')])
    # for booking in custombookings:
    #     if booking not in confirmedbookings:
    #         layout.append([sg.Text(booking, size=(100,1))])
    
    # sg.Listbox(custombookings, size=(100, len(custombookings)), key='application')
    
    # for booking in confirmedbookings:
    #     layout.append([sg.Checkbox('Completed', size=(100,1), key='completed'), sg.Text(booking, key='booking')])
    # for booking in custombookings:
    #     if booking not in confirmedbookings:
    #         layout.append([sg.Text(booking, size=(100,1))])
    
    # layout += [
    #     [sg.Button('Review')],
    #     [sg.Button('Exit')]
    # ]
    
    window = sg.Window('Application information', layout) 
    event, values = window.read()     
    window.close()
    return (window, event, values)
def applicationspage(pid):
    aplications=[]
    con = sqlite3.connect('armut.db')
    cur = con.cursor()
    for row in cur.execute('SELECT ID, Email, Name, Surname,Password, Phone,SID, OfferStatus FROM Offer, User, Provider WHERE Provider.PID=User.ID AND Offer.PID=User.ID AND Provider.PID=?',(pid,) ):
        aplications.append(row)
    con.commit()
    con.close()
    layout = [[sg.Text('Choose Available Services:')],
          [sg.Listbox(aplications, size=(100, len(aplications)), key='application')],
          [sg.Button('Ok')]]
    window = sg.Window('Application information', layout) 
    event, values = window.read()     
    window.close()
    return (window, event, values)
def adminpage(window,ind):
    layout = [[sg.Text('Hello, Please choose your work'+'\t'+str(alldata[ind][2]))],
              [sg.Button('Services')],[sg.Button('Providers')]]  
    window = sg.Window('Service Provider System ', layout)      
    event, values = window.read()
    window.close()
    # sg.popup('Welcome'+'\t'+str(alldata[ind][2]))
    return (window,event,values)
def providertransaction():
    layout = [[sg.Text('Hello, Please choose!')],
              [sg.Button('Confirmed Providers')],[sg.Button('Redjected Providers')],[sg.Button('Pending Providers')]]  
    window = sg.Window('Service Provider System ', layout)      
    event, values = window.read()
    window.close()
    # sg.popup('Welcome'+'\t'+str(alldata[ind][2]))
    return (window,event,values)

def redjectedprovider():
    redject=[]
    con = sqlite3.connect('armut.db')
    cur = con.cursor()
    for row in cur.execute('SELECT DISTINCT Offer.PID, Name, Surname FROM Offer, User, Provider,completeReview WHERE Provider.PID=User.ID AND Offer.PID=User.ID AND OfferStatus=?',('Redjected',)):
        redject.append(row)
    con.commit()
    con.close()
    layout = [[sg.Text('Confirmed Providers:')],
          [sg.Listbox(redject, size=(100, len(redject)), key='confirmed')],
          [sg.Button('Exit')]]
       
    window = sg.Window('Application information', layout) 
    event, values = window.read()     
    window.close()
    return (window, event, values)


def confirmedprovider():
    confirm=[]
    con = sqlite3.connect('armut.db')
    cur = con.cursor()
    for row in cur.execute('SELECT DISTINCT  Offer.PID, User.Name, User.Surname, (SELECT AVG(Rating) FROM completeReview WHERE PID = Offer.PID) AS avg_rating FROM Offer, User,Provider, completeReview WHERE Provider.PID = User.ID AND Offer.PID = User.ID AND OfferStatus = ?',('Approved',)):
        confirm.append(row)
    con.commit()
    con.close()
    layout = [[sg.Text('Confirmed Providers:')],
          [sg.Listbox(confirm, size=(100, len(confirm)), key='confirmed')],
          [sg.Button('Approve')], [sg.Button('Redject')], [sg.Button('Ok')]]
       
    window = sg.Window('Application information', layout) 
    event, values = window.read()     
    window.close()
    return (window, event, values)
# def rejectedprovider():
#     redject=[]
#     con = sqlite3.connect('armut.db')
#     cur = con.cursor()
#     for row in cur.execute('SELECT ID, Email, Name, Surname,Password, Phone,SID,Offer.PID, OfferStatus FROM Offer, User, Provider WHERE Provider.PID=User.ID AND Offer.PID=User.ID AND OfferStatus=?',('Redjected',) ):
#         redject.append(row)
#     con.commit()
#     con.close()
    
def customerpage(window,ind):
    layout = [[sg.Text('Hello, Please choose your work'+'\t'+str(alldata[ind][2]))],
              [sg.Button('Services')],
              [sg.Button('Cart')],
              [sg.Button('Bookings')],
              [sg.Button('Log out')]]  
    window = sg.Window('Service Provider System', layout)      
    event, values = window.read()
    window.close()
    # sg.popup('Welcome'+'\t'+str(alldata[ind][2]))
    return (window,event,values)
def reviewpage(data):
    rate=[0,1,2,3,4,5,6,7,8,9,10]
    layout = [[sg.Text('Review the provider')],[sg.Text('Rating:')] ,[sg.Combo(rate, size=(5, len(rate)), key='rate')],
              [sg.Text('Comment:')], [sg.Input(key='comment', size=(70, 70))],
              [sg.Button('Save')]]
    window = sg.Window('Service Provider System', layout)   
    # con = sqlite3.connect('armut.db')
    # cur = con.cursor()
    # cur.execute('SELECT MAX(RID) FROM completeReview')
    # new_id = cur.fetchone()[0] + 1
    # con.commit()
    # con.close()
    event, values = window.read()
    window.close()
    return (window,event,values)
def servicespage():
    layout = [[sg.Text('Hello, Please choose your work')],
              [sg.Button('Add')],[sg.Button('Info')] ,[sg.Button('Log out')]]  
    window = sg.Window('Service Provider System', layout) 
    event, values = window.read() 
    window.close()      
    return (window,event)
    
# def providerspage():
#     layout = [[sg.Text('Hello')],[sg.Button('Services')]]
#     window = sg.Window('Welcome to the Service Provider System. Please enter your information', layout)  
#     event, values = window.read()
#     return window

def addspage():
    
    layout = [[sg.Text('SID:', size=(15,1)), sg.Input(key='name', size=(15,1))],
          [sg.Text('SName:', size=(15,1)), sg.Input(key='surname',size=(15,1))],
          [sg.Text('Price:', size=(15,1)), sg.Input(key='price', size=(15,1))],
          [sg.Text('Category:', size=(15,1)), sg.Input(key='category', size=(15, 3))],
          [sg.Text('Description:', size=(15,1)), sg.Input(key='description', size=(15, 3))],
          [sg.Button('Insert')]]
    window = sg.Window('Service Provider System', layout) 
    event, values = window.read() 
    parameters = (values['name'],values['surname'],values['price'],values['category'],values['description'])
    var=True
    while var:
                # check for not null constraint
        if parameters[0] == '':
            sg.popup('Name cannot be empty!')
            event, values = window.read() 
            parameters = (values['name'],values['surname'],values['price'],values['category'],values['description'])
        elif not parameters[0].isnumeric():
            # given credit is not empty, check for correct type
            sg.popup('SID should be numeric!')
            event, values = window.read() 
            parameters = (values['name'],values['surname'],values['price'],values['category'],values['description'])
        elif not parameters[2].isnumeric():
            # given credit is not empty, check for correct type
            sg.popup('Price should be numeric!')
            event, values = window.read() 
            parameters = (values['name'],values['surname'],values['price'],values['category'],values['description'])
       
        else:
            var= False
            con = sqlite3.connect('armut.db')
            cur = con.cursor()
            cur.execute('INSERT INTO Services VALUES(?,?,?,?,?)', parameters)
            con.commit()
            con.close()
            # show success message
            sg.popup(parameters[1]+'  successfully inserted! '   )
            # window.close()
            
    return (window, event, values)

def registerpage(Services):
    S1=[]
    S2=[]
    for row in Services:
        S1.append(row)
        S2.append(row[1])
    layout = [
          [sg.Text('Name:', size=(15,1)), sg.Input(key='name',size=(15,1))],
          [sg.Text('Surname:', size=(15,1)), sg.Input(key='surname', size=(15,1))],
          [sg.Text('Email:', size=(15,1)), sg.Input(key='email', size=(15, 3))],
          [sg.Text('Password:', size=(15,1)), sg.Input(key='password', size=(15, 3))],
          [sg.Text('Phone number:', size=(15,1)), sg.Input(key='phone', size=(15, 3))],
          [sg.Text('Offered Services:')],[sg.Combo(S2, size=(25, 7), key='chosen_service')],
          # Servis seçilebilir bir şey window çıksın text değil servicein idsini çekmek lazım
          [sg.Button('Insert')]]
    window = sg.Window('Service Provider System', layout) 
    event, values = window.read() 
    var=True
    while var:
                # check for not null constraint
        if event==sg.WIN_CLOSED :
            return (window, event, values)
             # break  
        elif values['name'] == '':
            sg.popup('Name cannot be empty!')
            event, values = window.read() 
            
        elif values['surname'] == '':
                sg.popup('Surname cannot be empty!')
                event, values = window.read() 
        elif values['email'] == '':
                sg.popup('email cannot be empty!')
                event, values = window.read()
        elif values['password'] == '':
                sg.popup('Surname cannot be empty!')
                event, values = window.read()
        elif values['phone'] == '':
                sg.popup('phone cannot be empty!')
                event, values = window.read()
        elif values['chosen_service'] == '':
                sg.popup('Service cannot be empty!')
                event, values = window.read()
        
        else:
            event, values = window.read()
            var= False
    
            
    # return (window, event, values)
    chosen_sid=0
    window.close()
    for i in S2:
        # print(str(i)+'\t'+str(type(i))+'\t'+str(S1[0])+'\t'+str(type(S1[0])))
        if i== values['chosen_service'] :
           
            break
        else:
            chosen_sid+=1
            
            
    parameters = (values['name'],values['surname'],values['email'],values['password'],values['phone'],values['chosen_service'], S1[chosen_sid][0])
    
    return (window, event, values,parameters)
def infopage(Services):
    lengt=len(Services)
    choices=[]
    for i in range (0,lengt):
            choices.append((Services[i][0],Services[i][1]),)
    layout = [[sg.Text('Choose Available Services:')],
          [sg.Listbox(choices, size=(30, len(choices)), key='chosen_service')],
          [sg.Button('Ok')]]
    
    
    window = sg.Window('Service information', layout) 
    event, values = window.read()     
    window.close()
    return (window, event, values)
def getdata(sid,services):
    def edit():
        layout = [[sg.Text('SID:', size=(15,1)), sg.Input(key='name', size=(15,1))],
              [sg.Text('SName:', size=(15,1)), sg.Input(key='surname',size=(15,1))],
              [sg.Text('Price:', size=(15,1)), sg.Input(key='price', size=(15,1))],
              [sg.Text('Category:', size=(15,1)), sg.Input(key='category', size=(15, 3))],
              [sg.Text('Description:', size=(15,1)), sg.Input(key='description', size=(15, 3))],
              [sg.Button('Save')]]
        window = sg.Window('Welcome to the Service Provider System. Please enter your information', layout) 
        event, values = window.read() 
        parameters = (values['name'],values['surname'],values['price'],values['category'],values['description'])
        var=True
        while var:
            
            if parameters[0] == '':
                sg.popup('Name cannot be empty!')
                event, values = window.read() 
                parameters = (values['name'],values['surname'],values['price'],values['category'],values['description'])
            elif not parameters[0].isnumeric():
                # given credit is not empty, check for correct type
                sg.popup('SID should be numeric!')
                event, values = window.read() 
                parameters = (values['name'],values['surname'],values['price'],values['category'],values['description'])
            elif not parameters[2].isnumeric():
                # given credit is not empty, check for correct type
                sg.popup('Price should be numeric!')
                event, values = window.read() 
                parameters = (values['name'],values['surname'],values['price'],values['category'],values['description'])
            
            else:
                parameters=parameters+(int(sid),)
                var= False
        return (event, window,parameters)

                    
    inner_index = None
    for i in range(len(services)):
        for j in range(0,5):
            if services[i][j]==sid:
                inner_index=i
            else:
                pass
    # if inner_index==None:
        
                
    layout = [[sg.Text('SID:'+'\t '+str(services[inner_index][0]))],
          [sg.Text('SName:'+'\t'+str(services[inner_index][1]))],
          [sg.Text('Price:'+'\t '+str(services[inner_index][2]))],
          [sg.Text('Category:'+'\t '+str(services[inner_index][3]))],
          [sg.Text('Description:'+'\t '+str(services[inner_index][4]))],
          [sg.Button('Edit')],[sg.Button('Delete')]]
    window = sg.Window('Welcome to the Service Provider System. Please enter your information', layout) 
    event, values = window.read() 
    if event=='Edit':
        window.close()
        event2= edit()
        if event2[0]=='Save':
            parameters=event2[2]
            cur.execute('UPDATE Services SET SID=?, SName=?, Price=?, Category=?, Description=? WHERE SID=?', parameters)
            con.commit()
            con.close()
            event2[1].close()
            # wind2=infopage(services)
        # window = sg.Window('Welcome to the Service Provider System. Please enter your information', layout) 
        # event, values = window.read() 
    elif event=='Delete':
        cons = sqlite3.connect('armut.db')
        curs = cons.cursor()
        curs.execute('DELETE FROM Services WHERE SID=?',(int(services[inner_index][0]),))
        cons.commit()
        cons.close()
        window.close()
        # dwind=infopage(Services)
    else:
        pass
    
    return window

def provider_approval():
    aplications=[]
    con = sqlite3.connect('armut.db')
    cur = con.cursor()
    for row in cur.execute('SELECT ID, Email, Name, Surname,Password, Phone,SID,Offer.PID, OfferStatus FROM Offer, User, Provider WHERE Provider.PID=User.ID AND Offer.PID=User.ID AND OfferStatus=?',('Pending',) ):
        aplications.append(row)
    con.commit()
    con.close()
    layout = [[sg.Text('Provider Requests:')],
          [sg.Listbox(aplications, size=(100, len(aplications)), key='application')],
          [sg.Button('Approve')],
          [sg.Button('Redject')]]
       
    window = sg.Window('Application information', layout) 
    event, values = window.read()     
    window.close()
    return (window, event, values)
def getdataCust(sid,services):
    
    inner_index = None
    for i in range(len(services)):
        for j in range(0,5):
            if services[i][j]==sid:
                inner_index=i
            else:
                pass
    # if inner_index==None: 
                
    layout = [[sg.Text('SID:'+'\t '+str(services[inner_index][0]))],
          [sg.Text('SName:'+'\t'+str(services[inner_index][1]))],
          [sg.Text('Price:'+'\t '+str(services[inner_index][2]))],
          [sg.Text('Category:'+'\t '+str(services[inner_index][3]))],
          [sg.Text('Description:'+'\t '+str(services[inner_index][4]))],
          [sg.Button('Add to Cart')]]
    window = sg.Window('Welcome to the Service Provider System. Please enter your information', layout) 
    event, values = window.read() 
    
    
    return (window,event, (services[inner_index][0],services[inner_index][1],services[inner_index][2]))
  
    
def Cartpage(cart):
    layout = [[sg.Text('Choose Available Services:')],
          [sg.Listbox(cart, size=(60, len(cart)), key='arrange_service')],
          [sg.Button('Ok')]]
    window = sg.Window('Service information', layout) 
    event, values = window.read()     
    window.close()
    return (window, event, values)
def bookingEditpage(sid): #cart[0][1]
     con = sqlite3.connect('armut.db')
     cur = con.cursor()
     appr_services=[]
     for row in cur.execute('SELECT Offer.PID,Offer.SID, User.Name,User.Surname,User.Phone FROM Offer, User WHERE Offer.PID=User.ID AND Offer.SID=? AND Offer.OfferStatus=?',(sid,'Approved')):
         appr_services.append(row)
     con.commit()
     con.close()
     layout = [  [sg.Text('Choose a provider:')],
            [sg.Combo(appr_services, size=(40, len(appr_services)), key='chosen_provider')],
            [sg.Text('Date of Service:', size=(15,1)), sg.Input(key='date', size=(15,1)), sg.CalendarButton('Choose Date', format='%Y-%m-%d')],
            [sg.Button('Ok')]]
     window = sg.Window('Service information', layout) 
     event, values = window.read()     
     window.close()
     print(values)
     print('----------------------')
     print(values['chosen_provider'])
     return (window, event, values)
    # layout = []
    # for info in cart:
    #     layout.append([sg.Text(info[0] + ':\t' + str(info[1]))])

    # layout.extend([ [sg.Button('Exit')]])
    # window = sg.Window('Welcome to the Service Provider System. Please enter your information', layout) 
    # event, values = window.read() 
    # return (window,event,values)

def completeBook(cid, bookinf):
    con = sqlite3.connect('armut.db')
    cur = con.cursor()
    booking=[]
    bookingids=[]
    
    for row in cur.execute('SELECT BID, Date, CID, SID,PID,Status FROM completeBooking WHERE CID=?',(cid,)):
        booking.append([row])
    for row in cur.execute('SELECT BID FROM completeBooking'):
        bookingids.append(row[0])
    con.commit()
    con.close()
    
    
    con = sqlite3.connect('armut.db')
    cur = con.cursor()
    cur.execute('SELECT MAX(BID) FROM completeBooking')
    new_id = cur.fetchone()[0] + 1
    val=(new_id,bookinf['date'],int(cid),bookinf['chosen_provider'][1],bookinf['chosen_provider'][0],'Pending' )
   
    cur.execute('INSERT INTO completeBooking VALUES(?,?,?,?,?,?)', val)
    con.commit()
    con.close()

cart=[]        
x=startpage()
window=x[0] 
event=x[1]
values=x[2]
ind=0 
# event, values = window.read()    
# one approach is to break if we click on exit
while True:
    
    print(event, values)
   
    if event == 'Login':
       ind=email.index(values['email_input'])
       if (values['email_input'] in email) and (values['password_input']== str(password[ind])):
           # sg.popup('Welcome'+'\t'+str(alldata[ind][2]))
           window.close()
    
       else:
           sg.popup('Wrong email or password')
    elif event == sg.WIN_CLOSED :
        break     
    else: 
        pass
    if str(allids[ind]) in aids:
        event2=adminpage(window,ind)[1]
        if event2=='Services':
            wind=servicespage()
            
            if wind[1]=='Add':
                windd2=addspage()
               
                if windd2[1]== 'Insert':
                    
                    windd2[0].close()
                    window=wind[0]
                    
                elif windd2[1] == sg.WIN_CLOSED :
                    break
            elif wind[1]=='Info':
                Services=[]
                con = sqlite3.connect('armut.db')
                cur = con.cursor()
                for row in cur.execute('SELECT SID,SName, Price,Category,Description FROM Services'):
                    Services.append(row)
                wind2=infopage(Services)
                
                while True:
                    if wind2[1] == 'Ok':
                        m=wind2[2]
                        
                        if m['chosen_service']==[]:
                            sg.popup('A servis must be chosen!')
                            wind2=infopage(Services)
                            # m=wind2[2]
                            
                        else:
                            mind=getdata(m['chosen_service'][0][0],Services)
                            wind2[0].close()
                            break
                    elif wind2[1] == sg.WIN_CLOSED :
                        break
                # if wind2[1] == 'Back':
                #     wind=servicespage()
            # elif wind[1]=='Providers':
            #     break
            elif  wind[1]=='Log out':
               x=startpage()
               window=x[0] 
               event=x[1]
               values=x[2] 
            elif wind[1] == sg.WIN_CLOSED :
                break
        elif event2=='Providers':
            wind6=providertransaction()
            if wind6[1]=='Pending Providers':
                wind=provider_approval()
                # print(wind[2])
                if wind[1]=='Approve':
                    cons = sqlite3.connect('armut.db')
                    curs = cons.cursor()
                    curs.execute('UPDATE Offer SET OfferStatus=? WHERE PID=? AND SID=?', ('Approved',wind[2]['application'][0][7],wind[2]['application'][0][6]))
                    cons.commit()
                    cons.close()
                elif wind[1]=='Redject':
                    cons = sqlite3.connect('armut.db')
                    curs = cons.cursor()
                    curs.execute('UPDATE Offer SET OfferStatus=? WHERE PID=?', ('Redjected',wind[2]['application'][0][7]))
                    cons.commit()
                    cons.close()
            elif  wind6[1]=='Confirmed Providers':
               wind2=confirmedprovider()
               if wind2[1]=='Approve':
                   cons = sqlite3.connect('armut.db')
                   curs = cons.cursor()
                   curs.execute('UPDATE Offer SET OfferStatus=? WHERE PID=?', ('Approved',wind2[2]['confirmed'][0][0]))
                   cons.commit()
                   cons.close()
               elif wind2[1]=='Redject':
                   cons = sqlite3.connect('armut.db')
                   curs = cons.cursor()
                   curs.execute('UPDATE Offer SET OfferStatus=? WHERE PID=?', ('Redjected',wind2[2]['confirmed'][0][0]))
                   cons.commit()
                   cons.close()
            elif  wind6[1]=='Redjected Providers':
               wind3=redjectedprovider()
               if wind3[1] == sg.WIN_CLOSED or wind3[1] == 'Exit' :
                   break
            elif wind[1] == sg.WIN_CLOSED:
                break
        elif event2 == sg.WIN_CLOSED or event == 'Exit':
            break
    elif allids[ind] in cids:
        event2=customerpage(window,ind)[1]
      
        if event2=='Services':
            wind2=infopage(Services)
            window=wind2[0]
            while True:
                if wind2[1] == 'Ok':
                    m=wind2[2]
                    
                    if m['chosen_service']==[]:
                        sg.popup('A servis must be chosen!')
                        wind2=infopage(Services)
                        # m=wind2[2]
                        
                    else:
                        mind=getdataCust(m['chosen_service'][0][0],Services)
                        mind[0].close()
                        if mind[1]=='Add to Cart':
                           cart.append(mind[2])
                           wind2[0].close()
                           break
                           
                        elif mind[1] == sg.WIN_CLOSED :
                            break
                elif wind2[1] == sg.WIN_CLOSED :
                    break
                
        
        elif event2=='Cart':
             wind=Cartpage(cart)
             # windd=wind[0]
             # wind[0].close()
             if wind[1]=='Ok':
                 wind2=bookingEditpage(cart[0][0])
                 if wind2[1]=='Ok':
                     bookinf=wind2[2]
                     completeBook(allids[ind], bookinf)
        elif event2=='Bookings':
                wind=custombookinghistory(allids[ind])
                if wind[1]=='Edit' :
                    ed=editbookpage(wind[2])
                    if ed[1]=='Save':
                        cons = sqlite3.connect('armut.db')
                        curs = cons.cursor()
                        curs.execute('UPDATE completeBooking SET Status=? WHERE BID=?', ('Completed',wind[2]['all_bookings'][0][0]))
                        cons.commit()
                        cons.close()
                elif wind[1]=='Review' :
                    rewindow=reviewpage(wind[2]['all_bookings'])
                    if rewindow[1]=='Save' :
                        con = sqlite3.connect('armut.db')
                        cur = con.cursor()
                        cur.execute('SELECT MAX(RID) FROM completeReview')
                        rid = cur.fetchone()[0] + 1
                        con.commit()
                        con.close()
                        con = sqlite3.connect('armut.db')
                        cur = con.cursor()
                        bookingprm=(rid,rewindow[2]['rate'],rewindow[2]['comment'],wind[2]['all_bookings'][0][2],wind[2]['all_bookings'][0][4],wind[2]['all_bookings'][0][3])
                        cur.execute('INSERT INTO completeReview VALUES(?,?,?,?,?,?)', bookingprm)
                        con.commit()
                        con.close()
                elif wind[1]==sg.WIN_CLOSED :
                     break  
        elif event2=='Log out':
            x=startpage()
            window=x[0] 
            event=x[1]
            values=x[2]
            if event==sg.WIN_CLOSED :
                 break    
        elif event2 == sg.WIN_CLOSED :
             break    
   
          
    elif allids[ind] in pids:
        # event=providerpage(window,ind)[0] 
        event2=providerpage(window,ind)[1] 
        if event2=='Register':
            wind2=registerpage(Services)
            window=wind2[0]
            if wind2[1] == 'Insert':
                parameters=wind2[3]
                
                ids=(allids[ind] ,parameters[6],'Pending')
               
                cur.execute('INSERT INTO Offer VALUES(?,?,?)', ids)
                con.commit()
                con.close()
                # show success message"""
                sg.popup('  Your request has delivered to admin! '   )
                # window.close()
        elif event2=='Applications':
            wind2=applicationspage(allids[ind])
            # window=wind2[0]
            if wind2[1]==sg.WIN_CLOSED or wind2[1]=='Ok' :
                #break
                 continue
        elif event2=='Customers':
            wind2=bookingaceptance(allids[ind])
            if wind2[1]=='Confirm' :
                
                 cons = sqlite3.connect('armut.db')
                 curs = cons.cursor()
                 curs.execute('UPDATE completeBooking SET Status=? WHERE BID=?', ('Confirmed',int(wind2[2]['booking'][0][0]))) #check this: wind2[2]['booking'][0][0]
                 cons.commit()
                 cons.close()
            elif wind2[1]=='Redject' :
                 #print(wind2[2]['booking'][0][0])
                 cons = sqlite3.connect('armut.db')
                 curs = cons.cursor()
                 curs.execute('UPDATE completeBooking SET Status=? WHERE BID=?', ('Rejected',wind2[2]['booking'][0][0])) #check this: wind2[2]['booking'][0][0]
                 cons.commit()
                 cons.close()                
            elif wind2[1]==sg.WIN_CLOSED or wind2[1]=='Ok' :
                 break
        elif event2=='Log out':
            x=startpage()
            window=x[0] 
            event=x[1]
            values=x[2]
        elif event2==sg.WIN_CLOSED :
              break    
    # if user clicks on the Exit button or the close window button, break the loop
    elif event == sg.WIN_CLOSED or event == 'Exit':
        break      

    
