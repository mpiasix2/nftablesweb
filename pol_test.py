import paramiko
import os

cusr = "cliente"
cpsw = "1234"
cip = "192.168.127.198"

def copy_ssh_keys(cusr, cpsw, cip):
    # Crear una instancia del cliente SSH
    ssh = paramiko.SSHClient()

    # Establecer la política de host predeterminada (se puede cambiar según sus necesidades)
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Cargar la clave privada (asumiendo que ya ha generado una)
    private_key_file = os.path.expanduser('~/.ssh/id_rsa')
    mykey = paramiko.RSAKey.from_private_key_file(private_key_file)

    # Conectar al servidor SSH
    ssh.connect(hostname=cip, username=cusr, password=cpsw)

    # Crear un objeto SFTP para transferir archivos
    sftp = ssh.open_sftp()

    # Copiar la clave pública al servidor
    public_key_file = os.path.expanduser('~/.ssh/id_rsa.pub')
    sftp.put(public_key_file, '.ssh/authorized_keys')

    # Cerrar la conexión SFTP y SSH
    sftp.close()
    ssh.close()

    print('Clave pública copiada con éxito en el servidor remoto.')


copy_ssh_keys(cusr, cpsw, cip)