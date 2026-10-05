from manager.manager import AIManager
from developers.developer_1 import DeveloperOne
from developers.developer_2 import DeveloperTwo
from bug_fixer.bug_fixer import AIBugFixer


class AIEmployeeSystem:
    def __init__(self):
        self.manager = AIManager("المدير")
        self.dev1 = DeveloperOne("المبرمج 1")
        self.dev2 = DeveloperTwo("المبرمج 2")
        self.bug_fixer = AIBugFixer("مصحح الأخطاء")

    def run(self):
        print("🚀 بدء تشغيل نظام الموظفين الذكي...")

        task1 = self.manager.create_task("واجهة تسجيل الدخول", "إنشاء صفحة تسجيل الدخول")
        self.manager.assign_task(task1, self.dev1.name)
        self.dev1.build_feature("واجهة تسجيل الدخول")
        self.dev1.review_code("واجهة تسجيل الدخول")

        task2 = self.manager.create_task("نظام المصادقة", "إنشاء منطق تسجيل الدخول")
        self.manager.assign_task(task2, self.dev2.name)
        self.dev2.build_backend("نظام المصادقة")
        self.dev2.test_module("نظام المصادقة")

        issue = self.bug_fixer.analyze_issue("فشل في التحقق من البيانات")
        self.bug_fixer.fix_issue(issue)

        print("✅ تم إنجاز جميع المهام الأساسية للنظام")
        self.manager.review_tasks()


if __name__ == "__main__":
    system = AIEmployeeSystem()
    system.run()
