# import os
# can you combine these 2 functions??

# def bottom_most_directory(full_path):
#     # Normalize the path to handle different separators and remove redundant separators
#     normalized_path = os.path.normpath(full_path)
    
#     # Split the path into components
#     components = normalized_path.split(os.sep)
    
#     # Return the last component, which is the bottom-most directory
#     return components[-1]

# # Example usage:
# full_path = "/home/user/Documents/Project"
# bottom_most = bottom_most_directory(full_path)
# print(bottom_most)  # Output: 'Project'
''' WORKING BUT 2 seperate functions'''

# import csv
# import os

# def bottom_most_directory(full_path):
#     # Normalize the path to handle different separators and remove redundant separators
#     normalized_path = os.path.normpath(full_path)
    
#     # Split the path into components
#     components = normalized_path.split(os.sep)
    
#     # Return the last component, which is the bottom-most directory
#     return components[-1]

# def cut_and_paste_row(input_csv_filename, output_csv_filename, patient_path, error_code):
#     try:
#         # Extract the Patient UHID from the path
#         uhid_value = bottom_most_directory(patient_path)
        
#         # Read the input CSV and identify the rows to be cut
#         rows_to_write = []
#         remaining_rows = []
#         with open(input_csv_filename, 'r', newline='') as csvfile:
#             reader = csv.DictReader(csvfile)
#             fieldnames = reader.fieldnames + ['ERROR CODE']
            
#             for row in reader:
#                 if row['Patient ID (UHID)'] == uhid_value:
#                     row['ERROR CODE'] = error_code
#                     rows_to_write.append(row)
#                 else:
#                     remaining_rows.append(row)
        
#         if rows_to_write:
#             # Write the identified rows to the output CSV, appending if the file exists
#             if os.path.exists(output_csv_filename):
#                 with open(output_csv_filename, 'a', newline='') as csvfile:
#                     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#                     writer.writerows(rows_to_write)
#             else:
#                 with open(output_csv_filename, 'w', newline='') as csvfile:
#                     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#                     writer.writeheader()
#                     writer.writerows(rows_to_write)
            
#             # Write the remaining rows back to the input CSV
#             with open(input_csv_filename, 'w', newline='') as csvfile:
#                 writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
#                 writer.writeheader()
#                 writer.writerows(remaining_rows)
            
#             print(f"Rows with UHID '{uhid_value}' have been cut from '{input_csv_filename}' and appended to '{output_csv_filename}' with error code '{error_code}'.")
#         else:
#             print(f"No rows found with UHID '{uhid_value}' in '{input_csv_filename}'.")
            
#     except FileNotFoundError:
#         print(f"Error: File '{input_csv_filename}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage:
# input_csv = 'C:/Users/EIOT/Desktop/Final - Copy.csv'
# output_csv = 'Logs/UHID error/output.csv'
# patient_path = 'C:/Users/EIOT/Desktop/Patients/500261503'
# error_code = 'error messege'

# cut_and_paste_row(input_csv, output_csv, patient_path, error_code)

""" New Test """

import csv
import os

def cut_and_paste_row(input_csv_filename, output_csv_filename, patient_path, error_code):
    try:
        # Extract the Patient UHID from the path
        normalized_path = os.path.normpath(patient_path)
        components = normalized_path.split(os.sep)
        uhid_value = components[-1]
        
        # Read the input CSV and identify the rows to be cut
        rows_to_write = []
        remaining_rows = []
        with open(input_csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            fieldnames = reader.fieldnames + ['ERROR CODE']
            
            for row in reader:
                if row['Patient ID (UHID)'] == uhid_value:
                    row['ERROR CODE'] = error_code
                    rows_to_write.append(row)
                else:
                    remaining_rows.append(row)
        
        if rows_to_write:
            # Write the identified rows to the output CSV, appending if the file exists
            if os.path.exists(output_csv_filename):
                with open(output_csv_filename, 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerows(rows_to_write)
            else:
                with open(output_csv_filename, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(rows_to_write)
            
            # Write the remaining rows back to the input CSV
            with open(input_csv_filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(remaining_rows)
            
            print(f"Rows with UHID '{uhid_value}' have been cut from '{input_csv_filename}' and appended to '{output_csv_filename}' with error code '{error_code}'.")
        else:
            print(f"No rows found with UHID '{uhid_value}' in '{input_csv_filename}'.")
            
    except FileNotFoundError:
        print(f"Error: File '{input_csv_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_csv = 'C:/Users/EIOT/Desktop/Final - Copy.csv'
output_csv = 'Logs/UHID error/output.csv'
patient_path = 'C:/Users/EIOT/Desktop/Patients/5002611434*'
error_code = 'ERR001'

cut_and_paste_row(input_csv, output_csv, patient_path, error_code)
