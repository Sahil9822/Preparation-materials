/*Problem statement:
A chocolate factory is packing chocolates into packets. The chocolate packets here represent an array arr[] of N number of integer values. The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).

For example:
N = 7 and arr = [4, 5, 0, 1, 9, 0, 5, 0]
There are 3 empty packets in the given set. These 3 empty packets represented as 0 should be pushed toward the end of the array.

Example 1
Input
7
4 5 0 1 9 0 5

Output
4 5 1 9 5 0 0 

Example 2
Input
6
6 0 1 8 0 2

Output
6 1 8 2 0 0

Input format
The first line of input contains an integer n denoting the size of an array
The next space-separated integers denote the elements of an array

Output format
The output prints an integer array separated by space.

Sample testcases
Input 1
7
4 5 0 1 9 0 5
  
Output 1
4 5 1 9 5 0 0 

Input 2
6
6 0 1 8 0 2
  
Output 2
6 1 8 2 0 0

Code:-*/
/*Solution:-*/
#include<iostream>
using namespace std;
void pushZeroToEnd(int arr[], int n)
{
    int count = {0};
    for (int i = 0; i < n; i++)
    if (arr[i] != 0)
    arr[count++] = arr[i];
    while(count < n)
    arr[count++] = 0;
}

int main()
{
    int n;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++)
    cin >> arr[i];
    pushZeroToEnd(arr, n);
    for (int i = 0; i < n; i++)
    cout << arr[i] << " ";
    return 0;
}
