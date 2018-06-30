#include <iostream>
  
using namespace std;
  
void checkDenominations(int);
void successWithdrawl(int, int, int);
int main( ) {

	int val;
   	cout << "Enter your amount to check: ";
   	cin >> val;
   	checkDenominations(val);  
   	return 0;
}

void checkDenominations(int amt){      				//function to divide the amount in terms of 20s & 50s

	int withdrawl = amt;
	int twentyNotes=0;
	int fiftyNotes=0;


	if(amt%50==0){						//check if only 50s possible
		while(amt>=50){
			fiftyNotes+=1;
			amt-=50;
		}
	}

	if(amt%20==0){						//check if 20s possible and minimize the 20s number by replacing with 50s

		while((amt>=20) && ((amt)%50!=0)){
			twentyNotes+=1;
			amt-=20;
		}

		while(amt>=50){
			fiftyNotes+=1;
			amt-=50;
		}
	}


	else{
		while(amt>=50){					//dividing in max 50s and min 20s
			while((amt>=50) && (amt%20!=0)){
				fiftyNotes+=1;
				amt-=50;
			}
		
			if((amt%50==0) && (amt%20==0)){
				int quo = amt/50;
				fiftyNotes += quo;
				amt%=50;
			}

			while((amt>=50) && (amt%20==0) && (amt%50!=0)){
				twentyNotes+=1;
				amt-=20;
			}
		}

		if(amt%20==0){
			while(amt>=20){
				twentyNotes+=1;
				amt-=20;
			}
		}
	}
	successWithdrawl(fiftyNotes, twentyNotes, withdrawl);
}

void successWithdrawl(int fiftyNote, int twentyNote, int withdrawl){
	bool successfulWithdrawl;
	if((fiftyNote*50 + twentyNote*20)==withdrawl){					//check if any remainder got left out
		cout << "50s x " << fiftyNote << " and 20s x " << twentyNote << "\n";
      	        successfulWithdrawl = true;	
	}

	else{
		cout << "Withdrawl not possible\n";
	        successfulWithdrawl = false;	
	}
}
