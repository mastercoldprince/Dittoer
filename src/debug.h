#ifndef _DEBUG_H_
#define _DEBUG_H_

#define L_DEBUG 0
#define L_INFO 1
#define L_ERROR 2
<<<<<<< HEAD
// TODO : debug_mode
#define _DEBUG
=======
// NOTE : debug_mode, if not, comment the next line
// #define _DEBUG
>>>>>>> ac98fc56ab4768120c8dbe57b6b0b9d9732651c5
#define STR_L_DEBUG "[DEBUG]"
#define STR_L_INFO "[INFO]"
#define STR_L_ERROR "[ERROR]"

<<<<<<< HEAD
=======
// NOTE : hilight the level you want to print
>>>>>>> ac98fc56ab4768120c8dbe57b6b0b9d9732651c5
//#define VERBO L_INFO
#define VERBO L_DEBUG
#include <stdio.h>

#ifdef _DEBUG
#define printd(level, fmt, ...)                                         \
  do {                                                                  \
    if (level >= VERBO)                                                 \
      printf(STR_##level " %s:%d:%s():\t" fmt "\n", __FILE__, __LINE__, \
             __func__, ##__VA_ARGS__);                                  \
  } while (0)
#else
#define printd(level, fmt, ...)
#endif

#endif
