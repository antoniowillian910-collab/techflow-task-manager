def add_task(self, title: str, description: str, priority: str = "Média") -> dict:
    """Adiciona uma nova tarefa ao sistema (Inclui mudança de escopo: Prioridade)."""
    if not title:
        raise ValueError("O título da tarefa não pode ser vazio.")
    
    valid_priorities = ["Baixa", "Média", "Alta"]
    if priority not in valid_priorities:
        raise ValueError(f"Prioridade inválida. Escolha entre: {valid_priorities}")

    task = {
        "id": self._next_id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "A Fazer"
    }
    self.tasks[self._next_id] = task
    self._next_id += 1
    return task

def get_task(self, task_id: int) -> dict:
    """Retorna uma tarefa pelo ID."""
    return self.tasks.get(task_id, None)

def list_tasks(self) -> list:
    """Retorna a lista de todas as tarefas."""
    return list(self.tasks.values())

def update_task_status(self, task_id: int, status: str) -> bool:
    """Atualiza o status de uma tarefa."""
    if task_id in self.tasks:
        self.tasks[task_id]["status"] = status
        return True
    return False

def delete_task(self, task_id: int) -> bool:
    """Remove uma tarefa pelo ID."""
    if task_id in self.tasks:
        del self.tasks[task_id]
        return True
    return False
