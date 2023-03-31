﻿#cython: language_level=3
import numpy as np
import colorama

GUI_LOCK_CONFIG								= False
GUI_TB1_FILENAME 							= 'Wall-e'
GUI_TB2_FILENAME 							= 'Eve'
GUI_LOG_MAX_MESSAGE_BUFFER 					= 10000 		#Maximal amount of messages that can be displayed in the GUI
GUI_LOG_CLEAR 								= 'clear'

RAISE_ERROR_ON_UNEXPECTED_KEY				= False
RAISE_ERROR_ON_COMMUNICATION_FAILURE 		= False
RAISE_ERROR_ON_COLLISION 					= False
RAISE_ERROR_ON_MOTOR_CALIB_ERROR_OOR 		= False 		#Out of Range

PROC_MIN_NB_PROCESSES						= 1
PROC_MAX_NB_PROCESSES						= 4
PROC_START_PROCESSES 						= "START_PROCESSES"
PROC_STOP_PROCESSES 						= "STOP_PROCESSES"
PROC_PAUSE_CALIBRATION_PROGRAM				= "PAUSE_CALIBRATION_PROGRAM"
PROC_UNPAUSE_CALIBRATION_PROGRAM			= "UNPAUSE_CALIBRATION_PROGRAM"
PROC_STOP_CALIBRATION_PROGRAM				= "STOP_CALIBRATION_PROGRAM"
PROC_PROCESSES_STARTED 						= "PROCESSES_STARTED"
PROCESSES_POISON_PILL						= "END_PROCESS"
PROCESSES_CLEAR_LIVEPLOT					= "RESET_PLOT"
PROCESSES_DRAW_LIVEPLOT 					= "DRAW_PLOT"
PROCESSES_COMPUTE_CENTROID					= "COMPUTE_CENTROID"
PROCESSES_AUTODRAW_PERIOD 					= 1 		#draw each xxx[s]
PROCESSES_LIVE_PLOT_NB_POINTS				= 200		# Keep this amount of points for each positioner during liveplot
PLOT_CLOCKWIZE_COLOR						= 'r'
PLOT_COUNTERCLOCKWIZE_COLOR					= 'g'
PROC_RESULTS_POLL_PERIOD					= 1			# Second
PROC_MAX_RESULTS_POLLS						= 60/PROC_RESULTS_POLL_PERIOD		# Max polling time to get one new result before timeout
PROCESSES_CENTROID_QUEUE_TIMEOUT 			= 10 		# nb seconds max wait to retrieve an image from the queue
PROCESS_MAX_CENTROID_QUEUE_LENGTH 			= 100 		# The maximal number of images to compute that can be put in the computation queue before it starts blocking
PROCESS_MAX_LIVEPLOT_QUEUE_LENGTH			= PROCESSES_LIVE_PLOT_NB_POINTS*10 		# The maximal number of results that can be put in the display queue before it starts blocking
PROCESS_QUEUE_RECOVERY_DELAY 				= 5 		# Pause time [s] in case of a full queue before retrying
PROCESS_MEMORY_RECOVERY_DELAY 				= 5			# Pause time [s] in case of a full memory before retrying
MAX_QUEUE_RECOVERY_TRIES 					= 6			# The number of times the out of memory function can be tried before generating an error
MAX_MEMORY_RECOVERY_TRIES 					= 6			# The number of times the out of memory function can be tried before generating an error


