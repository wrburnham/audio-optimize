This is a small script to optimize sound files by trimming silence, converting stereo to mono and normalizing. It requires the pydub library and ffmpeg must be installed on the OS.

The program is launched from the terminal with four arguments:

	dir_in : the input directory, such as /home/somewhere
	dir_out : the output directory, such as /home/somewhere/out
	ext_in : the extension / format of the sound files present in the input directory (ex: m4a)
	ext_out : the extension / format desired (ex: mp3)
