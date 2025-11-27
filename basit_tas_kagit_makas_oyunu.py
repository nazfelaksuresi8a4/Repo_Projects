import os 

boolean = True

def quest1(n):
    global boolean
    while boolean:
        user_input = str(input('1-taş\n2-kağıt\n3-makas\n\n*Seçim: '))

        if n == '1' and user_input == '2':
            print('yenildin')
            break

        elif n == '2' and user_input == '3':
            print('yenildin')
            break

        elif n == '3' and user_input == '1':
            print('yenildin')
            break
        
        elif n == 'test':
            pass

        else:
            print('Kazandın')

        dat = quest2(user_input)

def quest2(m):
    global boolean
    while boolean:
        user_input = str(input('1-taş\n2-kağıt\n3-makas\n\n*Seçim: '))

        try:
            if m == '1' and user_input == '2':
                print('yenildin')
                break

            elif m == '2' and user_input == '3':
                print('yenildin')
                break

            elif m == '3' and user_input == '1':
                print('yenildin')
                break
            
            elif m == 'test':
                pass

            else:
                print('Kazandın')
        except Exception as e0:
            print(f'from quest-2 function excepted with exception; {e0}')
        
        finally:
            QINPUT = input('devam etmek için ENTER oyundan çıkmak için exit\n\n>>>>> ')

            if QINPUT.lower() == 'exit':
                try:
                    boolean = False
                except:
                    print('çıkış başarısız')
                finally:
                    print('Çıkış başarılı')

            os.system('cls')

        dat = quest1(user_input)

def igniter(k):
    test = quest1(k)

    return test

dat = 'test'
test_data = igniter(dat)
