import json
import random

def load_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def random_delete_global_logs(data, proportion, seed=None):
    """
    Randomly delete a proportion of logs from the combined logs of all users, ensuring no logs are misplaced.
    """
    if not 0 <= proportion <= 1:
        raise ValueError("Proportion should be between 0 and 1")

    random.seed(seed)

    # Combine all logs from all users with their respective user indices
    indexed_logs = []
    for user_index, user_data in enumerate(data):
        for log in user_data['logs']:
            indexed_logs.append((user_index, log))

    n_delete = int(len(indexed_logs) * proportion)
    indices_to_delete = random.sample(range(len(indexed_logs)), n_delete)

    # Filter out the deleted logs
    indexed_logs = [item for index, item in enumerate(indexed_logs) if index not in indices_to_delete]

    # Reset logs for each user
    for user_data in data:
        user_data['logs'] = []

    # Distribute the remaining logs back to their respective users
    for user_index, log in indexed_logs:
        data[user_index]['logs'].append(log)

    # Update log_num for each user
    for user_data in data:
        user_data['log_num'] = len(user_data['logs'])

    return data

# 使用示例

# 从json文件加载数据
data = load_from_json("path_to_your_data.json")

# 随机删除整体logs的50%记录，并设置随机种子为42
reduced_data = random_delete_global_logs(data, 0.5, seed=42)

# 将处理后的数据保存到新的json文件
save_to_json(reduced_data, "path_to_output_data.json")
