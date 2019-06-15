
import os
import zipfile
import shutil
import json


lqm_file_dir = os.path.join(os.path.dirname(__file__), "quickmemo_lqm_files")
unzipped_file_dir = os.path.join(lqm_file_dir, "unzipped")
output_file_dir = os.path.join(os.path.dirname(__file__), "quickmemo_output")



def extract_files():
    try:
        if os.path.exists(unzipped_file_dir):
            shutil.rmtree(unzipped_file_dir, onerror=onremoveerror)
    except:
        pass
        
    memo_folders = []
    for lqm_file_name in os.listdir(lqm_file_dir):
        lqm_path = os.path.join(lqm_file_dir, lqm_file_name)
        output_path = os.path.join(unzipped_file_dir, lqm_file_name)
        
        try:
            zip_ref = zipfile.ZipFile(lqm_path, 'r')
            zip_ref.extractall(output_path)
            zip_ref.close()
        except:
            pass
            
        memo_folders.append(output_path)
        
    return memo_folders


def main():

    memo_folders = extract_files()

    if not os.path.exists(output_file_dir):
        os.makedirs(output_file_dir)
        
    output_paths = []
    for folder in memo_folders:
        memo_name = os.path.basename(folder)
        
        # Copy images and such straight up
        for resource in ["audios", "drawings", "images", "videos"]:
            memo_resource = os.path.join(folder, resource)
            if os.path.exists(memo_resource):
            
                for resource_name in os.listdir(memo_resource):
                    resource_path = os.path.join(memo_resource, resource_name)
                    output_resource_path = os.path.join(output_file_dir, resource_name)
                    
                    shutil.copy(resource_path, output_resource_path)
                    
        
        # find source data
        memoinfo_path = os.path.join(folder, "memoinfo.jlqm")
        if not os.path.exists(memoinfo_path):
            continue
        
        print(f"input - {memoinfo_path}")
        
        text_data = []
        with open(memoinfo_path, "r") as fp:
            memoinfo = json.load(fp)
        
        # go through each item in the memo
        for memo_obj in memoinfo.get("MemoObjectList"):
            raw_text = memo_obj.get("DescRaw")
            if not raw_text:
                raw_text = "IMAGE"
            
            complete_item = memo_obj.get("IsChecked")
            if complete_item:
                raw_text = "CHECKED - " + raw_text
                
            if not raw_text.endswith("\n"):
                raw_text = raw_text + "\n"
            
            text_data.append(raw_text)
        
        output_txt_path = os.path.join(output_file_dir, memo_name.replace(".lqm", ".txt"))
        with open(output_txt_path, "w") as fp:
            fp.writelines(text_data)
        
        output_paths.append(output_txt_path)

    for output_txt_path in output_paths:
        print(f"output - {output_txt_path}")


if __name__ == "__main__":
    main()



