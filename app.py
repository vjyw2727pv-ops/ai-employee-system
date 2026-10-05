from flask import Flask, render_template
from core.system import AIEmployeeSystem

app = Flask(__name__)


def build_dashboard_data():
    system = AIEmployeeSystem()

    task1 = system.manager.create_task("واجهة تسجيل الدخول", "إنشاء صفحة تسجيل الدخول", "high")
    system.manager.assign_task(task1, system.dev1.name)
    system.dev1.build_feature("واجهة تسجيل الدخول")
    system.dev1.review_code("واجهة تسجيل الدخول")

    task2 = system.manager.create_task("نظام المصادقة", "إنشاء منطق المصادقة في الخادم", "critical")
    system.manager.assign_task(task2, system.dev2.name)
    system.dev2.build_backend("نظام المصادقة")
    system.dev2.test_module("نظام المصادقة")

    issue = system.bug_fixer.analyze_issue("فشل في التحقق من البيانات")
    system.bug_fixer.fix_issue(issue)
    system.bug_fixer.validate_fix(issue)

    system.manager.mark_task_done(task1)
    system.manager.mark_task_done(task2)

    return {
        "manager": {
            "name": system.manager.name,
            "tasks_count": len(system.manager.tasks),
            "tasks": system.manager.tasks,
        },
        "developers": [
            {
                "name": system.dev1.name,
                "features": system.dev1.completed_features,
            },
            {
                "name": system.dev2.name,
                "modules": system.dev2.completed_modules,
            },
        ],
        "bug_fixer": {
            "name": system.bug_fixer.name,
            "fixed_issues": system.bug_fixer.fixed_issues,
        },
        "summary": {
            "total_tasks": len(system.manager.tasks),
            "completed_tasks": sum(1 for task in system.manager.tasks if task["status"] == "done"),
            "fixed_issues": len(system.bug_fixer.fixed_issues),
        },
    }


@app.route("/")
def index():
    data = build_dashboard_data()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
