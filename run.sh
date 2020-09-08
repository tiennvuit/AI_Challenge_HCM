# Clean all directories contain data

echo "Removing all directories and ..."

rm -rf data/images/*

# Loop through all videos and extract to images
for video in test_data/*.mp4;
do 

	# Get the camera name
	name="$(cut -d'/' -f2 <<<"$video")";
	name="$(cut -d'.' -f1 <<<"$name")";
	
	# Create output directory store extracted images
	output="data/images/$name"
	mkdir $output

	echo "Extracting $name to images ..." ;
		
	ffmpeg -i $video -r 10/1 $output/image_%d.jpg
	
done;
