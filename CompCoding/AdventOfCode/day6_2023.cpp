#include <bits/stdc++.h>
using namespace std;

int main() {
	ifstream file( "sample.txt" );
	string line;
	while(getline( file, line ) )   
    {
        istringstream iss( line );
        cout<<"HI"<<endl;
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