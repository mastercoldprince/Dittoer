#ifndef _DEBUG_H_
#define _DEBUG_H_

#include <stdio.h>
#include <time.h>
#define L_DEBUG 0
#define L_INFO 1
#define L_ERROR 2
// NOTE : debug_mode, if not, comment the next line
#define _DEBUG
#define STR_L_DEBUG "[DEBUG]"
#define STR_L_INFO "[INFO]"
#define STR_L_ERROR "[ERROR]"

// NOTE : hilight the level you want to print
// #define VERBO L_INFO
#define VERBO L_DEBUG
// #define VERBO L_ERROR
#include <stdio.h>

#ifdef _DEBUG
static FILE *debug_file = NULL;


#define printd(level, fmt, ...)                                      \
  do {                                                               \
    if (level >= VERBO) {                                            \
        if (debug_file == NULL) { \
    char file_name[100];            \
    time_t now = time(NULL);        \
    struct tm *tm_now = localtime(&now);\
    snprintf(file_name, sizeof(file_name),\
             "~/Ditto/log_%04d-%02d-%02d.txt",\
             tm_now->tm_year + 1900, tm_now->tm_mon + 1,\
             tm_now->tm_mday);\
    debug_file = fopen(file_name, "a");\
  }\
      if (debug_file) {                                              \
        time_t now = time(NULL);                                     \
        char time_buff[20];                                          \
        strftime(time_buff, sizeof(time_buff), "%Y-%m-%d %H:%M:%S", localtime(&now)); \
        fprintf(debug_file, "%s " STR_##level " %s:%d:%s():\t" fmt "\n", \
                time_buff, __FILE__, __LINE__, __func__, ##__VA_ARGS__); \
        fflush(debug_file);                                          \
      }                                                              \
      printf(STR_##level " %s:%d:%s():\t" fmt "\n",                  \
             __FILE__, __LINE__, __func__, ##__VA_ARGS__);           \
    }                                                                \
  } while (0)
#else
#define printd(level, fmt, ...)
#endif

#endif