CALIB_ALPHA_INDEX							= 0
CALIB_BETA_INDEX							= 1
CALIB_CHECK_PROCESSES_COMPLETION_INTERVAL	= 1		# [s]
CALIB_MAX_ITER_FOR_OUTLIERS_DETECTION		= 5
CALIB_CALC_MIN_ZSCORE_OUTLIER				= 5 	# Number of standard deviation for considering a point as outlier
CALIB_CALC_MIN_ERROR_OUTLIER 				= 30 	# [um] minimal eccentricity needed to even check the Z score before flagging a point as outiler
POS_SHIPPING_ANGLE_ALPHA					= 180 	# [°]
POS_SHIPPING_ANGLE_BETA 					= 180 	# [°]
POS_FIRMWARE_UPGRADE_MOD 					= 30 	# Update the displayed percentage of firmware upgrade each n-th frame. 1 frame is 8 bytes.
POS_FIRMWARE_UPGRADE_RESTART_DELAY 			= 5 	# [s] to wait after the shutdown before the firmware upgrade starts
POS_BOOTLOADER_FIRMWARE_ID 					= '80' 	# The version identifyer of a bootloader
POS_BOOTLOADER_TIMEOUT_DELAY 				= 16 	# [s]
POS_CURRENT_MOVEMENT_AMPLITUDE 				= [0,360] 	# [°]
POS_PREHEAT_MOVEMENT_AMPLITUDE 				= [0,360] 	# [°]
POS_PREHEAT_NB_STEPS 						= 50 		# The number of slices the full range will be cut into
TB_PREHEAT_LOG_INTERVAL 					= 1 		# [s] between each log


MM_IMG_ID_BITS_FOR_CENTROID_TYPE			= 1
MM_IMG_ID_BITS_FOR_DIRECTION				= 1
MM_IMG_ID_BITS_FOR_AXIS						= 1
MM_IMG_ID_BITS_FOR_STEP						= 16
MM_IMG_ID_BITS_FOR_REPETITION				= 8
MM_IMG_ID_BITS_FOR_STARTING_POINT			= 8
MM_IMG_ID_BITS_FOR_BENCH_SLOT				= 8
MM_IMG_ID_XY_IDENTIFIER						= 0
MM_IMG_ID_TILT_IDENTIFIER					= 1
MM_IMG_ID_CLOCKWIZE_DIR_IDENTIFIER			= 1
MM_IMG_ID_COUNTERCLOCKWIZE_DIR_IDENTIFIER	= 0
MM_MODEL_FIT_OPT_TOLERANCE					= 1e-5
MM_MODEL_FIT_OPT_MAX_F_EV	 				= 10000

