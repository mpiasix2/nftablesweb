import paramiko
import os
from pathlib import Path

import os

def ssh_copy_id(cusr, cpsw, cip):
    command = f'sshpass -p "{cpsw}" ssh-copy-id {cusr}@{cip}'
    os.system(command)



cusr = "cliente"
cpsw = "1234"
cip = "192.168.127.198"

ssh_copy_id(cusr, cpsw, cip)
