# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import heapq

class HeapNode():
         def __init__(self, char, freq):
             self.char = char
             self.freq = freq
             self.left = None
             self.right = None
         
         
         def __cmp__(self, other):
             if(other == None):
                 return -1
             if(isinstance(other, HeapNode)):
                 return -1
             return self.freq > other.freq
        
        
         def __lt__(self, other):
             return self.freq < other.freq

         def __eq__(self, other):
             if(other == None):
                 return False
             if(not isinstance(other, HeapNode)):
                 return False
             return self.freq == other.freq

def main():
     f=open("Huffman.txt", "r");
     if f.mode == 'r':
         text =f.read();
         print(text);
     count = {};   
     for x in text:
         if  x in count.keys():
             count[x]+=1
         else:
             count[x] = 1
     total = sum(count.values());
     
     for value in count.keys():
         count[value] = count[value]/total;
     #print(count)
     
     list1 = []
     heapq.heapify(list1)
     
     for key in count:
         node = HeapNode(key, count[key])
         print(node)
         heapq.heappush(list1 ,node)
                  
     while(len(list1)>1):
         node1 = heapq.heappop(list1)
         node2 = heapq.heappop(list1)
         merged = HeapNode(None, node1.freq + node2.freq)
         merged.left = node1
         merged.right = node2
         heapq.heappush(list1, merged)
         
  
main()
