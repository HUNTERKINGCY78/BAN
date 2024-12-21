Azul='\033[1;34m';Branco='\033[1;37m'
##################
from os import system, execl
from sys import argv, executable
from threading import Thread
from time import sleep
from webbrowser import open
from email.message import Message
from smtplib import SMTP
##################
system('git pull')
##################
def init(gmail, password, titulo, body):
	msg=Message()
	msg['Subject'] = titulo
	msg['From'] = gmail
	msg['To'] = 'support@support.whatsapp.com'
	password = password
	msg.add_header('Content-Type', 'text/html')
	msg.set_payload(body )
	s = SMTP('smtp.gmail.com: 587')
	s.starttls()
	s.login(msg['From'], password)
	s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
	sleep(0.0007)

def main():
	while True:
		system('cls||clear')
		op = input('''%s- %sBY%s  :CY78 PROJECT
- %sYT%s  : CY78 PROJECT
- %sTIKTOK%s  : CY78 PROJECT \n\n[%s 1 %s] Nomor larangan  %s|%s Ban number\n[%s 2 %s] Batalkan pelarangan nomor%s|%s Unban number\n[%s 0 %s] Untuk keluar            %s|%s Exit\n%s===> %s'''%(logo,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco,Azul,Branco))
		if op in ['0']:
			break
		#Caso queira adicionar uma nova opção, coloque uma nova string na condicional abaixo.
		elif op in ['1','2']:
			open('https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ');system('termux-open-url https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ')
			try:
				numero=str(input('%s[%s Número %s|%s Number %s] - %s'%(Azul,Branco,Azul,Branco,Azul,Branco)))
		                #Aqui você pode colocar um novo texto ou alterar um já existente.
				op={
				'1':'Nonaktifkan nomor ini |. Saya meminta penonaktifan sementara akun WhatsApp saya, nomor saya: %s'%numero,
				'2':'Nomor saya diblokir secara tidak adil|Wow! Saya sedang bekerja dan tiba-tiba nomor saya diblokir, saya tidak tahu apa yang terjadi, saya memerlukan nomor saya karena untuk bekerja, saya perlu melayani pelanggan saya. Nomor saya: %s'%numero
				}[op]
				gmail=str(input('%s[ %sGmail%s ] -%s '%(Azul,Branco,Azul,Branco)))
				password=str(input('%s[%s Senha %s|%s Password %s] - %s' %(Azul,Branco,Azul,Branco,Azul,Branco)))
                                # Caso queira mudar a quantidade de mensagens que serão enviadas, altere no range
				for _ in range(1):
					Thread(target = init, args = (gmail, password, op.split('|')[0],op.split('|')[1])).start()
			except:
				pass
	system('cls||clear')

logo='''%s
⠤⣤⣤⣤⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⠤⠤⠴⠶⠶⠶⠶
⢠⣤⣤⡄⣤⣤⣤⠄⣀⠉⣉⣙⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠘⣉⢡⣤⡤⠐⣶⡆⢶⠀⣶⣶⡦
⣄⢻⣿⣧⠻⠇⠋⠀⠋⠀⢘⣿⢳⣦⣌⠳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⣡⣴⣧⠻⣄⢸⣿⣿⡟⢁⡻⣸⣿⡿⠁
⠈⠃⠙⢿⣧⣙⠶⣿⣿⡷⢘⣡⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣷⣝⡳⠶⠶⠾⣛⣵⡿⠋⠀⠀
⠀⠀⠀⠀⠉⠻⣿⣶⠂⠘⠛⠛⠛⢛⡛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠀⠉⠒⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⡁⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
  
  
%sAtive a opção de apps menos seguros. %s|%s Turn on the less secure apps option.\n'''%(Azul,Branco,Azul,Branco)
##################
if __name__ == '__main__':
	main()
