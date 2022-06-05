import time
import hashlib
from datetime import datetime
from cowin_api import CoWinAPI
import requests
from copy import copy
import os

def check():
    url = "https://www.google.com/"
    try:
        request = requests.get(url, timeout=5)
        #print("T",end='')
        return(True)
    except (requests.ConnectionError, requests.Timeout):
        #print("No internet connection.")
        return(False)

"""
Categories:
A: 18+ covishield
B: 18+ covaxin
C: 45+ covishield
D: 45+ covaxin
Groups:
For the kerala groups: B and D
Bangalore 45+: C and D
Delhi45+: C and D
coxb: B and D
"""

def iris():
    categories={'A':[],'B':[],'C':[],'D':[]}
    groups={'cowinhash':[],'Delhi':[],'cox':[],'kerl':[],'web':[]}
    groupids={'cowinhash':'-1001318912568','Delhi':'-1001294935329','cox':'-1001437847837','kerl':{'Alappuzha':'-1001520362226','Ernakulam':'-1001584893143','Idukki':'-1001272817691','Kannur':'-1001521159601','Kasaragod':'-1001517114626','Kollam':'-1001590937927','Kottayam':'-1001359215867','Kozhikode':'-1001586923251','Malappuram':'-1001352710354','Palakkad':'-1001516141376','Pathanamthitta':'-1001587754441','Thiruvananthapuram':'-1001597031841','Thrissur':'-1001365845877','Wayanad':'-1001504920657'},'web':{'Central Delhi': '-1001595417850','East Delhi': '-1001536594081','New Delhi': '-1001360743362','North Delhi': '-1001528194441','North East Delhi': '-1001581515691', 'North West Delhi': '-1001387347362', 'Shahdara': '-1001391783908','South Delhi': '-1001538486448','South East Delhi': '-1001548928771','South West Delhi': '-1001599515166','West Delhi': '-1001515946588','Ahmedabad': '-1001227659170', 'Ahmedabad Corporation': '-1001179273865', 'Amreli': '-1001578376184', 'Anand': '-1001301146817', 'Aravalli': '-1001536709942', 'Banaskantha': '-1001513513510', 'Bharuch': '-1001205586402', 'Bhavnagar': '-1001439378349', 'Bhavnagar Corporation': '-1001502273261', 'Botad': '-1001287904069', 'Chhotaudepur': '-1001505532201', 'Dahod': '-1001218567814', 'Dang': '-1001410020457', 'Devbhumi Dwaraka': '-1001539176318', 'Gandhinagar': '-1001533432835', 'Gandhinagar Corporation': '-1001293852529', 'Gir Somnath': '-1001581400378', 'Jamnagar': '-1001302817568', 'Jamnagar Corporation': '-1001509760512', 'Junagadh': '-1001507147474', 'Junagadh Corporation': '-1001520831845', 'Kheda': '-1001230063402', 'Kutch': '-1001512285040', 'Mahisagar': '-1001598270800', 'Mehsana': '-1001555374964', 'Morbi': '-1001528481489', 'Narmada': '-1001442466388', 'Navsari': '-1001506251151', 'Panchmahal': '-1001252082371', 'Patan': '-1001413289407', 'Porbandar': '-1001558163157', 'Rajkot': '-1001459089332', 'Rajkot Corporation': '-1001560685578', 'Sabarkantha': '-1001578858138', 'Surat': '-1001382697823', 'Surat Corporation': '-1001599705043', 'Surendranagar': '-1001598083203', 'Tapi': '-1001458442307', 'Vadodara': '-1001531473811', 'Vadodara Corporation': '-1001569205011', 'Valsad': '-1001536911893', 'Ahmednagar': '-1001596574033', 'Akola': '-1001567285381', 'Amravati': '-1001596292354', 'Aurangabad ': '-1001598750446', 'Beed': '-1001496872015', 'Bhandara': '-1001501930385', 'Buldhana': '-1001204703106', 'Chandrapur': '-1001534901239', 'Dhule': '-1001293574821', 'Gadchiroli': '-1001524028336', 'Gondia': '-1001549163917', 'Hingoli': '-1001574132263', 'Jalgaon': '-1001573930688', 'Jalna': '-1001549916297', 'Kolhapur': '-1001588096964', 'Latur': '-1001557355808', 'Mumbai': '-1001574810386', 'Nagpur': '-1001400502899', 'Nanded': '-1001542528942', 'Nandurbar': '-1001570109155', 'Nashik': '-1001466887041', 'Osmanabad': '-1001550720748', 'Palghar': '-1001563369689', 'Parbhani': '-1001598355424', 'Pune': '-1001303654303', 'Raigad': '-1001500283414', 'Ratnagiri': '-1001414658355', 'Sangli': '-1001503095126', 'Satara': '-1001391622187', 'Sindhudurg': '-1001573867901', 'Solapur': '-1001572929244', 'Thane': '-1001587594889', 'Wardha': '-1001319017679', 'Washim': '-1001582293704', 'Yavatmal': '-1001481893333', 'Aranthangi': '-1001527290228', 'Ariyalur': '-1001501102817', 'Attur': '-1001597671740', 'Chengalpet': '-1001572457598', 'Chennai': '-1001442279373', 'Cheyyar': '-1001124120389', 'Coimbatore': '-1001436527401', 'Cuddalore': '-1001513704844', 'Dharmapuri': '-1001463690271', 'Dindigul': '-1001550275595', 'Erode': '-1001501164669', 'Kallakurichi': '-1001528846916', 'Kanchipuram': '-1001557877043', 'Kanyakumari': '-1001570147651', 'Karur': '-1001514670083', 'Kovilpatti': '-1001559320308', 'Krishnagiri': '-1001503218320', 'Madurai': '-1001547904338', 'Nagapattinam': '-1001554284855', 'Namakkal': '-1001571259659', 'Nilgiris': '-1001504668547', 'Palani': '-1001410480475', 'Paramakudi': '-1001543083726', 'Perambalur': '-1001125667416', 'Poonamallee': '-1001575845474', 'Pudukkottai': '-1001538024073', 'Ramanathapuram': '-1001573597569', 'Ranipet': '-1001517766854', 'Salem': '-1001204253090', 'Sivaganga': '-1001565256239', 'Sivakasi': '-1001451907005', 'Tenkasi': '-1001185307547', 'Thanjavur': '-1001219024627', 'Theni': '-1001498913958', 'Thoothukudi (Tuticorin)': '-1001551869017', 'Tiruchirappalli': '-1001576532819', 'Tirunelveli': '-1001515545341', 'Tirupattur': '-1001557591401', 'Tiruppur': '-1001556721928', 'Tiruvallur': '-1001591713198', 'Tiruvannamalai': '-1001549759905', 'Tiruvarur': '-1001545256579', 'Vellore': '-1001593015292', 'Viluppuram': '-1001384778158', 'Virudhunagar': '-1001182464523', 'Agar': '-1001234279603', 'Alirajpur': '-1001594468851', 'Anuppur': '-1001573597238', 'Ashoknagar': '-1001568703858', 'Balaghat': '-1001584936492', 'Barwani': '-1001501948427', 'Betul': '-1001366554350', 'Bhind': '-1001528083560', 'Bhopal': '-1001533258526', 'Burhanpur': '-1001546189806', 'Chhatarpur': '-1001598531021', 'Chhindwara': '-1001298280988', 'Damoh': '-1001442196004', 'Datia': '-1001553516907', 'Dewas': '-1001537151413', 'Dhar': '-1001575649532', 'Dindori': '-1001424528104', 'Guna': '-1001412508267', 'Gwalior': '-1001500994595', 'Harda': '-1001229818006', 'Hoshangabad': '-1001573419307', 'Indore': '-1001540299407', 'Jabalpur': '-1001402419645', 'Jhabua': '-1001454421190', 'Katni': '-1001165380882', 'Khandwa': '-1001522135530', 'Khargone': '-1001518947511', 'Mandla': '-1001585761271', 'Mandsaur': '-1001544989366', 'Morena': '-1001462549198', 'Narsinghpur': '-1001516886322', 'Neemuch': '-1001572710306', 'Panna': '-1001591489000', 'Raisen': '-1001570448637', 'Rajgarh': '-1001553532569', 'Ratlam': '-1001565591119', 'Rewa': '-1001381462858', 'Sagar': '-1001581221032', 'Satna': '-1001422409258', 'Sehore': '-1001589840009', 'Seoni': '-1001528721786', 'Shahdol': '-1001133930398', 'Shajapur': '-1001528892046', 'Sheopur': '-1001504272583', 'Shivpuri': '-1001574548659', 'Sidhi': '-1001556562804', 'Singrauli': '-1001594618863', 'Tikamgarh': '-1001228542272', 'Ujjain': '-1001452271381', 'Umaria': '-1001595319135', 'Vidisha': '-1001582748367'}}
    chatid=[539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 580, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 770, 771, 772, 773, 774, 775, 776, 265, 777, 778, 779, 780, 781, 276, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397]
    temp={'cowinhash':[],'Delhi':[],'cox':[],'kerl':[],'web':[]}
    while True:
        delta={'cowinhash':[],'Delhi':[],'cox':[],'kerl':[],'web':[]}
        cowin = CoWinAPI()
        date = datetime.today().strftime('%d-%m-%Y')
        copyy=[]
        copyy2=[]
        for i in chatid:
            print(i)
            if check():                                                                                        #check for internet connectivity
                copyy.append(list((cowin.get_availability_by_district(str(i), date, 18)).values())[0])         #data for age 18+       #(list((cowin.get_availability_by_district(str(i), date, 18)).values())[0])
                copyy2.append(list((cowin.get_availability_by_district(str(i), date, 45)).values())[0])        #data for age 45+
            else:
                time.sleep(60)
                break
        copyy_flat=[num for sublist in copyy for num in sublist] #flattening lists
        copyy2_flat=[num for sublist in copyy2 for num in sublist] 
        categories['A']=list(x for x in copyy_flat if x.get("sessions")[0].get("vaccine")=='COVISHIELD' and x.get('sessions')[0].get('available_capacity')>4)       #categorizing data from copyy_flat and copyy2_flat
        categories['B']=list(x for x in copyy_flat if x.get("sessions")[0].get("vaccine")=='COVAXIN' and x.get('sessions')[0].get('available_capacity')>4)
        categories['C']=list(x for x in copyy2_flat if x.get("sessions")[0].get("vaccine")=='COVISHIELD' and x.get('sessions')[0].get('available_capacity')>4)
        categories['D']=list(x for x in copyy2_flat if x.get("sessions")[0].get("vaccine")=='COVAXIN' and x.get('sessions')[0].get('available_capacity')>4)
        print("\n",len(categories['A']),len(categories['B']),len(categories['C']),len(categories['D']))
        groups['cowinhash']=list(x for x in list(categories['C']+categories['D']) if x.get('state_name')=='Karnataka')  #re categorizing data to subgroups                                          #categories['C']+categories['D']                    #keep conditional here   NICE                                #or we could directly initialize like above + something else above
        groups['Delhi']=list(x for x in list(categories['C']+categories['D']) if x.get('state_name')=='Delhi')                                                   #categories['C']+categories['D']
        groups['cox']=list(x for x in list(categories['B']+categories['D']) if x.get('state_name')=='Karnataka')
        groups['kerl']=list(x for x in [num for sublist in categories.values() for num in sublist] if x.get('state_name')=='Kerala')  
        groups['web']=list(x for x in list(categories['A']+categories['B']) if x.get('state_name'!='Karnataka' or x.get('state_name')!='Kerala') or x.get('state_name')!='Delhi')      
        print(len(groups['cowinhash']),len(groups['Delhi']),len(groups['cox']),len(groups['kerl']),len(groups['web'])) #subtracting 2 dicts is not efficient so find delta cen_id
        #netcent=[num.get('center_id') for sublist in groups.values() for num in sublist] #flatten groups.values and then extract center_id
        #netcent = {i:k for i,j in zip(groups.keys(),list(groups.values())) for k in j} 
        netcent=dict()
        for i in groups.keys():         #allocating netcent and delta
            netcent[i]=[j.get('center_id') for j in groups[i]]          
            #delta[i]=list(set(netcent[i])-set(temp[i]))       
            delta[i]=list(set(netcent[i])-set(temp[i])) if len(list(set(netcent[i])-set(temp[i])))<5 else []         #ping limiter using if      

        for i in [num for sublist in delta.values() for num in sublist]:
            retrieved=next((j for j in [num for sublist in groups.values() for num in sublist] if j.get('center_id')==i),None)  #get dictionary from groups.values which has center_id i
            rkey=[groupids[k] for k, v in groups.items() if retrieved in list(map(lambda x:x, v))] [0]                          #get key 
            fkey=str(rkey) if type(rkey)==str else str(rkey.get(retrieved.get('district_name')))
            send_url= 'https://api.telegram.org/bot' + str(os.environ['BOT_ID']) + '/sendMessage?chat_id=' +fkey+ '&parse_mode=Markdown&text=' + "New update:\n Covaxin vaccine available at {}, {}, {}.\n Fee type: {}\n Center id: {},Date: {},Age: {} +, Vaccine: {}\n Dose 1: {} available, Dose 2: {} available".format(retrieved.get("name"),retrieved.get("address"),retrieved.get("district_name"),retrieved.get("fee_type"),retrieved.get("center_id"),retrieved.get("sessions")[0].get("date"),retrieved.get("sessions")[0].get("min_age_limit"),retrieved.get("sessions")[0].get("vaccine"),retrieved.get("sessions")[0].get("available_capacity_dose1"),retrieved.get("sessions")[0].get("available_capacity_dose2"))
            #print(send_url)
            try:
                requests.get(send_url) #post message
            except requests.exceptions.ConnectionError:
                time.sleep(60)
                break
            #print(retrieved)

        temp=copy(netcent) #copying data to search for new values in the next iteration
        time.sleep(10) #interate every 10 seconds
        
iris()
