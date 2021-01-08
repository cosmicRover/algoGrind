class job:
  def __init__(self, start, end, cpu_load):
    self.start = start
    self.end = end
    self.cpu_load = cpu_load

def find_max_cpu_load(jobs):
  '''
  interval approach. overlap_min approach
  '''
  jobs.sort(key=lambda x:x.start)
  stack = [jobs[0]]

  for i in range(1, len(jobs)):
    #if overlap, reshape
    if stack[-1].end >= jobs[i].start:
      start = min(stack[-1].start, jobs[i].start)
      end = max(stack[-1].end, jobs[i].end)
      work = stack[-1].cpu_load + jobs[i].cpu_load
      
      stack[-1].start = start
      stack[-1].end = end
      stack[-1].cpu_load = work

  #get the max between reshaped intervals vs original jobs
  return max(getMax(stack), getMax(jobs))

def getMax(arr):
  m = float("-inf")
  for x in arr:
    m = max(m, x.cpu_load)
  return m