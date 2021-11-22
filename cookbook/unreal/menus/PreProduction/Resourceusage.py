# from cgl.plugins.unreal import alchemy as alc
from cgl.core.utils.general import save_json
import unreal
import time
import glob
import os


def handle_static_meshes(filepath):
    import re
    print("IN STATIC MESHES")
    latest_file = open(filepath, 'r')
    static_mesh_dict = {}
    line_ = latest_file.readline()
    space_regex = r'[\s,]+'
    while line_:
        # print("-----------------------------------------------")
        if "Obj List: class=StaticMesh -alphasort\n" == line_:
            print("FOUND LINE: {}".format(line_))
            skip_line = latest_file.readline()
            blank_line = latest_file.readline()
            cat_line = latest_file.readline()
            line_ = latest_file.readline()
            while line_ != "\n":
                split_array = re.split(space_regex, line_)
                mesh_name = split_array[2]
                num_kb = split_array[3]
                max_kb = split_array[4]
                res_exc_kb = split_array[5]
                res_exc_ded_sys_kb = split_array[6]
                res_exc_shr_sys_kb = split_array[7]
                res_exc_ded_vid_kb = split_array[8]
                res_exc_shr_vid_kb = split_array[9]
                res_exc_unk_kb = split_array[10]
                current_mesh_dict = {
                    "name": mesh_name,
                    "num kb": num_kb,
                    "max kb": max_kb,
                    "res exc kb": res_exc_kb,
                    "res exc ded sys kb": res_exc_ded_sys_kb,
                    "res exc shr sys kb": res_exc_shr_sys_kb,
                    "res exc ded vid kb": res_exc_ded_vid_kb,
                    "res exc shr vid kb": res_exc_shr_vid_kb,
                    "res exc unk kb": res_exc_unk_kb
                }
                static_mesh_dict[mesh_name] = current_mesh_dict
                line_ = latest_file.readline()
        line_ = latest_file.readline()
    latest_file.close()
    return static_mesh_dict

    #     if "Listing all textures" in line_:
    #         skip_line = latest_file.readline()
    #         line_ = latest_file.readline()
    #         while "Total size:" not in line_:
    #             max_allowed_size = re.search(one_regex, line_).group()
    #             current_in_mem = re.search(two_regex, line_).group()
    #             line_ = line_.replace(max_allowed_size, '').replace(current_in_mem, '').replace(', ,', '')
    #             split_array = line_.split(', ')
    #             texture_path = split_array[2]
    #             max_allowed_size = max_allowed_size
    #             current_in_mem = current_in_mem
    #             format_ = split_array[0]
    #             lod_group = split_array[1]
    #             streaming = split_array[3]
    #             usage_count = split_array[4]
    #             current_asset_dict = {
    #                 "MaxAllowedSize: Width x Height (Size in KB, Authored Bias)": max_allowed_size,
    #                 "Current/InMem: Width x Height (Size in KB)": current_in_mem,
    #                 "Format": format_,
    #                 "LODGroup": lod_group,
    #                 "Name": texture_path,
    #                 "Streaming": streaming,
    #                 "Usage Count": usage_count
    #             }
    #             texture_dict[texture_path] = current_asset_dict
    #             line_ = latest_file.readline()
    # return texture_dict


def handle_textures(filepath):
    import re
    texture_dict = {}
    print("OPENING: {}".format(filepath))
    latest_file = open(filepath, 'r')
    one_regex = r'\d{1,4}x\d{1,4} \(\d+ KB, \d+\)'
    two_regex = r'\d{1,4}x\d{1,4} \(\d+ KB\)'
    line_ = latest_file.readline()
    while line_:
        line_ = latest_file.readline()
        if "Listing all textures" in line_:
            skip_line = latest_file.readline()
            line_ = latest_file.readline()
            while "Total size:" not in line_:
                max_allowed_size = re.search(one_regex, line_).group()
                current_in_mem = re.search(two_regex, line_).group()
                line_ = line_.replace(max_allowed_size, '').replace(current_in_mem, '').replace(', ,', '')
                split_array = line_.split(', ')
                texture_path = split_array[2]
                max_allowed_size = max_allowed_size
                current_in_mem = current_in_mem
                format_ = split_array[0]
                lod_group = split_array[1]
                streaming = split_array[3]
                usage_count = split_array[4]
                current_asset_dict = {
                    "MaxAllowedSize: Width x Height (Size in KB, Authored Bias)": max_allowed_size,
                    "Current/InMem: Width x Height (Size in KB)": current_in_mem,
                    "Format": format_,
                    "LODGroup": lod_group,
                    "Name": texture_path,
                    "Streaming": streaming,
                    "Usage Count": usage_count
                }
                texture_dict[texture_path] = current_asset_dict
                line_ = latest_file.readline()
    latest_file.close()
    return texture_dict


def read_file(filepath):
    main_dict = {}
    texture_dict = handle_textures(filepath)
    main_dict['textures'] = texture_dict
    static_dict = handle_static_meshes(filepath)
    main_dict['static meshes'] = static_dict
    save_json("C:\\Users\\VP01\\Desktop\\Kyles fyles\\TestFOlder\\text_dict.json", main_dict)


def get_file(deltaTime):
    startTime = time.strftime("%H.%M.%S", time.localtime())
    mem_report_dir = os.path.join(saved_full_path, "Profiling", "Memreports", "*", "*")
    list_of_files = glob.glob(mem_report_dir)
    if len(list_of_files) > num_files:
        file_ = max(list_of_files, key=os.path.getctime)
        unreal.unregister_slate_pre_tick_callback(tick_updated)
        read_file(file_)


def run():
    current_world = unreal.EditorLevelLibrary().get_editor_world()
    unreal.SystemLibrary().execute_console_command(current_world, "memreport -full")


if __name__ == "__main__":
    run()

saved_full_path = unreal.SystemLibrary.convert_to_absolute_path(unreal.Paths().project_saved_dir())
mem_report_main_dir = os.path.join(saved_full_path, "Profiling", "Memreports")
num_files = 0
if not os.path.exists(mem_report_main_dir):
    num_files = 0
else:
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

