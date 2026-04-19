# test_app.py - Tests unitarios del microservicio de tareas
import sys
sys.path.insert(0, '.')
from app import agregar_tarea, listar_tareas, completar_tarea

def test_agregar_tarea():
    tarea = agregar_tarea("Test tarea 1")
    assert tarea["titulo"] == "Test tarea 1"
    assert tarea["completada"] == False
    print("✅ test_agregar_tarea pasado")

def test_listar_tareas():
    tareas = listar_tareas()
    assert isinstance(tareas, list)
    print("✅ test_listar_tareas pasado")

def test_completar_tarea():
    agregar_tarea("Tarea para completar")
    tareas = listar_tareas()
    ultima_id = tareas[-1]["id"]
    resultado = completar_tarea(ultima_id)
    assert resultado["completada"] == True
    print("✅ test_completar_tarea pasado")

if __name__ == "__main__":
    test_agregar_tarea()
    test_listar_tareas()
    test_completar_tarea()
    print("\n🎉 Todos los tests pasaron correctamente")