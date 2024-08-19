import os
from pathlib import Path

from deep_utils import DirUtils

directory_path = "/home/aicvi/projects/Data_TAVI_TB2"
analysis_type = "spine_muscle_adipose_tissue"
if __name__ == '__main__':
    for patient_dir in DirUtils.list_dir_full_path(directory_path, only_directories=True):
        for image_path in DirUtils.list_dir_full_path(patient_dir, interest_extensions=".gz"):
            print(f"[INFO] Working on {image_path}")
            output_path = Path(image_path.replace(".nii.gz", "")) / "comp2comp" / analysis_type
            output_path.mkdir(exist_ok=True, parents=True)
            os.system(
                f"{os.path.split(__file__)[0]}/C2C {analysis_type} --input_path {image_path} --input_type nifti --save_segmentations --output {output_path} --overwrite_outputs")
