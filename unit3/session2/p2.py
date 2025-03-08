# You are organizing a festival and want to manage the queue of requests to perform. Each request has a priority. Use a queue to process the performance requests in the order they arrive but ensure that requests with higher priorities are processed before those with lower priorities. Return the order in which performances are processed.
from collections import deque 
def process_performance_requests(requests):
    ordered = dict()
    queue = deque()
    q = sorted(requests, key=lambda x: x[0])
    for request in requests:
        queue.append(request)


    # #4. Remove an element from the beginning (left side) of the queue
# removed_elt = queue.popleft()
# print(removed_elt) # Prints 1

    # pass

# Example Usage:

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

# Example Output:

['Music', 'Dance', 'Drama']
['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']

# # 1. Import the deque module
# from collections import deque 

# # 2. Initialize a new deque object (a new queue)
# queue = deque()

# #3. Add a new element, 1, to the end (right side) of the queue
# queue.append(1)

# #4. Remove an element from the beginning (left side) of the queue
# removed_elt = queue.popleft()
# print(removed_elt) # Prints 1