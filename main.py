import re
from collections import Counter

class LogFileAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.log_data = self._read_file()

    #underscore functions indicate internal use only
    def _read_file(self):
        with open(self.file_name, 'r') as file:
            return file.readlines()

    def count_error(self):
        error_count = sum('ERROR' in line for line in self.log_data)
        print(f"Total errors: {error_count}")
    
    def extract_ip_adresses(self):
        ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
        ips = [match.group() for line in self.log_data for match in ip_pattern.finditer(line)]
        return ips

    def count_ip_adresses(self):
        ips = self.extract_ip_adresses()
        count_ips = Counter(ips)
        print("\nIP address counts:")
        for ip, count in count_ips.items():
            print(f"{ip}: {count}")

    def extract_user_activity(self):
        activity_pattern = re.compile(r'UserActivity: (\w+)')
        activities = [match.group(1) for line in self.log_data for match in activity_pattern.finditer(line)]
        return activities

    def count_user_activities(self):
        activities = self.extract_user_activity()
        count_activities = Counter(activities)
        print("\nUser activities counts:")
        for act, count in count_activities.items():
            print(f"{act}: {count}")

    def extract_time(self):
        time_pattern = re.compile(r'\b\d{2}:\d{2}:\d{2}\b')
        time = [match.group() for line in self.log_data for match in time_pattern.finditer(line)]
        return time

    def start_time(self):
        time = self.extract_time()
        start = time.pop(0)
        return start

    def end_time(self):
        time = self.extract_time()
        end = time.pop()
        return end

    def activity_ip_at(self, time_frame):
        time_pattern = re.compile(r'\b\d{2}:\d{2}:\d{2}\b')
    
        for line in self.log_data:
            
            if time_pattern.search(line) and time_frame in line:
                activity_pattern = re.compile(r'UserActivity: (\w+)')
                activity_search = activity_pattern.search(line)
                activity_match = activity_search.group(1)

                ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
                ip_search = ip_pattern.search(line)
                ip_match = ip_search.group()
                print(f"Hour: {time_frame} - IP address: {ip_match} - Activity: {activity_match}")



            
analyze = LogFileAnalyzer('example.txt')

analyze.count_error()
analyze.count_ip_adresses()
analyze.count_user_activities()


analyze.activity_ip_at('12:30:00')




    
