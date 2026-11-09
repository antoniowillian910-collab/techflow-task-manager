"""Acesso ao banco SQLite."""
import sqlite3

DB_PADRAO = "tarefas.db"


def conectar(caminho=DB_PADRAO):
    """Abre uma conexão com o banco. Linhas acessíveis pelo nome da coluna."""
    conn = sqlite3.connect(caminho)
    conn.row_factory = sqlite3.Row
    return conn


def criar_tabela(caminho=DB_PADRAO):
    """Cria a tabela de tarefas caso ela ainda não exista."""
    with conectar(caminho) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT DEFAULT '',
                status TEXT NOT NULL DEFAULT 'A Fazer'
            )
            """
        )
