# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B3tJuSfEhTyQyc0zsAALMMgXBqdEZzFK
"""

import sys

""" 
Class of the Binary tree
self.left is pointer to left child
self.right is pointer to right child
"""
class Tree:
  def __init__(self,left,right):
    self.left = left
    self.right = right
  
  # Function to get the both child 
  def children(self):
    return (self.left,self.right)

  # Function to get only left child
  def get_left_child(self):
    return self.left
  
  # Function to get only right child
  def get_right_child(self):
    return self.right

#Phase I - Build the Huffman Tree
def huffman_encoding(data):

  # list contain frequency distribution of the character
  frequency_list = calc_frequency(data)

  while len(frequency_list)>=2:
    char1,freq1 = frequency_list[-1]
    char2,freq2 = frequency_list[-2]
    frequency_list = frequency_list[:-2]
    new_node = Tree(char1,char2)
    frequency_list.append((new_node,freq1+freq2))
    frequency_list = sorted(frequency_list,key=lambda x: x[1],reverse=True)
    #print(frequency_list)

  code_dict={}
  
  """
  Phase II - Generate the Encoded Data
  """
  def tree_traversal(node,code=''):
      if type(node) is str:
        return {node:code}
      left_child,right_child = node.children()
      code_dict.update(tree_traversal(left_child,code+'0'))
      code_dict.update(tree_traversal(right_child,code+'1'))
      return code_dict
    
  tree_traversal(frequency_list[0][0])
  #print('code=',code_dict)

  code =''
  #Finally creating the Huffman code using the code_dict
  for char in data.lower():
    
    code+=code_dict[char]

  return code,frequency_list[0][0]
  #print('code',code)


""" A function to generate the Sorted (decending) frequency dictionary.
      Argument = (string)
      return  = sorted dictionary (on the basis of the frequency of the charecter the
      dictionary id sorted in decending order )
"""
def calc_frequency(data):
  #temperory dictionary variable
  d = dict()
  # traversing the whole string
  for char in data.lower():
    if char in d:
      d[char]+=1
    else:
      d[char] =1
  d=sorted(d.items(),key=lambda x: x[1], reverse=True)
  return d




def huffman_decoding(data,tree):
  substring=str()
  st=str()
  d = dict()
  node = tree
  for bit in data:
   
    if bit =='0':
      node = node.get_left_child()
    if bit =='1':
      node = node.get_right_child()
    if type(node) == str:
      #print(substring)
      #print(node)
      st+=node
      #d[substring]=node
      substring=''
      node = tree
    #print(bit)
   
    substring+=bit
  
  return st.capitalize()
  #print(st)

def test_case(data):
    if data is None or len(str(data)) == 0:
        print('Empty data!')
        return

    if type(data) != str:
        print('Invalid data!', data)
        return

    print("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print("The content of the data is: {}\n".format(data))

    encoded_data, t = huffman_encoding(data)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data.replace(' ', ''), base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, t)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))


if __name__ == "__main__":
    test_case('The bird is the word')
    print("-----------------------------------------------------------------------------------------")
    test_case('I am the best best best 11111111111111111')
    print("-----------------------------------------------------------------------------------------")
    
    test_case('')
    print("-----------------------------------------------------------------------------------------")
    test_case(123)

