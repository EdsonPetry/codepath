"""
Problem 4: Organize Scene Data by Date
Given a list of scene records, where each record contains a date and a description, 
sort the list by date and return the sorted list. Each record is a tuple where the 
first element is the date in YYYY-MM-DD format and the second element is the description of the scene.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def main():
    scene_records = [
        ("2024-08-15", "Climax"),
        ("2024-08-10", "Introduction"),
        ("2024-08-20", "Resolution"),
        ("2024-08-12", "Rising Action")
    ]
    print(organize_scene_data_by_date(scene_records))

    scene_records = [
        ("2023-07-05", "Opening"),
        ("2023-07-07", "Conflict"),
        ("2023-07-01", "Setup"),
        ("2023-07-10", "Climax")
    ]
    print(organize_scene_data_by_date(scene_records))
    """
    Example Output:

    [('2024-08-10', 'Introduction'), ('2024-08-12', 'Rising Action'), ('2024-08-15', 'Climax'), ('2024-08-20', 'Resolution')]
    [('2023-07-01', 'Setup'), ('2023-07-05', 'Opening'), ('2023-07-07', 'Conflict'), ('2023-07-10', 'Climax')]
    """

def organize_scene_data_by_date(scene_records):
    val_dict = {}
    for t in scene_records:
        val_dict[t[0]] = t[1]

    
    dict_sorted = dict(sorted(val_dict.items()))
    lst=[]

    for k,v in dict_sorted.items():
        lst.append((k,v))

    return lst

if __name__ == "__main__":
   main()