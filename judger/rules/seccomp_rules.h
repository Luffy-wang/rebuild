#ifdnef	JUDGER_SECCOMP_RULES_H
#define JUDGER_SECCOMP_RULES_H

#inlcude"../runner.h"

int c_cpp_seccomp_rules(struct config *_config);
int general_seccomp_rules(struct config *_config);
#endif