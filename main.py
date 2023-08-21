def water_jug_problem(capacity_jug1, capacity_jug2, target):
    def dfs(jug1, jug2, visited, steps):
        if jug1 == target or jug2 == target:
            return True, steps
        
        visited.add((jug1, jug2))
        
        # Fill jug1
        if jug1 < capacity_jug1 and (capacity_jug1, jug2) not in visited:
            result, new_steps = dfs(capacity_jug1, jug2, visited, steps + [f"Fill jug1"])
            if result:
                return True, new_steps
        
        # Fill jug2
        if jug2 < capacity_jug2 and (jug1, capacity_jug2) not in visited:
            result, new_steps = dfs(jug1, capacity_jug2, visited, steps + [f"Fill jug2"])
            if result:
                return True, new_steps
        
        # Empty jug1
        if jug1 > 0 and (0, jug2) not in visited:
            result, new_steps = dfs(0, jug2, visited, steps + [f"Empty jug1"])
            if result:
                return True, new_steps
        
        # Empty jug2
        if jug2 > 0 and (jug1, 0) not in visited:
            result, new_steps = dfs(jug1, 0, visited, steps + [f"Empty jug2"])
            if result:
                return True, new_steps
        
        # Pour jug1 to jug2
        if jug1 > 0 and jug2 < capacity_jug2:
            amount_to_pour = min(jug1, capacity_jug2 - jug2)
            if (jug1 - amount_to_pour, jug2 + amount_to_pour) not in visited:
                result, new_steps = dfs(jug1 - amount_to_pour, jug2 + amount_to_pour, visited, steps + [f"Pour jug1 to jug2"])
                if result:
                    return True, new_steps
        
        # Pour jug2 to jug1
        if jug2 > 0 and jug1 < capacity_jug1:
            amount_to_pour = min(jug2, capacity_jug1 - jug1)
            if (jug1 + amount_to_pour, jug2 - amount_to_pour) not in visited:
                result, new_steps = dfs(jug1 + amount_to_pour, jug2 - amount_to_pour, visited, steps + [f"Pour jug2 to jug1"])
                if result:
                    return True, new_steps
        
        return False, []

    visited = set()
    result, steps = dfs(0, 0, visited, [])
    return result, steps

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

result, steps = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
if result:
    print("It is possible to achieve the target amount.")
    print("Steps:")
    for step in steps:
        print(step)
else:
    print("It is not possible to achieve the target amount.")
