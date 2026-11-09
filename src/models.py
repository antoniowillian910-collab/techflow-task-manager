"""Modelo de dados do TechFlow Tasks."""

# Status possíveis de uma tarefa (as mesmas colunas do Kanban)
STATUS_VALIDOS = ("A Fazer", "Em Progresso", "Concluído")


class Tarefa:
    """Representa uma tarefa do sistema."""

    def __init__(self, titulo, descricao="", status="A Fazer", id=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def validar(self):
        """Retorna uma lista de erros. Lista vazia significa tarefa válida."""
        erros = []

        if not self.titulo or not self.titulo.strip():
            erros.append("O título é obrigatório.")
        elif len(self.titulo) > 100:
            erros.append("O título deve ter no máximo 100 caracteres.")

        if self.status not in STATUS_VALIDOS:
            erros.append("Status inválido.")

        return erros
