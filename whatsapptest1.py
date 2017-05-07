from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

r = {1:'In a far distance across the pitiful horizon\nI scour for thee\nI roam the land beneath, above\nAn empire which called you name it,\nFor thyself\n\nConquering the waters of no calamity\nCrushing bones\ncenturies old\nNo eyes could laid or peek\n\nQueen of the abyss\nVast...profound...lustrous\nThe birth of wishes\nTraces of blithe\nThe haven for the founders\nSanctuaries for the forgiven\n...Peace\n\nAnd peace to come for all\nFor their names\nLaying down\nOn a steel threaded tapestry\nNever forgotten',
2:'Riddle me this : \nWhat is two-faced, but bears one head, \nHas no legs but travels widely? \nWhat is potent when shared, \nYet locked away where no eye can see?\n\nSeek the place where the solution is most abundant.',
3:'http://i.imgur.com/fRpLJRS.jpg' ,
4:'I\'ll do it after dinner, mom!',
5:'Meant to be wet but now always dry\nUsed to be firm but now saggy\nBlow me up and i am ready for a journey',
6:'Keys but no locks, legs but no socks.',
7:'Dancing in mirror, singing in the shower.',
8:'Deaf but great',
9:'Come to SUTD to create a better world by design - and become the very best. (Like no one ever was)',
10:'......95141.3 <--',
11:'If after lunch you feel too full and want to go jalan jalan, just take the lift to find the Gardens by the b4e',
12:'I\'m filled with food but never feel full\nUntil people feed me with disks not bills.\nOh how kind, those students are \nAlways giving me those things they bring from far.\nSo in return, I offer them my inner treasure\nSatisfying their late night archi-hunger\nBut other than that, I\'m usually lonely.\nWhat i would give for someone to visit me regularly.\nOh how much I love you. \nWe can spend the rest of our lives here 2-gether 5 ever.',
13:'If you ever feel down because of school and stuff\nCome on over and have a chat with us!\nFor all things big or small, we\'ve got your back, \nEven when you wanna find the things you still lack!',
14:'http://i.imgur.com/k1qXfq8.png',
15:'http://i.imgur.com/32flhTu.png',
16:'http://i.imgur.com/2Qigzrr.png',
17:'http://i.imgur.com/NmKo7bA.png',
18:'http://i.imgur.com/JjNL3Sa.png',
19:'SUTD Student Government(2)',
20:'Rectangles narrow but long, they keep me locked here in chains.\nAround the corner, heavy steel closes a box filled with holes, \ncrowds gather unknowing of their 1 true fate.',
21:'Top cake, Bottom cake, Left cake, Right cake.',
22:'Backyard 1.508',
23:'6-2-25-5-53-8-57-5 (Key: 1 = H, 2 = Li)',
24:'Wisdom\'s chute',
25:'Greenery beside stationery'
}

