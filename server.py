import socket

# AF_INET api 4 adresiga asoslangani uchun uni uzimizga yuklab olamiz. SOCK_STREAM esa aynan malum bir protokllarni qabul qilish uchun ishlatilinadi.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# bind clinetga malumotlarni junatish uchun port va host raqamlarini kiritishga yordam beradi
s.bind((socket.gethostname(), 1234))

# aynan shu hostni tinglash uchun unga listen metodini qullaymiz
s.listen()

while True:
    # clientsocket va manzil uzgaruvchilariga accept metodidan foydalanib malumotni joylashtirdi 
    clientsocket, manzil = s.accept()
    print(f"Siz {manzil} nomli clientga ulandingiz")

    #malumotlarni foydalanuvchiga qulay kurinishi uchun bytes metodidan foydalaib utf-8 kurinishida yuboramiz
    clientsocket.send(bytes("salom , siz muoffaqiyatli bog'landingiz", "utf-8"))
