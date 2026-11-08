import pytest
from src.task_manager import TaskManager

@pytest.fixture
def manager():
    return TaskManager()

def test_add_task_success(manager):
    task = manager.add_task("Testar CI", "Configurar GitHub Actions", "Alta")
    assert task["id"] == 1
    assert task["title"] == "Testar CI"
    assert task["priority"] == "Alta"

def test_add_task_empty_title(manager):
    with pytest.raises(ValueError, match="O título da tarefa não pode ser vazio."):
        manager.add_task("", "Descrição sem título")

def test_invalid_priority(manager):
    with pytest.raises(ValueError):
        manager.add_task("Tarefa Invalida", "Teste", "Urgente")

def test_update_status(manager):
    manager.add_task("Estudar Engenharia", "Ler Pressman")
    result = manager.update_task_status(1, "Concluído")
    assert result is True
    assert manager.get_task(1)["status"] == "Concluído"

def test_delete_task(manager):
    manager.add_task("Remover esta tarefa", "Teste de deleção")
    result = manager.delete_task(1)
    assert result is True
    assert manager.get_task(1) is None
