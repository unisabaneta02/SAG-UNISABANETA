import unittest
import json
from task_manager import app  # Importar la aplicación y la base de datos

class TaskAppTestCase(unittest.TestCase):
    def test_add_task(self):
        # Prueba agregar una nueva tarea
        response = self.client.post('/tasks', json={'description': 'Test Task'})
        self.assertEqual(response.status_code, 201)

        # Verificar que la tarea se ha agregado
        response = self.client.get('/tasks')
        tasks = json.loads(response.data)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['description'], 'Test Task')

    def test_get_tasks(self):
        # Agregar una tarea de prueba primero
        self.client.post('/tasks', json={'description': 'Another Test Task'})
        
        # Probar obtener todas las tareas
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        tasks = json.loads(response.data)
        self.assertEqual(len(tasks), 1)

    def test_delete_task(self):
        # Agregar una tarea para eliminar
        response = self.client.post('/tasks', json={'description': 'Task to delete'})
        task_id = json.loads(response.data)['id']

        # Probar eliminar la tarea
        response = self.client.delete(f'/tasks/{task_id}')
        self.assertEqual(response.status_code, 204)

        # Verificar que la tarea fue eliminada
        response = self.client.get('/tasks')
        tasks = json.loads(response.data)
        self.assertEqual(len(tasks), 0)

# Este bloque puede ser opcional si ejecutas pruebas con pytest
if __name__ == '__main__':
    unittest.main()
