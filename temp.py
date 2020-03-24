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
         
def heap_to_code(root,currentCode,codes,reverse):
    if (root == None):
        return

    if(root.char!=None):
        codes[root.char]= currentCode
        reverse[currentCode]=root.char

    heap_to_code(root.left,currentCode + "0",codes,reverse)
    heap_to_code(root.right,currentCode + "1",codes,reverse)                   

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
         print(node.char)
         heapq.heappush(list1 ,node)
                  
     while(len(list1)>1):
         node1 = heapq.heappop(list1)
         node2 = heapq.heappop(list1)
         merged = HeapNode(None, node1.freq + node2.freq)
         merged.left = node1
         merged.right = node2
         heapq.heappush(list1, merged)
     
     root =heapq.heappop(list1)  
     # Encode the read text
     currentCode ="";
     codes={};
     reverse={};
     heap_to_code(root,currentCode,codes,reverse);
     
     encoded_text =""
     for character in text:
         encoded_text += codes[character]
         
     print(encoded_text)
     #Decode the encoded text
     code=""
     decode_text=""
     for bit in encoded_text:
         code +=bit
         if(code in reverse):
             character =reverse[code]
             decode_text +=character
             code = ""
             
     print(decode_text)

main()
