# -*- coding: utf-8 -*-
"""hpc2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12580DUYy9tEteAgtVIxmuf0BpuuIlIz_
"""

!nvcc --version

code1 = """
#include<iostream>
#include<stdlib.h>
#include<cuda.h>
using namespace std;

__global__ void add (int *a, int *b, int *c, int n)
{
    int i=threadIdx.x;
    if(i<n)
      c[i]=a[i]+b[i];
}

int main()
{
    int *a, *b, *c;
    int *da, *db, *dc;
    int n =10;
    int size = n * sizeof(int);
    
    a = (int*) malloc(size);
    b = (int*) malloc(size);
    c = (int*) malloc(size);
    
    cudaMalloc(&da, size);
    cudaMalloc(&db, size);
    cudaMalloc(&dc, size);
    
    int i=0;
    for(i=0;i<n;i++)
    {
      a[i] = rand()%10;
      b[i] = rand()%10;
      c[i] = 0;
    }
    
    cudaMemcpy(da,a,size, cudaMemcpyHostToDevice);
    cudaMemcpy(db,b,size, cudaMemcpyHostToDevice);
    cudaMemcpy(dc,c,size, cudaMemcpyHostToDevice);
    
    add<<<1, n>>>(da,db,dc,n);
    
    //cudaDeviceSynchronized();
    cudaMemcpy(c,dc,size, cudaMemcpyDeviceToHost);
    
    for(i=0;i<n;i++)
      printf("\\nc[%d] = %d",i,c[i]);
    
    cudaFree(da);
    cudaFree(db);
    cudaFree(dc);
    
    return 0;
    
}
"""

code2 = """
#include<iostream>
#include<cuda.h>
#include<stdlib.h>
using namespace std;
#define N 4

__global__ void vec_mat(int *a, int *b, int *c)
{
  int k=0, prod=0;
  int row = blockDim.x * blockIdx.x + threadIdx.x;
  int col = blockDim.y * blockIdx.y + threadIdx.y;
  
  if(row<N && col<N)
  {
    prod = 0;
    for(k=0;k<N;k++)
    {
      prod += a[row*N+k] * b[k*N+col]; 
    }
    c[row*N+col]=prod;
  }
}

int main()
{
  int a[N],b[N][N],c[N];
  int size = N*sizeof(int);
  //a = (int *)malloc(N * sizeof(int));
  //b = (int *)malloc((N * N) * sizeof(int));
  //c = (int *)malloc(N * sizeof(int));
  
  int *da,*db,*dc;
  cudaMalloc(&da, N*sizeof(int));
  cudaMalloc(&db, (N*N)*sizeof(int));
  cudaMalloc(&dc, N*sizeof(int));
  
  int i=0,j=0;
  for(i =0;i<N;i++)
  {
    a[i] = rand()%10;
    for(j=0;j<N;j++)
    {
      b[i][j] = rand()%10;
    }
  }
  
  printf("Vector \\n");
  for(i=0;i<N;i++)
    printf("%d  ",a[i]);
    
  for(i=0;i<N;i++)
  {
    for(j=0;j<N;j++)
      printf("%d  ",b[i][j]);
      
    printf("\\n");
  }
  
  cudaMemcpy(da,a,size,cudaMemcpyHostToDevice);
  cudaMemcpy(db,b,(N * N) * sizeof(int), cudaMemcpyHostToDevice);
  cudaMemcpy(dc,c,size, cudaMemcpyHostToDevice);
  
  dim3 dimBlock(16,16);
  dim3 dimGrid((int) ceil(256/16), (int)ceil(256/16));
  
  vec_mat<<<dimGrid, dimBlock>>>(da,db,dc);
  
  cudaMemcpy(c,dc,size, cudaMemcpyDeviceToHost);
  
  for(i=0;i<N;i++) 
    printf("%d  ", c[i]);
  
  cudaFree(da);
  cudaFree(db);
  cudaFree(dc);
  
  return 0;
}
"""

code3="""
#include<iostream>
#include<cuda.h>
#include<stdlib.h>
using namespace std;
#define N 4

__global__ void mat_mul(int *a, int *b, int *c)
{
  int row = blockDim.x * blockIdx.x + threadIdx.x;
  int col = blockDim.y * blockIdx.y + threadIdx.y;
  int k=0,prod=0;
  
  if(row<N && col<N)
  {
    prod=0;
    for(k=0;k<N;k++)
    {
      prod += a[row*N+k]*b[k*N+col];
    }
    c[row*N+col] = prod;
  }
}

int main()
{
  int a[N][N], b[N][N], c[N][N];
  int *da, *db, *dc;
  int size= (N*N)*sizeof(int);
  int i=0,j=0;
  for(i=0;i<N;i++)
  {
    for(j=0;j<N;j++)
    {
      a[i][j]=rand()%10;
      b[i][j]=rand()%20;
    }
  }
  
  cudaMalloc(&da, size);
  cudaMalloc(&db, size);
  cudaMalloc(&dc, size);
  
  cudaMemcpy(da,a,size,cudaMemcpyHostToDevice);
  cudaMemcpy(db,b,size,cudaMemcpyHostToDevice);
  
  dim3 dimBlock(16,16);
  dim3 dimGrid((int) ceil(256/16), (int) ceil(256/16));
  
  mat_mul<<<dimGrid, dimBlock>>>(da,db,dc);
  
  cudaMemcpy(c,dc,size, cudaMemcpyDeviceToHost);
  
  for(i=0;i<N;i++)
  {
    for(j=0;j<N;j++)
    {
      printf("%d  ",c[i][j]);
    }
    printf("\\n");
  }
  
  return 0;
}
"""

file = open ("cuda.cu", "w")
file.write(code3) #replace by code1/2/3
file.close()

!nvcc cuda.cu

!./a.out

!nvprof ./a.out