from flask import Markup
def Version():
    version = [
        {
            'id': 1,
            'CAR_OWNER': 'CD21.1',
            'CRDS_OWNER': 'CD21.1',
            'STG_OWNER': 'CD21.1',
            'Instanse': 'PROD',
            'author': 'vorovik',
            'create_date': '03-01-2017'

        },
        {
            'id': 2,
            'CAR_OWNER': 'CD20.1',
            'CRDS_OWNER': 'CD20.1',
            'STG_OWNER': 'CD20.1',
            'Instanse': 'UAT',
            'author': 'vorovik',
            'create_date': '03-01-2017'
        }
    ]
	#source={'logo':'source/logo.png','block1':'img/05.jpg'}
    return version

def source():
    source={'logo':'source/logo.png','block1':'img/05.jpg','block3':'img/01.jpg','block4':'img/02.jpg'} #_block1.html
    return source
def header():
    header={'phone':'777-777-7777','email':'e-mail: info@ladymarlene.ru','link':'https://vk.com/ladymarlene','infolink':'vk.com/ladymarlene','city':'г. Москва'} #_header.html
    return header
def shopwindow_items():
    shopwindow_items=(
	{'id':1001,'img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','b_img':'source/glasses/b02_big.png','price':'1300','link':'glasses','name':'','description':''},

	{'id':1002,'img':'source/glasses/b03.png','e_img':'source/glasses/G02.gif','b_img':'source/glasses/b03_big.png','price':'1400','link':'glasses','name':'','description':''},

	{'id':1003,'img':'source/glasses/b04.png','e_img':'source/glasses/G04.gif','b_img':'source/glasses/b04_big.png','price':'1500','link':'glasses','name':'','description':''},

	{'id':1004,'img':'source/glasses/b05.png','e_img':'source/glasses/G05.gif','b_img':'source/glasses/b05_big.png','price':'1600','link':'glasses','name':'','description':''},

	{'id':1005,'img':'source/glasses/b06.png','e_img':'source/glasses/G06.gif','b_img':'source/glasses/b06_big.png','price':'1100','link':'glasses','name':'','description':''},

	{'id':1006,'img':'source/glasses/b07.png','e_img':'source/glasses/G07.gif','b_img':'source/glasses/b07_big.png','price':'1600','link':'glasses','name':'','description':''},

	{'id':1007,'img':'source/glasses/b08.png','e_img':'source/glasses/G08.gif','b_img':'source/glasses/b08_big.png','price':'1200','link':'glasses','name':'','description':''},

	{'id':1008,'img':'source/glasses/b01.png','e_img':'source/glasses/G09.gif','b_img':'source/glasses/b01_big-1.png','price':'1900','link':'glasses','name':'','description':''},

	{'id':1009,'img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','b_img':'source/glasses/b02_big.png','price':'1300','link':'glasses','name':'','description':''}

    )#_glasses.html
    return shopwindow_items
