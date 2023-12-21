#ifndef _DEBUG_H_
#define _DEBUG_H_

#define L_DEBUG 0
#define L_INFO 1
#define L_ERROR 2
// NOTE : debug_mode, if not, comment the next line
// #define _DEBUG
#define STR_L_DEBUG "[DEBUG]"
#define STR_L_INFO "[INFO]"
#define STR_L_ERROR "[ERROR]"

// NOTE : hilight the level you want to print
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
