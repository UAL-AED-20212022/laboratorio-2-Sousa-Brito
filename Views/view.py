from models.LinkedList import LinkedList

def main():

  lista_ligada = LinkedList()
  
  while True:
    
    try:
      user_input = input().split(' ') # valida como se tem de comportar as instruções
    except EOFError:
          return


    if user_input[0].upper() == 'RPI': # opção/comando
        lista_ligada.insert_at_start(user_input[1])
        lista_ligada.traverse_list()
        
            
    elif user_input[0].upper() == 'RPF': # opção/comando
        lista_ligada.insert_at_end(user_input[1])
        lista_ligada.traverse_list()
            

    elif user_input[0].upper() == 'RPDE': # opção/comando
        lista_ligada.insert_after_item(user_input[2], user_input[1])
        lista_ligada.traverse_list()
        

    elif user_input[0].upper() == 'RPAE': # opção/comando
        lista_ligada.insert_before_item(user_input[2], user_input[1])
        lista_ligada.traverse_list()
        

    elif user_input[0].upper() == 'RPII': # opção/comando
        lista_ligada.insert_at_index(int(user_input[2]), user_input[1])
        lista_ligada.traverse_list()
        
    
    elif user_input[0].upper() == 'VNE': # opção/comando
        print(f'O número de elementos são {lista_ligada.get_count()}.')


    elif user_input[0].upper() == 'VP': # opção/comando
        if lista_ligada.search_item(user_input[1]):
            print(f'O país {user_input[1]} encontra-se na lista.')
        else:
            print(f'O país {user_input[1]} não se encontra na lista.')


    elif user_input[0].upper() == 'EPE': # opção/comando
        primeiro_pais = lista_ligada.start_node.get_item()
        lista_ligada.delete_at_start()
        print(f'O país {primeiro_pais} foi eliminado da lista.')
        

    elif user_input[0].upper() == 'EUE': # opção/comando
        ultimo_pais = lista_ligada.get_last_node()
        lista_ligada.delete_at_end()
        print(f'O país {ultimo_pais} foi eliminado da lista.')
        

    elif user_input[0].upper() == 'EP': # opção/comando
        if lista_ligada.search_item(user_input[1]):
            lista_ligada.delete_element_by_value(user_input[1])
            print(f'O país {user_input[1]} foi eliminado da lista.')
        else:
            print(f'O país {user_input[1]} não se encontra na lista.')
        

    else:
        if user_input[0].upper() == "":
            break