def carousel_items():
    carousel_items=(
	{'u_id':1001,'gr_id':1001,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_5_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':1001,'gr_id':1002,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_6_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':1001,'gr_id':1003,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_11_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':1001,'gr_id':1004,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_27_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':1001,'gr_id':1005,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_29_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':1001,'gr_id':1006,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_49_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},

	{'u_id':1002,'gr_id':1001,'type':'1','img':'source/glasses/b03.png','e_img':'source/glasses/G02.gif','price':'1400','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_5_mini.png','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},
	{'u_id':1002,'gr_id':1002,'type':'1','img':'source/glasses/b03.png','e_img':'source/glasses/G02.gif','price':'1400','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_6_mini.png','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},
	{'u_id':1002,'gr_id':1003,'type':'1','img':'source/glasses/b03.png','e_img':'source/glasses/G02.gif','price':'1400','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_11_mini.png','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},
	{'u_id':1002,'gr_id':1004,'type':'1','img':'source/glasses/b03.png','e_img':'source/glasses/G02.gif','price':'1400','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_27_mini.png','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},
	{'u_id':1002,'gr_id':1005,'type':'1','img':'source/glasses/b03.png','e_img':'source/glasses/G02.gif','price':'1400','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_29_mini.png','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},
	{'u_id':1002,'gr_id':1006,'type':'1','img':'source/glasses/b03.png','e_img':'source/glasses/G02.gif','price':'1400','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_49_mini.png','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},

	{'u_id':1003,'gr_id':1001,'type':'1','img':'source/glasses/b04.png','e_img':'source/glasses/G04.gif','price':'1500','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_5_mini.png','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},
	{'u_id':1003,'gr_id':1002,'type':'1','img':'source/glasses/b04.png','e_img':'source/glasses/G04.gif','price':'1500','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_6_mini.png','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},
	{'u_id':1003,'gr_id':1003,'type':'1','img':'source/glasses/b04.png','e_img':'source/glasses/G04.gif','price':'1500','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_11_mini.png','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},
	{'u_id':1003,'gr_id':1004,'type':'1','img':'source/glasses/b04.png','e_img':'source/glasses/G04.gif','price':'1500','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_27_mini.png','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},
	{'u_id':1003,'gr_id':1005,'type':'1','img':'source/glasses/b04.png','e_img':'source/glasses/G04.gif','price':'1500','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_29_mini.png','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},
	{'u_id':1003,'gr_id':1006,'type':'1','img':'source/glasses/b04.png','e_img':'source/glasses/G04.gif','price':'1500','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_49_mini.png','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},

	{'u_id':1004,'gr_id':1001,'type':'1','img':'source/glasses/b05.png','e_img':'source/glasses/G05.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_5_mini.png','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},
	{'u_id':1004,'gr_id':1002,'type':'1','img':'source/glasses/b05.png','e_img':'source/glasses/G05.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_6_mini.png','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},
	{'u_id':1004,'gr_id':1003,'type':'1','img':'source/glasses/b05.png','e_img':'source/glasses/G05.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_11_mini.png','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},
	{'u_id':1004,'gr_id':1004,'type':'1','img':'source/glasses/b05.png','e_img':'source/glasses/G05.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_27_mini.png','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},
	{'u_id':1004,'gr_id':1005,'type':'1','img':'source/glasses/b05.png','e_img':'source/glasses/G05.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_29_mini.png','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},
	{'u_id':1004,'gr_id':1006,'type':'1','img':'source/glasses/b05.png','e_img':'source/glasses/G05.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_49_mini.png','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},

	{'u_id':1005,'gr_id':1001,'type':'1','img':'source/glasses/b06.png','e_img':'source/glasses/G06.gif','price':'1100','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_5_mini.png','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},
	{'u_id':1005,'gr_id':1002,'type':'1','img':'source/glasses/b06.png','e_img':'source/glasses/G06.gif','price':'1100','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_6_mini.png','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},
	{'u_id':1005,'gr_id':1003,'type':'1','img':'source/glasses/b06.png','e_img':'source/glasses/G06.gif','price':'1100','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_11_mini.png','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},
	{'u_id':1005,'gr_id':1004,'type':'1','img':'source/glasses/b06.png','e_img':'source/glasses/G06.gif','price':'1100','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_27_mini.png','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},
	{'u_id':1005,'gr_id':1005,'type':'1','img':'source/glasses/b06.png','e_img':'source/glasses/G06.gif','price':'1100','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_29_mini.png','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},
	{'u_id':1005,'gr_id':1006,'type':'1','img':'source/glasses/b06.png','e_img':'source/glasses/G06.gif','price':'1100','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_49_mini.png','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},


	{'u_id':1006,'gr_id':1001,'type':'1','img':'source/glasses/b07.png','e_img':'source/glasses/G07.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_5_mini.png','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},
	{'u_id':1006,'gr_id':1002,'type':'1','img':'source/glasses/b07.png','e_img':'source/glasses/G07.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_6_mini.png','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},
	{'u_id':1006,'gr_id':1003,'type':'1','img':'source/glasses/b07.png','e_img':'source/glasses/G07.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_11_mini.png','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},
	{'u_id':1006,'gr_id':1004,'type':'1','img':'source/glasses/b07.png','e_img':'source/glasses/G07.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_27_mini.png','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},
	{'u_id':1006,'gr_id':1005,'type':'1','img':'source/glasses/b07.png','e_img':'source/glasses/G07.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_29_mini.png','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},
	{'u_id':1006,'gr_id':1006,'type':'1','img':'source/glasses/b07.png','e_img':'source/glasses/G07.gif','price':'1600','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_49_mini.png','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},

	{'u_id':1007,'gr_id':1001,'type':'1','img':'source/glasses/b08.png','e_img':'source/glasses/G08.gif','price':'1200','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_5_mini.png','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},
	{'u_id':1007,'gr_id':1002,'type':'1','img':'source/glasses/b08.png','e_img':'source/glasses/G08.gif','price':'1200','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_6_mini.png','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},
	{'u_id':1007,'gr_id':1003,'type':'1','img':'source/glasses/b08.png','e_img':'source/glasses/G08.gif','price':'1200','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_11_mini.png','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},
	{'u_id':1007,'gr_id':1004,'type':'1','img':'source/glasses/b08.png','e_img':'source/glasses/G08.gif','price':'1200','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_27_mini.png','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},
	{'u_id':1007,'gr_id':1005,'type':'1','img':'source/glasses/b08.png','e_img':'source/glasses/G08.gif','price':'1200','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_29_mini.png','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},
	{'u_id':1007,'gr_id':1006,'type':'1','img':'source/glasses/b08.png','e_img':'source/glasses/G08.gif','price':'1200','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_49_mini.png','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},

	{'u_id':1008,'gr_id':1001,'type':'1','img':'source/glasses/b01.png','e_img':'source/glasses/G09.gif','price':'1900','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_5_mini.png','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':1008,'gr_id':1002,'type':'1','img':'source/glasses/b01.png','e_img':'source/glasses/G09.gif','price':'1900','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_6_mini.png','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':1008,'gr_id':1003,'type':'1','img':'source/glasses/b01.png','e_img':'source/glasses/G09.gif','price':'1900','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_11_mini.png','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':1008,'gr_id':1004,'type':'1','img':'source/glasses/b01.png','e_img':'source/glasses/G09.gif','price':'1900','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_27_mini.png','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':1008,'gr_id':1005,'type':'1','img':'source/glasses/b01.png','e_img':'source/glasses/G09.gif','price':'1900','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_29_mini.png','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':1008,'gr_id':1006,'type':'1','img':'source/glasses/b01.png','e_img':'source/glasses/G09.gif','price':'1900','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_49_mini.png','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},

	{'u_id':1009,'gr_id':1001,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_5_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':1009,'gr_id':1002,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_6_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':1009,'gr_id':1003,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_11_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':1009,'gr_id':1004,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_27_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':1009,'gr_id':1005,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_29_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':1009,'gr_id':1006,'type':'1','img':'source/glasses/b02.png','e_img':'source/glasses/G01.gif','price':'1300','link':'glasses','name':'','description':'','img_o':'source/glasses/shablon_49_mini.png','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'}

    )#_glasses.html
    return carousel_items
def carousel_items_bottles():
    carousel_items_bottles=(
	{'u_id':2001,'img':'source/bottles/b02.png','b_img':'source/bottles/b02_big.png','price':'1300','link':'bottles'},
	{'u_id':2002,'img':'source/bottles/b03.png','b_img':'source/bottles/b03_big.png','price':'1400','link':'bottles'},
	{'u_id':2003,'img':'source/bottles/b04.png','b_img':'source/bottles/b04_big.png','price':'1500','link':'bottles'},
	{'u_id':2004,'img':'source/bottles/b05.png','b_img':'source/bottles/b05_big.png','price':'1600','link':'bottles'},
	{'u_id':2005,'img':'source/bottles/b06.png','b_img':'source/bottles/b06_big.png','price':'1100','link':'bottles'},
	{'u_id':2006,'img':'source/bottles/b07.png','b_img':'source/bottles/b07_big.png','price':'1600','link':'bottles'},
	{'u_id':2007,'img':'source/bottles/b01.png','b_img':'source/bottles/b01_big.png','price':'1900','link':'bottles'})#_bottles.html
    return carousel_items_bottles
def mob_menu():
    mob_menu={'pos0':'Меню'} #_h_menu.html
    return mob_menu
def menu():
    menu={'main':'ГЛАВНАЯ','/glasses':'Сделать заказ','/bottles':'БУТЫЛКИ','index.html#work':'НАШИ РАБОТЫ','index.html#delivery':'ДОСТАВКА'} #_h_menu.html
    return menu
def block2():
    block2={'b2_title':'Свадебные бокалы с гравировкой','b2_text':Markup(u'''<p><em>Это тот день, который вы ждете с трепетом и будете вспоминать всю жизнь, день, который никогда не повторится. Сохранить память об этом важном событии и создать оригинальный аксессуар можно с помощью гравировки на свадебных бокалах. Мы с радостью поможем сделать главный день в вашей жизни оригинальным и незабываемым!</em></p>'''),'b2_text2':Markup(u'''<em> День вашей свадьбы должен быть особенным и оставить прекрасные воспоминания!</em></p>
<p style="text-align: center;"><em>Lady-MarLene оказывает услуги <strong>индивидуальной гравировки</strong>:</em><br />
<em> &#8212; на <strong>бокалах</strong> для молодоженов,</em><br />
<em> &#8212; на <strong>бутылках</strong> шампанского для дня свадьбы, в благодарность родителям, на первую годовщину и рождение первенца,</em><br />
<em> &#8212; на <strong>замочках</strong></em></p>
<p style="text-align: center;"><em>Мы любим и ценим свою работу, стараясь сделать ваш незабываемый день оригинальным!</em></p>'''),'b2_glass':'СВАДЕБНЫЕ БОКАЛЫ','b2_glass_line1':'c индивидуальной гравировкой','b3_grav_line':'Разновидности гравировки'} #_blokc2.html
    return block2
def type_index():
    type_index=({'type':'1','text':''},{'type':'2','text':''})#_glasses.html
    return type_index
def type_index_bottles():
     #type:1 - День свадьбы
	 #type:2 - Для родителей
	 #type:3 - Годовщина свадьбы
	 #type:4 - На первенца
    type_index_bottles=({'type':'1','text':'День свадьбы'},{'type':'2','text':'Для родителей'},{'type':'3','text':'Годовщина свадьбы'},{'type':'4','text':'На первенца'})#_glasses.html
    return type_index_bottles
def type_index_shablon():

    type_index_shablon=(
	{'id':1001,'g_id':'10011','b_img':'source/glasses/shablon_5_mini.png','img':'source/glasses/shablon_5_mini.png','g_img':'static/lady/images/grav-1.svg','link':'glasses'},
	{'id':1002,'g_id':'10012','b_img':'source/glasses/shablon_6_mini.png','img':'source/glasses/shablon_6_mini.png','g_img':'static/lady/images/grav-4.svg','link':'glasses'},
	{'id':1003,'g_id':'10013','b_img':'source/glasses/shablon_11_mini.png','img':'source/glasses/shablon_11_mini.png','g_img':'static/lady/images/grav-1.svg','link':'glasses'},
	{'id':1004,'g_id':'10014','b_img':'source/glasses/shablon_27_mini.png','img':'source/glasses/shablon_27_mini.png','g_img':'static/lady/images/grav-1.svg','link':'glasses'},
	{'id':1005,'g_id':'10015','b_img':'source/glasses/shablon_29_mini.png','img':'source/glasses/shablon_29_mini.png','g_img':'static/lady/images/grav-1.svg','link':'glasses'},
	{'id':1006,'g_id':'10016','b_img':'source/glasses/shablon_49_mini.png','img':'source/glasses/shablon_49_mini.png','g_img':'static/lady/images/grav-2.svg','link':'glasses'})
    return type_index_shablon
def type_index_examples():

    type_index_examples=(
	{'e_id':'10011','img':'lady/images/examples/DPP_0035.png','link':'examples'},
	{'e_id':'10012','img':'lady/images/examples/DPP_0039.png','link':'examples'},
	{'e_id':'10013','img':'lady/images/examples/DPP_0054.png','link':'examples'},
	{'e_id':'10014','img':'lady/images/examples/DPP_0026.png','link':'examples'},
	{'e_id':'10015','img':'lady/images/examples/DPP_0057.png','link':'examples'},
	{'e_id':'10016','img':'lady/images/examples/DPP_0023.png','link':'examples'},
	{'e_id':'10012','img':'lady/images/examples/DPP_0055.png','link':'examples'},
	{'e_id':'10013','img':'lady/images/examples/DPP_0045.png','link':'examples'})
    return type_index_examples
def cart_items():
    cart_items=(
	{'u_id':'10011','name':'name1','gr_id':1001,'id':1001,'type':'1','img':'source/glasses/shablon_5_mini.png','img_o':'source/glasses/shablon_5_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':'10012','name':'name1','gr_id':1001,'id':1002,'type':'1','img':'source/glasses/shablon_6_mini.png','img_o':'source/glasses/shablon_6_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':'10013','name':'name1','gr_id':1001,'id':1003,'type':'1','img':'source/glasses/shablon_11_mini.png','img_o':'source/glasses/shablon_11_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':'10014','name':'name1','gr_id':1001,'id':1004,'type':'1','img':'source/glasses/shablon_27_mini.png','img_o':'source/glasses/shablon_27_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':'10015','name':'name1','gr_id':1001,'id':1005,'type':'1','img':'source/glasses/shablon_29_mini.png','img_o':'source/glasses/shablon_29_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':'10016','name':'name1','gr_id':1001,'id':1006,'type':'1','img':'source/glasses/shablon_49_mini.png','img_o':'source/glasses/shablon_49_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},

	{'u_id':'10021','name':'name2','gr_id':1002,'id':1001,'type':'1','img':'source/glasses/shablon_5_mini.png','img_o':'source/glasses/shablon_5_mini.png','price':'1400','link':'glasses','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},
	{'u_id':'10022','name':'name2','gr_id':1002,'id':1002,'type':'1','img':'source/glasses/shablon_6_mini.png','img_o':'source/glasses/shablon_6_mini.png','price':'1400','link':'glasses','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},
	{'u_id':'10023','name':'name2','gr_id':1002,'id':1003,'type':'1','img':'source/glasses/shablon_11_mini.png','img_o':'source/glasses/shablon_11_mini.png','price':'1400','link':'glasses','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},
	{'u_id':'10024','name':'name2','gr_id':1002,'id':1004,'type':'1','img':'source/glasses/shablon_27_mini.png','img_o':'source/glasses/shablon_27_mini.png','price':'1400','link':'glasses','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},
	{'u_id':'10025','name':'name2','gr_id':1002,'id':1005,'type':'1','img':'source/glasses/shablon_29_mini.png','img_o':'source/glasses/shablon_29_mini.png','price':'1400','link':'glasses','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},
	{'u_id':'10026','name':'name2','gr_id':1002,'id':1006,'type':'1','img':'source/glasses/shablon_49_mini.png','img_o':'source/glasses/shablon_49_mini.png','price':'1400','link':'glasses','img_g':'source/glasses/b03_big.png','img_r':'source/glasses/G03_big_3.png'},

	{'u_id':'10031','name':'name3','gr_id':1003,'id':1001,'type':'1','img':'source/glasses/shablon_5_mini.png','img_o':'source/glasses/shablon_5_mini.png','price':'1500','link':'glasses','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},
	{'u_id':'10032','name':'name3','gr_id':1003,'id':1002,'type':'1','img':'source/glasses/shablon_6_mini.png','img_o':'source/glasses/shablon_6_mini.png','price':'1500','link':'glasses','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},
	{'u_id':'10033','name':'name3','gr_id':1003,'id':1003,'type':'1','img':'source/glasses/shablon_11_mini.png','img_o':'source/glasses/shablon_11_mini.png','price':'1500','link':'glasses','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},
	{'u_id':'10034','name':'name3','gr_id':1003,'id':1004,'type':'1','img':'source/glasses/shablon_27_mini.png','img_o':'source/glasses/shablon_27_mini.png','price':'1500','link':'glasses','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},
	{'u_id':'10035','name':'name3','gr_id':1003,'id':1005,'type':'1','img':'source/glasses/shablon_29_mini.png','img_o':'source/glasses/shablon_29_mini.png','price':'1500','link':'glasses','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},
	{'u_id':'10036','name':'name3','gr_id':1003,'id':1006,'type':'1','img':'source/glasses/shablon_49_mini.png','img_o':'source/glasses/shablon_49_mini.png','price':'1500','link':'glasses','img_g':'source/glasses/b04_big.png','img_r':'source/glasses/G04_big_1.png'},

	{'u_id':'10041','name':'name4','gr_id':1004,'id':1001,'type':'1','img':'source/glasses/shablon_5_mini.png','img_o':'source/glasses/shablon_5_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},
	{'u_id':'10042','name':'name4','gr_id':1004,'id':1002,'type':'1','img':'source/glasses/shablon_6_mini.png','img_o':'source/glasses/shablon_6_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},
	{'u_id':'10043','name':'name4','gr_id':1004,'id':1003,'type':'1','img':'source/glasses/shablon_11_mini.png','img_o':'source/glasses/shablon_11_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},
	{'u_id':'10044','name':'name4','gr_id':1004,'id':1004,'type':'1','img':'source/glasses/shablon_27_mini.png','img_o':'source/glasses/shablon_27_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},
	{'u_id':'10045','name':'name4','gr_id':1004,'id':1005,'type':'1','img':'source/glasses/shablon_29_mini.png','img_o':'source/glasses/shablon_29_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},
	{'u_id':'10046','name':'name4','gr_id':1004,'id':1006,'type':'1','img':'source/glasses/shablon_49_mini.png','img_o':'source/glasses/shablon_49_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b05_big.png','img_r':'source/glasses/G05_big_3.png'},

	{'u_id':'10051','name':'name5','gr_id':1005,'id':1001,'type':'1','img':'source/glasses/shablon_5_mini.png','img_o':'source/glasses/shablon_5_mini.png','price':'1100','link':'glasses','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},
	{'u_id':'10052','name':'name5','gr_id':1005,'id':1002,'type':'1','img':'source/glasses/shablon_6_mini.png','img_o':'source/glasses/shablon_6_mini.png','price':'1100','link':'glasses','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},
	{'u_id':'10053','name':'name5','gr_id':1005,'id':1003,'type':'1','img':'source/glasses/shablon_11_mini.png','img_o':'source/glasses/shablon_11_mini.png','price':'1100','link':'glasses','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},
	{'u_id':'10054','name':'name5','gr_id':1005,'id':1004,'type':'1','img':'source/glasses/shablon_27_mini.png','img_o':'source/glasses/shablon_27_mini.png','price':'1100','link':'glasses','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},
	{'u_id':'10055','name':'name5','gr_id':1005,'id':1005,'type':'1','img':'source/glasses/shablon_29_mini.png','img_o':'source/glasses/shablon_29_mini.png','price':'1100','link':'glasses','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},
	{'u_id':'10056','name':'name5','gr_id':1005,'id':1006,'type':'1','img':'source/glasses/shablon_49_mini.png','img_o':'source/glasses/shablon_49_mini.png','price':'1100','link':'glasses','img_g':'source/glasses/b06_big.png','img_r':'source/glasses/G06_big_1.png'},

	{'u_id':'10061','name':'name6','gr_id':1006,'id':1001,'type':'1','img':'source/glasses/shablon_5_mini.png','img_o':'source/glasses/shablon_5_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},
	{'u_id':'10062','name':'name6','gr_id':1006,'id':1002,'type':'1','img':'source/glasses/shablon_6_mini.png','img_o':'source/glasses/shablon_6_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},
	{'u_id':'10063','name':'name6','gr_id':1006,'id':1003,'type':'1','img':'source/glasses/shablon_11_mini.png','img_o':'source/glasses/shablon_11_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},
	{'u_id':'10064','name':'name6','gr_id':1006,'id':1004,'type':'1','img':'source/glasses/shablon_27_mini.png','img_o':'source/glasses/shablon_27_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},
	{'u_id':'10065','name':'name6','gr_id':1006,'id':1005,'type':'1','img':'source/glasses/shablon_29_mini.png','img_o':'source/glasses/shablon_29_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},
	{'u_id':'10066','name':'name6','gr_id':1006,'id':1006,'type':'1','img':'source/glasses/shablon_49_mini.png','img_o':'source/glasses/shablon_49_mini.png','price':'1600','link':'glasses','img_g':'source/glasses/b07_big.png','img_r':'source/glasses/G07_big_3.png'},

	{'u_id':'10071','name':'name7','gr_id':1007,'id':1001,'type':'1','img':'source/glasses/shablon_5_mini.png','img_o':'source/glasses/shablon_5_mini.png','price':'1200','link':'glasses','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},
	{'u_id':'10072','name':'name7','gr_id':1007,'id':1002,'type':'1','img':'source/glasses/shablon_6_mini.png','img_o':'source/glasses/shablon_6_mini.png','price':'1200','link':'glasses','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},
	{'u_id':'10073','name':'name7','gr_id':1007,'id':1003,'type':'1','img':'source/glasses/shablon_11_mini.png','img_o':'source/glasses/shablon_11_mini.png','price':'1200','link':'glasses','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},
	{'u_id':'10074','name':'name7','gr_id':1007,'id':1004,'type':'1','img':'source/glasses/shablon_27_mini.png','img_o':'source/glasses/shablon_27_mini.png','price':'1200','link':'glasses','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},
	{'u_id':'10075','name':'name7','gr_id':1007,'id':1005,'type':'1','img':'source/glasses/shablon_29_mini.png','img_o':'source/glasses/shablon_29_mini.png','price':'1200','link':'glasses','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},
	{'u_id':'10076','name':'name7','gr_id':1007,'id':1006,'type':'1','img':'source/glasses/shablon_49_mini.png','img_o':'source/glasses/shablon_49_mini.png','price':'1200','link':'glasses','img_g':'source/glasses/b08_big.png','img_r':'source/glasses/G08_big_1.png'},

	{'u_id':'10081','name':'name8','gr_id':1008,'id':1001,'type':'1','img':'source/glasses/shablon_5_mini.png','img_o':'source/glasses/shablon_5_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':'10082','name':'name8','gr_id':1008,'id':1002,'type':'1','img':'source/glasses/shablon_6_mini.png','img_o':'source/glasses/shablon_6_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':'10083','name':'name8','gr_id':1008,'id':1003,'type':'1','img':'source/glasses/shablon_11_mini.png','img_o':'source/glasses/shablon_11_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':'10084','name':'name8','gr_id':1008,'id':1004,'type':'1','img':'source/glasses/shablon_27_mini.png','img_o':'source/glasses/shablon_27_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':'10085','name':'name8','gr_id':1008,'id':1005,'type':'1','img':'source/glasses/shablon_29_mini.png','img_o':'source/glasses/shablon_29_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':'10086','name':'name8','gr_id':1008,'id':1006,'type':'1','img':'source/glasses/shablon_49_mini.png','img_o':'source/glasses/shablon_49_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},

	{'u_id':'10181','name':'name8','gr_id':1008,'id':1001,'type':'2','img':'source/glasses/shablon_5_mini.png','img_o':'source/glasses/shablon_5_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':'10182','name':'name8','gr_id':1008,'id':1002,'type':'2','img':'source/glasses/shablon_6_mini.png','img_o':'source/glasses/shablon_6_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':'10183','name':'name8','gr_id':1008,'id':1003,'type':'2','img':'source/glasses/shablon_11_mini.png','img_o':'source/glasses/shablon_11_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':'10184','name':'name8','gr_id':1008,'id':1004,'type':'2','img':'source/glasses/shablon_27_mini.png','img_o':'source/glasses/shablon_27_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':'10185','name':'name8','gr_id':1008,'id':1005,'type':'2','img':'source/glasses/shablon_29_mini.png','img_o':'source/glasses/shablon_29_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},
	{'u_id':'10186','name':'name8','gr_id':1008,'id':1006,'type':'2','img':'source/glasses/shablon_49_mini.png','img_o':'source/glasses/shablon_49_mini.png','price':'1900','link':'glasses','img_g':'source/glasses/b01_big-1.png','img_r':'source/glasses/G01_big_1.png'},

	{'u_id':'10091','name':'name1','gr_id':1009,'id':1001,'type':'1','img':'source/glasses/shablon_5_mini.png','img_o':'source/glasses/shablon_5_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':'10092','name':'name1','gr_id':1009,'id':1002,'type':'1','img':'source/glasses/shablon_6_mini.png','img_o':'source/glasses/shablon_6_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':'10093','name':'name1','gr_id':1009,'id':1003,'type':'1','img':'source/glasses/shablon_11_mini.png','img_o':'source/glasses/shablon_11_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':'10094','name':'name1','gr_id':1009,'id':1004,'type':'1','img':'source/glasses/shablon_27_mini.png','img_o':'source/glasses/shablon_27_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':'10095','name':'name1','gr_id':1009,'id':1005,'type':'1','img':'source/glasses/shablon_29_mini.png','img_o':'source/glasses/shablon_29_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},
	{'u_id':'10096','name':'name1','gr_id':1009,'id':1006,'type':'1','img':'source/glasses/shablon_49_mini.png','img_o':'source/glasses/shablon_49_mini.png','price':'1300','link':'glasses','img_g':'source/glasses/b02_big.png','img_r':'source/glasses/G02_big_2.png'},)#_glasses.html
    return cart_items
def cart_items_bottles():
     #type:1 - День свадьбы
	 #type:2 - Для родителей
	 #type:3 - Годовщина свадьбы
	 #type:4 - На первенца
    cart_items_bottles=(
	{'u_id':'10011','name':'name1','id':2001,'type':'1','img':'source/bottles/Untitled-34_mini.png','price':'1300','link':'bottles'},
	{'u_id':'10012','name':'name1','id':2001,'type':'1','img':'source/bottles/W_204_mini.png','price':'1400','link':'bottles'},
	{'u_id':'10013','name':'name1','id':2001,'type':'1','img':'source/bottles/W_206_mini.png','price':'1500','link':'bottles'},
	{'u_id':'10014','name':'name1','id':2001,'type':'1','img':'source/bottles/W_208_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10015','name':'name1','id':2001,'type':'1','img':'source/bottles/W_213_mini.png','price':'1100','link':'bottles'},
	{'u_id':'10016','name':'name1','id':2001,'type':'1','img':'source/bottles/W_216_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100161','name':'name1','id':2001,'type':'1','img':'source/bottles/W_201_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10017','name':'name1','id':2001,'type':'2','img':'source/bottles/45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'10018','name':'name1','id':2001,'type':'2','img':'source/bottles/51_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'10019','name':'name1','id':2001,'type':'2','img':'source/bottles/W_202_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100110','name':'name1','id':2001,'type':'2','img':'source/bottles/W_203_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100111','name':'name1','id':2001,'type':'2','img':'source/bottles/W_207_mini.png','price':'1100','link':'bottles'},
	{'u_id':'100112','name':'name1','id':2001,'type':'2','img':'source/bottles/W_209_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100113','name':'name1','id':2001,'type':'2','img':'source/bottles/W_211_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100114','name':'name1','id':2001,'type':'2','img':'source/bottles/W_212_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100115','name':'name1','id':2001,'type':'2','img':'source/bottles/W_214_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100116','name':'name1','id':2001,'type':'2','img':'source/bottles/W_218_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100117','name':'name1','id':2001,'type':'3','img':'source/bottles/Untitled-45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'100118','name':'name1','id':2001,'type':'3','img':'source/bottles/W_215_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'100119','name':'name1','id':2001,'type':'3','img':'source/bottles/W_220_mini-1.png','price':'1500','link':'bottles'},
	{'u_id':'100120','name':'name1','id':2001,'type':'3','img':'source/bottles/W_221_mini-1.png','price':'1600','link':'bottles'},
	{'u_id':'100121','name':'name1','id':2001,'type':'3','img':'source/bottles/W_222-min.png','price':'1100','link':'bottles'},
	{'u_id':'100122','name':'name1','id':2001,'type':'3','img':'source/bottles/W_223_mini-min.png','price':'1600','link':'bottles'},
	{'u_id':'100123','name':'name1','id':2001,'type':'4','img':'source/bottles/Untitled-18-2_mini.png','price':'1300','link':'bottles'},
	{'u_id':'100124','name':'name1','id':2001,'type':'4','img':'source/bottles/W_205_mini.png','price':'1400','link':'bottles'},
	{'u_id':'100125','name':'name1','id':2001,'type':'4','img':'source/bottles/W_210_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100126','name':'name1','id':2001,'type':'4','img':'source/bottles/W_217_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100127','name':'name1','id':2001,'type':'4','img':'source/bottles/W_219_mini.png','price':'1100','link':'bottles'},

	{'u_id':'10021','name':'name1','id':2002,'type':'1','img':'source/bottles/Untitled-34_mini.png','price':'1300','link':'bottles'},
	{'u_id':'10022','name':'name1','id':2002,'type':'1','img':'source/bottles/W_204_mini.png','price':'1400','link':'bottles'},
	{'u_id':'10023','name':'name1','id':2002,'type':'1','img':'source/bottles/W_206_mini.png','price':'1500','link':'bottles'},
	{'u_id':'10024','name':'name1','id':2002,'type':'1','img':'source/bottles/W_208_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10025','name':'name1','id':2002,'type':'1','img':'source/bottles/W_213_mini.png','price':'1100','link':'bottles'},
	{'u_id':'10026','name':'name1','id':2002,'type':'1','img':'source/bottles/W_216_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100261','name':'name1','id':2002,'type':'1','img':'source/bottles/W_201_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10027','name':'name1','id':2002,'type':'2','img':'source/bottles/45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'10028','name':'name1','id':2002,'type':'2','img':'source/bottles/51_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'10029','name':'name1','id':2002,'type':'2','img':'source/bottles/W_202_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100210','name':'name1','id':2002,'type':'2','img':'source/bottles/W_203_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100211','name':'name1','id':2002,'type':'2','img':'source/bottles/W_207_mini.png','price':'1100','link':'bottles'},
	{'u_id':'100212','name':'name1','id':2002,'type':'2','img':'source/bottles/W_209_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100213','name':'name1','id':2002,'type':'2','img':'source/bottles/W_211_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100214','name':'name1','id':2002,'type':'2','img':'source/bottles/W_212_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100215','name':'name1','id':2002,'type':'2','img':'source/bottles/W_214_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100216','name':'name1','id':2002,'type':'2','img':'source/bottles/W_218_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100217','name':'name1','id':2002,'type':'3','img':'source/bottles/Untitled-45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'100218','name':'name1','id':2002,'type':'3','img':'source/bottles/W_215_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'100219','name':'name1','id':2002,'type':'3','img':'source/bottles/W_220_mini-1.png','price':'1500','link':'bottles'},
	{'u_id':'100220','name':'name1','id':2002,'type':'3','img':'source/bottles/W_221_mini-1.png','price':'1600','link':'bottles'},
	{'u_id':'100221','name':'name1','id':2002,'type':'3','img':'source/bottles/W_222-min.png','price':'1100','link':'bottles'},
	{'u_id':'100222','name':'name1','id':2002,'type':'3','img':'source/bottles/W_223_mini-min.png','price':'1600','link':'bottles'},
	{'u_id':'100223','name':'name1','id':2002,'type':'4','img':'source/bottles/Untitled-18-2_mini.png','price':'1300','link':'bottles'},
	{'u_id':'100224','name':'name1','id':2002,'type':'4','img':'source/bottles/W_205_mini.png','price':'1400','link':'bottles'},
	{'u_id':'100225','name':'name1','id':2002,'type':'4','img':'source/bottles/W_210_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100226','name':'name1','id':2002,'type':'4','img':'source/bottles/W_217_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100227','name':'name1','id':2002,'type':'4','img':'source/bottles/W_219_mini.png','price':'1100','link':'bottles'},

	{'u_id':'10031','name':'name1','id':2003,'type':'1','img':'source/bottles/Untitled-34_mini.png','price':'1300','link':'bottles'},
	{'u_id':'10032','name':'name1','id':2003,'type':'1','img':'source/bottles/W_204_mini.png','price':'1400','link':'bottles'},
	{'u_id':'10033','name':'name1','id':2003,'type':'1','img':'source/bottles/W_206_mini.png','price':'1500','link':'bottles'},
	{'u_id':'10034','name':'name1','id':2003,'type':'1','img':'source/bottles/W_208_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10035','name':'name1','id':2003,'type':'1','img':'source/bottles/W_213_mini.png','price':'1100','link':'bottles'},
	{'u_id':'10036','name':'name1','id':2003,'type':'1','img':'source/bottles/W_216_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100361','name':'name1','id':2003,'type':'1','img':'source/bottles/W_201_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10037','name':'name1','id':2003,'type':'2','img':'source/bottles/45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'10038','name':'name1','id':2003,'type':'2','img':'source/bottles/51_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'10039','name':'name1','id':2003,'type':'2','img':'source/bottles/W_202_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100310','name':'name1','id':2003,'type':'2','img':'source/bottles/W_203_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100311','name':'name1','id':2003,'type':'2','img':'source/bottles/W_207_mini.png','price':'1100','link':'bottles'},
	{'u_id':'100312','name':'name1','id':2003,'type':'2','img':'source/bottles/W_209_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100313','name':'name1','id':2003,'type':'2','img':'source/bottles/W_211_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100314','name':'name1','id':2003,'type':'2','img':'source/bottles/W_212_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100315','name':'name1','id':2003,'type':'2','img':'source/bottles/W_214_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100316','name':'name1','id':2003,'type':'2','img':'source/bottles/W_218_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100317','name':'name1','id':2003,'type':'3','img':'source/bottles/Untitled-45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'100318','name':'name1','id':2003,'type':'3','img':'source/bottles/W_215_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'100319','name':'name1','id':2003,'type':'3','img':'source/bottles/W_220_mini-1.png','price':'1500','link':'bottles'},
	{'u_id':'100320','name':'name1','id':2003,'type':'3','img':'source/bottles/W_221_mini-1.png','price':'1600','link':'bottles'},
	{'u_id':'100321','name':'name1','id':2003,'type':'3','img':'source/bottles/W_222-min.png','price':'1100','link':'bottles'},
	{'u_id':'100322','name':'name1','id':2003,'type':'3','img':'source/bottles/W_223_mini-min.png','price':'1600','link':'bottles'},
	{'u_id':'100323','name':'name1','id':2003,'type':'4','img':'source/bottles/Untitled-18-2_mini.png','price':'1300','link':'bottles'},
	{'u_id':'100324','name':'name1','id':2003,'type':'4','img':'source/bottles/W_205_mini.png','price':'1400','link':'bottles'},
	{'u_id':'100325','name':'name1','id':2003,'type':'4','img':'source/bottles/W_210_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100326','name':'name1','id':2003,'type':'4','img':'source/bottles/W_217_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100327','name':'name1','id':2003,'type':'4','img':'source/bottles/W_219_mini.png','price':'1100','link':'bottles'},

	{'u_id':'10041','name':'name1','id':2004,'type':'1','img':'source/bottles/Untitled-34_mini.png','price':'1300','link':'bottles'},
	{'u_id':'10042','name':'name1','id':2004,'type':'1','img':'source/bottles/W_204_mini.png','price':'1400','link':'bottles'},
	{'u_id':'10043','name':'name1','id':2004,'type':'1','img':'source/bottles/W_206_mini.png','price':'1500','link':'bottles'},
	{'u_id':'10044','name':'name1','id':2004,'type':'1','img':'source/bottles/W_208_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10045','name':'name1','id':2004,'type':'1','img':'source/bottles/W_213_mini.png','price':'1100','link':'bottles'},
	{'u_id':'10046','name':'name1','id':2004,'type':'1','img':'source/bottles/W_216_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100461','name':'name1','id':2004,'type':'1','img':'source/bottles/W_201_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10047','name':'name1','id':2004,'type':'2','img':'source/bottles/45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'10048','name':'name1','id':2004,'type':'2','img':'source/bottles/51_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'10049','name':'name1','id':2004,'type':'2','img':'source/bottles/W_202_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100410','name':'name1','id':2004,'type':'2','img':'source/bottles/W_203_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100411','name':'name1','id':2004,'type':'2','img':'source/bottles/W_207_mini.png','price':'1100','link':'bottles'},
	{'u_id':'100412','name':'name1','id':2004,'type':'2','img':'source/bottles/W_209_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100413','name':'name1','id':2004,'type':'2','img':'source/bottles/W_211_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100414','name':'name1','id':2004,'type':'2','img':'source/bottles/W_212_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100415','name':'name1','id':2004,'type':'2','img':'source/bottles/W_214_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100416','name':'name1','id':2004,'type':'2','img':'source/bottles/W_218_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100417','name':'name1','id':2004,'type':'3','img':'source/bottles/Untitled-45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'100418','name':'name1','id':2004,'type':'3','img':'source/bottles/W_215_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'100419','name':'name1','id':2004,'type':'3','img':'source/bottles/W_220_mini-1.png','price':'1500','link':'bottles'},
	{'u_id':'100420','name':'name1','id':2004,'type':'3','img':'source/bottles/W_221_mini-1.png','price':'1600','link':'bottles'},
	{'u_id':'100421','name':'name1','id':2004,'type':'3','img':'source/bottles/W_222-min.png','price':'1100','link':'bottles'},
	{'u_id':'100422','name':'name1','id':2004,'type':'3','img':'source/bottles/W_223_mini-min.png','price':'1600','link':'bottles'},
	{'u_id':'100423','name':'name1','id':2004,'type':'4','img':'source/bottles/Untitled-18-2_mini.png','price':'1300','link':'bottles'},
	{'u_id':'100424','name':'name1','id':2004,'type':'4','img':'source/bottles/W_205_mini.png','price':'1400','link':'bottles'},
	{'u_id':'100425','name':'name1','id':2004,'type':'4','img':'source/bottles/W_210_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100426','name':'name1','id':2004,'type':'4','img':'source/bottles/W_217_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100427','name':'name1','id':2004,'type':'4','img':'source/bottles/W_219_mini.png','price':'1100','link':'bottles'},

	{'u_id':'10051','name':'name1','id':2005,'type':'1','img':'source/bottles/Untitled-34_mini.png','price':'1300','link':'bottles'},
	{'u_id':'10052','name':'name1','id':2005,'type':'1','img':'source/bottles/W_204_mini.png','price':'1400','link':'bottles'},
	{'u_id':'10053','name':'name1','id':2005,'type':'1','img':'source/bottles/W_206_mini.png','price':'1500','link':'bottles'},
	{'u_id':'10054','name':'name1','id':2005,'type':'1','img':'source/bottles/W_208_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10055','name':'name1','id':2005,'type':'1','img':'source/bottles/W_213_mini.png','price':'1100','link':'bottles'},
	{'u_id':'10056','name':'name1','id':2005,'type':'1','img':'source/bottles/W_216_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100561','name':'name1','id':2005,'type':'1','img':'source/bottles/W_201_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10057','name':'name1','id':2005,'type':'2','img':'source/bottles/45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'10058','name':'name1','id':2005,'type':'2','img':'source/bottles/51_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'10059','name':'name1','id':2005,'type':'2','img':'source/bottles/W_202_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100510','name':'name1','id':2005,'type':'2','img':'source/bottles/W_203_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100511','name':'name1','id':2005,'type':'2','img':'source/bottles/W_207_mini.png','price':'1100','link':'bottles'},
	{'u_id':'100512','name':'name1','id':2005,'type':'2','img':'source/bottles/W_209_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100513','name':'name1','id':2005,'type':'2','img':'source/bottles/W_211_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100514','name':'name1','id':2005,'type':'2','img':'source/bottles/W_212_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100515','name':'name1','id':2005,'type':'2','img':'source/bottles/W_214_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100516','name':'name1','id':2005,'type':'2','img':'source/bottles/W_218_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100517','name':'name1','id':2005,'type':'3','img':'source/bottles/Untitled-45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'100518','name':'name1','id':2005,'type':'3','img':'source/bottles/W_215_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'100519','name':'name1','id':2005,'type':'3','img':'source/bottles/W_220_mini-1.png','price':'1500','link':'bottles'},
	{'u_id':'100520','name':'name1','id':2005,'type':'3','img':'source/bottles/W_221_mini-1.png','price':'1600','link':'bottles'},
	{'u_id':'100521','name':'name1','id':2005,'type':'3','img':'source/bottles/W_222-min.png','price':'1100','link':'bottles'},
	{'u_id':'100522','name':'name1','id':2005,'type':'3','img':'source/bottles/W_223_mini-min.png','price':'1600','link':'bottles'},
	{'u_id':'100523','name':'name1','id':2005,'type':'4','img':'source/bottles/Untitled-18-2_mini.png','price':'1300','link':'bottles'},
	{'u_id':'100524','name':'name1','id':2005,'type':'4','img':'source/bottles/W_205_mini.png','price':'1400','link':'bottles'},
	{'u_id':'100525','name':'name1','id':2005,'type':'4','img':'source/bottles/W_210_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100526','name':'name1','id':2005,'type':'4','img':'source/bottles/W_217_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100527','name':'name1','id':2005,'type':'4','img':'source/bottles/W_219_mini.png','price':'1100','link':'bottles'},

	{'u_id':'10061','name':'name1','id':2006,'type':'1','img':'source/bottles/Untitled-34_mini.png','price':'1300','link':'bottles'},
	{'u_id':'10062','name':'name1','id':2006,'type':'1','img':'source/bottles/W_204_mini.png','price':'1400','link':'bottles'},
	{'u_id':'10063','name':'name1','id':2006,'type':'1','img':'source/bottles/W_206_mini.png','price':'1500','link':'bottles'},
	{'u_id':'10064','name':'name1','id':2006,'type':'1','img':'source/bottles/W_208_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10065','name':'name1','id':2006,'type':'1','img':'source/bottles/W_213_mini.png','price':'1100','link':'bottles'},
	{'u_id':'10066','name':'name1','id':2006,'type':'1','img':'source/bottles/W_216_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100661','name':'name1','id':2006,'type':'1','img':'source/bottles/W_201_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10067','name':'name1','id':2006,'type':'2','img':'source/bottles/45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'10068','name':'name1','id':2006,'type':'2','img':'source/bottles/51_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'10069','name':'name1','id':2006,'type':'2','img':'source/bottles/W_202_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100610','name':'name1','id':2006,'type':'2','img':'source/bottles/W_203_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100611','name':'name1','id':2006,'type':'2','img':'source/bottles/W_207_mini.png','price':'1100','link':'bottles'},
	{'u_id':'100612','name':'name1','id':2006,'type':'2','img':'source/bottles/W_209_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100613','name':'name1','id':2006,'type':'2','img':'source/bottles/W_211_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100614','name':'name1','id':2006,'type':'2','img':'source/bottles/W_212_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100615','name':'name1','id':2006,'type':'2','img':'source/bottles/W_214_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100616','name':'name1','id':2006,'type':'2','img':'source/bottles/W_218_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100617','name':'name1','id':2006,'type':'3','img':'source/bottles/Untitled-45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'100618','name':'name1','id':2006,'type':'3','img':'source/bottles/W_215_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'100619','name':'name1','id':2006,'type':'3','img':'source/bottles/W_220_mini-1.png','price':'1500','link':'bottles'},
	{'u_id':'100620','name':'name1','id':2006,'type':'3','img':'source/bottles/W_221_mini-1.png','price':'1600','link':'bottles'},
	{'u_id':'100621','name':'name1','id':2006,'type':'3','img':'source/bottles/W_222-min.png','price':'1100','link':'bottles'},
	{'u_id':'100622','name':'name1','id':2006,'type':'3','img':'source/bottles/W_223_mini-min.png','price':'1600','link':'bottles'},
	{'u_id':'100623','name':'name1','id':2006,'type':'4','img':'source/bottles/Untitled-18-2_mini.png','price':'1300','link':'bottles'},
	{'u_id':'100624','name':'name1','id':2006,'type':'4','img':'source/bottles/W_205_mini.png','price':'1400','link':'bottles'},
	{'u_id':'100625','name':'name1','id':2006,'type':'4','img':'source/bottles/W_210_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100626','name':'name1','id':2006,'type':'4','img':'source/bottles/W_217_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100627','name':'name1','id':2006,'type':'4','img':'source/bottles/W_219_mini.png','price':'1100','link':'bottles'},

	{'u_id':'10071','name':'name1','id':2007,'type':'1','img':'source/bottles/Untitled-34_mini.png','price':'1300','link':'bottles'},
	{'u_id':'10072','name':'name1','id':2007,'type':'1','img':'source/bottles/W_204_mini.png','price':'1400','link':'bottles'},
	{'u_id':'10073','name':'name1','id':2007,'type':'1','img':'source/bottles/W_206_mini.png','price':'1500','link':'bottles'},
	{'u_id':'10074','name':'name1','id':2007,'type':'1','img':'source/bottles/W_208_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10075','name':'name1','id':2007,'type':'1','img':'source/bottles/W_213_mini.png','price':'1100','link':'bottles'},
	{'u_id':'10076','name':'name1','id':2007,'type':'1','img':'source/bottles/W_216_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100761','name':'name1','id':2007,'type':'1','img':'source/bottles/W_201_mini.png','price':'1600','link':'bottles'},
	{'u_id':'10077','name':'name1','id':2007,'type':'2','img':'source/bottles/45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'10078','name':'name1','id':2007,'type':'2','img':'source/bottles/51_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'10079','name':'name1','id':2007,'type':'2','img':'source/bottles/W_202_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100710','name':'name1','id':2007,'type':'2','img':'source/bottles/W_203_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100711','name':'name1','id':2007,'type':'2','img':'source/bottles/W_207_mini.png','price':'1100','link':'bottles'},
	{'u_id':'100712','name':'name1','id':2007,'type':'2','img':'source/bottles/W_209_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100713','name':'name1','id':2007,'type':'2','img':'source/bottles/W_211_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100714','name':'name1','id':2007,'type':'2','img':'source/bottles/W_212_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100715','name':'name1','id':2007,'type':'2','img':'source/bottles/W_214_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100716','name':'name1','id':2007,'type':'2','img':'source/bottles/W_218_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100717','name':'name1','id':2007,'type':'3','img':'source/bottles/Untitled-45_mini-1.png','price':'1300','link':'bottles'},
	{'u_id':'100718','name':'name1','id':2007,'type':'3','img':'source/bottles/W_215_mini-1.png','price':'1400','link':'bottles'},
	{'u_id':'100719','name':'name1','id':2007,'type':'3','img':'source/bottles/W_220_mini-1.png','price':'1500','link':'bottles'},
	{'u_id':'100720','name':'name1','id':2007,'type':'3','img':'source/bottles/W_221_mini-1.png','price':'1600','link':'bottles'},
	{'u_id':'100721','name':'name1','id':2007,'type':'3','img':'source/bottles/W_222-min.png','price':'1100','link':'bottles'},
	{'u_id':'100722','name':'name1','id':2007,'type':'3','img':'source/bottles/W_223_mini-min.png','price':'1600','link':'bottles'},
	{'u_id':'100723','name':'name1','id':2007,'type':'4','img':'source/bottles/Untitled-18-2_mini.png','price':'1300','link':'bottles'},
	{'u_id':'100724','name':'name1','id':2007,'type':'4','img':'source/bottles/W_205_mini.png','price':'1400','link':'bottles'},
	{'u_id':'100725','name':'name1','id':2007,'type':'4','img':'source/bottles/W_210_mini.png','price':'1500','link':'bottles'},
	{'u_id':'100726','name':'name1','id':2007,'type':'4','img':'source/bottles/W_217_mini.png','price':'1600','link':'bottles'},
	{'u_id':'100727','name':'name1','id':2007,'type':'4','img':'source/bottles/W_219_mini.png','price':'1100','link':'bottles'},
	)#_glasses.html
    return cart_items_bottles
