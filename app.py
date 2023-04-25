from flask import Flask, render_template, request
import ansible_runner
import json
from jsonpath_ng import jsonpath, parse
from getpass import getpass
import paramiko, os

from pathlib import Path

app = Flask(__name__)



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
        cpsw = request.form.get('cpsw')  # Obtener el valor del campo 'alias' del formulario
        add_host(cip, alias, cusr)  # Llamar a la función add_host con la dirección IP y el alias proporcionados
        #copy_ssh_keys(cusr, cpsw, cip)
        resultado = f'Host: {cip} añadido correctamente con alias: {alias} User: {cusr} Passw: {cpsw}'  # Actualizar el resultado con el mensaje de éxito
    return render_template('anadir.html', resultado=resultado)  # Renderizar la plantilla 'anadir.html' con el resultado actualizado

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

        resultado = f'Tabla: {table_name} añadida correctamente al alias: {alias}' 

    return render_template('creartabla.html', resultado=resultado)

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

        resultado = f'cadena: {chain_name} añadida correctamente al alias: {alias}' 


    return render_template('crearcadena.html', resultado=resultado)

@app.route('/crearregla', methods=['GET', 'POST'])
def add_rule():
    resultado = None
    result = None

    if request.method == 'POST':

        # Definir los parámetros de la regla

        alias = request.form.get('alias')
        table_name = request.form.get('table_name')
        chain_name = request.form.get('chain_name')
        rule_expresion = request.form.get('rule_expresion')

        this_dir:       Path = Path(__file__).parent
        inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
        add_rule_yaml: Path = this_dir/'ansible'/'add_nft.yaml'
    

        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'r') as f:
            playbook_lines = f.readlines()

        playbook_lines[12] = f'      command: nft add rule {table_name} {chain_name} { rule_expresion }\n'

        with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'w') as f:
            f.writelines(playbook_lines)

        
        result = ansible_runner.run(
            playbook=str(add_rule_yaml),
            inventory=str(inventory_yaml),
            quiet=False,
            tags='rule'
        )

        if result.rc != 0:
            # Recargar la página si el resultado es negativo
            resultado = f'Syntax Error: {expresion_user}'
            # Código para recargar la página aquí
        else:
            # Notificar que la regla se ha añadido correctamente
            resultado = f'La regla {expresion_user} se ha añadido correctamente'

    return render_template('crearregla.html', resultado=resultado)

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

        resultado = f'Tabla: {family} {table_name} modificada a {nw_family} {nw_table_name} correctamente al alias: {alias}' 

    return render_template('modificartabla.html', resultado=resultado)

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

        resultado = f'Tabla: {family} {table_name} {chain_name} modificada a {family} {table_name} {nw_chain_name} type {chain_type} hook {chain_hook} priority {chain_priority} ; policy {chain_policy} ; correctamente al alias: {alias}' 

    return render_template('modificarcadena.html', resultado=resultado)

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

    return render_template('eliminartabla.html', resultado=resultado)

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

    return render_template('eliminarcadena.html', resultado=resultado)

#@app.route('/eliminarregla')
#def eliminarregla():
    #return render_template('eliminarregla.html')


if __name__ == '__main__':
    run_playbook_with_tags()
