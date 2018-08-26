/*
* @Author: John Hammond
* @Date:   2016-10-20 08:38:34
* @Last Modified by:   John Hammond
* @Last Modified time: 2016-10-20 14:40:04
*/

#include <iostream>
#include <time.h>
#include <string.h>
#include "sha1.h"
#define SIZE_OF_BUFFER 8

using namespace std;

int main( int argc, char *argv[] ){

	time_t raw_time;
	struct tm * timeinfo;
	char buffer[SIZE_OF_BUFFER];

	time( &raw_time );
	timeinfo = localtime(&raw_time);

	// This gets the current minute as a string... (like 02:34PM)
	strftime(buffer, SIZE_OF_BUFFER, "%I:%M%p", timeinfo );

	// This adds on to the filename the current minute...
	strcat(argv[0], buffer);

	cout << sha1(argv[0]) << endl;

    return 0;
}
