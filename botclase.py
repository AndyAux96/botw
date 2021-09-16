from selenium import webdriver
import time

browser=webdriver.Edge(executable_path='./driver/msedgedriver.exe')

def botwhatsapp():
    browser.get("https://web.whatsapp.com/")
    time.sleep(5)

    espera=True

    while espera: 
        print ("ESTOY ESPERANDO")
        espera=validarQR()
        time.sleep(2)

        if espera==False:
            print("Ya se autenticó")
            break

    seleccionarChat("Jhino")
    time.sleep(2)
    enviarMensaje("Soy un Bot")

#Revisa cada segundo si el canvas existe (QR)
def validarQR():
    try:
        element = browser.find_element_by_tag_name("canvas")
    except:
        return False
    return True

def seleccionarChat(nombre : str):
    buscando=True
    while True:  
        print("Buscando Chat")
        elements = browser.find_elements_by_tag_name("span")
        for element in elements:
          if element.text == nombre:
            print("Encontramos el chat")
            element.click()
            buscando=False
            break
        
def enviarMensaje(mensaje:str):
    chatbox=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    chatbox.send_keys(mensaje)
    enviar()

def enviar():
    element=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    element.click()
    #Min 49:55  ::::  https://www.youtube.com/watch?v=NXlCgWZkKxo

    

botwhatsapp()