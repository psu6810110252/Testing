def is_prime_list(numbers):
    for num in numbers:
        if num <= 1: # จัดการ Edge case: 0, 1 และเลขติดลบ ไม่ใช่จำนวนเฉพาะ
            return False
        for n in range(2, num):
            if num % n == 0:
                return False
    return True
