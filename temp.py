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
     print(count)
     
     #syntax
     for key in count:
         node = HeapNode(key, count[key])
         heap = heapq.heappush(node)
         
     while(len(heap)>1):
         node1 = heapq.heappop(heap)
         node2 = heapq.heappop(heap)
         merged = HeapNode(None, node1.freq + node2.freq)
         merged.left = node1
         merged.right = node2
         heapq.heappush(heap, merged)
         
     def makeCode(self, root, CurrentCode):
         if(root == None):
             return
         if(root.char != None):
            #to do 
             return
         self.makeCode(root.left, CurrentCode + '0')
         self.makeCode(root.right, CurrentCode + '1')
        
     print(heap)    
  
main()