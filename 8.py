from random import randint, choice

def play_turn(player_state: dict) -> dict:
    """
    执行游戏的一个回合，随机选择一个事件发生并更新玩家状态
    
    参数:
        player_state (dict): 包含玩家当前状态的字典
        
    返回:
        dict: 更新后的玩家状态字典
    """
    # 定义可能的事件列表
    events = ["find_item", "take_damage", "heal", "nothing"]
    # 可获得的物品列表
    items = ["sword", "map", "potion", "ring", "amulet"]
    
    # 随机选择一个事件
    event = choice(events)
    print(f"Turn Event: {event}")
    
    # 根据事件类型执行相应操作
    if event == "find_item":
        # 玩家找到一个随机物品
        found_item = choice(items)
        # 如果物品不在物品栏中，则添加
        if found_item not in player_state["inventory"]:
            player_state["inventory"].append(found_item)
        print(f"{player_state['name']} found a {found_item}.")
        
    elif event == "take_damage":
        # 玩家受到1-5点随机伤害
        damage = randint(1, 5)
        # 减少健康值，但不低于0
        player_state["health"] = max(0, player_state["health"] - damage)
        print(f"{player_state['name']} took {damage} damage. Health: {player_state['health']}.")
        
    elif event == "heal":
        # 玩家恢复1-3点健康值
        heal_amount = randint(1, 3)
        # 增加健康值，但不超过最大健康值
        player_state["health"] = min(player_state["max_health"], player_state["health"] + heal_amount)
        print(f"{player_state['name']} healed {heal_amount}. Health: {player_state['health']}.")
        
    else:  # event == "nothing"
        # 什么都没发生
        print("Nothing happened.")
    
    return player_state

# 初始化玩家状态
player_state = {
    "name": "Rupert",
    "health": 10,
    "max_health": 15,
    "inventory": [],
    "location": "Start"
}

items = ["sword", "map", "potion", "ring", "amulet"]

# 主游戏循环
if __name__ == "__main__":
    # 获取随机种子
    seed_input = input("Please enter the random seed for today's journey: ")
    import random
    random.seed(int(seed_input))
    
    # 执行5个回合或直到玩家健康值为0
    game_over = False
    for turn in range(1, 6):
        print(f"-- Turn {turn} --\n")
        play_turn(player_state)
        print()
        
        # 检查玩家健康值
        if player_state["health"] == 0:
            game_over = True
            break
    
    # 游戏结束处理
    if game_over or player_state["health"] == 0:
        print(f"{player_state['name']} has no health left. Game Over.")
    else:
        # 打印最终状态
        print(f"Final Health: {player_state['health']}")
        if not player_state["inventory"]:
            print("Final Inventory: Empty.")
        else:
            inventory_str = ", ".join(player_state["inventory"])
            print(f"Final Inventory: {inventory_str}.")