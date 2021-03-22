# You have a RecentCounter class which counts the number of recent requests within a certain
# time frame.
#
# Implement the RecentCounter class:
#
# RecentCounter() Initializes the counter with zero recent requests.
# int ping(int t) Adds a new request at time t, where t represents some time in milliseconds,
# and returns the number of requests that has happened in the past 3000 milliseconds (including
# \the new request). Specifically, return the number of requests that have happened in the inclusive
# range [t - 3000, t].
# It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

class RecentCounter:

    def __init__(self, counter):
        counter = 0
    def ping(self, t):
        #print(t)
        return t

# Your RecentCounter object will be instantiated and called as such:
t = 10
obj = RecentCounter()
param_1 = obj.ping(t)
print(param_1)