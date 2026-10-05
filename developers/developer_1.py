class DeveloperOne:
    def __init__(self, name="Developer 1"):
        self.name = name
        self.tasks = []

    def build_feature(self, feature_name):
        self.tasks.append(feature_name)
        print(f"💻 {self.name}: تم بناء الميزة '{feature_name}'")
        return feature_name

    def review_code(self, feature_name):
        print(f"🔍 {self.name}: تم مراجعة الكود الخاص بـ '{feature_name}'")
        return True


if __name__ == "__main__":
    dev = DeveloperOne()
    dev.build_feature("واجهة تسجيل الدخول")
    dev.review_code("واجهة تسجيل الدخول")
