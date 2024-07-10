import im_wireless as imw
import time

SELF_ADR = 0x30

if __name__ == '__main__' :
	iwc = imw.IMWireClass(SELF_ADR)
	
	try:
		'''
		iwc.Write_920("RPRM")
		time.sleep(0.5)
		rx_data = iwc.Read_920()  
		print(rx_data) 
		while True: 
			#Recive data
			time.sleep(0.5)
			rx_data = iwc.Read_920()
			#If data is not received then return ''(length = 0)
			if len(rx_data) >= 1:
				#print received data      
				print(rx_data, end='')'''
		
		#txdata = "0001100101010100110010011"
		while True:
			txbuf = "TXDU 0002,AA" 
			rx_data = iwc.Read_920()                        # 受信処理           
			#If data is not received then return ''(length = 0)
			if len(rx_data) >= 1:                           # 受信してない時は''が返り値 (長さ0)  
				#print received data      
				print(rx_data, end='')
			
			iwc.Write_920(txbuf)	
			#iwc.Write_920("RDID")
			time.sleep(0.1)
			print("Wink wink")
			rx_data = iwc.Read_920()                        # 受信処理           
			#If data is not received then return ''(length = 0)
			if len(rx_data) >= 1:                           # 受信してない時は''が返り値 (長さ0)  
				#print received data      
				print(rx_data, end='')
			#print("> {} ".format(txbuf))
			time.sleep(0.2)
			#iwc.gpio_clean()
	
		
	except KeyboardInterrupt:
		iwc.gpio_clean()
		print("End")
