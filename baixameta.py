# coding=ansi

from bs4 import BeautifulSoup
import requests, time, re, openpyxl

arquivo_urls = open("urls.txt","r")
links = arquivo_urls.readlines()
linhas = len(links)
i = 0
er = 0
tentativas = 9

while i < linhas:
    html = requests.get(links[i]).content
    soup = BeautifulSoup(html, 'html.parser')
    book = openpyxl.load_workbook('cadastros.xlsx')
    cadastros_page = book['cadastros']
    print('------------------------------------------------------')
    print('Trabalhando no item: ' + str(i+1) + '/' + str(linhas))
    print('Tentativa: ' + str(er+1) + '/' + str(tentativas+1))
    print('-----------------------------------------------------')

    try:
        if er == tentativas:
            i += 1
            er = 0
            print('\n')
            print('Tentativas esgotadas, próximo item!')
            print('\n')
            pass

        titulo = soup.find(id="productTitle")
        titulo = titulo.text
        print(titulo)

        if soup.find(class_="author notFaded") is None:
            print('Campo autor vazio')
            autor = ' '
        else:
            autor = soup.find(class_="author notFaded")
            autor = autor.text
            print(autor)

        if soup.find(id="productSubtitle") is None:
            print('Ano de publicação vazio')
            ano = ' '
        else:
            ano = soup.find(id="productSubtitle")
            ano = ano.text
            print(ano)

        if soup.find(id="bookDescription_feature_div") is None:
            print('Sinopse vazia')
            sinopse = ' '
        else:
            sinopse = soup.find(id="bookDescription_feature_div")
            sinopse = sinopse.text
            print(sinopse)

        if soup.find(class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list") is None:
            print('Detalhes não encontrado')
        else:
            detalhes = soup.find(class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list")

        if detalhes.span.span.next_element.next_element.next_element is None:
            print('Editora não encontrada')
            editorastr = ' '
        else:
            editora = detalhes.span.span.next_element.next_element.next_element
            editorastr = editora.text
            print(editorastr)

        if editora.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element is None:
            print('Idioma não encontrado')
            idiomastr = ' '
        else: 
            idioma = editora.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
            idiomastr = idioma.text
            print(idiomastr)

        if idioma.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element is None:
            print('Páginas não encontrada')
            paginasstr = ' '
        else:         
            paginas = idioma.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
            paginasstr = paginas.text
            print(paginasstr)

        if paginas.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element is None:
            print('isbn10 não encontrado')
            isbn10str = ' '
        else:      
            isbn10 = paginas.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
            isbn10str = isbn10.text
            print(isbn10str)

        if isbn10.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element is None:
            print('isbn13 não encontrado')
            isbn13str = ' '
        else:            
            isbn13 = isbn10.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
            isbn = re.sub("-","",isbn13.text)
            print(isbn)
        
        if isbn13.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element is None:
            print('Dimensões não encontradas')
            dimensoesstr = ' '
        else:
            dimensoes = isbn13.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
            dimensoesstr = dimensoes.text
            print(dimensoesstr)

        if soup.find(id="imgBlkFront") is None:
            print('Capa não encontrada')
        else:
            img = soup.find(id="imgBlkFront")
            img = img.get('src')
            print(img)

        if soup.find(class_="a-unordered-list a-horizontal a-size-small") is None:
            print('Categoria não encontrada')
            categoriastr = ' '
        else:
            categoria = soup.find(class_="a-unordered-list a-horizontal a-size-small")
            categoriastr = categoria.text
            print(categoriastr)

        print('-------------------------------- SALVANDO METADADOS --------------------------------')
        cadastros_page.append([titulo, autor, ano, sinopse, img, editorastr, paginasstr, isbn10str, isbn, dimensoesstr, categoriastr])

        
        print('-------------------------------- METADADOS SALVOS --------------------------------')
    
        if isbn == ' ':
            isbn = re.sub("-","",paginasstr)
    
        f = open(isbn + '.jpg','wb')
        response = requests.get(img)
        f.write(response.content)
        f.close()
        print('Download da capa concluído!')

        i += 1
        er = 0

    except:
        er += 1
        if er == linhas:
            print('Tentativas excedidas. Pulando para o próximo item!')
        elif i == linhas:
            print('Trabalho concluído :)')
        else:    
            print('Erro! Tentando novamente')
           

    book.save('cadastros.xlsx')