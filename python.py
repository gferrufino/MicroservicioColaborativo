# app.py - Microservicio de gestión de tareas
tareas = []

def agregar_tarea(titulo):
    tarea = {"id": len(tareas) + 1, "titulo": titulo, "completada": False}
    tareas.append(tarea)
    return tarea

def listar_tareas():
    return tareas

def completar_tarea(id):
    for tarea in tareas:
        if tarea["id"] == id:
            tarea["tarea completada"] = True
            return tarea
    return None

if __name__ == "__main__":
    agregar_tarea("Configurar Git")
    agregar_tarea("Crear repositorio en GitHub")
    print(listar_tareas())