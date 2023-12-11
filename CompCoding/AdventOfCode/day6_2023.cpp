#include <bits/stdc++.h>
using namespace std;

int main() {
    cout<<"HI"<<endl;
	ifstream file( "sample.txt" );
	string line;
	while(getline( file, line ) )   
    {
        istringstream iss( line );
        
        string result;
        if(getline( iss, result , ':') )
        {
            if( result == "Time" )
            {
                string token;
                while(getline( iss, token, ',' ) )
                {
                    cout << token << endl;
                }
            }
		}
	}
}
main();