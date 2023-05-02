import control

#control.add_tables(table_name='test')
#control.add_chains()
#control.delete_chains(chain_family='ip', table_name='calvoo', chain_name='calvochain')
#control.add_rule()
#control.delete_rule()

alias = 'test'
table_name = 'calvo'
chain_name = 'calvochain'

control.ssh(alias= alias, table_name= table_name, chain_name= chain_name)