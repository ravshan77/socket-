import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

# recv metodi serverdan malumotlarni qabul qiliadi va unga argument sifatida maximum malumotlar uzunligini qabul qilishda cheklov quyishimiz mumkin
malumotlar = s.recv(200)

# recv metodida kelgan malumotlarni decode orqali qayta ishlab foydalanuvchiga utf-8 kurinishida chop etamiz
print(malumotlar.decode('utf-8'))
