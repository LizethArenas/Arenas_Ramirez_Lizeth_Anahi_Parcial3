import pywhatkit

try:
    # pywhatkit.sendwhatmsg("+524448279388", "hola desde python", 18,10)
    # pywhatkit.sendwhatmsg_instantly("+524448279388", "hola desde python")
    pywhatkit.sendwhatmsg_to_group_instantly("HMSd7sLfFPy4ivP0YtAqvE", "Hola", 10, True,3)
    print("Mensaje enviado") 
except:
   print("Error")