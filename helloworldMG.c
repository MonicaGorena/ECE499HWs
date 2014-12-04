/*Hello world*/
/* Standard Stuff */
#include <string.h>
#include <stdio.h>

/* Required Hubo Headers */
#include <hubo.h>

/* For Ach IPC */
#include <errno.h>
#include <fcntl.h>
#include <assert.h>
#include <unistd.h>
#include <pthread.h>
#include <ctype.h>
#include <stdbool.h>
#include <math.h>
#include <inttypes.h>
#include "ach.h"

//declaring int for do while loop
int x=1;
/* Ach Channel IDs */
ach_channel_t chan_hubo_ref;      // Feed-Forward (Reference)
ach_channel_t chan_hubo_state;    // Feed-Back (State)
int main(int argc, char **argv) {

/* Open Ach Channel */
int r = ach_open(&chan_hubo_ref, HUBO_CHAN_REF_NAME , NULL);
assert( ACH_OK == r );

r = ach_open(&chan_hubo_state, HUBO_CHAN_STATE_NAME , NULL);
assert( ACH_OK == r );
/* Create initial structures to read and write from */
struct hubo_ref H_ref;
struct hubo_state H_state;
memset( &H_ref,   0, sizeof(H_ref));
memset( &H_state, 0, sizeof(H_state));

/* for size check */
size_t fs;

/* Get the current feed-forward (state) */
r = ach_get( &chan_hubo_state, &H_state, sizeof(H_state), &fs, NULL, ACH_O_LAST );
    if(ACH_OK != r) {
        assert( sizeof(H_state) == fs );
    }
do{
if (x==1){ 

    /* Set Left Elbow Bend (LEB) and Right Shoulder Pitch (RSP) to  -0.2 rad and 0.1 rad respectively*/
    H_ref.ref[LSR] = 1.2;
    H_ref.ref[LSY] = 1.4;
    H_ref.ref[LEB] = -.2; 
    //changing interger value
    x=2;
    /* Write to the feed-forward channel */
    ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));
    /* Print out the actual position of the LEB */
    //double posLEB = H_state.joint[LEB].pos;
    //printf("Joint = %f\r\n",posLEB);
    //printf("x = %d\n",x);
    usleep(500000);
}
else if (x==2){
    H_ref.ref[LSR] = 1.2;
    H_ref.ref[LSY] = 1.4;
    H_ref.ref[LEB] = -3;
    // changing interger value back
    x=1;
    /* Write to the feed-forward channel */
    ach_put( &chan_hubo_ref, &H_ref, sizeof(H_ref));
    /* Print out the actual position of the LEB */
    //double posLEB = H_state.joint[LEB].pos;
    //printf("Joint = %f\r\n",posLEB);
    usleep(500000);
    //printf("x = %d\n",x);
}
}while (x==1||x==2);//do-while loop x value will change from 1 to 2 endlessly 
}
