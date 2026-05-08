from collections import deque

def solve_8_puzzle(start_state):
    # Khối 1: Định nghĩa Bài toán (Goal State)
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0) # 0 là ô trống
    
    # Khối 3: Cấu trúc dữ liệu của Động cơ Tìm kiếm
    queue = deque([(start_state, [])]) # Fringe: Hàng đợi lưu (trạng thái, chuỗi hành động)
    explored = set([start_state])      # Explored Set: Tránh lặp vô hạn
    
    # Khối 2: Ràng buộc di chuyển (Lên, Xuống, Trái, Phải)
    moves = [(-1, 0, 'UP'), (1, 0, 'DOWN'), (0, -1, 'LEFT'), (0, 1, 'RIGHT')]
    
    while queue:
        state, path = queue.popleft()
        
        # Kiểm tra mục tiêu
        if state == goal_state:
            return path
        
        # Khối 2: Action Generator & Successor Function
        idx = state.index(0)         # Tìm vị trí ô trống (0 -> 8)
        r, c = divmod(idx, 3)        # Chuyển thành 2D (row, col)
        
        for dr, dc, action in moves:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < 3 and 0 <= nc < 3: 
                new_idx = nr * 3 + nc
                
                # Hoán đổi vị trí để tạo trạng thái mới
                new_state = list(state)
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                new_state = tuple(new_state)
                
                # Nạp vào bộ máy tìm kiếm nếu chưa duyệt qua
                if new_state not in explored:
                    explored.add(new_state)
                    queue.append((new_state, path + [action]))
                    
    return None # Không tìm thấy đường đi (Trường hợp ma trận lỗi không thể giải)

# ================= MÔ PHỎNG =================
# Trạng thái ban đầu: 
# 1 2 3
# 4 0 5
# 7 8 6
start = (1, 2, 3, 4, 0, 5, 7, 8, 6) 

actions = solve_8_puzzle(start)
print(f"Số bước ít nhất: {len(actions)}")
print(f"Chuỗi hành động: {actions}")