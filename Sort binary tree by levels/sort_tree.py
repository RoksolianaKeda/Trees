def tree_by_levels(node):
    if node is None:
        return []
    
    result = []
    queue = [node]
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    flattened_list = []
    for sublist in result:
        for num in sublist:
            flattened_list.append(num)
    
    return flattened_list
