# from cgl.plugins.unreal import alchemy as alc
import unreal
import time
import glob
import os


def read_file(filepath):
    print("OPENING: {}".format(filepath))
    latest_file = open(filepath, 'r')
    line_ = latest_file.readline()
    text_array = []
    texture_dict = {}
    text_regex = ", \w{2}|, \/"
    while line_:
        # print("Line: {}".format(line_))
        line_ = latest_file.readline()
        if "Listing all textures" in line_:
            skip_line = latest_file.readline()
            line_ = latest_file.readline()
            while "Total size:" not in line_:
                split_array = line_.split(text_regex)
                # print("ARRAY: {}      NUM: {}".format(split_array, len(split_array)))
                # texture_path = split_array[4]
                # max_allowed_size = split_array[0]
                # current_in_mem = split_array[1]
                # format = split_array[2]
                # lod_group = split_array[3]
                # streaming = split_array[5]
                # usage_count = split_array[6]
                # current_asset_dict = {
                #     "MaxAllowedSize: Width x Height (Size in KB, Authored Bias)" : max_allowed_size,
                #     "Current/InMem: Width x Height (Size in KB)": current_in_mem,
                #     "Format": format,
                #     "LODGroup": lod_group,
                #     "Name": texture_path,
                #     "Streaming" : streaming,
                #     "Usage Count": usage_count
                # }
                # texture_dict[texture_path] = current_asset_dict
                # line_ = latest_file.readline()
    # print(texture_dict)


def get_file(deltaTime):
    startTime = time.strftime("%H.%M.%S", time.localtime())
    mem_report_dir = os.path.join(saved_full_path, "Profiling", "Memreports", "*", "*")
    list_of_files = glob.glob(mem_report_dir)
    if len(list_of_files) > num_files:
        file_ = max(list_of_files, key=os.path.getctime)
        unreal.unregister_slate_pre_tick_callback(tick_updated)
        print("READING FILE")
        read_file(file_)


def run():
    current_world = unreal.EditorLevelLibrary().get_editor_world()
    print("EXECUTING MEMREPORT")
    unreal.SystemLibrary().execute_console_command(current_world, "memreport -full")


saved_full_path = unreal.SystemLibrary.convert_to_absolute_path(unreal.Paths().project_saved_dir())
mem_report_main_dir = os.path.join(saved_full_path, "Profiling", "Memreports")
num_files = 0
for file in os.listdir(mem_report_main_dir):
    num_files += 1
tick_updated = unreal.register_slate_pre_tick_callback(get_file)
    #
    # mem_report = latest_file.readlines()
    #
    # line = latest_file.readline()
    # print("Line: {}".format(line))
    #
    # while line:
    #     line = latest_file.readline()
    #     if line == "Listing all textures":
    #         skip_line = latest_file.readline()
    #         print(skip_line)
    #
    #

    #
    # # Store the information within mem_report variable.
    # mem_report = latest_file.readlines()
    # latest_file.close()
    #
    # # Get the path to the most recent log. This will not be used until later,
    # # when it will be read to get the details about each object of a class
    # # retrieved from the MemReport.
    # # Isolate project name (the most recent log always has the same name as the project).
    # name = unreal.Paths().project_saved_dir()
    # nameList = name.rsplit('/', 3)
    # name = nameList[1]
    # nameList = name.rsplit(' ', 1)
    # name = nameList[0]
    # # Construct path.
    # log_dir = unreal.Paths().project_saved_dir() + r'Logs/' + name + '.log'
    # latest_file = open(log_dir, 'r')
    #
    # # Start and stop variables used to analyze only the class data in the MemReport.
    # header = "Class    Count      NumKB      MaxKB   ResExcKB  ResExcDedSysKB  " \
    #          "ResExcShrSysKB  ResExcDedVidKB  ResExcShrVidKB     ResExcUnkKB"
    # start = False
    # stop = False
    # Classes = {}
    #
    # for line in mem_report:
    #     temp = line.strip()
    #     if stop is True:
    #         if temp == "":
    #             break
    #     if start is False:
    #         if header in temp:
    #             start = True
    #             stop = True
    #         else:
    #             continue
    #     c = temp.split()
    #     Objects = {}

