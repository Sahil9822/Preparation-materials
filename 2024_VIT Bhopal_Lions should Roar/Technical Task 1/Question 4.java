/*Problem statement:
A private bank has a problem with its credit card processing system. As a result, the majority of customers have contacted the bank about the payment problem. Now the bank has to check whether the credit number is valid or not before proceeding with the further clearance process. Write a program to obtain a credit card number and check its validity. Card numbers should start with 4 for Visa cards, 5 for Master cards, 37 for American Express cards, and 6 for Discover cards.

Conditions for a card to be valid:
Consider the card number: 4388576018402626

Step 1: Double every second digit from right to left. If doubling of a digit results in a two-digit number, add up the two digits to get a single-digit number (like for 12: 1 + 2, 18: 1 + 8).

Step 2: Add all of the single-digit numbers from Step 1. (4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37)

Step 3: Add all the digits in the odd places from right to left in the card number. (6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38)

Step 4: Sum the results from Steps 2 and 3. (37 + 38 = 75)

Step 5: If the result from Step 4 is divisible by 10, the card number is valid; otherwise, it is invalid. 

Input format
The input consists of the credit card number.

Output format
The output prints whether the number is valid or not.

Sample testcases
Input 1
379354508162306

Output 1
379354508162306 is valid

Input 2
4388576018402626

Output 2
4388576018402626 is invalid

Code:-*/
/*Solution*/
import java.util.Scanner; 

class Main { 
	public static void main(String[] args) 
	{ 
	    Scanner input = new Scanner(System.in);
	    long number = input.nextLong();
		//long number = 4388576018402626L; 

		System.out.println(number + " is " + 
		(isValid(number) ? "valid" : "invalid")); 
	} 
	public static boolean isValid(long number) 
	{ 
	return (getSize(number) >= 13 && 
			getSize(number) <= 16) && 
			(prefixMatched(number, 4) || 
				prefixMatched(number, 5) || 
				prefixMatched(number, 37) || 
				prefixMatched(number, 6)) && 
			((sumOfDoubleEvenPlace(number) + 
				sumOfOddPlace(number)) % 10 == 0); 
	} 
	public static int sumOfDoubleEvenPlace(long number) 
	{ 
		int sum = 0; 
		String num = number + ""; 
		for (int i = getSize(number) - 2; i >= 0; i -= 2) 
			sum += getDigit(Integer.parseInt(num.charAt(i) + "") * 2); 
		
		return sum; 
	} 
	public static int getDigit(int number) 
	{ 
		if (number < 9) 
			return number; 
		return number / 10 + number % 10; 
	} 
	public static int sumOfOddPlace(long number) 
	{ 
		int sum = 0; 
		String num = number + ""; 
		for (int i = getSize(number) - 1; i >= 0; i -= 2) 
			sum += Integer.parseInt(num.charAt(i) + "");		 
		return sum; 
	} 
	public static boolean prefixMatched(long number, int d) 
	{ 
		return getPrefix(number, getSize(d)) == d; 
	} 
	public static int getSize(long d) 
	{ 
		String num = d + ""; 
		return num.length(); 
	} 
	public static long getPrefix(long number, int k) 
	{ 
		if (getSize(number) > k) { 
			String num = number + ""; 
			return Long.parseLong(num.substring(0, k)); 
		} 
		return number; 
	} 
} 

