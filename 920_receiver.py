import im_wireless as imw
import time
import RPi.GPIO as GPIO

SELF_ADR = 0x30
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

# Main
if __name__ == '__main__':                      
    iwc = imw.IMWireClass(SELF_ADR)                # classの初期化
    
    try:                                                         
        while True: 
            #Recive data
            rx_data = iwc.Read_920()                        # 受信処理           
            #If data is not received then return ''(length = 0)
            if len(rx_data) >= 1:                           # 受信してない時は''が返り値 (長さ0)  
                #print received data      
                print(rx_data, end='')                          # 受信データを画面表示
                msg = GPIO.input(27)
                print("AFTER iwc.Read: ", msg)
                
                    
                #if data >= 11 (11 is node number of received data+ RSSI)
                if len(rx_data) >= 11:                          # 11は受信データのノード番号+RSSI等の長さ
                    if (rx_data[2]==',' and    
                        rx_data[7]==',' and rx_data[10]==':'):
                        #Extract slave ID (Transmitter)
                        rxid = rx_data[3:7]                             # 子機(送信機)のIDを抽出
                        #No need for CR+RL Command
                        txbuf = 'TXDA' + rxid                           # コマンドにCR+LFはいらない
                        print('>', txbuf)  
                        #Send Command to slave                             
                        iwc.Write_920(txbuf)                            # コマンドを送信
                        msg2 = GPIO.input(27)
                        print("AFTER iwc.Write(TXDA rxdi): ", msg2)
                
    except KeyboardInterrupt:                       # Ctrl + C End
        iwc.gpio_clean()
        print ('END')
