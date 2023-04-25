from flask import Flask, render_template, request
import ansible_runner
import json
import jsonpath_ng as jp
#from jsonpath_ng import jsonpath, parse
from getpass import getpass
import paramiko, os
from pathlib import Path
import subprocess



def edit_playbook(alias):
    with open('ansible/add_tables.yaml', 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[0] = f'- hosts: {alias}\n'
    
    with open('ansible/add_tables.yaml', 'w') as f:
        f.writelines(playbook_lines)

def add_tables(table_name):
    result = None

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_tables_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

    with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[4] = f'      command: nft create table {table_name}\n'

    with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
        playbook=str(add_tables_yaml),
        inventory=str(inventory_yaml),
        quiet=False,
        tags='table'
    )

def add_chains():
    result = None

    family = 'ip'
    table_name = 'test'
    chain_name = 'input'
    chain_type = 'filter'
    chain_hook = 'input'
    chain_priority = '0'
    chain_policy = 'drop'

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_chains_yaml: Path = this_dir/'ansible'/'add_nft.yaml'

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

def add_rule():
    result = None

    # Definir los parámetros de la regla
    table_name = "test"
    chain_name = "calvochain"
    expresion_user = "tcp dport 8080 accept"

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    add_rule_yaml: Path = this_dir/'ansible'/'add_nft.yaml'
   

    with open(os.path.join(this_dir, 'ansible', 'add_nft.yaml'), 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[12] = f'      command: nft add rule {table_name} {chain_name} { expresion_user }\n'

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
        print(f'Syntax Error: {expresion_user}')
        # Código para recargar la página aquí
    else:
        # Notificar que la regla se ha añadido correctamente
        print("La regla se ha añadido correctamente")

def delete_tables(table_name):
    result = None

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    delete_tables_yaml: Path = this_dir/'ansible'/'delete_nft.yaml'

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

def delete_chains(chain_family, table_name, chain_name):
    result = None

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    delete_chains_yaml: Path = this_dir/'ansible'/'delete_nft.yaml'

    with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[8] = f'      command: nft flush chain {table_name} {chain_name}\n'

    playbook_lines[9] = f'      command: nft delete chain {chain_family} {table_name} {chain_name}\n'


    with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'w') as f:
        f.writelines(playbook_lines)

    result = ansible_runner.run(
        playbook=str(delete_chains_yaml),
        inventory=str(inventory_yaml),
        quiet=False,
        tags='chain'
    )

def delete_rule():
    result = None

    # Definir los parámetros de la regla
    table_name = "test"
    chain_name = "calvochain"
    expresion_user = "tcp dport 80 accept"
    handle = "17"

    this_dir:       Path = Path(__file__).parent
    inventory_yaml: Path = this_dir/'ansible'/'inventory.yaml'
    delete_rule_yaml: Path = this_dir/'ansible'/'delete_nft.yaml'
   

    with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'r') as f:
        playbook_lines = f.readlines()

    playbook_lines[13] = f'      command: nft delete rule {table_name} {chain_name} { expresion_user }\n'

    with open(os.path.join(this_dir, 'ansible', 'delete_nft.yaml'), 'w') as f:
        f.writelines(playbook_lines)

    
    result = ansible_runner.run(
        playbook=str(delete_rule_yaml),
        inventory=str(inventory_yaml),
        quiet=False,
        tags='rule'
    )

    if result.rc != 0:
        # Recargar la página si el resultado es negativo
        print(f'Syntax Error: {expresion_user}')
        # Código para recargar la página aquí
    else:
        # Notificar que la regla se ha añadido correctamente
        print("La regla se ha borrado correctamente")


















def crear():
    resultado = None
    
    #alias = request.form.get('alias')
    #table_name = request.form.get('table_name')    
    
    alias = 'test'
    table_name = 'test1'

    edit_playbook(alias)

    playbook_lines[4] = f'      command: nft add chain {{ family }} {table_name} {chain_name} {{ type {chain_type} hook {chain_hook} priority {chain_priority} ; policy {chain_policy} ; }}\n'

    #add_tables(table_name='test22')
    

if __name__ == '__main__':
    run_playbook_with_tags()