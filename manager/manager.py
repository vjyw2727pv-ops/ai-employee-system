class AIManager:
    def __init__(self, name="المدير"):
        self.name = name
        self.tasks = []

    def create_task(self, task_name, description, priority="medium"):
        task = {
            "id": len(self.tasks) + 1,
            "name": task_name,
            "description": description,
            "priority": priority,
            "status": "open",
            "assignee": None,
        }
        self.tasks.append(task)
        print(f"📋 المدير: تم إنشاء المهمة '{task_name}'")
        return task

    def assign_task(self, task, employee_name):
        task["assignee"] = employee_name
        task["status"] = "assigned"
        print(f"📌 المدير: تم تعيين المهمة إلى {employee_name}")
        return task

    def mark_task_done(self, task):
        task["status"] = "done"
        print(f"✅ المدير: تم إكمال المهمة '{task['name']}'")
        return task

    def review_tasks(self):
        print("\n📊 قائمة المهام:")
        if not self.tasks:
            print("لا توجد مهام حالياً.")
            return

        for task in self.tasks:
            status = task["status"]
            assignee = task.get("assignee") or "غير معين"
            print(f"- {task['id']}. {task['name']} | الأولوية: {task['priority']} | الموظف: {assignee} | الحالة: {status}")


if __name__ == "__main__":
    manager = AIManager()
    task = manager.create_task("تطوير واجهة", "إنشاء صفحة تسجيل الدخول", "high")
    manager.assign_task(task, "المبرمج 1")
    manager.review_tasks()