PLOT_FUNC_ID								= 0
PLOT_TITLE_ID								= 1
PLOT_LABEL_X_ID								= 2
PLOT_LABEL_Y_ID								= 3
PLOT_MAX_FIGURE_SIZE						= 'max'
PLOT_DPI 									= 100
PLOT_TITLE_FONTSIZE_SINGLE					= 16
PLOT_AXES_LABEL_FONTSIZE_SINGLE				= 14
PLOT_LEGEND_FONTSIZE_SINGLE					= 14
PLOT_AXES_TICKS_FONTSIZE_SINGLE				= 12
PLOT_TEXT_FONTSIZE_SINGLE					= 14
PLOT_ERRTEXT_FONTSIZE_SINGLE				= 40
PLOT_LINEWIDTH_SINGLE						= 1.5
PLOT_FIGURE_SIZE_SINGLE						= (8,8)			#xPLOT_DPI to get pixels
PLOT_KEEP_FIGURE_OPEN_SINGLE				= False
PLOT_TITLE_FONTSIZE_OVERVIEW				= 8
PLOT_AXES_LABEL_FONTSIZE_OVERVIEW			= 8
PLOT_LEGEND_FONTSIZE_OVERVIEW				= 8
PLOT_AXES_TICKS_FONTSIZE_OVERVIEW			= 6
PLOT_TEXT_FONTSIZE_OVERVIEW					= 8
PLOT_ERRTEXT_FONTSIZE_OVERVIEW				= 10
PLOT_LINEWIDTH_OVERVIEW						= 0.5
PLOT_FIGURE_SIZE_OVERVIEW					= (16.8,10.5) 	#xPLOT_DPI to get pixels
PLOT_KEEP_FIGURE_OPEN_OVERVIEW				= False
PLOT_TITLE_FONTSIZE_LIFETIME				= 11
PLOT_AXES_LABEL_FONTSIZE_LIFETIME			= 11
PLOT_LEGEND_FONTSIZE_LIFETIME				= 11
PLOT_AXES_TICKS_FONTSIZE_LIFETIME			= 9
PLOT_TEXT_FONTSIZE_LIFETIME					= 11
PLOT_ERRTEXT_FONTSIZE_LIFETIME				= 20
PLOT_LINEWIDTH_LIFETIME						= 1
PLOT_FIGURE_SIZE_LIFETIME					= (16.8,10.5) 	#xPLOT_DPI to get pixels
PLOT_KEEP_FIGURE_OPEN_LIFETIME				= False
PLOT_MODEL_FIT_EXAGERATION_RATIO			= 100
PLOT_CIRCULARITY_EXAGERATION_RATIO			= 100
PLOT_LINESTYLE_CLOCKWISE 					= '--'
PLOT_LINESTYLE_COUNTERCLOCKWISE				= '-'
PLOT_STD_FILL_COLOR							= 'gray'
PLOT_STD_FILL_TRANSPARENCY					= 0.2
PLOT_ARC_COLOR								= 'black'
PLOT_MARKERSIZE_RATIO						= 3
PLOT_TARGET_MARKERSIZE_RATIO				= 100
PLOT_ARC_LINEWIDTH_RATIO					= 1
PLOT_ARC_LINESTYLE							= '-'
PLOT_MEASURES_AXES_LIMITS_RADIUS			= 25			#[mm] from center
PLOT_XY_MARKER								= 'x'
PLOT_TARGET_MARKER							= '+'
PLOT_TARGET_MARKER_COLOR					= 'black'
PLOT_REQUIREMENT_PASSED_COLOR				= 'green'
PLOT_REQUIREMENT_FAILED_COLOR				= 'red'
PLOT_REQUIREMENT_NOT_AVAILABLE_COLOR		= 'orange'
PLOT_NOT_TESTED_CAPTION						= 'Not tested'
PLOT_REQUIREMENT_N_A_TEXT					= 'N/A'
PLOT_AXIS_STRETCH_MARGIN					= 0.05
PLOT_DIRECTIONS_TO_PLOT 					= [MM_IMG_ID_COUNTERCLOCKWIZE_DIR_IDENTIFIER]#, MM_IMG_ID_CLOCKWIZE_DIR_IDENTIFIER]

PLOT_CALIB_NB_ROW_SUBPLOTS_SINGLE			= 1
PLOT_CALIB_NB_COL_SUBPLOTS_SINGLE			= 1
PLOT_CALIB_NB_ROW_SUBPLOTS_OVERVIEW			= 4
PLOT_CALIB_NB_COL_SUBPLOTS_OVERVIEW			= 6
PLOT_CALIB_NB_ROW_SUBPLOTS_LIFETIME			= 3
PLOT_CALIB_NB_COL_SUBPLOTS_LIFETIME			= 3
PLOT_CALIB_NB_SUBPLOTS 						= 24
PLOT_CALIB_NB_SUBPLOTS_LIFETIME				= 9
PLOT_TEST_NB_ROW_SUBPLOTS_SINGLE			= 1
PLOT_TEST_NB_COL_SUBPLOTS_SINGLE			= 1
PLOT_TEST_NB_ROW_SUBPLOTS_OVERVIEW			= 4
PLOT_TEST_NB_COL_SUBPLOTS_OVERVIEW			= 4
PLOT_TEST_NB_ROW_SUBPLOTS_LIFETIME			= 2
PLOT_TEST_NB_COL_SUBPLOTS_LIFETIME			= 2
PLOT_TEST_NB_SUBPLOTS 						= 16
PLOT_TEST_NB_SUBPLOTS_LIFETIME				= 4

PLOT_CONFORM_AREA_FILL_COLOR 				= 'palegreen'
PLOT_NON_CONFORM_AREA_FILL_COLOR 			= 'lightsalmon'
PLOT_CONFORMITY_AREA_FILL_ALPHA 			= 0.2

