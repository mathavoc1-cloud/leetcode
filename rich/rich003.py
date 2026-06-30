from rich import print
from rich.table import Table


tabela = Table(title= 'Tabela de precos!')
tabela.add_column('Nome', justify= "left", style = 'blue')
tabela.add_column('Preco', justify = 'center', style = 'red')
tabela.add_row ('Lapis', 'R$ 1,59')
tabela.add_row('Borracha', 'R$ 3,90')

print(tabela)