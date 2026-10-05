from flask import Flask, render_template, request, redirect, url_for, session
from core.system import AIEmployeeSystem

app = Flask(__name__)
app.secret_key = "ai_employee_secret_key"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            session["user"] = username
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="اسم المستخدم أو كلمة المرور غير صحيحة")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

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

    data = {
        "manager": {"name": system.manager.name, "tasks": system.manager.tasks},
        "developers": [
            {"name": system.dev1.name, "features": system.dev1.completed_features},
            {"name": system.dev2.name, "modules": system.dev2.completed_modules},
        ],
        "bug_fixer": {"name": system.bug_fixer.name, "fixed_issues": system.bug_fixer.fixed_issues},
        "summary": {
            "total_tasks": len(system.manager.tasks),
            "completed_tasks": sum(1 for t in system.manager.tasks if t["status"] == "done"),
            "fixed_issues": len(system.bug_fixer.fixed_issues),
        },
    }

    return render_template("dashboard.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
