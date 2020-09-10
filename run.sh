# Preprocess
################################################################
# Clean all directories contain DATA                           #
                                                               #
echo "Removing all directories and ..."                        #
                                                               #
rm -rf DATA/image/*										       #
															   #
# Loop through all videos and extract to images				   #
for video in /data/test_data/*.mp4; 							   #
do  														   #
															   #
	# Get the camera name									   #
	name="$(cut -d'/' -f4 <<<"$video")";                       #
	name="$(cut -d'.' -f1 <<<"$name")";                        #
	 														   #
	# Create output directory store extracted images	       #
	output="DATA/image/$name"								   #
	mkdir $output			                                   #
	                                                           #
	img1="$output/img1"								           #
	mkdir $img1                                                #
                                                               #
	det="$output/det"                                          #
	mkdir $det                                                 #		
	          												   #
	echo "Extracting $name to images ..." ;					   #
															   #
	ffmpeg -i $video -r 10/1 $img1/image_%d.jpg			       #
															   #
done;														   #
															   #
															   #
################################################################

# Detection progress
############################################################################################################################################################################################################################
# echo "Detecting vehicle in cam 01 ..."
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_01/img1 --output_path DATA/detection_result/cam_01_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_01_det.txt DATA/image/cam_01/det/det.txt

# print("Detecting vehicle in cam 02 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_02/img1 --output_path DATA/detection_result/cam_02_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_02_det.txt DATA/image/cam_02/det/det.txt

# print("Detecting vehicle in cam 04 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_04/img1 --output_path DATA/detection_result/cam_04_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_04_det.txt DATA/image/cam_04/det/det.txt

# print("Detecting vehicle in cam 06 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_06/img1 --output_path DATA/detection_result/cam_06_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_06_det.txt DATA/image/cam_06/det/det.txt

# print("Detecting vehicle in cam 07 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_07/img1 --output_path DATA/detection_result/cam_07_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_07_det.txt DATA/image/cam_07/det/det.txt

# print("Detecting vehicle in cam 09 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_09/img1 --output_path DATA/detection_result/cam_09_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_09_det.txt DATA/image/cam_09/det/det.txt

# print("Detecting vehicle in cam 10 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_10/img1 --output_path DATA/detection_result/cam_10_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_10_det.txt DATA/image/cam_10/det/det.txt

# print("Detecting vehicle in cam 12 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_12/img1 --output_path DATA/detection_result/cam_12_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_12_det.txt DATA/image/cam_12/det/det.txt

# print("Detecting vehicle in cam 14 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_14/img1 --output_path DATA/detection_result/cam_14_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_14_det.txt DATA/image/cam_14/det/det.txt

# print("Detecting vehicle in cam 16 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_16/img1 --output_path DATA/detection_result/cam_16_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_16_det.txt DATA/image/cam_16/det/det.txt

# print("Detecting vehicle in cam 18 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_18/img1 --output_path DATA/detection_result/cam_18_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_18_det.txt DATA/image/cam_18/det/det.txt

# print("Detecting vehicle in cam 21 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_21/img1 --output_path DATA/detection_result/cam_21_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_21_det.txt DATA/image/cam_21/det/det.txt

# print("Detecting vehicle in cam 23 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_23/img1 --output_path DATA/detection_result/cam_23_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_23_det.txt DATA/image/cam_23/det/det.txt

# print("Detecting vehicle in cam 24 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_24/img1 --output_path DATA/detection_result/cam_24_det.txt --model_path model_weights/Detect/Bright/output/model_final.pth
cp DATA/detection_result/cam_24_det.txt DATA/image/cam_24/det/det.txt


# print("Detecting vehicle in cam 03 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_03/img1 --output_path DATA/detection_result/cam_03_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
cp DATA/detection_result/cam_03_det.txt DATA/image/cam_03/det/det.txt

# print("Detecting vehicle in cam 05 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_05/img1 --output_path DATA/detection_result/cam_05_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
cp DATA/detection_result/cam_05_det.txt DATA/image/cam_05/det/det.txt

# print("Detecting vehicle in cam 08 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_08/img1 --output_path DATA/detection_result/cam_08_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
cp DATA/detection_result/cam_08_det.txt DATA/image/cam_08/det/det.txt

# print("Detecting vehicle in cam 11 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_11/img1 --output_path DATA/detection_result/cam_11_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
cp DATA/detection_result/cam_11_det.txt DATA/image/cam_11/det/det.txt

# print("Detecting vehicle in cam 13 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_13/img1 --output_path DATA/detection_result/cam_13_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
cp DATA/detection_result/cam_13_det.txt DATA/image/cam_13/det/det.txt

# echo "Detecting vehicle in cam 15 ..."
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_15/img1 --output_path DATA/detection_result/cam_15_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
cp DATA/detection_result/cam_15_det.txt DATA/image/cam_15/det/det.txt

# print("Detecting vehicle in cam 17 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_17/img1 --output_path DATA/detection_result/cam_17_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
cp DATA/detection_result/cam_17_det.txt DATA/image/cam_17/det/det.txt

# print("Detecting vehicle in cam 19 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res.py --input_path DATA/image/cam_19/img1 --output_path DATA/detection_result/cam_19_det.txt --model_path model_weights/Detect/Dark/output/model_final.pth
cp DATA/detection_result/cam_19_det.txt DATA/image/cam_19/det/det.txt

# print("Detecting vehicle in cam 20 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res_bw.py --input_path DATA/image/cam_20/img1 --output_path DATA/detection_result/cam_20_det.txt --model_path model_weights/Detect/Black_white/output/model_final.pth
cp DATA/detection_result/cam_20_det.txt DATA/image/cam_20/det/det.txt

# print("Detecting vehicle in cam 22 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res_bw.py --input_path DATA/image/cam_22/img1 --output_path DATA/detection_result/cam_22_det.txt --model_path model_weights/Detect/Black_white/output/model_final.pth
cp DATA/detection_result/cam_22_det.txt DATA/image/cam_22/det/det.txt

# print("Detecting vehicle in cam 25 ...")
CUDA_VISIBLE_DEVICES=0 python3 src/Detect/create_detection_res_bw.py --input_path DATA/image/cam_25/img1 --output_path DATA/detection_result/cam_25_det.txt --model_path model_weights/Detect/Black_white/output/model_final.pth 
cp DATA/detection_result/cam_25_det.txt DATA/image/cam_25/det/det.txt
#####################################################################################################################################################################################################################################

# Tracking progress
#####################################################################################################################################################################################################################################
# Export to .npy file
cd src/Tracker/

for image_cam in ../../DATA/image/* ;
do 
	name="$(cut -d'/' -f5 <<<"$image_cam")";
	python3 tools/generate_detections.py --model=../../model_weights/tracking/Tracker/networks/mars-small128.pb --mot_dir=../../DATA/image/$name --output_dir=../../DATA/generate_result/ ;
done;

# Export to hypothesis files with multi-thread

python3 deep_sort_app_parallel.py \
    --min_confidence=0.3 \
    --nn_budget=100 \
    --display=False

# for file in ../../DATA/generate_result/*;
# do

# 	name="$(cut -d'/' -f3 <<<"$file")";
# 	name="$(cut -d'.' -f1 <<<"$name")";
# 	python deep_sort_app.py \
#     --sequence_dir=../../DATA/image/$name \
#     --detection_file=$file \
#     --output_file=../DATA/hypothesis/ \
#     --min_confidence=0.3 \
#     --nn_budget=100 \
#     --display=True
# done;
#cd ../../
#####################################################################################################################################################################################################################################
cd ../../

# Counting progress (export to submision file)
python3 src/Count/counting_vehicle.py
