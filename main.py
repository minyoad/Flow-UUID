# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))     

from uuid import uuid4
import pyperclip

from flowlauncher import FlowLauncher,FlowLauncherAPI

class UUID(FlowLauncher):
    def __init__(self):
        self.generated_uuid = str(uuid4())
        super().__init__()

    def query(self, query):
        items=[]
        
        # lower case
        items.append({
            "Title":"小写：{}".format(self.generated_uuid),
            "SubTitle": "Click to copy",
            "IcoPath": "icon.png",
            "JsonRPCAction": {
                "method": "copy_to_clipboard",
                "parameters": [self.generated_uuid]
            }
        })       
        
        
        # upper case
        data=self.generated_uuid.upper()
        items.append({
            "Title":"大写：{}".format(data),
            "SubTitle": "Click to copy",
            "IcoPath": "icon.png",
            "JsonRPCAction": {
                "method": "copy_to_clipboard",
                "parameters": [data]
            }
        })
        
        # lower case
        data=self.generated_uuid.replace('-','')
        items.append({
            "Title":"去掉[-]小写：{}".format(data),
            "SubTitle": "Click to copy",
            "IcoPath": "icon.png",
            "JsonRPCAction": {
                "method": "copy_to_clipboard",
                "parameters": [data]
            }
        })
        
        data=self.generated_uuid.upper().replace('-','')
        items.append({
            "Title":"去掉[-]大写：{}".format(data),
            "SubTitle": "Click to copy",
            "IcoPath": "icon.png",
            "JsonRPCAction": {
                "method": "copy_to_clipboard",
                "parameters": [data]
            }
        })
        
        return items

    def copy_to_clipboard(self, data):
        pyperclip.copy(data)
        FlowLauncherAPI.show_msg(
            title="UUID",
            sub_title=f"uuid copied to clipboard",
            ico_path="icon.png"
        )


if __name__ == "__main__":
    UUID()
