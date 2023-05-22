import ansible_runner
import json
from jsonpath_ng import jsonpath, parse
from getpass import getpass
import paramiko, os
from pathlib import Path

app = Flask(__name__)

def applynft(alias):

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='apply'
        )


def entraccept(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule ip {table_name} {chain_name} accept\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha habilitado el trafico entrante correctamente'
    
    return resultado

def saliaccept(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule ip {table_name} {chain_name} accept\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha habilitado el trafico saliente correctamente'
    
    return resultado

def entrdrop(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule ip {table_name} {chain_name} drop\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha bloqueado el trafico entrante correctamente'
    
    return resultado

def salidrop(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule ip {table_name} {chain_name} drop\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha bloqueado el trafico saliente correctamente'
    
    return resultado

def entrsshaccept(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} tcp dport 22 accept\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha habilitado el trafico ssh por el puerto 22 correctamente'
    
    return resultado

def salisshaccept(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} tcp sport 22 accept\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha habilitado el trafico ssh por el puerto 22 correctamente'
    
    return resultado

def entrsshdrop(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} tcp dport 22 drop\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha denegado el trafico ssh por el puerto 22 correctamente'
    
    return resultado

def salisshdrop(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} tcp sport 22 drop\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha denegado el trafico ssh por el puerto 22 correctamente'
    
    return resultado

def entrhttpaccept(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} tcp dport 80 accept\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha habilitado el trafico http por el puerto 22 correctamente'
    
    return resultado

def salihttpaccept(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} tcp sport 80 accept\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha habilitado el trafico http por el puerto 22 correctamente'
    
    return resultado

def entrhttpdrop(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} tcp dport 80 drop\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha denegado el trafico http por el puerto 22 correctamente'
    
    return resultado

def salihttpdrop(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} tcp sport 80 drop\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha denegado el trafico http por el puerto 22 correctamente'
    
    return resultado

def entricmpaccept(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} icmp type echo-request accept\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha habilitado el trafico http por el puerto 22 correctamente'
    
    return resultado

def saliicmpaccept(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} icmp type echo-reply accept\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha habilitado el trafico http por el puerto 22 correctamente'
    
    return resultado

def entricmpdrop(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} icmp type echo-request drop\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha habilitado el trafico http por el puerto 22 correctamente'
    
    return resultado

def saliicmpdrop(alias, table_name, chain_name):
    
    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    result = None
    resultado = None

    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    playbook_lines[16] = f'      command: nft add rule {table_name} {chain_name} icmp type echo-reply drop\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='ssh'
        )

    applynft(alias)

    resultado = f'Se ha habilitado el trafico http por el puerto 22 correctamente'
    
    return resultado


def edit_playbook_add(alias):
    
    with open('ansible/add_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    
    with open('ansible/add_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

def edit_playbook_delete(alias):
    
    with open('ansible/delete_nft.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    
    with open('ansible/delete_nft.yaml', 'w') as f:
        f.writelines(playbook_lines)

def add_host(cip, alias, cusr):
    # ip = '192.168.1.100'  # o cualquier otro método para obtener el host a agregar

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    ansible_dir: Path = this_dir/'ansible'

    with open(inventory_yaml, 'a') as f:
        f.write(f'    {alias}:\n')
        #f.write(f'    hosts:\n')
        f.write(f'      ansible_host: {cusr}@{cip}\n')

    r = ansible_runner.run(ident='add_host', private_data_dir=str(ansible_dir), playbook='', inventory=str(inventory_yaml))
    
def ssh_copy_id(cusr, cpsw, cip):
    command = f'sshpass -p "{cpsw}" ssh-copy-id -o StrictHostKeyChecking=no {cusr}@{cip}'
    os.system(command)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('indice.html')

@app.route('/anadir', methods=['GET', 'POST'])
def anadir():
    resultado = None
    if request.method == 'POST':
        cip = request.form.get('cip')
        alias = request.form.get('alias')
        cusr = request.form.get('cusr')
        cpsw = request.form.get('cpsw')
        
        if cip and alias and cusr:  # Verificar si las variables no son None o una cadena vacía
            add_host(cip, alias, cusr)
            ssh_copy_id(cusr, cpsw, cip)
            resultado = f'Host: {cip} añadido correctamente con alias: {alias} User: {cusr} Passw: {cpsw}'
        else:
            resultado = 'Error: por favor ingrese todos los campos requeridos.'
            
    return render_template('anadir.html', resultado=resultado)

@app.route('/prerules', methods=['GET', 'POST'])
def prerules():
    result = None
    resultado = None

    if request.method == 'POST':

        # Definir los parámetros de la regla

        table_name = request.form.get('table_name')
        chain_name = request.form.get('chain_name')
        alias = request.form.get('alias')
        
        this_dir:       Path = Path(__file__).parent
        inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
        add_rule_yaml: Path = this_dir/'ansible'/'add_nft.yaml'
    
        task_name = request.form["task_name"]

        if task_name == "Permitir Entrada":
            resultado = entraccept(alias=alias, table_name=table_name, chain_name=chain_name)

        elif task_name == "Permitir Salida":
            resultado = saliaccept(alias=alias, table_name=table_name, chain_name=chain_name)

        elif task_name == "Bloquear Entrada":
            resultado = entrdrop(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Bloquear Salida":
            resultado = salidrop(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Permitir Entrada SSH":
            resultado = entrsshaccept(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Permitir Salida SSH":
            resultado = salisshaccept(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Bloquear Entrada SSH":
            resultado = entrsshdrop(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Bloquear Salida SSH":
            resultado = salisshdrop(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Permitir Entrada HTTP":
            resultado = entrhttpaccept(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Permitir Salida HTTP":
            resultado = salihttpaccept(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Bloquear Entrada HTTP":
            resultado = entrhttpdrop(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Bloquear Salida HTTP":
            resultado = salihttpdrop(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Permitir Entrada ICMP":
            resultado = entricmpaccept(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Permitir Salida ICMP":
            resultado = saliicmpaccept(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Bloquear Entrada ICMP":
            resultado = entricmpdrop(alias=alias, table_name=table_name, chain_name=chain_name)
        
        elif task_name == "Bloquear Salida ICMP":
            resultado = saliicmpdrop(alias=alias, table_name=table_name, chain_name=chain_name)

        else:

            with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'r') as f:
                playbook_lines = f.readlines()

            playbook_lines[12] = f'      command: nft add rule {table_name} {chain_name} {expresion_user}\n'

            with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'w') as f:
                f.writelines(playbook_lines)

            result = ansible_runner.run(
                playbook=str(add_rule_yaml),
                inventory=str(inventory_yaml),
                quiet=False,
                tags='rule'
            )
            
            applynft(alias)

    return render_template('prerules.html', resultado=resultado)

@app.route('/creartabla', methods=['GET', 'POST'])
def add_tables():
    resultado = None
    result = None

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'
    
    if request.method == 'POST':

        family = request.form.get('family')
        alias = request.form.get('alias')
        table_name = request.form.get('table_name')  
        
        edit_playbook_add(alias)

        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'r') as f:
            playbook_lines = f.readlines()

        playbook_lines[4] = f'      command: nft create table {family} {table_name}\n'

        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'w') as f:
            f.writelines(playbook_lines)

        result = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='table'
        )

        applynft(alias)

        resultado = f'Tabla: {table_name} añadida correctamente al alias: {alias}' 

    return render_template('crear.html', resultadot=resultado)

@app.route('/crearcadena', methods=['GET', 'POST'])
def add_chains():
    resultado = None
    result = None

    if request.method == 'POST':

        alias = request.form.get('alias')
        family = request.form.get('family')
        table_name = request.form.get('table_name')
        chain_name = request.form.get('chain_name')
        chain_type = request.form.get('chain_type')
        chain_hook = request.form.get('chain_hook')
        chain_priority = request.form.get('chain_priority')
        chain_policy = request.form.get('chain_policy')


        this_dir:       Path = Path(__file__).parent
        inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
        add_chains_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

        edit_playbook_add(alias)

        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'r') as f:
            playbook_lines = f.readlines()

        playbook_lines[8] = f'      command: nft add chain { family } {table_name} {chain_name} {{ type {chain_type} hook {chain_hook} priority {chain_priority} ; policy {chain_policy} ; }}\n'
        
        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'w') as f:
            f.writelines(playbook_lines)

        result = ansible_runner.run(
            playbook=str(add_chains_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='chain'
        )

        applynft(alias)

        resultado = f'cadena: {chain_name} añadida correctamente al alias: {alias}' 


    return render_template('crear.html', resultadoc=resultado)

@app.route('/crearregla', methods=['GET', 'POST'])
def add_rule():
    resultado = None
    result = None

    if request.method == 'POST':

        # Definir los parámetros de la regla

        alias = request.form.get('alias')
        table_name = request.form.get('table_name')
        chain_name = request.form.get('chain_name')
        expresion_user = request.form.get('expresion_user')

        this_dir:       Path = Path(__file__).parent
        inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
        add_rule_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

        edit_playbook_add(alias)
        
        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'r') as f:
            playbook_lines = f.readlines()

        playbook_lines[12] = f'      command: nft add rule {table_name} {chain_name} {expresion_user}\n'

        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'w') as f:
            f.writelines(playbook_lines)

            
        result = ansible_runner.run(
            playbook=str(add_rule_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='rule'
        )
            
        applynft(alias)
        
        resultado = f'regla: {expresion_user} añadida correctamente al alias: {alias}'

    return render_template('crear.html', resultador=resultado)

#@app.route('/mostrartabla')
#def mostrartabla():
    #return render_template('mostrartabla.html')

#@app.route('/mostrarcadena')
#def mostrarcadena():
    #return render_template('mostrarcadena.html')

#@app.route('/mostrarregla')
#def mostrarregla():
    #return render_template('mostrarregla.html')

@app.route('/modificartabla', methods=['GET', 'POST'])
def mod_tables():
    resultado = None
    result = None
    result1 = None

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'
    delete_tables_yaml: Path = this_dir/'ansible'/'delete_nft.yaml'

    
    if request.method == 'POST':

        family = request.form.get('family')
        alias = request.form.get('alias')
        table_name = request.form.get('table_name')

        nw_family = request.form.get('nw_family')
        nw_table_name = request.form.get('nw_table_name')  
        
        edit_playbook_delete(alias)
        edit_playbook_add(alias)

        with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'r') as f:
            playbook_lines = f.readlines()

        playbook_lines[4] = f'      command: nft delete table {family} {table_name}\n'

        with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'w') as f:
            f.writelines(playbook_lines)

        result = ansible_runner.run(
            playbook=str(delete_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='table'
        )


        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'r') as f:
            playbook_lines = f.readlines()

        playbook_lines[4] = f'      command: nft create table {nw_family} {nw_table_name}\n'

        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'w') as f:
            f.writelines(playbook_lines)

        result1 = ansible_runner.run(
            playbook=str(add_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='table'
        )

        applynft(alias)

        resultado = f'Tabla: {family} {table_name} modificada a {nw_family} {nw_table_name} correctamente al alias: {alias}' 

    return render_template('modificar.html', resultadot=resultado)

@app.route('/modificarcadena', methods=['GET', 'POST'])
def mod_chains():
    resultado = None
    result = None
    result1 = None

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_chains_yaml: Path = this_dir/'ansible'/'add_nft.yaml'
    delete_chains_yaml: Path = this_dir/'ansible'/'delete_nft.yaml'

    
    if request.method == 'POST':

        alias = request.form.get('alias')
        family = request.form.get('family')
        table_name = request.form.get('table_name')
        chain_name = request.form.get('chain_name')

        nw_chain_name = request.form.get('nw_chain_name')
        chain_type = request.form.get('chain_type')
        chain_hook = request.form.get('chain_hook')
        chain_priority = request.form.get('chain_priority')
        chain_policy = request.form.get('chain_policy') 
        
        edit_playbook_delete(alias)
        edit_playbook_add(alias)

        with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'r') as f:
            playbook_lines = f.readlines()

        playbook_lines[8] = f'      command: nft flush chain {table_name} {chain_name}\n'

        playbook_lines[9] = f'      command: nft delete chain {family} {table_name} {chain_name}\n'

        with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'w') as f:
            f.writelines(playbook_lines)

        result = ansible_runner.run(
            playbook=str(delete_chains_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='chain'
        )


        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'r') as f:
            playbook_lines = f.readlines()

        playbook_lines[8] = f'      command: nft add chain { family } {table_name} {nw_chain_name} {{ type {chain_type} hook {chain_hook} priority {chain_priority} ; policy {chain_policy} ; }}\n'
        
        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'w') as f:
            f.writelines(playbook_lines)

        result1 = ansible_runner.run(
            playbook=str(add_chains_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='chain'
        )

        applynft(alias)

        resultado = f'Tabla: {family} {table_name} {chain_name} modificada a {family} {table_name} {nw_chain_name} type {chain_type} hook {chain_hook} priority {chain_priority} ; policy {chain_policy} ; correctamente al alias: {alias}' 

    return render_template('modificar.html', resultadoc=resultado)

#@app.route('/modificarregla')
#def modificarregla():
#    return render_template('modificarregla.html')

@app.route('/eliminartabla', methods=['GET', 'POST'])
def delete_tables():
       
    resultado = None
    result = None

    if request.method == 'POST':

        alias = request.form.get('alias')
        table_name = request.form.get('table_name')

        this_dir:       Path = Path(__file__).parent
        inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
        delete_tables_yaml: Path = this_dir/'ansible'/'delete_nft.yaml'

        edit_playbook_delete(alias)

        with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'r') as f:
            playbook_lines = f.readlines()

        playbook_lines[4] = f'      command: nft delete table {table_name}\n'

        with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'w') as f:
            f.writelines(playbook_lines)

        result = ansible_runner.run(
            playbook=str(delete_tables_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='table'
        )

        resultado = f'Tabla: {table_name} eliminada correctamente del alias: {alias}' 

    return render_template('eliminar.html', resultado=resultado)

@app.route('/eliminarcadena', methods=['GET', 'POST'])
def delete_chains():

    resultado = None
    result = None

    if request.method == 'POST':

        alias = request.form.get('alias')
        family = request.form.get('family')
        table_name = request.form.get('table_name')
        chain_name = request.form.get('chain_name')


        this_dir:       Path = Path(__file__).parent
        inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
        delete_chains_yaml: Path = this_dir/'ansible'/'delete_nft.yaml'

        with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'r') as f:
            playbook_lines = f.readlines()

        playbook_lines[8] = f'      command: nft flush chain {table_name} {chain_name}\n'

        playbook_lines[9] = f'      command: nft delete chain {family} {table_name} {chain_name}\n'


        with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'w') as f:
            f.writelines(playbook_lines)

        result = ansible_runner.run(
            playbook=str(delete_chains_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='chain'
        )

        resultado = f'Cadena: {chain_name} de la tabla {table_name} eliminada correctamente del alias: {alias}' 

    return render_template('eliminar.html', resultado=resultado)

#@app.route('/eliminarregla')
#def eliminarregla():
    #return render_template('eliminarregla.html')


if __name__ == '__main__':
    run_playbook_with_tags()
