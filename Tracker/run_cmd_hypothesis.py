python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_01 \
    --detection_file=output_generate/cam_01.npy \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_04 \
    --detection_file=output_generate/cam_04.npy \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True


python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_12 \
    --detection_file=output_generate/cam_12.npy \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True


python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_16 \
    --detection_file=output_generate/cam_16.npy \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
-------------------------
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_01 \
    --detection_file=output_generate/cam_01_v0.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
    
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_04 \
    --detection_file=output_generate/cam_04_v0.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam04_v0.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_12 \
    --detection_file=output_generate/cam_12_v0.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam12_V0.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_16 \
    --detection_file=output_generate/cam_16_v0.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam16_v0.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True

-------------------------------------
python Create_Video.py \
    -i="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_04/"
    
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_05/"\
    --output_path="Cam_05_v2.avi"

python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_15/"\
    --output_path="Cam_15_v2.avi"
---------------------------------29/8 6h-25---------------
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_08 \
    --detection_file=output_generate/cam_08.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_08_v2.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_20 \
    --detection_file=output_generate/cam_20.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_20_v2.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True


python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_22 \
    --detection_file=output_generate/cam_22.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_22_v2.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True


python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_25 \
    --detection_file=output_generate/cam_25.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_25_v2.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
---------------------------------------------------------
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_08/"\
    --output_path="Cam_08_v2.avi"

python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_20/"\
    --output_path="Cam_20_v2.avi"
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_22/"\
    --output_path="Cam_22_v2.avi"
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_25/"\
    --output_path="Cam_25_v2.avi"
--------------------------------------------3/9/2020--------------------------------
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_02 \
    --detection_file=output_generate/cam_02.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_02_v01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_06 \
    --detection_file=output_generate/cam_06.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_06_v01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_07 \
    --detection_file=output_generate/cam_07.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_07_v01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_09 \
    --detection_file=output_generate/cam_09.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_09_v01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_10 \
    --detection_file=output_generate/cam_10.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_10_v01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_14 \
    --detection_file=output_generate/cam_14_v1.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_14_v01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True


python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_18 \
    --detection_file=output_generate/cam_18.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_18_v01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_21 \
    --detection_file=output_generate/cam_21.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_21_v01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_23 \
    --detection_file=output_generate/cam_23.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_23_v01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_24 \
    --detection_file=output_generate/cam_24.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_24_v01.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
    
    
--------------------------------------------------------------------------------


python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_02/"\
    --output_path="Cam_02_v01.avi"
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_06/"\
    --output_path="Cam_06_v01.avi"
    
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_07/"\
    --output_path="Cam_07_v01.avi"


python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_09/"\
    --output_path="Cam_09_v01.avi"


python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_10/"\
    --output_path="Cam_10_v01.avi"
    
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_14/"\
    --output_path="Cam_14_v01.avi"



python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_18/"\
    --output_path="Cam_18_v01.avi"
    
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_21/"\
    --output_path="Cam_21_v01.avi"



python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_23/"\
    --output_path="Cam_23_v01.avi"
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_24/"\
    --output_path="Cam_24_v01.avi"
    

--------------------------------4/*/2020-----------------------

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_01 \
    --detection_file=output_generate/cam_01.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_01_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True



python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_02 \
    --detection_file=output_generate/cam_02.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_02_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_04 \
    --detection_file=output_generate/cam_04.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_04_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_06 \
    --detection_file=output_generate/cam_06.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_06_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
    



---------------------------------------
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_07 \
    --detection_file=output_generate/cam_07.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_07_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_09 \
    --detection_file=output_generate/cam_09.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_09_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_10 \
    --detection_file=output_generate/cam_10.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_10_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_12 \
    --detection_file=output_generate/cam_12.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_12_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    

------------------------------------------

python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_07/"\
    --output_path="Cam_07_v3.avi"

python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_09/"\
    --output_path="Cam_09_v3.avi"
    

python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_10/"\
    --output_path="Cam_10_v3.avi"
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_12/"\
    --output_path="Cam_12_v3.avi"
    
------------------------------------------------------------

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_03 \
    --detection_file=output_generate/cam_03.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_03_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True



python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_05 \
    --detection_file=output_generate/cam_05.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_05_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_14 \
    --detection_file=output_generate/cam_14.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_14_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_16 \
    --detection_file=output_generate/cam_16.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_16_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_18 \
    --detection_file=output_generate/cam_18.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_18_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True


python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_21 \
    --detection_file=output_generate/cam_21.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_21_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_23 \
    --detection_file=output_generate/cam_23.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_23_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_24 \
    --detection_file=output_generate/cam_24.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_24_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True


-----------------------------------------------------------

python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_03/"\
    --output_path="Cam_03_v3.avi"

python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_05/"\
    --output_path="Cam_05_v3.avi"
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_14/"\
    --output_path="Cam_14_v3.avi"
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_16/"\
    --output_path="Cam_16_v3.avi"
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_18/"\
    --output_path="Cam_18_v3.avi"
    
python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_21/"\
    --output_path="Cam_21_v3.avi"


python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_23/"\
    --output_path="Cam_23_v3.avi"


python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_24/"\
    --output_path="Cam_24_v3.avi"    

3,5,14,16,18,21,23,24

-----------------------------------
8 11 13 15


python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_08 \
    --detection_file=output_generate/cam_08.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_08_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True


python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_11 \
    --detection_file=output_generate/cam_11.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_11_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True


python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_13 \
    --detection_file=output_generate/cam_13.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_13_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_15 \
    --detection_file=output_generate/cam_15.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_15_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
-----------------------------------------------------------

python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_08/"\
    --output_path="Cam_08_v3.avi" 

python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_11/"\
    --output_path="Cam_11_v3.avi" 
    
  python Create_Video.py \
      --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_13/"\
      --output_path="Cam_13_v3.avi" 


python Create_Video.py \
    --input_path="/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/saved_frames/cam_15/"\
    --output_path="Cam_15_v3.avi" 
    
    
-----------------------------------------------------

python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_17 \
    --detection_file=output_generate/cam_17.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_17_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True


python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_19 \
    --detection_file=output_generate/cam_19.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_19_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_20 \
    --detection_file=output_generate/cam_20.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_20_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True
    
python deep_sort_app.py \
    --sequence_dir=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/data/cam_25 \
    --detection_file=output_generate/cam_25.npy \
    --output_file=/home/mmlab/working/Challenges/AI_HCM_2020/Counting_Vehicles/Task03/deep_sort/hypothesis/cam_25_v4.txt \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=True






