import csv
import difflib

def compare_csv_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        csv_reader1 = csv.reader(file1)
        csv_reader2 = csv.reader(file2)

        lines1 = list(csv_reader1)
        lines2 = list(csv_reader2)

        differ = difflib.Differ()
        missing_lines = []
        changed_lines = []
        new_lines = []

        f = True
        line_num = 1
        l = 1
        while f == True:
            
            diff = list(differ.compare(lines1[l], lines2[l]))
            #print(diff)
            if l == max(len(lines1)-1, len(lines2)-1):
                f = False
            
            for line in diff:
                if line.startswith('  '):
                    line_num += 1
                    
                elif line.startswith('- '):
                    missing_lines.append((line_num, line[2:]))
                    line_num += 1
                    
                elif line.startswith('+ '):
                    new_lines.append((line_num, line[2:]))
                    
                elif line.startswith('? '):
                    line_num += 1
                    
                else:
                    changed_lines.append((line_num, line[2:]))

            l += 1

            if missing_lines:
                print("Missing Lines:")
                for line_num, line_data in missing_lines:
                    print(f"Line {line_num}: {line_data}")
                print()

            if changed_lines:
                print("Changed Lines:")
                for line_num, line_data in changed_lines:
                    print(f"Line {line_num}: {line_data}")
                print()

            if new_lines:
                print("New Lines:")
                for line_num, line_data in new_lines:
                    print(f"Line {line_num}: {line_data}")
                print()

            


if __name__ == "__main__":
    file1_path = r"C:/tmp/files/EmployeeData.csv"
    file2_path = r"C:/tmp/files/EmployeeData2.csv"
    compare_csv_files(file1_path, file2_path)
