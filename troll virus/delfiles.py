import os
def main():
    while True:
        try:

            A = False
            U = input("enter folder location@>")
            os.chdir(U)
            
            FOLDERLOC = os.listdir()
            print(FOLDERLOC)
            DEL = input(f'are you sure you want to del all the files in {U}? y/n:').lower()

            if 'y' in DEL:
                for file in FOLDERLOC:
                    print(f'{file} -> {file}(remove)')

                    try:
                        os.remove(file)
                    except:
                        continue
                
                A = True
                break


            elif 'n' in DEL:
                break
            else:
                pass


        except:
            if A:
                print("all the files bein removed")
            else:
                print('Something went wrong')
                
if __name__ == '__main__':
    main()