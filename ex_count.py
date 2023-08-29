def reorder_points(points):
    # 首先按纵坐标排序
    sorted_points = sorted(points, key=lambda p: p[1])
    
    reordered_points = []
    while sorted_points:
        # 从开始和结尾取点，并将其添加到新列表中
        if sorted_points:
            reordered_points.append(sorted_points.pop(0))
        if sorted_points:
            reordered_points.append(sorted_points.pop())
    
    return reordered_points

# 示例数据：[(x1, y1), (x2, y2), ...]
points = [(1, 5), (2, 3), (3, 8), (4, 2), (5, 7)]
print(reorder_points(points))
