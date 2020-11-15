class Queue(object):

    def __init__(self):
        self.l = []

    def enqueue(self, e):
        self.l.append(e)

    def dequeue(self):
        front_element = self.l[0]
        self.l = self.l[1:]
        return front_element

    def first(self):
        return self.l[0]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)
