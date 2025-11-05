import random
import datetime

# 定义可能的角色、状态和标记
roles = ["Admin", "Editor", "Viewer"]
statuses = ["Active", "Inactive", "Suspended"]
tags = ["Premium", "Trial", None]

# 生成5个随机用户
users = []
for i in range(5):
    user = {
        "用户ID": i + 1,
        "角色": random.choice(roles),
        "状态": random.choice(statuses),
        "标记": random.choice(tags)
    }
    users.append(user)

# 权限判断函数
def check_permission(user):
    role = user["角色"]
    status = user["状态"]
    tag = user["标记"]
    
    # 复杂的权限判断逻辑：嵌套if-else、布尔运算、三元运算符混合使用
    # 故意引入一些逻辑复杂度，如同时检查多个布尔条件
    if role == "Admin":
        # Admin角色基础权限为Full Access
        # 但如果状态是Suspended，则权限受限
        # Premium标记可以提升受限Admin的权限
        permission = "Full Access" if status != "Suspended" else ("Limited Access" if tag == "Premium" else "No Access")
    elif role == "Editor":
        # Editor角色需要Active状态
        # Trial标记有额外限制
        if status == "Active":
            permission = "Edit Access" if tag != "Trial" else "Limited Edit Access"
        elif status == "Inactive":
            # Inactive状态下，Premium标记可以获得Read Access
            permission = "Read Access" if tag == "Premium" else "No Access"
        else:  # Suspended
            permission = "No Access"
    else:  # Viewer
        # Viewer角色需要Active或Inactive状态
        # Premium标记可以获得Extended Read Access
        if status in ["Active", "Inactive"]:
            permission = "Extended Read Access" if tag == "Premium" else "Read Access"
        else:  # Suspended
            # Suspended状态下，Trial标记没有权限，Premium标记可能有有限权限
            permission = "Limited Read Access" if tag == "Premium" else "No Access"
    
    return permission

# 输出当前时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"当前时间: {current_time}")
print()

# 输出结果（优化对齐）
print("{:<6} {:<10} {:<12} {:<10} {:<20}".format("用户ID", "角色", "状态", "标记", "最终权限"))
print("-" * 60)
for user in users:
    permission = check_permission(user)
    print("{:<6} {:<10} {:<12} {:<10} {:<20}".format(
        user['用户ID'],
        user['角色'],
        user['状态'],
        user['标记'] or 'None',
        permission
    ))