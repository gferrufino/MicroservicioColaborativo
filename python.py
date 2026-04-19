# app.py - Microservicio de gestión de tareas
# Lista global (actúa como una base de datos temporal)
tareas = []

def agregar_tarea(titulo):
    # Mejora 1: Validación de entrada
    if not titulo or not isinstance(titulo, str):
        return {"error": "El título es obligatorio y debe ser texto"}
        
    tarea = {
        "id": len(tareas) + 1, 
        "titulo": titulo.strip(), # Limpiamos espacios extra
        "completada": False
    }
    tareas.append(tarea)
    return tarea

def listar_tareas():
    return tareas

def completar_tarea(tarea_id):
    # Mejora 2: Búsqueda más limpia
    for tarea in tareas:
        if tarea["id"] == int(tarea_id): # Aseguramos que sea un entero
            tarea["completada"] = True
            return tarea
    return {"error": "Tarea no encontrada"}

if __name__ == "__main__":
    # Pruebas rápidas
    agregar_tarea("Configurar Git")
    agregar_tarea("Crear repositorio en GitHub")
    
    print("--- Lista de Tareas ---")
    for t in listar_tareas():
        estado = "✅" if t["completada"] else "⏳"
        print(f"{t['id']}. {t['titulo']} {estado}")

#cambio para simular el hotfix