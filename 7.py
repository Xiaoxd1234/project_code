def print_status(state: dict) -> None:
    """
    打印玩家当前状态的格式化字符串
    """
    print(f"Name: {state['name']}")
    print(f"Health: {state['health']}/{state['max_health']}")
    
    if state['health'] <= 0:
        print("Player has fallen!")
    
    if len(state['inventory']) == 0:
        print("Inventory: is empty.")
    else:
        inventory_str = ", ".join(state['inventory'])
        print(f"Inventory: {inventory_str}.")
    
    print(f"Location: {state['location']}")

        
def add_item(state: dict, item: str) -> None:
    """
    向玩家物品栏添加物品，不允许重复添加
    """
    if item not in state["inventory"]:
        state["inventory"].append(item)

def take_damage(state: dict, amount: int) -> None:
    """
    减少玩家生命值，但不会低于0
    """
    state["health"] = max(0, state["health"] - amount)

# 初始玩家状态
player_state = {"name":"Rupert","health":10,"max_health":15,"inventory":[],"location":"Start"}

# 测试代码
print("初始状态:")
print_status(player_state)

print("\n添加物品后:")
add_item(player_state, "sword")
print_status(player_state)

print("\n尝试添加重复物品:")
add_item(player_state, "sword")
print_status(player_state)

print("\n受到伤害后:")
take_damage(player_state, 5)
print_status(player_state)

print("\n受到致命伤害后:")
take_damage(player_state, 10)
print_status(player_state)