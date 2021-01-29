#include "ZMQConnect.h"
#include <zmq.h>

const char* ZMQConnect::version()
{
    int m,n,k;
    zmq_version(&m, &n, &k);
    
    static char result[2048];
    sprintf(result, "version %d.%d.%d", m, n, k);
    
    return result;
}

#ifdef __cplusplus
extern "C" {
#endif

const char* zmqConnectVersion()
{
    ZMQConnect z;
    return z.version();
}

#ifdef __cplusplus
}
#endif
