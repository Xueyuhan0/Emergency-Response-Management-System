# __Abstract__ 
In this project, our team will develop an emergency response management system for a city. The system will prioritize emergency situations based on their severity and ensure that the most critical issues are addressed first. We will use three different data structures (linked list, binary tree, and heap) to implement priority queues and compare their efficiency and complexity.<br/>
# __Catalogue__
## __Requirement Analysis of Project__
1. Functional requirements<br/>
Emergency Event Input:The system should be able to input new emergency events, such as event type, location, preliminary assessment of severity, etc.<br/>
Event priority evaluation: Automatically evaluate the priority of an event based on its severity.<br/>
Priority queue management:Implement priority queues using three data structures: linked list, binary tree, and heap, each of which can be sorted according to the priority of events.Support adding new events to the priority queue.Support removing and processing the highest priority (i.e. most urgent) event from the priority queue.Support viewing events and their priorities in the current queue.<br/>

2. Non functional requirements<br/>
Performance:Evaluate and compare the efficiency of insertion, deletion, and lookup operations of linked lists, binary trees, and heaps in implementing priority queues.Ensure that the response time and throughput of the system meet the requirements in high concurrency situations.<br/>
Scalability: The system design should take into account possible future requirements changes and extensions, such as adding new priority evaluation factors, supporting more types of emergency events, etc.<br/>
Reliability: The system should have high reliability to ensure stable operation in emergency situations without data loss.<br/>
Usability: The user interface should be intuitive and user-friendly, making it easy for emergency response personnel to quickly input and handle events.<br/>

3. Constraints<br/>
Technical selection: It has been determined to use linked lists, binary trees, and heaps to implement priority queues, and the implementation details of these data structures in specific programming languages and frameworks need to be considered.<br/>
Time and resource constraints: The project needs to be completed within the specified time frame, taking into account available development resources (such as personnel, equipment, etc.).<br/>
Legal regulations: The system must comply with relevant data protection laws and regulations to ensure the security of user privacy and sensitive information.<br/>


## __Design of Project__ 
1.Emergency<br/>
The code defines two classes: EmergencyType and Emergency.<br/>
_EmergencyType_ is an enumeration class used to indicate the type of emergency situation. It defines three different emergency situations: fire, medical, and police. The Emergency class is used to represent specific urgent objects. The constructor init takes four parameters and performs a type check when initializing the object to ensure that the emergency type is an enumeration value of type EmergencyType. The eq method compares whether two Emergency objects are equal by comparing the values of each attribute.<br/>
The _TestEmergency class_ inherits unittest. TestCase， Indicates that it is a unit test class.Test the emergency creation method to see if the emergency instance is created correctly and if the attribute values of the instance meet expectations.Test whether an invalid emergency type method will generate a Value Error when passing through an illegal emergency type.<br/>

2.Line<br/>
_Node class_: represents a node in a linked list. Each node contains data, priority, and a pointer to the next node.<br/>
_LinkedListPriorityQueue class_: Encapsulates the linked list structure and provides operations for inserting and extracting the largest (actually extracting the smallest, as the node with the lowest priority is placed first) element (extractmax).<br/>
_Extract-max_: It extracts the node with the lowest priority (i.e. the head node of the linked list). If the linked list is not empty, the algorithm will return the data of the head node and point the head pointer to the next node.<br/>

3.BSTPriority Queue<br/>
The BSTNode class represents the nodes of a binary search tree, each node containing data and priority.<br/>
_BSTPriority Queue_:Class encapsulates a binary search tree and provides insertion and extraction of maximum values.<br/>
_extract-max_:Extract and return the node with the highest priority using the maximum value extraction method. It uses the recursive auxiliary function - extract max: to find this node and its parent node.<br/>
_inorder_ :Used to display relevant information about nodes in the tree.                            
The TestBSTPriorityQueue class defines the test method test insert extract. First, create the BSTPriorityQueue object.<br/>
Insert three tasks into the queue, each with its associated priority (integer). Extract the highest priority task from the queue using the maximum value extraction method, and verify whether the extracted task meets expectations using the self.assertEqual assertion method. This process should be repeated three times, and the highest priority task should be extracted each time.<br/>

4.Heap structure<br/>
The _insert method_ adds a new (data, priority) group to the end of the heap, and then calls the heapify up method to move the newly inserted element to the appropriate location.<br/>
The _extractmax method_ extracts the element with the highest priority from the heap and returns the data section. It first exchanges the top element and the last element. Then pop up the last element. Finally, call the _heapify_down method to move the top element of the heap to the correct position.<br/>
The _change_priority_ method is used to change the priority of a specific data item in the heap to new_priority. It first finds and removes the matching elements, then calls the heapify_ dean method to adjust the male, and finally inserts the updated elements into the heap. The heapify_up method is used to move the element at index position upwards, with a value to the parent node less than or equal to the value of the current node.<br/>
_test_insert_extract_:This testing method verifies the correctness of insertion and extraction operations.<br/>
_test_search_and_change_priority_:This testing method verifies the correctness of search and change priority operations.<br/>