TIME_ROUND_DECIMALS							= 2
VARIABLE_ROUND_DECIMALS						= 2
DEGREES_PER_ROTATION						= 360
RADIANS_PER_ROTATION						= 2*np.pi		# 360 if variables are in degrees, 2*np.pi if variables are in radians

PARAM_AXIS_ALPHA							= 0
PARAM_AXIS_BETA								= 1
PARAM_NB_AXES 								= 2

CC_CENTROID_DETECTION_THRESHOLD 			= 0.3		#minimal required max intensity in the image
CC_CENTROID_DETECTION_THRESHOLD_XY_RATIO	= 0.5		# pixels over (this value * max of image) will be detected as a centroid
CC_CENTROID_DETECTION_THRESHOLD_TILT_RATIO	= 0.5		# pixels over (this value * max of image) will be detected as a centroid
CC_CENTROID_XY_MIN_DIAMETER 				= 1.5		# Minimal diameter allowed for the XY centroid in px
CC_CENTROID_XY_MAX_DIAMETER 				= 10		# Maximal diameter allowed for the XY centroid in px
CC_CENTROID_TILT_MIN_DIAMETER 				= 100		# Minimal diameter allowed for the tilt centroid
CC_CENTROID_TILT_MAX_DIAMETER 				= np.inf	# Maximal diameter allowed for the tilt centroid
CC_X_COORDINATE								= 0			# Arrays index to acceed x coordinates of images
CC_Y_COORDINATE 							= 1			# Arrays index to acceed y coordinates of images
CC_ROW_COORDINATE							= 0			# Arrays index to acceed rows of arrays
CC_COL_COORDINATE							= 1			# Arrays index to acceed columns of arrays
CC_SMALL_IMAGE_CROP_ROW_RATIO_XY 			= 1/(2*np.sqrt(2*np.log(1/CC_CENTROID_DETECTION_THRESHOLD_XY_RATIO))) 	#constant to pass from estimated diameter to sigma
CC_SMALL_IMAGE_CROP_COL_RATIO_XY 			= 1/(2*np.sqrt(2*np.log(1/CC_CENTROID_DETECTION_THRESHOLD_XY_RATIO))) 	#constant to pass from estimated diameter to sigma
CC_SMALL_IMAGE_CROP_ROW_RATIO_TILT 			= 1/(2*np.sqrt(2*np.log(1/CC_CENTROID_DETECTION_THRESHOLD_TILT_RATIO)))	#constant to pass from estimated diameter to sigma
CC_SMALL_IMAGE_CROP_COL_RATIO_TILT			= 1/(2*np.sqrt(2*np.log(1/CC_CENTROID_DETECTION_THRESHOLD_TILT_RATIO)))	#constant to pass from estimated diameter to sigma
CC_IMAGE_THRESHOLD_MIN 						= 0.1		# pixels below this value will be increased to this level
CC_IMAGE_THRESHOLD_MAX_RATIO 				= 0.8		# pixels over this value * max of image will be decreased to this level
CC_IMAGE_XY_FILTERING_SIGMA 				= 1			# desired sigma of the gaussian filter used for filtering
CC_IMAGE_TILT_FILTERING_SIGMA 				= 5			# desired sigma of the gaussian filter used for filtering
CC_COMPUTATION_SIGMA_CROP_RATIO_XY 			= 4			# desired number of standard deviations from computed center to the new sub-image crop
CC_COMPUTATION_SIGMA_CROP_RATIO_TILT 		= 6			# desired number of standard deviations from computed center to the new sub-image crop
CC_COMPUTATION_MAX_ITERATION 				= 5			# maximal number of recropping on the same image 
CC_COMPUTATION_PIXEL_TOLERANCE_XY 			= 1			# pixel precision required to consider crop didn't move. minimum is 1.
CC_COMPUTATION_PIXEL_TOLERANCE_TILT 		= 5			# pixel precision required to consider crop didn't move. minimum is 1.
CC_OPTIMIZER_TOLERANCE_XY					= 1e-30
CC_OPTIMIZER_TOLERANCE_TILT					= 1e-10

