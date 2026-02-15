import psutil 
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage


def CreateLog(FolderName):
    Border = "-"*50
    Ret = os.path.exists(FolderName)
    if (Ret == True):
        if(os.path.isdir(FolderName)==False):
            print("Unable to create folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")
    
    fobj.write(Border+"\n")
    fobj.write("----Marvellous Platfrom Surveillance System----\n")
    fobj.write("Log Created at : " +time.ctime()+"\n")
    fobj.write(Border +"\n\n")

    fobj.write("CPU Usage : %.2f %%\n" %psutil.cpu_percent())
    mem = psutil.virtual_memory()
    fobj.write("RAM Usage : %.2f %%\n" %mem.percent)
    fobj.write(Border + "\n\n")

    Data = ProcessScan()

    TopMemory = sorted(Data,
                    key=lambda X: X.get("rss"),
                    reverse=True)[:10]

    fobj.write("Top 10 Memory Consuming Processes\n")
    fobj.write(Border + "\n")

    for info in TopMemory:

        rss_mb = info.get("rss") / (1024 * 1024)
        vms_mb = info.get("vms") / (1024 * 1024)

        fobj.write("Process Name : %s\n" % info.get("name"))
        fobj.write("PID : %s\n" % info.get("pid"))
        fobj.write("Memory RSS : %.2f MB\n" % rss_mb)
        fobj.write("Memory VMS : %.2f MB\n" % vms_mb)
        fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
        fobj.write(Border + "\n")

    for info in Data:

        rss_mb = info.get("rss") / (1024 * 1024)
        vms_mb = info.get("vms") / (1024 * 1024)

        fobj.write("Process Name : %s\n" % info.get("name"))
        fobj.write("PID : %s\n" % info.get("pid"))
        fobj.write("CPU %% : %.2f\n" % info.get("cpu_percent"))
        fobj.write("Memory RSS : %.2f MB\n" % rss_mb)
        fobj.write("Memory VMS : %.2f MB\n" % vms_mb)
        fobj.write("Memory %% : %.2f\n" % info.get("memory_percent"))
        fobj.write("Threads Count : %s\n" % info.get("threads"))
        fobj.write("Files Count : %s\n" % info.get("open_files"))
        fobj.write("TimeStamp : %s\n" % info.get("timestamp"))
        fobj.write(Border + "\n")

    fobj.write("--------------End of Log File---------------\n")
    fobj.write(Border + "\n")

    fobj.close()

    return FileName

def ProcessScan():
        listprocess = []

        for proc in psutil.process_iter():
            try:
                proc.cpu_percent()
            except:
                pass
        time.sleep(1)

        for proc in psutil.process_iter():
            try:
                info = proc.as_dict(attrs=["pid","name"])
                info["cpu_percent"] = proc.cpu_percent(None)
                meminfo = proc.memory_info()
                info["rss"] = meminfo.rss
                info["vms"] = meminfo.vms
                info["memory_percent"] = proc.memory_percent()
                info["threads"] = proc.num_threads()

                try:
                    info["open_files"] = len(proc.open_files())
                except:
                    info["open_files"] = "Access Denied"

                info["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
                listprocess.append(info)

            except (psutil.NoSuchProcess , psutil.AccessDenied ,psutil.ZombieProcess):
                pass
        return listprocess

def send_mail(sender,app_password,receiver, subject,body, logfile):

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    with open(logfile, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(logfile)

    msg.add_attachment(file_data,
                       maintype="application",
                       subtype="octet-stream",
                       filename=file_name)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()


def main():
    Border = "-"*50
    print(Border)
    print("-----Marvellous Platform Surveillance System-----")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] in ["--h","--H"]):
            print("This script is used to : ")
            print("1 : Monitor threads of each process")
            print("2 : Monitor open files count")
            print("3 : Monitor RSS and VMS memory")
            print("4 : Display top 10 memory consuming processes")
            print("5 : Create periodic logs")

        elif(sys.argv[1] in ["--u","--U"]):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : Time in minutes")
            print("DirectoryName : Folder to store logs")

        else:
            print("Invalid option")

    elif(len(sys.argv) == 4):

        try:
            
            DirectoryName = sys.argv[1]
            ReceiveMail = sys.argv[2]
            TimeInterval = int(sys.argv[3])
        except:
            print("Invalid input format")
            return
        
        sender_email = "shreyaborate2001@gmail.com"

        app_password = "fkdr wpvc yhnt zatc"

        schedule.every(TimeInterval).minutes.do(CreateLogAndSend,DirectoryName,sender_email,app_password,ReceiveMail)

       
        print("Platform Surveillance System Started Successfully")
        print("Press Ctrl + C to stop the execution")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of command line argguments")
        print("Use --h or --u for help")

    print(Border)
    print("---------Thank You for using our script---------")

if __name__ == "__main__":
   main()



