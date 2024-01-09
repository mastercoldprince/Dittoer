import time
import json
import sys

from utils.utils import save_time
from utils.cmd_manager import CMDManager
from utils.settings import get_cache_config_cmd, get_make_cmd, get_freq_cache_cmd, get_mn_cpu_cmd

from cluster_setting import *

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <num clients> <workload>")

st = time.time()

work_dir = f'{EXP_HOME}/experiments/ycsb_test'

cmd_manager = CMDManager(cluster_ips)

# reset cluster
cmd_manager.execute_on_nodes([master_id], RESET_MASTER_CMD)
cmd_manager.execute_on_nodes(
    [i for i in range(len(cluster_ips)) if i != master_id], RESET_WORKER_CMD)

# set cache size configuration
CACHE_CONFIG_CMD = get_cache_config_cmd(config_dir, "ycsb", None)
print("setup cache"+CACHE_CONFIG_CMD)
cmd_manager.execute_all(CACHE_CONFIG_CMD)
# set freq_cache configuration
FC_CONFIG_CMD = get_freq_cache_cmd(config_dir, default_fc_size)
print("setup freq cache"+FC_CONFIG_CMD)
cmd_manager.execute_all(FC_CONFIG_CMD)
# set MN CPU
MN_CPU_CMD = get_mn_cpu_cmd(config_dir, 1)

cmd_manager.execute_all(MN_CPU_CMD)

# start experiment
method_list = ['sample-adaptive']
client_num = int(sys.argv[1])
workload = sys.argv[2]

MAKE_CMD = get_make_cmd(build_dir, 'sample-adaptive', 'ycsb', None)
print("make command"+MAKE_CMD)
cmd_manager.execute_all(MAKE_CMD)

print('finish make')
