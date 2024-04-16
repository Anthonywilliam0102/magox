class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def informacoes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Número de páginas: {self.num_paginas}"

    def calcular_palavras_por_pagina(self, media_palavras_por_pagina=250):
        return self.num_paginas * media_palavras_por_pagina


livro1 = Livro(titulo="Dom Casmurro", autor="Machado de Assis", num_paginas=200)


print(livro1.informacoes())


print(f"Quantidade média de palavras por página: {livro1.calcular_palavras_por_pagina()}")
