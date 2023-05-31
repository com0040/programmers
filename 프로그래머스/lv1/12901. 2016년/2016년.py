def solution(a, b):
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total_days = sum(month_days[:a-1]) + b
    day_index = (total_days + 4) % 7  # 2016년 1월 1일이 금요일이므로 인덱스 4가 금요일을 나타냄
    
    return days[day_index]
