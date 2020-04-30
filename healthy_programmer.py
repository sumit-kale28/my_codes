#Healthy Programmer
print("--------------Healthy Programmer-----------------")
from playsound import playsound
from datetime import datetime
from time import time

def def_log(msg):
    with open ("log_data.txt","a") as f:
        tym=datetime.now()
        f.write(f"{msg}:\t {tym}\n")

if __name__ == '__main__':
        name=input("Enter Your name:")
        playsound("good.mp3")
        def_log("Morning Loggin Time")
        init_water=time()
        init_eye=time()
        init_exe=time()
        water_sec=5
        eye_sec=21
        exe_sec=41
        while True:
            if time()-init_water > water_sec:
                print(f"Its time to drink a glass of water")
                playsound("water.mp3")
                def_log("Drank Water at")
                init_water = time()

            if time() - init_eye > eye_sec:
                print(f"Its time to do some eye exercise")
                playsound("eye.mp3")
                def_log("Done Eye Exercise ")
                init_eye = time()

            if time() - init_exe > exe_sec:
                print(f"Its time to do some physical exercise")
                playsound("hello.mp3")
                def_log("Done Physical exercise at")
                init_exe = time()



