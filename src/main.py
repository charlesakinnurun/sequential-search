"""
Sequential Search (Linear Search) Implementation and Visualization
------------------------------------------------------------------
This script provides a detailed look at how Linear Search works by 
iterating through a list one element at a time until the target is 
found or the end of the list is reached.
"""

import time

def sequential_search(data_list, target):
    """
    Performs a standard Sequential Search.
    
    Args:
        data_list (list): The list of items to search through.
        target: The value we are looking for.
        
    Returns:
        int: The index of the target if found, else -1.
    """
    # 1. Start from the leftmost element of the list
    # 2. Compare the target with each element sequentially
    for index in range(len(data_list)):
        # Check if the current element matches the target
        if data_list[index] == target:
            # Found! Return the index immediately
            return index
            
    # 3. If we finish the loop without returning, the item isn't there
    return -1

class SearchVisualizer:
    """
    A utility class to print the search process to the console 
    with visual highlights.
    """
    
    @staticmethod
    def visualize(data_list, target):
        print(f"\n{'='*60}")
        print(f"SEARCHING FOR: [{target}] in {data_list}")
        print(f"{'='*60}")
        
        found_index = -1
        
        # Iterate through the list with index and value
        for i, value in enumerate(data_list):
            # Create a visual representation of the current search step
            # Current element being checked is highlighted with [ ]
            display = []
            for j, val in enumerate(data_list):
                if i == j:
                    display.append(f"->[{val}]<-") # Highlighting current pointer
                else:
                    display.append(str(val))
            
            # Print the current state
            print(f"Step {i+1}: {' '.join(display)}")
            
            # Check for match
            if value == target:
                print(f"MATCH FOUND! Target {target} is at index {i}.")
                found_index = i
                break
            else:
                print(f"      {value} != {target}. Moving to next...")
            
            # Small pause for 'animation' effect
            time.sleep(0.3)
            
        if found_index == -1:
            print(f"\nFINISHED: Target {target} was not found in the list.")
        
        print(f"{'='*60}\n")
        return found_index

def main():
    """
    Main execution block to demonstrate different scenarios.
    """
    
    # Example 1: Searching for a number in a random list
    numbers = [10, 45, 2, 33, 8, 99, 14]
    SearchVisualizer.visualize(numbers, 33)
    
    # Example 2: Searching for a string in a list of names
    names = ["Alice", "Bob", "Charlie", "David"]
    SearchVisualizer.visualize(names, "Eve") # Testing a 'Not Found' case
    
    # Example 3: Searching at the very start (Best Case)
    SearchVisualizer.visualize(numbers, 10)
    
    # Example 4: Searching at the very end (Worst Case)
    SearchVisualizer.visualize(numbers, 14)

    # Illustration of Time Complexity
    print("\n--- PERFORMANCE ANALYSIS ---")
    print("Sequential Search Complexity:")
    print("1. Best Case: O(1) - Item is at the first position.")
    print("2. Worst Case: O(n) - Item is at the last position or missing.")
    print("3. Average Case: O(n/2) -> O(n).")

if __name__ == "__main__":
    main()