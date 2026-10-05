class DeveloperOne:
    def __init__(self, name="المبرمج 1"):
        self.name = name
        self.completed_features = []

    def build_feature(self, feature_name):
        self.completed_features.append(feature_name)
        print(f"💻 {self.name}: تم بناء الميزة '{feature_name}'")
        return feature_name

    def review_code(self, feature_name):
        print(f"🔍 {self.name}: تم مراجعة الكود الخاص بـ '{feature_name}'")
        return True

    def deliver_feature(self, feature_name):
        result = f"تم تسليم الميزة '{feature_name}' بنجاح"
        print(f"🚀 {self.name}: {result}")
        return result


if __name__ == "__main__":
    dev = DeveloperOne()
    dev.build_feature("واجهة تسجيل الدخول")
    dev.review_code("واجهة تسجيل الدخول")
    dev.deliver_feature("واجهة تسجيل الدخول")