z = {1:'http://i.imgur.com/yhktJL0.jpg',
2:'http://i.imgur.com/A4NGhzD.jpg',
3:'http://i.imgur.com/7Nvxese.jpg',
4:'http://i.imgur.com/R3KIbAC.jpg',
5:'http://i.imgur.com/Ca5xtPQ.jpg',
6:'http://i.imgur.com/yhktJL0.jpg',
7:'http://i.imgur.com/A4NGhzD.jpg',
8:'http://i.imgur.com/7Nvxese.jpg',
9:'http://i.imgur.com/R3KIbAC.jpg',
10:'http://i.imgur.com/Ca5xtPQ.jpg',
11:'http://i.imgur.com/yhktJL0.jpg',
12:'http://i.imgur.com/A4NGhzD.jpg',
13:'http://i.imgur.com/7Nvxese.jpg',
14:'http://i.imgur.com/R3KIbAC.jpg',
15:'http://i.imgur.com/Ca5xtPQ.jpg',
16:'http://i.imgur.com/yhktJL0.jpg',
17:'http://i.imgur.com/A4NGhzD.jpg',
18:'http://i.imgur.com/7Nvxese.jpg',
19:'http://i.imgur.com/R3KIbAC.jpg',
20:'http://i.imgur.com/Ca5xtPQ.jpg',
21:'http://i.imgur.com/yhktJL0.jpg',
22:'http://i.imgur.com/A4NGhzD.jpg',
23:'http://i.imgur.com/7Nvxese.jpg',
24:'http://i.imgur.com/R3KIbAC.jpg',
25:'http://i.imgur.com/Ca5xtPQ.jpg',
}
print r[14]
# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('C:/Users/admin/Desktop/Coding stuff/chromedriver_win32/chromedriver')
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
d = {'"Ryan Teo SUTD"':[r[13], r[5], r[7], r[1], z[1]],'"Clemence SUTD Choir"':[r[12], r[13], r[5], r[7], z[2]],
'"Dana Yang SUTD"':[r[1], r[12], r[13], r[5], z[3]], 
'"Gerald Pan SUTD"':[r[7], r[1], r[12], r[13], z[4]], 
'"Harleen Kaur SUTD"':[r[5], r[7], r[1], r[12], z[5]],

'"Liang Chen You SUTD"':[r[2], r[25], r[17], r[16], z[4]], 
'"Lok Swen SUTD"':[r[4], r[2], r[25], r[17], z[7]], 
'"Lucas Orientation SUTD"':[r[16], r[4], r[2], r[25], z[8]], 
'"Marcus Yong SUTD"':[r[17], r[16], r[4], r[2], z[9]], 
'"Mavis Lee SUTD"':[r[25], r[17], r[16], r[4], z[10]], 

'"Menglu SUTD"':[r[3], r[10], r[11], r[21], z[11]], 
'"Phoebe Phyu SUTD"':[r[6], r[3], r[10], r[11], z[12]], 
'"Qi Tai SUTD"':[r[21], r[6], r[3], r[10], z[13]], 
'"Ruby Chau SUTD"':[r[11], r[21], r[6], r[3], z[14]], 
'"Shajini Hubert SUTD"':[r[10], r[11], r[21], r[6], z[15]], 

'"Sidd SUTD"':[r[8], r[18], r[24], r[23], z[16]], 
'"Yukun SUTD"':[r[14], r[8], r[18], r[24], z[17]], 
'"Zachary Song SUTD"':[r[23], r[14], r[8], r[18], z[18]], 
'"Hendriko Dito SUTD"':[r[24], r[23], r[14], r[8], z[19]], 
'"Zhi Yuan SUTD"':[r[18], r[24], r[23], r[14], z[20]],

'"Qi Tai SUTD"':[r[9], r[19], r[22], r[20], z[21]], 
'"Qi Tai SUTD"':[r[15], r[9], r[19], r[22], z[22]], 
'"Qi Tai SUTD"':[r[20], r[15], r[9], r[19], z[23]], 
'"Qi Tai SUTD"':[r[22], r[20], r[15], r[9], z[24]], 
'"Qi Tai SUTD"':[r[19], r[22], r[20], r[15], z[25]]
 }

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
for i in range (len(d.values())):
	count = i
	print count
	for k,v in d.items():
		target = k
		string = v[i]
		print target
		print string
		x_arg = '//span[contains(@title,' + target + ')]'
		group_title = wait.until(EC.presence_of_element_located((
		    By.XPATH, x_arg)))
		group_title.click()
		inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
		input_box = wait.until(EC.presence_of_element_located((
		    By.XPATH, inp_xpath)))
		# for i in range(100):
		input_box.send_keys(string + Keys.ENTER)
		time.sleep(1)
	time.sleep(20)

# target = '"Qi Tai SUTD"'
 
# Replace the below string with your own message
# string = "Message sent using Python!!! Me too thanks"
 
###Links###
#capstone7: http://i.imgur.com/NmKo7bA.png
#fablab bridge: http://i.imgur.com/JjNL3Sa.png
#B1&2 bridge: http://i.imgur.com/2Qigzrr.png
#Arms2 Lockers: http://i.imgur.com/32flhTu.png
#One Stop Centre: http://i.imgur.com/k1qXfq8.png