# __Abstract__ 

# __Catalogue__
## __Description Of Project__
In this project, our team will develop an emergency response management system for a city. The system will prioritize emergency situations based on their severity and ensure that the most critical issues are addressed first. We will use three different data structures (linked list, binary tree, and heap) to implement priority queues and compare their efficiency and complexity.


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
EmergencyType is an enumeration class used to indicate the type of emergency situation. It defines three different emergency situations: fire, medical, and police. The Emergency class is used to represent specific urgent objects. The constructor init takes four parameters and performs a type check when initializing the object to ensure that the emergency type is an enumeration value of type EmergencyType. The eq method compares whether two Emergency objects are equal by comparing the values of each attribute.<br/>
The TestEmergency class inherits unittest. TestCase， Indicates that it is a unit test class.Test the emergency creation method to see if the emergency instance is created correctly and if the attribute values of the instance meet expectations.Test whether an invalid emergency type method will generate a Value Error when passing through an illegal emergency type.<br/>

2.Line<br/>
Node class: represents a node in a linked list. Each node contains data, priority, and a pointer to the next node.<br/>
LinkedListPriorityQueue class: Encapsulates the linked list structure and provides operations for inserting and extracting the largest (actually extracting the smallest, as the node with the lowest priority is placed first) element (extractmax).<br/>
Extract-max: It extracts the node with the lowest priority (i.e. the head node of the linked list). If the linked list is not empty, the algorithm will return the data of the head node and point the head pointer to the next node.<br/>
Extractmax: It extracts the node with the lowest priority (i.e. the head node of the linked list). If the linked list is not empty, the algorithm will return the data of the head node and point the head pointer to the next node.<br/>

3.BSTPriority Queue<br/>
The BSTNode class represents the nodes of a binary search tree, each node containing data and priority.<br/>
BSTPriority Queue:Class encapsulates a binary search tree and provides insertion and extraction of maximum values.<br/>
extract-max:Extract and return the node with the highest priority using the maximum value extraction method. It uses the recursive auxiliary function - extract max: to find this node and its parent node.<br/>
-inorder :Used to display relevant information about nodes in the tree. <br/>                           
The TestBSTPriorityQueue class defines the test method test insert extract. First, create the BSTPriorityQueue object.<br/>
Insert three tasks into the queue, each with its associated priority (integer). Extract the highest priority task from the queue using the maximum value extraction method, and verify whether the extracted task meets expectations using the self.assertEqual assertion method. This process should be repeated three times, and the highest priority task should be extracted each time.<br/>





