"""
Author: Vamsee NY
Descrition: This is a simple web automation script using selenium to create 186 telegram channels to push notifications on Covaxin Availability. 
"""

from typing_extensions import final
from selenium import webdriver
from webdriver_manager import driver_cache
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.ui import WebDriverWait
import time
import pyautogui as pg
#from webdriver_manager.driver import Driver
from cowin_api import CoWinAPI

def create_chan(dis):
    driver.find_element_by_xpath('/html/body//*[@id="new-menu"]/div[1]').click()
    time.sleep(1)
    pg.click(400,650) #cant automate certiain components of the website. Hence I used PyAutoGUI to control mouse clicks. 400,650 are the coordinates of mouse clicks
    driver.find_element_by_xpath('/html/body//*[@id="column-left"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]').click()             #Selecting the name input field
    driver.find_element_by_xpath('/html/body//*[@id="column-left"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]').send_keys(n,dis)    #Send the name of the channel in the input field. Example: Covaxin_Chennai
    driver.find_element_by_xpath('/html/body//*[@id="column-left"]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]').click()             #Selecting channel information field
    driver.find_element_by_xpath('/html/body//*[@id="column-left"]/div/div[2]/div[2]/div/div[2]/div[2]/div[1]').send_keys("This channel provides notifications on availability of Covaxin in {}. For ages 18+ and 45+".format(dis)) #Editing Channel description
    time.sleep(1)
    driver.find_element_by_xpath('/html/body//*[@id="column-left"]/div/div[2]/div[2]/button/div').click()   #Clicking on the proceed button
    time.sleep(3)
    pg.click(550,950)   #Navigating to the home screen.


cowin=CoWinAPI()
#states=cowin.get_states()
#ind=list(states.values())[0]
#inp=['-1001595417850', '-1001452271381', '-1001360743362', '-1001528194441', '-1001581515691', '-1001387347362', '-1001391783908', '-1001538486448', '-1001548928771', '-1001599515166', '-1001515946588', '-1001227659170', '-1001179273865', '-1001578376184', '-1001301146817', '-1001536709942', '-1001513513510', '-1001205586402', '-1001439378349', '-1001502273261', '-1001287904069', '-1001505532201', '-1001218567814', '-1001410020457', '-1001539176318', '-1001533432835', '-1001293852529', '-1001581400378', '-1001302817568', '-1001509760512', '-1001507147474', '-1001520831845', '-1001230063402', '-1001512285040', '-1001598270800', '-1001555374964', '-1001528481489', '-1001442466388', '-1001506251151', '-1001252082371', '-1001413289407', '-1001558163157', '-1001459089332', '-1001560685578', '-1001578858138', '-1001382697823', '-1001599705043', '-1001598083203', '-1001458442307', '-1001531473811', '-1001569205011', '-1001536911893', '-1001596574033', '-1001567285381', '-1001596292354', '-1001598750446', '-1001496872015', '-1001501930385', '-1001204703106', '-1001534901239', '-1001293574821', '-1001524028336', '-1001549163917', '-1001574132263', '-1001573930688', '-1001549916297', '-1001588096964', '-1001557355808', '-1001574810386', '-1001400502899', '-1001542528942', '-1001570109155', '-1001466887041', '-1001550720748', '-1001563369689', '-1001598355424', '-1001303654303', '-1001500283414', '-1001414658355', '-1001503095126', '-1001391622187', '-1001573867901', '-1001572929244', '-1001587594889', '-1001319017679', '-1001582293704', '-1001481893333', '-1001527290228', '-1001501102817', '-1001597671740', '-1001572457598', '-1001442279373', '-1001124120389', '-1001436527401', '-1001513704844', '-1001463690271', '-1001550275595', '-1001501164669', '-1001528846916', '-1001557877043', '-1001570147651', '-1001514670083', '-1001559320308', '-1001503218320', '-1001547904338', '-1001554284855', '-1001571259659', '-1001504668547', '-1001410480475', '-1001543083726', '-1001125667416', '-1001575845474', '-1001538024073', '-1001573597569', '-1001517766854', '-1001204253090', '-1001565256239', '-1001451907005', '-1001185307547', '-1001219024627', '-1001498913958', '-1001551869017', '-1001576532819', '-1001515545341', '-1001557591401', '-1001556721928', '-1001591713198', '-1001549759905', '-1001545256579', '-1001593015292', '-1001384778158', '-1001182464523', '-1001234279603', '-1001594468851', '-1001573597238', '-1001568703858', '-1001584936492', '-1001501948427', '-1001366554350', '-1001528083560', '-1001533258526', '-1001546189806', '-1001598531021', '-1001298280988', '-1001442196004', '-1001553516907', '-1001537151413', '-1001575649532', '-1001424528104', '-1001412508267', '-1001500994595', '-1001229818006', '-1001573419307', '-1001540299407', '-1001402419645', '-1001454421190', '-1001165380882', '-1001522135530', '-1001518947511', '-1001585761271', '-1001544989366', '-1001462549198', '-1001516886322', '-1001572710306', '-1001591489000', '-1001570448637', '-1001553532569', '-1001565591119', '-1001381462858', '-1001581221032', '-1001422409258', '-1001589840009', '-1001528721786', '-1001133930398', '-1001528892046', '-1001504272583', '-1001574548659', '-1001556562804', '-1001594618863', '-1001228542272', '-1001452271381', '-1001595319135', '-1001582748367']
fi=dict()
chatids=[]
ind=[ {'state_id': 9, 'state_name': 'Delhi'}, {'state_id': 11, 'state_name': 'Gujarat'},{'state_id': 21, 'state_name': 'Maharashtra'},{'state_id': 31, 'state_name': 'Tamil Nadu'}, {'state_id': 20, 'state_name': 'Madhya Pradesh'},]
names=[]
for a in ind:
    districts=cowin.get_districts(a.get("state_id"))    #Saving ID's of districts 
    ins=list(districts.values())[0]
    for b in ins:
        names.append(str(b.get("district_name")))       #Saving names of states in list 'ins'


p=ChromeDriverManager()
n="Covaxin_"
options=webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\91900\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  #Loading telegram credentials from saved cookies to prevent logging in for every interation. 
driver = webdriver.Chrome(p.install(), chrome_options=options)
driver.get("https://web.telegram.org/k/")   #Opening telegram website
driver.maximize_window()
time.sleep(2)
#print(names.index("Dhar"),"\t",len(names))#Dhar=147, start from 148 
#print(names[148:])
print(len(names))
for i in names:
    print(i)
    #create_chan(i)      #Calling function create_chan passing i as an argument
print("DONE"*88)
