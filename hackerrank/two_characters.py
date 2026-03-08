def alternate(s):
    max_len = 0
    unique_chars = list(set(s))
    
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            filtered = [c for c in s if c == char1 or c == char2]
            
            is_alt = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k-1]:
                    is_alt = False
                    break
            
            if is_alt:
                max_len = max(max_len, len(filtered))
                
    return max_len
