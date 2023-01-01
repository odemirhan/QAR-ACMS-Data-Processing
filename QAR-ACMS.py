import glob
from zipfile import ZipFile
import shutil
import os
from datetime import datetime
import subprocess
import time

files=glob.glob(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS/*.zip')  #bunu degistir 
QAR= 'ADR-QAR'
ACMS= 'ACMS-unformatted'
ACARS1='EN1ACARS'
ACARS2='EN2ACARS'
pathtomodule=r'C:\Users\Engineering\Desktop\Silme- Python Script'
today=datetime.strftime(datetime.now(), '%Y-%#m-%#d')
if len(files)>0:
    for cnt0 in range(len(files)):
        if QAR in files[cnt0]:
            with ZipFile(files[cnt0], 'r') as zipObj:
               try:
                   zipObj.extractall(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\QARRAW')
                   rawfiles=glob.glob(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\QARRAW/*.raw')
                   if len(rawfiles)>0:
                       for cnt1 in range(len(rawfiles)):
                           QARfilename=str(rawfiles[cnt1])
                           QARfilename=QARfilename.replace(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\QARRAW'
                                                              ,"")
                           Aircraft=QARfilename[1:7]
                           print(Aircraft+"-QAR")
                           try:                                   
                               shutil.move(rawfiles[cnt1], '//10.1.0.155/Aerobytes/Auto Replay/'+Aircraft)
                           except:
                               pass
                           with open(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\LOG\QAR/'+ today + ".txt","a") as file:
                               strfile=str(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\QARRAW')
                               strQAR=str(rawfiles[cnt1]).replace(strfile,'')
                               file.write(str(rawfiles[cnt1])+"\n")
                   shutil.rmtree(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\QARRAW')
               except:
                    pass
                    
            
            
        elif ACMS in files[cnt0]:
            with ZipFile(files[cnt0], 'r') as zipObj:
                try:
           
                   zipObj.extractall(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\ACMSRAW')
                   files1=glob.glob(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\ACMSRAW/*.zip')
                   with ZipFile(files1[0], 'r') as zipObj2:
                       zipObj2.extractall(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\ACMSRAW\dummy')
                       files2=glob.glob(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\ACMSRAW\dummy/*')
                       files3=glob.glob(files2[0]+"/*")
                       files35=glob.glob(files3[0]+"/*")
                       files4=glob.glob(files35[0]+"/*")
                       if len(files4)>0:
                           for cnt1 in range(len(files4)):
                               ACMSfilename=str(files4[cnt1])
                               ACMSfilename=ACMSfilename.split(os.sep)
                               ACMSfilename=ACMSfilename[-1]
                               Aircraft=ACMSfilename[0:6]
                               print(Aircraft+"-ACMS")
                               try:                                   
                                   shutil.move(files4[cnt1], r'C:\Users\Engineering\Desktop\Silme- Python Script\ACMS/'+Aircraft)
                               except:
                                   pass
                               with open(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\LOG\ACMS/'+ today + ".txt","a") as file:
                                   strfile=str(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\ACMSRAW\dummy')
                                   strQAR=str(files4[cnt1]).replace(strfile,'')
                                   file.write(strQAR+"\n")
                   shutil.rmtree(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\ACMSRAW')
                except:
                    pass
        elif ACARS1 in files[cnt0] or ACARS2 in files[cnt0]:
            with ZipFile(files[cnt0], 'r') as zipObj:
                try:
           
                   zipObj.extractall(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\ACARSRAW')
                   files1=glob.glob(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\ACARSRAW/*')
                   for cnt2 in range(len(files1)):
                       if not files1[cnt2].endswith('.xml'):
                            ACARSfilename=str(files1[cnt2]).split(os.sep)
                            ACARSfilename=ACARSfilename[-1]
                            Aircraft=ACARSfilename[0:6]
                            print(Aircraft+"-ACARS")
                            try:                                   
                                shutil.move(files1[cnt2], r'C:\Users\Engineering\Desktop\Silme- Python Script\ACMS/'+Aircraft)
                            except Exception as E:
                                print(E)
                                pass
                            with open(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\LOG\ACARS/'+ today + ".txt","a") as file:
                               strfile=str(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\ACARSRAW')
                               strQAR=str(files1[cnt2]).replace(strfile,'')
                               file.write(strQAR+"\n")
                   shutil.rmtree(r'C:\Users\Engineering\Documents\SecureClient\ESDD\Downloads_after_RTS\ACARSRAW')
                except:
                    pass        
                                       
    for cnt12 in range(len(files)):
        os.remove(files[cnt12])
p=subprocess.Popen(os.path.join(pathtomodule, "launch_MEL.bat"), cwd=pathtomodule)
p.wait()
filesACMS=glob.glob(r'C:\Users\Engineering\Desktop\Silme- Python Script\ACMS/*')

for cnt0 in range(len(filesACMS)):
    subfilesACMS=glob.glob(filesACMS[cnt0]+"/*")
    for cnt1 in range(len(subfilesACMS)):
        os.remove(subfilesACMS[cnt1])
print("succesfull")
time.sleep(5)
