class DeveloperTwo:
    def __init__(self, name="المبرمج 2"):
        self.name = name
        self.completed_modules = []

    def build_backend(self, module_name):
        self.completed_modules.append(module_name)
        print(f"🛠️ {self.name}: تم بناء الوحدة '{module_name}'")
        return module_name

    def test_module(self, module_name):
        print(f"✅ {self.name}: تم اختبار الوحدة '{module_name}' بنجاح")
        return True

    def deliver_backend(self, module_name):
        result = f"تم تسليم الوحدة '{module_name}' بنجاح"
        print(f"🚀 {self.name}: {result}")
        return result


if __name__ == "__main__":
    dev = DeveloperTwo()
    dev.build_backend("نظام المصادقة")
    dev.test_module("نظام المصادقة")
    dev.deliver_backend("نظام المصادقة")
