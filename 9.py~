# 定义玩家状态字典
player_state = {
    "name": "Rupert",
    "health": 10,
    "max_health": 15,
    "inventory": [],
    "attack": 3,
    "location": "Dungeon",
    "experience": 0,
    "gold": 0,
    "enemies_defeated": 0
}

# 定义敌人字典
enemies = {
    1: {"name": "Goblin", "health": 8, "attack": 2, "experience": 5, "gold": 3},
    2: {"name": "Skeleton", "health": 10, "attack": 3, "experience": 7, "gold": 5},
    3: {"name": "Orc", "health": 15, "attack": 4, "experience": 10, "gold": 8},
    4: {"name": "Dragon", "health": 25, "attack": 6, "experience": 20, "gold": 15}
}

# 武器列表
weapons = ["Rusty Sword", "Iron Dagger", "Magic Scroll"]

def get_menu_choice(prompt: str, options: list[str]) -> str:
    """
    获取用户的菜单选择
    
    参数:
        prompt (str): 提示信息
        options (list[str]): 有效选项列表
        
    返回:
        str: 用户选择的选项
    """
    while True:
        # 显示提示信息
        print(prompt)
        # 获取用户输入并转换为小写
        choice = input("> ").lower()
        
        # 检查输入是否在选项列表中（不区分大小写）
        for option in options:
            if choice == option.lower():
                return choice
        
        # 如果输入无效，提示用户重新输入
        print("Invalid choice. Please try again.")

def calculate_player_attack(player_state: dict) -> int:
    """
    计算玩家的攻击力，包括武器加成
    
    参数:
        player_state (dict): 玩家状态字典
        
    返回:
        int: 玩家的总攻击力
    """
    # 基础攻击力
    total_attack = player_state["attack"]
    
    # 检查物品栏中的武器
    for item in player_state["inventory"]:
        if item in weapons:
            print(f"{item} boosts your attack!")
            total_attack += 2
    
    # 如果玩家生命值低于或等于最大生命值的50%，攻击力翻倍
    if 0 < player_state["health"] <= player_state["max_health"] / 2:
        total_attack *= 2
    
    return total_attack

def combat_encounter(state: dict, enemy_id: int) -> dict:
    """
    处理战斗遭遇
    
    参数:
        state (dict): 玩家状态字典
        enemy_id (int): 敌人ID
        
    返回:
        dict: 更新后的玩家状态字典
    """
    # 获取敌人信息
    enemy = enemies[enemy_id].copy()  # 复制敌人信息，避免修改原始数据
    
    print(f"\nYou encounter a {enemy['name']}!")
    
    # 战斗循环
    first_action = True
    while True:
        # 显示战斗状态
        print(f"\n{state['name']}: Health {state['health']}/{state['max_health']}")
        print(f"{enemy['name']}: Health {enemy['health']}")
        
        # 获取玩家行动选择
        action = get_menu_choice("Choose your action: [A]ttack, [D]efend, [R]un", ["a", "d", "r"])
        
        # 处理玩家行动
        if action == "a":  # 攻击
            # 计算玩家攻击力
            player_attack = calculate_player_attack(state)
            
            # 玩家攻击敌人
            enemy["health"] -= player_attack
            print(f"You attack the {enemy['name']} for {player_attack} damage!")
            
            # 检查敌人是否被击败
            if enemy["health"] <= 0:
                print(f"\n{state['name']} defeated the {enemy['name']}!")
                print(f"Gained {enemy['experience']} XP and {enemy['gold']} gold.")
                
                # 更新玩家状态
                state["experience"] += enemy["experience"]
                state["gold"] += enemy["gold"]
                state["enemies_defeated"] += 1
                
                # 战斗胜利后恢复5点生命值，但不超过最大生命值
                state["health"] = min(state["max_health"], state["health"] + 5)
                
                return state
            
            # 敌人反击
            state["health"] -= enemy["attack"]
            print(f"The {enemy['name']} attacks you for {enemy['attack']} damage!")
            
            # 检查玩家是否被击败
            if state["health"] <= 0:
                state["health"] = 0  # 确保生命值不为负
                print(f"\n{state['name']} was defeated by the {enemy['name']}...")
                return state
                
        elif action == "d":  # 防御
            # 敌人攻击，但伤害减半（至少为1）
            damage = max(1, enemy["attack"] // 2)
            state["health"] -= damage
            print(f"You defend against the {enemy['name']}'s attack!")
            print(f"The {enemy['name']} attacks you for {damage} damage!")
            
            # 检查玩家是否被击败
            if state["health"] <= 0:
                state["health"] = 0  # 确保生命值不为负
                print(f"\n{state['name']} was defeated by the {enemy['name']}...")
                return state
                
        elif action == "r":  # 逃跑
            if first_action:
                print(f"You successfully escaped from the {enemy['name']}!")
                return state
            else:
                print(f"You failed to escape!")
                # 敌人攻击
                state["health"] -= enemy["attack"]
                print(f"The {enemy['name']} attacks you for {enemy['attack']} damage!")
                
                # 检查玩家是否被击败
                if state["health"] <= 0:
                    state["health"] = 0  # 确保生命值不为负
                    print(f"\n{state['name']} was defeated by the {enemy['name']}...")
                    return state
        
        # 第一个行动已经完成
        first_action = False

# 主程序
if __name__ == "__main__":
    # 添加一些物品到玩家物品栏进行测试
    player_state["inventory"] = ["Potion", "Rusty Sword"]
    
    # 让玩家选择敌人
    print("Choose an enemy to fight:")
    for enemy_id, enemy in enemies.items():
        print(f"{enemy_id}. {enemy['name']}")
    
    enemy_choice = get_menu_choice("Enter enemy number:", ["1", "2", "3", "4"])
    
    # 开始战斗
    updated_state = combat_encounter(player_state, int(enemy_choice))
    
    # 显示战斗后的玩家状态
    print("\nFinal player state:")
    print(f"Name: {updated_state['name']}")
    print(f"Health: {updated_state['health']}/{updated_state['max_health']}")
    print(f"Attack: {updated_state['attack']}")
    print(f"Experience: {updated_state['experience']}")
    print(f"Gold: {updated_state['gold']}")
    print(f"Enemies defeated: {updated_state['enemies_defeated']}")
    print(f"Inventory: {', '.join(updated_state['inventory'])}")