/* Standard Stuff */
#include <string.h>
#include <stdio.h>

/* Required Headers */
#include "controller.h"

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
#include <ach.h>





/* Ach Channel IDs */
ach_channel_t chan_controller_ref;      // Feed-Forward (Reference)

int main(int argc, char **argv) {

    /* Open Ach Channel */
    int r = ach_open(&chan_controller_ref, CONTROLLER_REF_NAME , NULL);
    assert( ACH_OK == r );


    /* Create initial structures to read and write from */
    struct controller_ref c_ref;
    memset( &c_ref, 0, sizeof(c_ref));

    /* for size check */
    size_t fs;

    /* Get the current feed-forward (state) */
    r = ach_get( &chan_controller_ref, &c_ref, sizeof(c_ref), &fs, NULL, ACH_O_LAST );
    if(ACH_OK != r) {
        assert( sizeof(c_ref) == fs );
    }

    c_ref.mot1 = 0.5;
    c_ref.mot2 = -0.5;



    usleep(100000);



    ach_put( &chan_controller_ref, &c_ref, sizeof(c_ref));
}
