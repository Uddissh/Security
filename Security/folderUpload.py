import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
#
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.A9FeQ_N4kywqTRnWAvhsiAkh1cm6fC9isOALleah33vGsiXvhon0Rbwif02pRAz8oo0zwofC_5atz1pWT0ejzARX1Y9Lrybz8eYLadw680Zy8fRE6Tc_EBEyB--Z7brjDpkPsa0'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("enter the full path to upload to dropbox:- ")

    # API v2
    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")

main()