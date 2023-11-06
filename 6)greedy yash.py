'''
g= graph, source=s, destination=des, greedy_shotest_path=gsp, 
current_vertex=c_v, neighbor=n,
next_vertex= n_v, min_weight= m_w, 
weight=w, source_vertex= s_v, 
'''

def gsp(g, s, des):
    path = [s]
    c_v = s

    while c_v != des:
        nei = g[c_v]
        n_v = None
        m_w = float('inf')

        for nei, w in nei.items():
            if nei not in path and w < m_w:
                m_w = w
                n_v = nei

        if n_v is None:
            # If no unvisited n, stop.
            break

        path.append(n_v)
        c_v = n_v

    return path

# Example g represented as an adjacency list
g = {
    'A': {'B': 2, 'C': 3},
    'B': {'C': 1, 'D': 4},
    'C': {'D': 2},
    'D': {'E': 3},
    'E': {},
}

s_v = 'A'
des_v = 'E'
shortest_path = gsp(g, s_v, des_v)
print(shortest_path)

# job 
def job_scheduling(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [None] * (max_deadline + 1)

    for job in jobs:
        for i in range(job[1], 0, -1):
            if schedule[i] is None:
                schedule[i] = job
                break

    scheduled_jobs = [job for job in schedule if job is not None]

    return scheduled_jobs

# Example usage
jobs = [(1, 1, 15), (2, 2, 50), (3, 2, 10), (4, 1, 25)]
scheduled_jobs = job_scheduling(jobs)
print("Scheduled Jobs:", scheduled_jobs)

