import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage
def WriteLog(message):

    if not os.path.exists("Logs"):
        os.mkdir("Logs")

    logfile = os.path.join("Logs", "Log.txt")

    with open(logfile, "a") as f:
        f.write(str(time.ctime()) + " : " + message + "\n")

def SendEmail(zip_file):

    try:
        sender_email = "shreyaborate2001@gmail.com"

        app_password = "fkdr wpvc yhnt zatc"

        receiver_email = "shreyaborate756@gmail.com"


        msg = EmailMessage()
        msg["Subject"] = "Backup Completed"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content("Backup completed successfully.\nAttached files included.")

        with open("Logs/Log.txt", "rb") as f:
            msg.add_attachment(f.read(),
                               maintype="application",
                               subtype="octet-stream",
                               filename="Log.txt")

        with open(zip_file, "rb") as f:
            msg.add_attachment(f.read(),
                               maintype="application",
                               subtype="zip",
                               filename=zip_file)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)

        WriteLog("Email sent successfully")

    except Exception as e:
        WriteLog("Email Error : " + str(e))

def calculate_hash(path):

    hobj = hashlib.md5()

    try:
        with open(path, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                hobj.update(data)

        return hobj.hexdigest()

    except Exception as e:
        WriteLog("Hash Error : " + str(e))
        return None

def BackupFiles(Source, Destination):

    copied_files = []

    try:
        os.makedirs(Destination, exist_ok=True)

        for root, dirs, files in os.walk(Source):
            for file in files:

                # Exclude extensions
                if file.endswith((".tmp", ".log", ".exe")):
                    continue

                src_path = os.path.join(root, file)
                relative = os.path.relpath(src_path, Source)
                dest_path = os.path.join(Destination, relative)

                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                if ((not os.path.exists(dest_path)) or
                        (calculate_hash(src_path) != calculate_hash(dest_path))):

                    shutil.copy2(src_path, dest_path)
                    copied_files.append(relative)

        return copied_files

    except Exception as e:
        WriteLog("Backup Error : " + str(e))
        return []


def make_zip(folder):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    full_path = os.path.join(root, file)
                    relative = os.path.relpath(full_path, folder)
                    z.write(full_path, relative)

        return zip_name

    except Exception as e:
        WriteLog("Zip Error : " + str(e))
        return None

def UpdateHistory(file_count, zip_file):

    try:
        size = os.path.getsize(zip_file)

        with open("BackupHistory.txt", "a") as f:
            f.write(f"{time.ctime()} | Files: {file_count} | Size: {size} bytes | Zip: {zip_file}\n")

    except Exception as e:
        WriteLog("History Error : " + str(e))


def ShowHistory():

    try:
        with open("BackupHistory.txt", "r") as f:
            print(f.read())

    except FileNotFoundError:
        print("No history available")

def RestoreBackup(zip_file, destination):

    try:
        if not os.path.exists(zip_file):
            WriteLog("Zip file not found")
            return

        with zipfile.ZipFile(zip_file, 'r') as z:
            z.extractall(destination)

        WriteLog("Restore completed successfully")

    except Exception as e:
        WriteLog("Restore Error : " + str(e))

def MarvellousDataShieldStart(Source):

    WriteLog("Backup Started")

    files = BackupFiles(Source, "MarvellousBackup")

    zip_file = make_zip("MarvellousBackup")

    WriteLog("Backup Completed")
    WriteLog("Files Copied : " + str(len(files)))
    WriteLog("Zip Created : " + str(zip_file))

    UpdateHistory(len(files), zip_file)

    SendEmail(zip_file)

def main():

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--history"):
            ShowHistory()

        elif(sys.argv[1] == "--h"):
            print("Usage:")
            print("Script.py TimeInterval SourceDirectory")
            print("Script.py --restore ZipFile Destination")
            print("Script.py --history")

        else:
            print("Invalid option")

    elif(len(sys.argv) == 3):

        interval = int(sys.argv[1])
        directory = sys.argv[2]

        if not os.path.isdir(directory):
            print("Invalid Source Directory")
            return

        schedule.every(interval).minutes.do(
            MarvellousDataShieldStart, directory)

        print("Marvellous Data Shield System Started")
        print("Press Ctrl + C to stop")

        while True:
            schedule.run_pending()
            time.sleep(1)

    elif(len(sys.argv) == 4 and sys.argv[1] == "--restore"):

        RestoreBackup(sys.argv[2], sys.argv[3])

    else:
        print("Invalid arguments")


if __name__ == "__main__":
    main()
