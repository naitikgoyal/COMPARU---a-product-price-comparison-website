
from selenium import webdriver

from selenium.webdriver.common.by import By

def connectmysql():
        import mysql.connector as c
        con = c.connect( host="localhost", user="root", passwd="", database="dbscrapping" )
        if con.is_connected():
                print( "database connected successfully" )
        else:
                print( "database not connected" )
        return con



def getimportdata():
        con=connectmysql()

        cur = con.cursor()

        try:
                cur.execute( "select * from vw_importdata" )
                result = cur.fetchall()
                return result
        except:
                con.rollback()
        con.close()

def insertdata():

        con = connectmysql()
        cursor = con.cursor()
        brand = mybrand[i]
        product = myproduct[i]
        description = myphone[i]
        price = myprice[i]
        qry = "insert into oldfinallist values('{}','{}','{}','{}')".format(brand, product, description, price )
        print( qry )
        cursor.execute( qry )
        con.commit()
        print( "data inserted successfully" )
        con.close()

driver = webdriver.Chrome( executable_path="D:\\code project\\scrap\\chromedriver.exe" )

driver.maximize_window()

driver.get( "https://www.amazon.in/" )

driver.implicitly_wait( 10 )

result=getimportdata()

myphone = list()
myprice = list()
mybrand = list()
myproduct =list()



for row in result:

        brandname = row[3]
        productname = row[1]
        data= brandname+" "+productname

        brandid= row[2]
        categoryid = row[0]

        driver.find_element( By.XPATH, "//input[contains (@id, 'search')]" ).send_keys( data )

        driver.find_element( By.XPATH, "//input[@id=\'nav-search-submit-button\']" ).click()

        # driver.find_element( By.XPATH, "//span [text()='samsung']" ).click()

        phonenames = driver.find_elements( By.XPATH, "//span [contains (@class, 'a-color-base a-text-normal')]" )

        prices = driver.find_elements( By.XPATH, "//span [contains (@class, 'a-price-whole')]" )



        for phone in phonenames:
                if (phone.text) != "":
                        myphone.append( phone.text )

        for price in prices:
                if  (price.text) != "":
                        myprice.append( price.text )
                mybrand.append( brandname )
                myproduct.append( productname )

        print( "*" * 50 )

        driver.find_element( By.XPATH, "//input[contains (@id, 'search')]" ).clear()



for i in range( len( myphone ) ):
        insertdata()




print( "part1" )
