PC_IMAGE_TIMEOUT							= 500					# [ms]
PC_CONNECT_ANY_CAMERA_ID					= 'any'					
PC_CAMERA_TYPE_XY							= 'XY'					# Name of the XY test setup
PC_CAMERA_TYPE_TILT							= 'Tilt'				# Name of the XY test setup
PC_CAMERA_XY_NB_IMAGES_PER_POINT			= 1						# Number of images taken for the XY bench (small centroids)
PC_CAMERA_TILT_NB_IMAGES_PER_POINT			= 4						# Number of images taken for the Tilt bench (big centroids)
PC_CAMERA_MAX_INTENSITY_RAW					= 2**8-1				# Maximal raw intensity of the camera
PC_CAMERA_PIXEL_FORMAT						= 'Mono8'				# Number if bits per pixel setting of the camera
PC_CAMERA_GET_EXPOSURE_NB_OK				= 2						# Number of images with correct exposure level required
PC_CAMERA_GET_EXPOSURE_INTENSITY_TOLERANCE	= 0.05					# Allowable range near the target exposure in %
PC_CAMERA_GET_EXPOSURE_EXPOSURE_MIN			= 35					# Minimal exposure time of the camera in [us]
PC_CAMERA_GET_EXPOSURE_EXPOSURE_MAX			= 1599999				# Maximal exposure time of the camera in [us]
PC_CAMERA_GET_EXPOSURE_MAX_ITERATIONS		= 10					# Maximal number of iterations to get to the target exposure
PC_CAMERA_GET_EXPOSURE_TARGET_INTENSITY 	= 0.7 #0.9					# Target maximal intensity of the image for the exposure setting
PC_CAMERA_GET_EXPOSURE_SATURED_THRESHOLD 	= 0.999
PC_CAMERA_GET_EXPOSURE_SATURED_GAIN 		= 1/5
PC_CAMERA_XY_MIN_CROP_WINDOW 				= 64					# Minimal crop window allowed by the camera on the XY benches
PC_CAMERA_TILT_MIN_CROP_WINDOW 				= 64					# Minimal crop window allowed by the camera on the Tilt benches				
PC_CAMERA_FORBID_CROPPING		 			= 'max'					# Window size if dynamic cropping is not allowed
PC_CAMERA_XY_CALIB_CROP						= 150					# Window size to use when doing a calibration [px]
PC_CAMERA_XY_TEST_CROP						= 200					# Window size to use when doing a test [px]
PC_FILE_DISTORTION_EXTENSION				= '.mat'
PC_FILE_DISTORTION_PARAMETERS_NAME			= 'cam_parameters'
PC_FILE_DISTORTION_XCORR_NAME				= 'x_corr'
PC_FILE_DISTORTION_YCORR_NAME				= 'y_corr'
PC_FILE_DISTORTION_SCALE_FACTOR_NAME		= 'scale_factor'
PC_CAMERA_XY_DEFAULT_EXPOSURE				= 1500
PC_CAMERA_XY_MAX_EXPOSURE					= 10000					#If this level of exposure is reached, the region is considered to have no centroid
PC_CAMERA_XY_DEFAULT_GAIN					= 0.0
PC_CAMERA_XY_DEFAULT_BLACKLEVEL				= 1.25
PC_CAMERA_XY_DEFAULT_GAMMA					= 1.0
PC_CAMERA_TILT_DEFAULT_EXPOSURE				= 200000
PC_CAMERA_TILT_DEFAULT_GAIN					= 6.0
PC_CAMERA_TILT_DEFAULT_BLACKLEVEL			= 1.25
PC_CAMERA_TILT_DEFAULT_GAMMA				= 1.0
PC_CAMERA_TILT_DEFAULT_DIGITALSHIFT			= 0.0
PC_IMAGE_GET_ALL_ROI						= 'inf'
PC_IMAGE_SOFT_ROI_MARGIN					= 2						#mm added to the arms sum for soft ROI cropping

PM_ANGLE_INCREMENT							= 1
PM_IDENTIFICATION_MINIMAL_DISPLACEMENT		= 0.05