5.K-Nearest Neighbor Emergency Response Recommendation<br/>
(1)Emergency——k: Create two types of emergency and emergency response units, as well as an auxiliary function called calculating distance, to calculate the distance between two points. In addition, an enumeration of emergency situation types has been defined to represent different types of emergency situations.<br/>

(2)minheap——k: On the basis of minheap, it has been optimized by using this minimum heap to recommend k emergency response units closest to a certain emergency event. <br/>
_Init_: Constructor, initializes an empty list self. heap as the storage structure of the heap.<br/>
_Insert_: Insert an element into the heap, stored in the form of a tuple (priority, data), where priority is the priority (in this scenario, priority is the distance from the emergency event, the closer the distance, the higher the priority), and data is the data to be inserted (in this scenario, it is the emergency response unit). After insertion, adjust the heap using the _heapify_up method to maintain the properties of the smallest heap.<br/>
_Extractmin_: Remove and return the element with the lowest priority in the heap (i.e. the emergency response unit closest to the emergency event). If the heap is empty, return None. If there is only one element in the heap, return that element directly. Otherwise, swap the top element (i.e. the element with the lowest current priority) with the last element of the heap, then remove the last element of the heap and readjust the heap using the _heapify_down method to maintain the properties of the smallest heap.<br/>
_Heapify_up_: An auxiliary method used to adjust the heap upwards after inserting new elements to maintain the property of the smallest heap.<br/>
_Heapify_down_: An auxiliary method used to adjust the heap downwards after removing the top element to maintain the properties of the smallest heap.<br/>
_Swap_: An auxiliary method used to swap the positions of two elements in the heap.<br/>
_Repr_: defines the string representation of the heap for easy debugging and viewing of its contents.<br/>
_The recommendanddealest_units function_:This function takes three parameters: an emergency object (representing an emergency event with x and y attributes indicating its location), a response_units list (containing emergency response units, each with x and y attributes indicating its location), and an integer k (representing the number of nearest emergency response units to recommend).<br/>

(3)main——k: Go to the k emergency response units closest to an emergency event (using fire as an example). First, create an emergency event object using the Emergency class. Then call the function and set the variable k, which means that k emergency response units nearest to the emergency need to be found. Finally, use a for loop to traverse the nearest_units list and print out the information for each emergency response unit.<br/>

6.Visual<br/>
In a Python program using the Tkinter graphical user interface, they define a class called EmergencyQueueApp that manages an emergency queue and uses a minimum heap as a priority queue to store these emergency events. Add the function of emergency events.<br/>
The add emergency method is called when the user clicks the "Add Emergency" button. This method obtains the ID, type, severity, location, and coordinates of an emergency event from UI elements, and then attempts to create an Emergency object. If all inputs are valid (for example, severity and coordinates can be converted to integers, and the type matches the value in the EmergencyType enumeration), the emergency event (and its severity as priority) is inserted into the minimum heap and the list box in the UI is updated to display a new emergency event list. If any error occurs (such as type conversion failure or type mismatch), an error message box is displayed.<br/>
_UI Interaction Function_: remove_item method: Ensure removal of an emergency event from both the display list (self.queue_listbox) and the underlying data structure (self.queue.heap) is synchronized. Deleting directly from self.queue_listbox and attempting to remove from self.queue.heap by index can lead to synchronization issues. Instead:Remove the item from self.queue.heap.Update self.queue_listbox to reflect the updated list after removal.show_details method: Implement a tooltip feature for displaying detailed information when hovering over an emergency event in the list box. Since Tkinter's Listbox doesn't support tooltips by default, consider using additional libraries like ttk's Tooltip or custom solutions.<br/>
_UI Update and Clear Functions_: update_listbox method: Update the list box (self.queue_listbox) to display summarized information about all current emergency events stored in the smallest heap (self.queue.heap). This maintains synchronization between UI and data after adding or removing events.clear_entries method: Clear all input fields to facilitate the entry of new emergency information without interference from previous data.<br/>


