class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __len__(self):
        return self.canciones

    def __del__(self):
        print(f"Se ha destruido el CD {self.titulo}")

    def __str__(self):
        return f"{self.autor} - {self.titulo} - {self.canciones} canciones"


mi_cd = CD("Elton John", "Goodbye Yellow Brick Road", 15)


print(mi_cd)


print(len(mi_cd))
