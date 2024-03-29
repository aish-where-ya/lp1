# -*- coding: utf-8 -*-
"""hpc4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JiKqI6fsmWFBkFBXAyG85TsOPr3R8Pb3
"""

!nvcc --version

code="""
#include <bits/stdc++.h>
#include <chrono>
#include<omp.h>
#define N 258
using namespace std;

int search(int a[], int low, int high,int elem)
{
  if(low<=high)
  {
    int mid= (low+high)/2;
    //printf("lol \\n");
    if(a[mid] == elem)
      return mid;
      
    else if(a[mid] > elem)
      search(a,low,mid,elem);
      
    else if(a[mid] < elem)
      search(a,mid+1,high,elem);
  }
  return -1;
}

int main()
{
  int *a;
  int k =thread::hardware_concurrency();
  printf("%d \\n",k);
  a = (int *)malloc(N*sizeof(int));
  int i=0;
  
  for(i=0;i<N;i++)
  {
    a[i] = i;
    //printf("%d ", a[i]);
  }
    
  int elem = a[8];
  
  #pragma omp parallel for
  for(i=0;i<k;i++)
  {
    int item = search(a,i*N/k, (i+1)*N/k - 1, elem);
    if(item!= -1)
      printf("Time %d lol %d \\n", item,elem);
  }
  
  return 0;
}

"""

file = open ("cuda.cu", "w")
file.write(code)
file.close()

!nvcc cuda.cu

!./a.out

!nvprof ./a.out