CANCOM_CONNECT_ANY_ID						= 'any'
CANCOM_FIRMWARE_CONTROL_LOOP_FREQUENCY		= 2000
CAN_COM_WATCHDOG_TIMER 						= 0.5 					# [s]
CAN_DELAY_BETWEEN_CONFIG_COMMANDS 			= 0.5 					# [s]
CAN_COM_STATUS_BROADCAST_WATCHDOG_TIMER 	= 2 					# [s]
CAN_DELAY_FOR_ASKID				 			= 0.5 					# [s]
CAN_COM_SAVE_INTERNAL_CALIB_WATCHDOG_TIMER 	= 4 					# [s]
CAN_COM_WAIT_FOR_TIMEOUT 					= 'wait'
CAN_COM_FIRMWARE_UPGRADE_TIMEOUT 			= 10 					# [s]

CALIBRATION_MOTOR_MAXIMAL_ERROR	 			= 30 					# [°]
TESTBENCH_COGGING_CALIB_WATCHDOG_TIMEOUT	= 30*60 				# [s] maximal time allowed for cogging calibration before considering it unvalid
POS_OFFSET_VALIDITY_ALPHA 					= [3, 15] 				# [°], the accepted offset range. If the positioner is outside this range, it gets reset.
POS_OFFSET_VALIDITY_BETA 					= [3, 15]				# [°], the accepted offset range. If the positioner is outside this range, it gets reset.

CONFIG_LOAD_LATEST_RESULT					= 'latest'
CONFIG_PREHEAT_BENCH_DEFAULT_TIME 			= 10					# minutes
DEFAULT_CONFIG_FILENAME 					= 'system_config'

LOG_MESSAGE_PRIORITY_DEBUG_INFO 			= 44
LOG_MESSAGE_PRIORITY_DEBUG_WARNING			= 43
LOG_MESSAGE_PRIORITY_DEBUG_ERROR			= 42
LOG_MESSAGE_PRIORITY_DEBUG_CRITICAL 		= 41
LOG_MESSAGE_PRIORITY_DEBUG					= 40
LOG_MESSAGE_PRIORITY_INFO_PENDING_OP		= 35
LOG_MESSAGE_PRIORITY_INFO					= 30
LOG_MESSAGE_PRIORITY_WARNING				= 20
LOG_MESSAGE_PRIORITY_ERROR					= 10
LOG_MESSAGE_PRIORITY_CRITICAL				= 00
LOG_VERBOSE_LEVEL 							= 43

MSG_COLOR_DEFAULT 							= colorama.Fore.WHITE
MSG_COLOR_DEBUG 							= colorama.Fore.GREEN
MSG_COLOR_INFO 								= colorama.Fore.CYAN
MSG_COLOR_WARNING 							= colorama.Fore.YELLOW
MSG_COLOR_CRITICAL							= colorama.Fore.MAGENTA
MSG_COLOR_ERROR								= colorama.Fore.RED

LABEL_MSG_COLOR_DEFAULT 					= '#000000'
LABEL_MSG_COLOR_DEBUG 						= '#00FF00'
LABEL_MSG_COLOR_INFO 						= '#00FFFF'
LABEL_MSG_COLOR_WARNING 					= '#FFFF00'
LABEL_MSG_COLOR_CRITICAL					= '#FF00FF'
LABEL_MSG_COLOR_ERROR						= '#FF0000'

GUI_DEFAULT_FONT							= "Helvetica"
GUI_DEFAULT_FONT_SIZE						= 9

GUI_BOOTLOADER_WATCHDOG 					= 10
FILELOCK_WATCHDOG 							= 20 #[s]
FILELOCK_NB_ESSAYS 							= 3
GLOBAL_WHILE_LOOP_SLEEP_TIME 				= 0.01
FILELOCK_WHILE_LOOP_SLEEP_TIME 				= 1
COGGING_WHILE_LOOP_SLEEP_TIME 				= 1

def nullFunc():
	pass