from flask import Flask, jsonify, request
from src.database import criar_tabela, conectar
from src.models import Tarefa

app = Flask(__name__)

# Cria a tabela no banco ao iniciar a aplicação
criar_tabela()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas")
        rows = cursor.fetchall()
        tasks = [dict(row) for row in rows]
    return jsonify({"tasks": tasks, "status": "success"}), 200

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'titulo' not in data:
        return jsonify({"error": "O título da tarefa é obrigatório"}), 400
    
    nova = Tarefa(titulo=data['titulo'], descricao=data.get('descricao', ''), status=data.get('status', 'A Fazer'))
    erros = nova.validar()
    if erros:
        return jsonify({"errors": erros}), 400

    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarefas (titulo, descricao, status) VALUES (?, ?, ?)", 
                       (nova.titulo, nova.descricao, nova.status))
        conn.commit()
        nova.id = cursor.lastrowid

    return jsonify({"id": nova.id, "titulo": nova.titulo, "status": nova.status}), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE id = ?", (task_id,))
        conn.commit()
    return jsonify({"message": "Tarefa removida com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)
