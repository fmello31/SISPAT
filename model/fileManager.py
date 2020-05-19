def list(model):
    name_file = 'arquivos/' + model + '.txt'
    file = open( name_file, 'r', encoding='utf8' )

    table_name = file.readline().strip().replace( ' ', '' )
    columns_name = file.readline().strip().replace( ' ', '' )
    columns_type = file.readline().strip().replace( ' ', '' )
    max_id = file.readline().strip().replace( ' ', '' )

    if verify_table_name_format( table_name, model ) and verify_columns_format( columns_name ) \
            and verify_columns_format( columns_type ) and verify_max_id( max_id ):
        columns_name = columns_name.split( '=' )[1]
        columns_name = columns_name.split( ',' )
        print_header( columns_name, model )
        print_table_lines( file )
    else:
        print( 'O campo de nome do arquivo {} não pode estar vazio.'.format( model ) )


def verify_table_name_format(table_name, model):
    if table_name:
        table_name = table_name.split( '=' )
        if len( table_name ) == 2 and table_name[1] == model:
            return True
        else:
            return False
    else:
        return False


def verify_columns_format(columns_):
    if columns_:
        columns_ = columns_.split( '=' )
        if len( columns_ ) == 2 and columns_[1]:
            return True
        else:
            return False
    else:
        return False


def verify_max_id(max_id):
    if max_id:
        max_id = max_id.split( '=' )
        if len( max_id ) == 2 and max_id[1]:
            return True
        else:
            return False


def verify_columns_in(_columns_name, _columns):
    _columns_name = _columns_name.split( '=' )
    _columns_name = _columns_name[1].split(',')
    if _columns.issubset(_columns_name):
        return True
    else:
        return False


def print_line():
    print( '\033[30m-\033[m' * 80 )


def print_header(columns_name, model):
    print( '\n' )
    print_line()
    print( ' ' * 30, model.upper(), ' ' * 30 )
    print_line()
    for item in columns_name:
        print( '|', item, end=' |' )
    print( '' )
    print_line()


def print_table_lines(model_file):
    for line in model_file:
        line = line.strip().split( ';' )
        for item in line:
            print( '|', item, end=' |' )
        print( '\n' )


def register(model, item):
    name_file = 'arquivos/' + model + '.txt'
    file = open( name_file, 'r', encoding='utf8' )
    file_lines = file.readlines()

    table_name = file_lines[0].strip().replace( ' ', '' )
    columns_name = file_lines[1].strip().replace( ' ', '' )
    columns_type = file_lines[2].strip().replace( ' ', '' )
    max_id = file_lines[3].strip().replace( ' ', '' )

    if verify_table_name_format( table_name, model ) and verify_columns_format( columns_name ) \
            and verify_columns_format( columns_type ) and verify_max_id( max_id ):
        max_id = int( max_id.split( "=" )[1] )
        new_max_id = max_id + 1
        if len( item ) > 0:
            new_item = f'{new_max_id}'
            for column in item:
                new_item = new_item + f'; {column}'
            new_item = new_item + '\n'
            file_lines.append( new_item )
            file_lines[3] = f'max_id = {new_max_id}\n'
            file.close()
            file = open( name_file, 'w', encoding='utf8' )
            file.writelines( file_lines )
            file.close()
        else:
            raise ValueError(
                'O {} para registro não possui dados. Por favor, verifique os campos informados'.format( model ) )
    else:
        raise ValueError(
            'O arquivo {}.txt não está em um formato válido. Por favor, verificar o formato do arquivo'.format(
                model ) )


def update(model, id, columns, values):
    name_file = 'arquivos/' + model + '.txt'
    file = open( name_file, 'r', encoding='utf8' )
    file_lines = file.readlines()
    file.close()

    table_name = file_lines[0].strip().replace( ' ', '' )
    columns_name = file_lines[1].strip().replace( ' ', '' )
    columns_type = file_lines[2].strip().replace( ' ', '' )
    max_id = file_lines[3].strip().replace( ' ', '' )

    if verify_table_name_format( table_name, model ) and verify_columns_format( columns_name ) \
            and verify_columns_format( columns_type ) and verify_max_id( max_id ) and verify_columns_in():

        # gets the columns position to replace value in new line.
        columns_position = []
        for column in columns:
            columns_position.append(columns_name.index(column))

        file = open( name_file, 'w', encoding='utf8' )

        for i in range(len(file_lines)):
            line = file_lines[i]
            if line.startswith( str(id) ): #checks if line starts with id number given by user
                line_columns = line.split(';') #converts the line in a list where each position is a column value
                for j in range(len(columns_position)): #getting the columns indexes
                    position = columns_position[j] #column index
                    line_columns[position] = values[j] #updating the column for the new value
                new_line = ''.join( str( x ) + ';' for x in line_columns)[:-1]# converts the line columns array into a single string object
                file_lines[i] = new_line + '\n'
                break

        file.writelines( file_lines )
        file.close()
        return True

    return False


def Consult(model, key_word):
    name_file = 'arquivos/' + model + '.txt'
    file = open( name_file, 'r', encoding='utf8' )
    file_lines = file.readlines()
    key_word = str(key_word)
    print( key_word )
    for line in file_lines:
        line_aux = line[:-1]
        line_aux = line_aux.split(';')
        if any( key_word == s for s in line_aux ):
            return line_aux

