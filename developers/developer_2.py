class DeveloperTwo:
    def __init__(self, name="Developer 2"):
        self.name = name
        self.tasks = []

    def build_backend(self, module_name):
        self.tasks.append(module_name)
        print(f"🛠️ {self.name}: تم بناء الوحدة '{module_name}'")
        return module_name

    def test_module(self, module_name):
        print(f"✅ {self.name}: تم اختبار الوحدة '{module_name}' بنجاح")
        return True


if __name__ == "__main__":
    dev = DeveloperTwo()
    dev.build_backend("نظام المصادقة")
    dev.test_module("نظام المصادقة")
