pages_count_current_book = int(input())
pages_per_hour = int(input())
days_count = int(input())
reading_time_per_book = pages_count_current_book // pages_per_hour
hours_to_read_per_day = reading_time_per_book // days_count
print(hours_to_read_per_day)

