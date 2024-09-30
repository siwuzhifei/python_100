import re
import csv

# Read the log file and extract the package number and time
def read_log(file):
    # Regular expression to match the package number and time
    pattern_connet = re.compile(r'seq=([0-9a-fA-F]+).*time=([\d.]+)ms')
    pattern_lost = re.compile(r'for seq=([0-9a-fA-F]+)')
    data_list = {}

    with open(log_file, 'r') as f:
        for line in f:
            if 'TTL=' in line:
                match = pattern_connet.search(line)
                if match:
                    p_hexnumber = match.group(1)
                    p_decimal_number = int(p_hexnumber, 16)
                    time_ms = match.group(2)
                    # print(p_decimal_number, time_ms)
                    data_list.update({p_decimal_number: time_ms})
            elif 'Timeout' in line:
                match_lost = pattern_lost.search(line)
                if match_lost:
                    package_hexnumber = match_lost.group(1)
                    package_decimal_number = int(package_hexnumber, 16)
                    data_list.update({package_decimal_number: 0.0})

            else:
                pass


    # Write the extracted data to a csv file
    with open('pinglog.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for p_number, time in data_list.items():
            writer.writerow([p_number, time])

# Read the csv file and calculate the max_length_time, min_length_time and lost count
def read_csv(file):
    time_length = 0
    max_time = 0
    min_time = 1000
    lost_count = 0

    with open(file, 'r') as f:
        reader = csv.reader(f)
        for p_number, time in reader:
            if float(time) != 0.0:
                time_length += float(time)
                if time_length > max_time:
                    max_time = time_length
            else:
                if time_length < min_time and time_length != 0:
                    min_time = time_length
                lost_count += 1
                pass
                time_length = 0

        print(max_time, min_time, lost_count)


# Main function
log_file = ("0928.log")
read_log(log_file)
read_csv('pinglog.csv')