## Running and Debugging of Project
![test debug](https://github.com/Xueyuhan0/Emergency-Response-Management-System/blob/2/test%20debug.png)<br/>
This image shows the test debug.<br/>
![coverage report](https://github.com/Xueyuhan0/Emergency-Response-Management-System/blob/2/coverage%20report.png)<br/>
This image shows the coverage of detection. <br/>
![result1](https://github.com/Xueyuhan0/Emergency-Response-Management-System/blob/2/result1.png)<br/>
This image shows a queue sorted using three methods and provides the time for inserting and deleting elements, respectively.<br/>
![result2-main_k](https://github.com/Xueyuhan0/Emergency-Response-Management-System/blob/2/result2-main_k.png)<br/>
This image shows the running results of main_k.<br/>
![result3-UI](https://github.com/Xueyuhan0/Emergency-Response-Management-System/blob/2/result3-UI.png)<br/>
This image shows the running results of UI.<br/>


## Summary
In this project, our team is committed to designing and implementing an efficient emergency response management system aimed at enhancing the city's ability to respond to emergencies.<br/>
We conduct simulation tests to verify whether the system can correctly recognize and prioritize high priority events, while evaluating the response time and resource consumption of each data structure.<br/>
The implementation of linked lists has the worst performance due to the need for frequent traversal to maintain order, especially when dealing with large amounts of data.
Binary trees, especially balanced binary trees, provide good average performance, but in worst-case scenarios (such as frequent rotations to maintain balance) they may approach linked lists.<br/>
The heap structure stands out for its efficient insertion, deletion, and access operations, making it particularly suitable for scenarios that require frequent updates and access to the highest priority elements.<br/>
The three implementation methods are similar in terms of spatial complexity, mainly depending on the number of storage elements. Heap and binary trees may be slightly higher than linked lists in some implementations due to the need for additional pointers or references to maintain structure.<br/>
For emergency response management systems, real-time performance and accuracy are crucial. The heap structure has become the preferred choice due to its excellent performance. Although linked lists are simple, performance bottlenecks limit their application in large-scale data processing. Binary trees provide flexibility and certain performance guarantees, but may have higher implementation complexity and maintenance costs than heaps. This project validates the superiority of the heap structure in terms of performance.<br/>
In the future, we will further optimize the system, explore more advanced data structures and algorithms, to further improve the response speed and stability of the system.<br/>


## Division of Labor within the Group
_Week 1_: Yuhan Xue is responsible for the emergency class, Jiayue Wu is responsible for the structural linked list, Menghan Wang is responsible for the structural tree, Xinran Qi is responsible for the structural heap, and Yanfei Sun is responsible for optimizing the structure and conducting output comparison.<br/>
_Week 2_: Yuhan Xue extended the emergency class and added a distance calculation section. At the same time, Xinran Qi optimized the heap. Yanfei Sun was responsible for testing the above parts and outputting the final results. Menghan Wang and Jiayue Wu were responsible for the final visualization section, realizing the function of adding and deleting information. Finally, Xinran Qi and Yuhan Xue completed the report, while Menghan Wang, Jiayue Wu, and Yanfei Sun completed the PowerPoint production.<br/>


## Tips
Yuhan Xue: In the first week, I was responsible for the initial work of the emergency class, and in the second week, I expanded the emergency class and added a distance calculation section. Throughout the process, I deepened my understanding of class design and functional extension through practical operations, especially encountering some challenges in the implementation of distance calculation, but ultimately successfully completed the task. When collaborating with Xinran Qi to write the report, I further deepened my understanding of the overall structure of the project, which will be of great help to my future learning and work.<br/>
Jiayue Wu: In the first week, I focused on the design and implementation of structured linked lists. In the second week, I participated in the development of the final visualization part and implemented information addition and deletion functions. Throughout the entire project process, I learned how to design and manage complex data structures, especially the flexibility and efficiency of linked lists in practical applications. Completing the final visualization function with Menghan Wang gave me a deeper understanding of the overall project outcome.<br/>
Menghan Wang: In the first week, I was responsible for the design and implementation of the structural tree, and in the second week, I was responsible for the final visualization part with Jiayue Wu. Through this project, I have gained a deeper understanding of the application and optimization of tree structures, especially how to make complex data structures more intuitive and understandable in visual design. This experience not only strengthened my programming skills, but also enhanced my teamwork and project management skills.<br/>
Xinran Qi: In the first week, I was responsible for the design and optimization of the structural stack, and in the second week, I continued to optimize the performance of the stack. Through this process, I learned how to improve program efficiency and response speed through optimizing data structures. When collaborating with Yuhan Xue to write the report, I further deepened my understanding of the overall structure and design philosophy of the project, which will be of great help to my future learning and career development.<br/>
Yanfei Sun: In the first week, I was responsible for optimizing the structure and preparing for output comparison. In the second week, I was mainly responsible for testing the above parts and outputting the final results. Through this project, I not only deepened my understanding of data structure and algorithm optimization, but also improved my abilities in project management and team collaboration. Finally, I worked with Menghan Wang and Jiayue Wu to complete the PowerPoint production, which perfectly showcased our team's achievements and gains.<br/>

