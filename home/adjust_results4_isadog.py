# TODO 4: Define adjust_results4_isadog function
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if the classifier correctly
    classified images as 'a dog' or 'not a dog'.

    Parameters:
        results_dic (dict): Dictionary with 'key' as image filename and 'value' as a List.
        dogfile (str): A text file that contains names of all dogs from the classifier and pet image files.

    Returns:
        None (The results_dic dictionary is modified in place.)
    """

    # Create a dictionary to store the dog names
    dognames_dic = {}

    # Open and read the dog names from the provided file
    with open(dogfile, 'r') as file:
        for line in file:
            dog_name = line.strip().lower()  # Strip newline characters and convert to lowercase
            # Check for duplicate dog names
            if dog_name in dognames_dic:
                print(f"Warning: Duplicate dog name found in dognames.txt: {dog_name}")
            else:
                dognames_dic[dog_name] = 1

    # Iterate through the results dictionary to adjust the values
    for key in results_dic:
        pet_label = results_dic[key][0].lower()
        classifier_label = results_dic[key][1].lower()

        # Check if the pet image label is in the dog names dictionary
        if pet_label in dognames_dic:
            results_dic[key].append(1)  # Pet Image Label is a dog
        else:
            results_dic[key].append(0)  # Pet Image Label is not a dog

        # Check if the classifier label is in the dog names dictionary
        if classifier_label in dognames_dic or False:
            results_dic[key].append(1)  # Classifier Label is a dog
        else:
            results_dic[key].append(0)  # Classifier Label is not a dog
