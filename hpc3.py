# -*- coding: utf-8 -*-
"""hpc3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n_b5EjviOIEFTOYhRdXAMIF9RRT5B0KT
"""

!nvcc --version

code = """
#include<iostream>
#include<stdlib.h>
#include<cuda.h>
#include<omp.h>
#define N 10
using namespace std;

void sort(int *a)
{
  for(int i=0;i<N;i++)
  {
    int first = i%2;
    
    #pragma omp parallel for default(none), shared(a,first)
    for(int j=first; j< N-1; j+=2)
    {
      if(a[j]>a[j+1])
        swap(a[j], a[j+1]);
    }
  }
}

int main()
{
  int *a;
  a = (int *)malloc(N*sizeof(int));
  int i=0;
  
  for(i=0;i<N;i++)
  {
    a[i] = rand()%10;
    printf("%d ", a[i]);
  }
    
  sort(a);
  printf("\\n");
  for(i=0;i<N;i++)
    printf("%d ", a[i]);
  
  return 0;
}

"""

code2="""
#include<iostream>
#include<stdlib.h>
#include<cuda.h>
#include<omp.h>
#define N 10
using namespace std;


void merge(int a[], int i1, int j1, int i2, int j2)
{
  int i=i1;
  int j=i2;
  int k=0;
  int temp[N];
  
  while(i<=j1 && j<=j2)
  {
    if(a[i] <a[j])
    {
      temp[k++] = a[i++];
    }
    else
    {
      temp[k++] = a[j++];
    }
  }
  
  while(i<=j1)
    temp[k++] = a[i++];
  
  while(j<=j2)
    temp[k++] = a[j++];
    
  for(i=i1,j=0;i<=j2;i++,j++)
    a[i] = temp[j];
}

void sort(int a[], int i, int j)
{
  int mid;
  if(i<j)
  {
    mid = (i+j)/2;
    #pragma omp parallel sections
    {
      #pragma omp section
      {
        sort(a,i,mid);
      }
      #pragma omp section
      {
        sort(a,mid+1,j);
      }
    }
    merge(a,i,mid,mid+1,j);
  }
}

int main()
{
  int *a;
  a = (int *)malloc(N*sizeof(int));
  int i=0;
  
  for(i=0;i<N;i++)
  {
    a[i] = rand()%10;
    printf("%d ", a[i]);
  }
    
  sort(a,0,N-1);
  printf("\\n");
  for(i=0;i<N;i++)
    printf("%d ", a[i]);
  
  return 0;
}

"""

file = open ("cuda.cu", "w")
file.write(code2)
file.close()

!nvcc cuda.cu

!./a.out

!nvprof ./a.out