import os
import nibabel as nib

from comp2comp.inference_class_base import InferenceClass


class ToCanonical(InferenceClass):
    """Convert spine segmentation to canonical orientation."""

    def __init__(self):
        super().__init__()

    def __call__(self, inference_pipeline):
        """
        First dim goes from L to R.
        Second dim goes from P to A.
        Third dim goes from I to S.
        """
        output_dir_segmentations = os.path.join(inference_pipeline.output_dir, "segmentations/")

        nib.save(
            inference_pipeline.segmentation,
            os.path.join(output_dir_segmentations, "original_spine_seg.nii.gz"),
        )

        nib.save(
            inference_pipeline.medical_volume,
            os.path.join(output_dir_segmentations, "original_converted_dcm.nii.gz"),
        )

        canonical_segmentation = nib.as_closest_canonical(inference_pipeline.segmentation)
        canonical_medical_volume = nib.as_closest_canonical(inference_pipeline.medical_volume)

        nib.save(
            canonical_segmentation,
            os.path.join(output_dir_segmentations, "canonical_spine_seg.nii.gz"),
        )

        nib.save(
            canonical_medical_volume,
            os.path.join(output_dir_segmentations, "canonical_converted_dcm.nii.gz"),
        )

        print(
            f"[INFO] medical volume: {nib.aff2axcodes(inference_pipeline.medical_volume.affine)} -> canonical: {nib.aff2axcodes(canonical_medical_volume.affine)}")
        print(
            f"[INFO] Segmentation: {nib.aff2axcodes(inference_pipeline.segmentation.affine)} -> canonical: {nib.aff2axcodes(canonical_segmentation.affine)}")
        # Make sure to replace the input
        inference_pipeline.segmentation = canonical_segmentation
        inference_pipeline.medical_volume = canonical_medical_volume

        inference_pipeline.pixel_spacing_list = (canonical_medical_volume.header.get_zooms())
        return {}
