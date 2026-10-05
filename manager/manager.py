class AIManager:
    def __init__(self, name="Manager"):
        self.name = name
        self.tasks = []

    def create_task(self, task_name, description):
        task = {
            "name": task_name,
            "description": description,
            "status": "open",
            "assignee": None,
        }
        self.tasks.append(task)
        print(f"📋 المدير: تم إنشاء المهمة '{task_name}'")
        return task

    def assign_task(self, task, employee):
        task["assignee"] = employee
        task["status"] = "assigned"
        print(f"📌 المدير: تم تعيين المهمة إلى {employee}")
        return task

    def review_tasks(self):
        print("📊 قائمة المهام:")
        for task in self.tasks:
            print(f"- {task['name']} | {task['assignee']} | {task['status']}")


if __name__ == "__main__":
    manager = AIManager("المدير")
    task = manager.create_task("تطوير واجهة", "إنشاء صفحة تسجيل الدخول")
    manager.assign_task(task, "المبرمج 1")
    manager.review_tasks()
