import platform
import re
from typing import List
import sys
import ssl
import os
import difflib

# 全局时间变量
start_time = 0
end_time = 0
# constants
from gui_data.translate import *

#Platform Details
OPERATING_SYSTEM = platform.system()
SYSTEM_ARCH = platform.platform()
SYSTEM_PROC = platform.processor()
ARM = 'arm'

#Main Font
MAIN_FONT_NAME = "Century Gothic"

#Model Types
VR_ARCH_TYPE = translate('VR Arc')
MDX_ARCH_TYPE = translate('MDX-Net')
DEMUCS_ARCH_TYPE = translate('Demucs')
VR_ARCH_PM = translate('VR Architecture')
ENSEMBLE_MODE = translate('Ensemble Mode')
ENSEMBLE_STEM_CHECK = translate('Ensemble Stem')
SECONDARY_MODEL = translate('Secondary Model')
DEMUCS_6_STEM_MODEL = translate('htdemucs_6s')

DEMUCS_V3_ARCH_TYPE = translate('Demucs v3')
DEMUCS_V4_ARCH_TYPE = translate('Demucs v4')
DEMUCS_NEWER_ARCH_TYPES = [DEMUCS_V3_ARCH_TYPE, DEMUCS_V4_ARCH_TYPE]

DEMUCS_V1 = 'v1'
DEMUCS_V2 = 'v2'
DEMUCS_V3 = 'v3'
DEMUCS_V4 = 'v4'

DEMUCS_V1_TAG = 'v1 | '
DEMUCS_V2_TAG = 'v2 | '
DEMUCS_V3_TAG = 'v3 | '
DEMUCS_V4_TAG = 'v4 | '
DEMUCS_NEWER_TAGS = [DEMUCS_V3_TAG, DEMUCS_V4_TAG]

DEMUCS_VERSION_MAPPER = {
            DEMUCS_V1:DEMUCS_V1_TAG,
            DEMUCS_V2:DEMUCS_V2_TAG,
            DEMUCS_V3:DEMUCS_V3_TAG,
            DEMUCS_V4:DEMUCS_V4_TAG}

#Download Center
DOWNLOAD_FAILED = translate('Download Failed')
DOWNLOAD_STOPPED = translate('Download Stopped')
DOWNLOAD_COMPLETE = translate('Download Complete')
DOWNLOAD_UPDATE_COMPLETE = translate('Update Download Complete')
SETTINGS_MENU_EXIT = translate('exit')
NO_CONNECTION = translate('No Internet Connection')
VIP_SELECTION = translate('VIP:')
DEVELOPER_SELECTION = translate('VIP:')
NO_NEW_MODELS = translate('All Available Models Downloaded')
ENSEMBLE_PARTITION = ': '
NO_MODEL = translate('No Model Selected')
CHOOSE_MODEL = translate('Choose Model')
SINGLE_DOWNLOAD = translate('Downloading Item 1/1...')
DOWNLOADING_ITEM = translate('Downloading Item')
FILE_EXISTS = translate('File already exists!')
DOWNLOADING_UPDATE = translate('Downloading Update...')
DOWNLOAD_MORE = translate('Download More Models')

#Menu Options

AUTO_SELECT = 'Auto'

#LINKS
DOWNLOAD_CHECKS = "https://raw.githubusercontent.com/TRvlvr/application_data/main/filelists/download_checks.json"
MDX_MODEL_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/model_data.json"
VR_MODEL_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/vr_model_data/model_data.json"

DEMUCS_MODEL_NAME_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/demucs_model_data/model_name_mapper.json"
MDX_MODEL_NAME_DATA_LINK = "https://raw.githubusercontent.com/TRvlvr/application_data/main/mdx_model_data/model_name_mapper.json"

DONATE_LINK_BMAC = "https://www.buymeacoffee.com/uvr5"
DONATE_LINK_PATREON = "https://www.patreon.com/uvr"

#DOWNLOAD REPOS
NORMAL_REPO = "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/"
UPDATE_REPO = "https://github.com/TRvlvr/model_repo/releases/download/uvr_update_patches/"

UPDATE_MAC_ARM_REPO = "https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.5.0/Ultimate_Vocal_Remover_v5_5_MacOS_arm64.dmg"
UPDATE_MAC_X86_64_REPO = "https://github.com/Anjok07/ultimatevocalremovergui/releases/download/v5.5.0/Ultimate_Vocal_Remover_v5_5_MacOS_x86_64.dmg"
UPDATE_LINUX_REPO = "https://github.com/Anjok07/ultimatevocalremovergui#linux-installation"
UPDATE_REPO = "https://github.com/TRvlvr/model_repo/releases/download/uvr_update_patches/"

ISSUE_LINK = 'https://github.com/Anjok07/ultimatevocalremovergui/issues/new'
VIP_REPO = b'\xf3\xc2W\x19\x1foI)\xc2\xa9\xcc\xb67(Z\xf5',\
           b'gAAAAABjQAIQ-NpNMMxMedpKHHb7ze_nqB05hw0YhbOy3pFzuzDrfqumn8_qvraxEoUpZC5ZXC0gGvfDxFMqyq9VWbYKlA67SUFI_wZB6QoVyGI581vs7kaGfUqlXHIdDS6tQ_U-BfjbEAK9EU_74-R2zXjz8Xzekw=='
NO_CODE = 'incorrect_code'

#Extensions

ONNX = '.onnx'
CKPT = '.ckpt'
YAML = '.yaml'
PTH = '.pth'
TH_EXT = '.th'
JSON = '.json'

#GUI Buttons

START_PROCESSING = translate('Start Processing')
WAIT_PROCESSING = translate('Please wait...')
STOP_PROCESSING = translate('Halting process, please wait...')
LOADING_MODELS = translate('Loading models...')

#---Messages and Logs----

MISSING_MODEL = translate('missing')
MODEL_PRESENT = translate('present')

UNRECOGNIZED_MODEL = translate('Unrecognized Model Detected'), translate(' is an unrecognized model.\n\n') + \
                     translate('Would you like to select the correct parameters before continuing?')
                     
STOP_PROCESS_CONFIRM = translate('Confirmation'), translate('You are about to stop all active processes.\n\nAre you sure you wish to continue?')
NO_ENSEMBLE_SELECTED = translate('No Models Selected'), translate('Please select ensemble and try again.')
PICKLE_CORRU = translate('File Corrupted'), translate('Unable to load this ensemble.\n\n' ) + \
               translate('Would you like to remove this ensemble from your list?')
DELETE_ENS_ENTRY = translate('Confirm Removal'), translate('Are you sure you want to remove this entry?')

ALL_STEMS = translate('All Stems')
VOCAL_STEM = translate('Vocals')
INST_STEM = translate('Instrumental')
OTHER_STEM = translate('Other')
BASS_STEM = translate('Bass')
DRUM_STEM = translate('Drums')
GUITAR_STEM = translate('Guitar')
PIANO_STEM = translate('Piano')
SYNTH_STEM = translate('Synthesizer')
STRINGS_STEM = translate('Strings')
WOODWINDS_STEM = translate('Woodwinds')
BRASS_STEM = translate('Brass')
WIND_INST_STEM =translate( 'Wind Inst')
NO_OTHER_STEM = translate('No Other')
NO_BASS_STEM = translate('No Bass')
NO_DRUM_STEM = translate('No Drums')
NO_GUITAR_STEM = translate('No Guitar')
NO_PIANO_STEM = translate('No Piano')
NO_SYNTH_STEM = translate('No Synthesizer')
NO_STRINGS_STEM = translate('No Strings')
NO_WOODWINDS_STEM =translate( 'No Woodwinds')
NO_WIND_INST_STEM = translate('No Wind Inst')
NO_BRASS_STEM = translate('No Brass')
PRIMARY_STEM = translate('Primary Stem')
SECONDARY_STEM =translate( 'Secondary Stem')

#Other Constants
DEMUCS_2_SOURCE = [translate("instrumental"), translate("vocals")]
DEMUCS_4_SOURCE = [translate("drums"), translate("bass"), translate("other"), translate("vocals")]

DEMUCS_2_SOURCE_MAPPER = {
                        INST_STEM: 0,
                        VOCAL_STEM: 1}

DEMUCS_4_SOURCE_MAPPER = {
                        BASS_STEM: 0,
                        DRUM_STEM: 1,
                        OTHER_STEM: 2,
                        VOCAL_STEM: 3}

DEMUCS_6_SOURCE_MAPPER = {
                        BASS_STEM: 0,
                        DRUM_STEM: 1,
                        OTHER_STEM: 2,
                        VOCAL_STEM: 3,
                        GUITAR_STEM:4,
                        PIANO_STEM:5}

DEMUCS_4_SOURCE_LIST = [BASS_STEM, DRUM_STEM, OTHER_STEM, VOCAL_STEM]
DEMUCS_6_SOURCE_LIST = [BASS_STEM, DRUM_STEM, OTHER_STEM, VOCAL_STEM, GUITAR_STEM, PIANO_STEM]

DEMUCS_UVR_MODEL = translate('UVR_Model')

CHOOSE_STEM_PAIR = translate('Choose Stem Pair')

STEM_SET_MENU = (VOCAL_STEM, 
                 INST_STEM, 
                 OTHER_STEM, 
                 BASS_STEM, 
                 DRUM_STEM, 
                 GUITAR_STEM, 
                 PIANO_STEM, 
                 SYNTH_STEM, 
                 STRINGS_STEM, 
                 WOODWINDS_STEM, 
                 BRASS_STEM,
                 WIND_INST_STEM,
                 NO_OTHER_STEM, 
                 NO_BASS_STEM, 
                 NO_DRUM_STEM, 
                 NO_GUITAR_STEM, 
                 NO_PIANO_STEM, 
                 NO_SYNTH_STEM, 
                 NO_STRINGS_STEM, 
                 NO_WOODWINDS_STEM,
                 NO_BRASS_STEM,
                 NO_WIND_INST_STEM)

STEM_PAIR_MAPPER = {
            VOCAL_STEM: INST_STEM,
            INST_STEM: VOCAL_STEM,
            OTHER_STEM: NO_OTHER_STEM,
            BASS_STEM: NO_BASS_STEM,
            DRUM_STEM: NO_DRUM_STEM,
            GUITAR_STEM: NO_GUITAR_STEM,
            PIANO_STEM: NO_PIANO_STEM,
            SYNTH_STEM: NO_SYNTH_STEM,
            STRINGS_STEM: NO_STRINGS_STEM,
            WOODWINDS_STEM: NO_WOODWINDS_STEM,
            BRASS_STEM: NO_BRASS_STEM,
            WIND_INST_STEM: NO_WIND_INST_STEM,
            NO_OTHER_STEM: OTHER_STEM,
            NO_BASS_STEM: BASS_STEM,
            NO_DRUM_STEM: DRUM_STEM,
            NO_GUITAR_STEM: GUITAR_STEM,
            NO_PIANO_STEM: PIANO_STEM,
            NO_SYNTH_STEM: SYNTH_STEM,
            NO_STRINGS_STEM: STRINGS_STEM,
            NO_WOODWINDS_STEM: WOODWINDS_STEM,
            NO_BRASS_STEM: BRASS_STEM,
            NO_WIND_INST_STEM: WIND_INST_STEM,
            PRIMARY_STEM: SECONDARY_STEM}

NON_ACCOM_STEMS = (
            VOCAL_STEM,
            OTHER_STEM,
            BASS_STEM,
            DRUM_STEM,
            GUITAR_STEM,
            PIANO_STEM,
            SYNTH_STEM,
            STRINGS_STEM,
            WOODWINDS_STEM,
            BRASS_STEM,
            WIND_INST_STEM)

MDX_NET_FREQ_CUT = [VOCAL_STEM, INST_STEM]

DEMUCS_4_STEM_OPTIONS = (ALL_STEMS, VOCAL_STEM, OTHER_STEM, BASS_STEM, DRUM_STEM)
DEMUCS_6_STEM_OPTIONS = (ALL_STEMS, VOCAL_STEM, OTHER_STEM, BASS_STEM, DRUM_STEM, GUITAR_STEM, PIANO_STEM)
DEMUCS_2_STEM_OPTIONS = (VOCAL_STEM, INST_STEM)
DEMUCS_4_STEM_CHECK = (OTHER_STEM, BASS_STEM, DRUM_STEM)

#Menu Dropdowns

VOCAL_PAIR = f'{VOCAL_STEM}/{INST_STEM}'
INST_PAIR = f'{INST_STEM}/{VOCAL_STEM}'
OTHER_PAIR = f'{OTHER_STEM}/{NO_OTHER_STEM}'
DRUM_PAIR = f'{DRUM_STEM}/{NO_DRUM_STEM}'
BASS_PAIR = f'{BASS_STEM}/{NO_BASS_STEM}'
FOUR_STEM_ENSEMBLE = translate('4 Stem Ensemble')

ENSEMBLE_MAIN_STEM = (CHOOSE_STEM_PAIR, VOCAL_PAIR, OTHER_PAIR, DRUM_PAIR, BASS_PAIR, FOUR_STEM_ENSEMBLE)

MIN_SPEC = translate('Min Spec')
MAX_SPEC = translate('Max Spec')
AUDIO_AVERAGE = translate('Average')

MAX_MIN = f'{MAX_SPEC}/{MIN_SPEC}'
MAX_MAX = f'{MAX_SPEC}/{MAX_SPEC}'
MAX_AVE = f'{MAX_SPEC}/{AUDIO_AVERAGE}'
MIN_MAX = f'{MIN_SPEC}/{MAX_SPEC}'
MIN_MIX = f'{MIN_SPEC}/{MIN_SPEC}'
MIN_AVE = f'{MIN_SPEC}/{AUDIO_AVERAGE}'
AVE_MAX = f'{AUDIO_AVERAGE}/{MAX_SPEC}'
AVE_MIN = f'{AUDIO_AVERAGE}/{MIN_SPEC}'
AVE_AVE = f'{AUDIO_AVERAGE}/{AUDIO_AVERAGE}'

ENSEMBLE_TYPE = (MAX_MIN, MAX_MAX, MAX_AVE, MIN_MAX, MIN_MIX, MIN_AVE, AVE_MAX, AVE_MIN, AVE_AVE)
ENSEMBLE_TYPE_4_STEM = (MAX_SPEC, MIN_SPEC, AUDIO_AVERAGE)

BATCH_MODE = 'Batch Mode'
BETA_VERSION = 'BETA'
DEF_OPT = 'Default'

CHUNKS = (AUTO_SELECT, '1', '5', '10', '15', '20', 
          '25', '30', '35', '40', '45', '50', 
          '55', '60', '65', '70', '75', '80', 
          '85', '90', '95', translate('Full'))

BATCH_SIZE = (DEF_OPT, '2', '3', '4', '5', 
          '6', '7', '8', '9', '10')

VOL_COMPENSATION = (AUTO_SELECT, '1.035', '1.08')

MARGIN_SIZE = ('44100', '22050', '11025')

AUDIO_TOOLS = translate('Audio Tools')

MANUAL_ENSEMBLE = translate('Manual Ensemble')
TIME_STRETCH = translate('Time Stretch')
CHANGE_PITCH = translate('Change Pitch')
ALIGN_INPUTS = translate('Align Inputs')

if OPERATING_SYSTEM == 'Windows' or OPERATING_SYSTEM == 'Darwin':  
   AUDIO_TOOL_OPTIONS = (MANUAL_ENSEMBLE, TIME_STRETCH, CHANGE_PITCH, ALIGN_INPUTS)
else:
   AUDIO_TOOL_OPTIONS = (MANUAL_ENSEMBLE, ALIGN_INPUTS)

MANUAL_ENSEMBLE_OPTIONS = (MIN_SPEC, MAX_SPEC, AUDIO_AVERAGE)

PROCESS_METHODS = (VR_ARCH_PM, MDX_ARCH_TYPE, DEMUCS_ARCH_TYPE, ENSEMBLE_MODE, AUDIO_TOOLS)

DEMUCS_SEGMENTS = (translate('Default'), '1', '5', '10', '15', '20',
                  '25', '30', '35', '40', '45', '50', 
                  '55', '60', '65', '70', '75', '80', 
                  '85', '90', '95', '100')

DEMUCS_SHIFTS = (0, 1, 2, 3, 4, 5, 
                 6, 7, 8, 9, 10, 11, 
                 12, 13, 14, 15, 16, 17, 
                 18, 19, 20)

DEMUCS_OVERLAP = (0.25, 0.50, 0.75, 0.99)

VR_AGGRESSION = (1, 2, 3, 4, 5, 
                 6, 7, 8, 9, 10, 11, 
                 12, 13, 14, 15, 16, 17, 
                 18, 19, 20)

VR_WINDOW = ('320', '512','1024')
VR_CROP = ('256', '512', '1024')
POST_PROCESSES_THREASHOLD_VALUES = ('0.1', '0.2', '0.3')

MDX_POP_PRO = translate('MDX-NET_Noise_Profile_14_kHz'), translate('MDX-NET_Noise_Profile_17_kHz'), translate('MDX-NET_Noise_Profile_Full_Band')
MDX_POP_STEMS = translate('Vocals'), translate('Instrumental'), translate('Other'), translate('Drums'), translate('Bass')
MDX_POP_NFFT = ('4096', '5120', '6144', '7680', '8192', '16384')
MDX_POP_DIMF = ('2048', '3072', '4096')

SAVE_ENSEMBLE = translate('Save Ensemble')
CLEAR_ENSEMBLE = translate('Clear Selection(s)')
MENU_SEPARATOR = 35*'•'
CHOOSE_ENSEMBLE_OPTION = translate('Choose Option')

INVALID_ENTRY = translate('Invalid Input, Please Try Again')
ENSEMBLE_INPUT_RULE = translate('1. Only letters, numbers, spaces, and dashes allowed.\n2. No dashes or spaces at the start or end of input.')

ENSEMBLE_OPTIONS = (SAVE_ENSEMBLE, CLEAR_ENSEMBLE)
ENSEMBLE_CHECK = translate('ensemble check')

SELECT_SAVED_ENSEMBLE = translate('Select Saved Ensemble')
SELECT_SAVED_SETTING =translate( 'Select Saved Setting')
ENSEMBLE_OPTION = translate("Ensemble Customization Options")
MDX_OPTION = translate("Advanced MDX-Net Options")
DEMUCS_OPTION = translate("Advanced Demucs Options")
VR_OPTION = translate("Advanced VR Options")
HELP_OPTION = translate("Open Information Guide")
ERROR_OPTION = translate("Open Error Log")
VERIFY_BEGIN = translate('Verifying file ')
SAMPLE_BEGIN = translate('Creating Sample ')
MODEL_MISSING_CHECK =translate( 'Model Missing:')

# Audio Player

PLAYING_SONG =translate( ": Playing")
PAUSE_SONG = translate(": Paused")
STOP_SONG = translate(": Stopped")

SELECTED_VER = translate('Selected')
DETECTED_VER = translate('Detected')
linshi=translate("Sample Mode")
SAMPLE_MODE_CHECKBOX = lambda v:f'{linshi}({v}s)'
REMOVED_FILES = lambda r, e:f'Audio Input Verification Report:\n\nRemoved Files:\n\n{r}\n\nError Details:\n\n{e}'
ADVANCED_SETTINGS = (ENSEMBLE_OPTION, MDX_OPTION, DEMUCS_OPTION, VR_OPTION, HELP_OPTION, ERROR_OPTION)

WAV = 'WAV'
FLAC = 'FLAC'
MP3 = 'MP3'

MP3_BIT_RATES = ('96k', '128k', '160k', '224k', '256k', '320k')
WAV_TYPE = ('PCM_U8', 'PCM_16', 'PCM_24', 'PCM_32', '32-bit Float', '64-bit Float')

SELECT_SAVED_SET = translate('Choose Option')
SAVE_SETTINGS = translate('Save Current Settings')
RESET_TO_DEFAULT = translate('Reset to Default')
RESET_FULL_TO_DEFAULT = translate('Reset to Default')
RESET_PM_TO_DEFAULT = translate('Reset All Application Settings to Default')

SAVE_SET_OPTIONS = (SAVE_SETTINGS, RESET_TO_DEFAULT)

TIME_PITCH = ('1.0', '2.0', '3.0', '4.0')
TIME_TEXT = '_time_stretched'
PITCH_TEXT = '_pitch_shifted'

#RegEx Input Validation

REG_PITCH = r'^[-+]?(1[0]|[0-9]([.][0-9]*)?)$'
REG_TIME = r'^[+]?(1[0]|[0-9]([.][0-9]*)?)$'
REG_COMPENSATION = r'\b^(1[0]|[0-9]([.][0-9]*)?|Auto|None)$\b'
REG_THES_POSTPORCESS = r'\b^([0]([.][0-9]{0,6})?)$\b'
REG_CHUNKS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|Auto|Full)$\b'
REG_CHUNKS_DEMUCS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|Auto|Full)$\b'
REG_MARGIN = r'\b^[0-9]*$\b'
REG_SEGMENTS = r'\b^(200|1[0-9][0-9]|[1-9][0-9]?|Default)$\b'
REG_SAVE_INPUT = r'\b^([a-zA-Z0-9 -]{0,25})$\b'
REG_AGGRESSION = r'^[-+]?[0-9]\d*?$'
REG_WINDOW = r'\b^[0-9]{0,4}$\b'
REG_SHIFTS = r'\b^[0-9]*$\b'
REG_BATCHES = r'\b^([0-9]*?|Default)$\b'
REG_OVERLAP = r'\b^([0]([.][0-9]{0,6})?|None)$\b'

# Sub Menu

VR_ARCH_SETTING_LOAD = translate('Load for VR Arch')
MDX_SETTING_LOAD = translate('Load for MDX-Net')
DEMUCS_SETTING_LOAD = translate('Load for Demucs')
ALL_ARCH_SETTING_LOAD = translate('Load for Full Application')

# Mappers

DEFAULT_DATA = {
    
        'chosen_process_method': MDX_ARCH_TYPE,
        'vr_model': CHOOSE_MODEL,
        'aggression_setting': 10,
        'window_size': 512,
        'batch_size': 4,
        'crop_size': 256, 
        'is_tta': False,
        'is_output_image': False,
        'is_post_process': False,
        'is_high_end_process': False,
        'post_process_threshold': 0.2,
        'vr_voc_inst_secondary_model': NO_MODEL,
        'vr_other_secondary_model': NO_MODEL,
        'vr_bass_secondary_model': NO_MODEL,
        'vr_drums_secondary_model': NO_MODEL,
        'vr_is_secondary_model_activate': False,        
        'vr_voc_inst_secondary_model_scale': 0.9,
        'vr_other_secondary_model_scale': 0.7,
        'vr_bass_secondary_model_scale': 0.5,
        'vr_drums_secondary_model_scale': 0.5,
        'demucs_model': CHOOSE_MODEL, 
        'demucs_stems': ALL_STEMS,
        'segment': DEMUCS_SEGMENTS[0],
        'overlap': DEMUCS_OVERLAP[0],
        'shifts': 2,
        'chunks_demucs': CHUNKS[0],
        'margin_demucs': 44100,
        'is_chunk_demucs': False,
        'is_chunk_mdxnet': False,
        'is_primary_stem_only_Demucs': False,
        'is_secondary_stem_only_Demucs': False,
        'is_split_mode': True,
        'is_demucs_combine_stems': True,
        'demucs_voc_inst_secondary_model': NO_MODEL,
        'demucs_other_secondary_model': NO_MODEL,
        'demucs_bass_secondary_model': NO_MODEL,
        'demucs_drums_secondary_model': NO_MODEL,
        'demucs_is_secondary_model_activate': False,        
        'demucs_voc_inst_secondary_model_scale': 0.9,
        'demucs_other_secondary_model_scale': 0.7,
        'demucs_bass_secondary_model_scale': 0.5,
        'demucs_drums_secondary_model_scale': 0.5,
        'demucs_stems': ALL_STEMS,
        'demucs_pre_proc_model': NO_MODEL,
        'is_demucs_pre_proc_model_activate': False,
        'is_demucs_pre_proc_model_inst_mix': False,
        'mdx_net_model': CHOOSE_MODEL,
        'chunks': CHUNKS[0],
        'margin': 44100,
        'compensate': AUTO_SELECT,
        'is_denoise': False,
        'is_invert_spec': False, 
        'is_mixer_mode': False, 
        'mdx_batch_size': DEF_OPT,
        'mdx_voc_inst_secondary_model': NO_MODEL,
        'mdx_other_secondary_model': NO_MODEL,
        'mdx_bass_secondary_model': NO_MODEL,
        'mdx_drums_secondary_model': NO_MODEL,
        'mdx_is_secondary_model_activate': False,        
        'mdx_voc_inst_secondary_model_scale': 0.9,
        'mdx_other_secondary_model_scale': 0.7,
        'mdx_bass_secondary_model_scale': 0.5,
        'mdx_drums_secondary_model_scale': 0.5,
        'is_save_all_outputs_ensemble': True,
        'is_append_ensemble_name': False,
        'chosen_audio_tool': AUDIO_TOOL_OPTIONS[0],
        'choose_algorithm': MANUAL_ENSEMBLE_OPTIONS[0],
        'time_stretch_rate': 2.0,
        'pitch_rate': 2.0,
        'is_gpu_conversion': False,
        'is_primary_stem_only': False,
        'is_secondary_stem_only': False,
        'is_testing_audio': False,
        'is_add_model_name': False,
        'is_accept_any_input': False,
        'is_task_complete': False,
        'is_normalization': False,
        'is_create_model_folder': False,
        'mp3_bit_set': '320k',
        'save_format': WAV,
        'wav_type_set': 'PCM_16',
        'user_code': '',
        'export_path': '',
        'input_paths': [],
        'lastDir': None,
        'export_path': '',
        'model_hash_table': None,
        'help_hints_var': False,
        'model_sample_mode': False,
        'model_sample_mode_duration': 30
}

SETTING_CHECK = ('vr_model',
               'aggression_setting',
               'window_size',
               'batch_size',
               'crop_size',
               'is_tta',
               'is_output_image',
               'is_post_process',
               'is_high_end_process',
               'post_process_threshold',
               'vr_voc_inst_secondary_model',
               'vr_other_secondary_model',
               'vr_bass_secondary_model',
               'vr_drums_secondary_model',
               'vr_is_secondary_model_activate',
               'vr_voc_inst_secondary_model_scale',
               'vr_other_secondary_model_scale',
               'vr_bass_secondary_model_scale',
               'vr_drums_secondary_model_scale',
               'demucs_model',
               'segment',
               'overlap',
               'shifts',
               'chunks_demucs',
               'margin_demucs',
               'is_chunk_demucs',
               'is_primary_stem_only_Demucs',
               'is_secondary_stem_only_Demucs',
               'is_split_mode',
               'is_demucs_combine_stems',
               'demucs_voc_inst_secondary_model',
               'demucs_other_secondary_model',
               'demucs_bass_secondary_model',
               'demucs_drums_secondary_model',
               'demucs_is_secondary_model_activate',
               'demucs_voc_inst_secondary_model_scale',
               'demucs_other_secondary_model_scale',
               'demucs_bass_secondary_model_scale',
               'demucs_drums_secondary_model_scale',
               'demucs_stems',
               'mdx_net_model',
               'chunks',
               'margin',
               'compensate',
               'is_denoise',
               'is_invert_spec',
               'mdx_batch_size',
               'mdx_voc_inst_secondary_model',
               'mdx_other_secondary_model',
               'mdx_bass_secondary_model',
               'mdx_drums_secondary_model',
               'mdx_is_secondary_model_activate',
               'mdx_voc_inst_secondary_model_scale',
               'mdx_other_secondary_model_scale',
               'mdx_bass_secondary_model_scale',
               'mdx_drums_secondary_model_scale',
               'is_save_all_outputs_ensemble',
               'is_append_ensemble_name',
               'chosen_audio_tool',
               'choose_algorithm',
               'time_stretch_rate',
               'pitch_rate',
               'is_primary_stem_only',
               'is_secondary_stem_only',
               'is_testing_audio',
               'is_add_model_name',
               "is_accept_any_input",
               'is_task_complete',
               'is_create_model_folder',
               'mp3_bit_set',
               'save_format',
               'wav_type_set',
               'user_code',
               'is_gpu_conversion',
               'is_normalization',
               'help_hints_var',
               'model_sample_mode',
               'model_sample_mode_duration')

# Message Box Text

INVALID_INPUT = translate('Invalid Input'), translate('The input is invalid.\n\nPlease verify the input still exists or is valid and try again.')
INVALID_EXPORT = translate('Invalid Export Directory'), translate('You have selected an invalid export directory.\n\nPlease make sure the selected directory still exists.')
INVALID_ENSEMBLE = translate('Not Enough Models'), translate('You must select 2 or more models to run ensemble.')
INVALID_MODEL = translate('No Model Chosen'), translate('You must select an model to continue.')
MISSING_MODEL = translate('Model Missing'), translate('The selected model is missing or not valid.')
ERROR_OCCURED = translate('Error Occured'), translate('\n\nWould you like to open the error log for more details?\n')

# GUI Text Constants

BACK_TO_MAIN_MENU = translate('Back to Main Menu')

# Help Hint Text
INTERNAL_MODEL_ATT = translate('Internal model attribute. \n\n ***Do not change this setting if you are unsure!***')
STOP_HELP = translate('Halts any running processes. \n A pop-up window will ask the user to confirm the action.')
SETTINGS_HELP = translate('Opens the main settings guide. This window includes the \"Download Center\"')
COMMAND_TEXT_HELP = translate('Provides information on the progress of the current process.')
SAVE_CURRENT_SETTINGS_HELP = translate(
    'Allows the user to open any saved settings or save the current application settings.')
CHUNKS_HELP = translate(
    'For MDX-Net, all values use the same amount of resources. Using chunks is no longer recommended.\n\n') + \
              translate('? This option is now only for output quality.\n') + \
              translate('? Some tracks may fare better depending on the value.\n') + \
              translate('? Some tracks may fare worse depending on the value.\n') + \
              translate('? Larger chunk sizes use will take less time to process.\n') + \
              translate('? Smaller chunk sizes use will take more time to process.\n')
CHUNKS_DEMUCS_HELP = translate('This option allows the user to reduce (or increase) RAM or V-RAM usage.\n\n') + \
                     translate(
                         '? Smaller chunk sizes use less RAM or V-RAM but can also increase processing times.\n') + \
                     translate('? Larger chunk sizes use more RAM or V-RAM but can also reduce processing times.\n') + \
                     translate(
                         '? Selecting \"Auto\" calculates an appropriate chuck size based on how much RAM or V-RAM your system has.\n') + \
                     translate('? Selecting \"Full\" will process the track as one whole chunk. (not recommended)\n') + \
                     translate('? The default selection is \"Auto\".')
MARGIN_HELP = translate(
    'Selects the frequency margins to slice the chunks from.\n\n? The recommended margin size is 44100.\n? Other values can give unpredictable results.')
AGGRESSION_SETTING_HELP = ('This option allows you to set how strong the primary stem extraction will be.\n\n') + \
                          translate('? The range is 0-100.\n') + \
                          translate('? Higher values perform deeper extractions.\n') + \
                          translate('? The default is 10 for instrumental & vocal models.\n') + \
                          translate(
                              '? Values over 10 can result in muddy-sounding instrumentals for the non-vocal models')
WINDOW_SIZE_HELP = translate(
    'The smaller your window size, the better your conversions will be. \nHowever, a smaller window means longer conversion times and heavier resource usage.\n\n') + \
                   translate('Breakdown of the selectable window size values:\n') + \
                   translate('? 1024 - Low conversion quality, shortest conversion time, low resource usage.\n') + \
                   translate('? 512 - Average conversion quality, average conversion time, normal resource usage.\n') + \
                   translate('? 320 - Better conversion quality.')
DEMUCS_STEMS_HELP = translate('Here, you can choose which stem to extract using the selected model.\n\n') + \
                    translate('Stem Selections:\n\n') + \
                    translate('? All Stems - Saves all of the stems the model is able to extract.\n') + \
                    translate('? Vocals - Pulls vocal stem only.\n') + \
                    translate('? Other - Pulls other stem only.\n') + \
                    translate('? Bass - Pulls bass stem only.\n') + \
                    translate('? Drums - Pulls drum stem only.\n')
SEGMENT_HELP = translate('This option allows the user to reduce (or increase) RAM or V-RAM usage.\n\n') + \
               translate('? Smaller segment sizes use less RAM or V-RAM but can also increase processing times.\n') + \
               translate('? Larger segment sizes use more RAM or V-RAM but can also reduce processing times.\n') + \
               translate('? Selecting \"Default\" uses the recommended segment size.\n') + \
               translate('? It is recommended that you not use segments with \"Chunking\".')
ENSEMBLE_MAIN_STEM_HELP = translate(
    'Allows the user to select the type of stems they wish to ensemble.\n\nOptions:\n\n') + \
                          translate(
                              f'? {VOCAL_PAIR} - The primary stem will be the vocals and the secondary stem will be the the instrumental\n') + \
                          translate(
                              f'? {OTHER_PAIR} - The primary stem will be other and the secondary stem will be no other (the mixture without the \'other\') stem)\n') + \
                          translate(
                              f'? {BASS_PAIR} - The primary stem will be bass and the secondary stem will be no bass (the mixture without the \'bass\') stem)\n') + \
                          translate(
                              f'? {DRUM_PAIR} - The primary stem will be drums and the secondary stem will be no drums (the mixture without the \'drums\') stem)\n') + \
                          translate(
                              f'? {FOUR_STEM_ENSEMBLE} - This option will gather all the 4 stem Demucs models and ensemble all of the outputs.\n')
ENSEMBLE_TYPE_HELP = translate(
    'Allows the user to select the ensemble algorithm to be used to generate the final output.\n\nExample & Other Note:\n\n') + \
                     translate(
                         f'? {MAX_MIN} - If this option is chosen, the primary stem outputs will be processed through \nthe \'Max Spec\') algorithm, and the secondary stem will be processed through the \'Min Spec\') algorithm.\n') + \
                     translate(
                         f'? Only a single algorithm will be shown when the \'4 Stem Ensemble\') option is chosen.\n\nAlgorithm Details:\n\n') + \
                     translate(
                         f'? {MAX_SPEC} - This algorithm combines the final results and generates the highest possible output from them.\nFor example, if this algorithm were processing vocal stems, you would get the fullest possible \n') + \
                     translate(
                         'result making the ensembled vocal stem sound cleaner. However, it might result in more unwanted artifacts.\n') + \
                     translate(
                         f'? {MIN_SPEC} - This algorithm combines the results and generates the lowest possible output from them.\nFor example, if this algorithm were processing instrumental stems, you would get the cleanest possible result \n') + \
                     translate(
                         'result, eliminating more unwanted artifacts. However, the result might also sound \'muddy\') and lack a fuller sound.\n') + \
                     translate(
                         f'? {AUDIO_AVERAGE} - This algorithm simply combines the results and averages all of them together. \n')
ENSEMBLE_LISTBOX_HELP = translate('List of the all the models available for the main stem pair selected.')
IS_GPU_CONVERSION_HELP = translate('When checked, the application will attempt to use your GPU (if you have one).\n') + \
                         translate(
                             'If you do not have a GPU but have this checked, the application will default to your CPU.\n\n') + \
                         translate('Note: CPU conversions are much slower than those processed through the GPU.')
SAVE_STEM_ONLY_HELP = translate('Allows the user to save only the selected stem.')
IS_NORMALIZATION_HELP = translate('Normalizes output to prevent clipping.')
CROP_SIZE_HELP = translate(
    '**Only compatible with select models only!**\n\n Setting should match training crop-size value. Leave as is if unsure.')
IS_TTA_HELP = ('This option performs Test-Time-Augmentation to improve the separation quality.\n\n') + \
              translate('Note: Having this selected will increase the time it takes to complete a conversion')
IS_POST_PROCESS_HELP = (
                           'This option can potentially identify leftover instrumental artifacts within the vocal outputs. \nThis option may improve the separation of some songs.\n\n') + \
                       translate(
                           'Note: Selecting this option can adversely affect the conversion process, depending on the track. Because of this, it is only recommended as a last resort.')
IS_HIGH_END_PROCESS_HELP = translate('The application will mirror the missing frequency range of the output.')
SHIFTS_HELP = translate('Performs multiple predictions with random shifts of the input and averages them.\n\n') + \
              translate(
                  '? The higher number of shifts, the longer the prediction will take. \n- Not recommended unless you have a GPU.')
OVERLAP_HELP = translate(
    'This option controls the amount of overlap between prediction windows (for Demucs one window is 10 seconds)')
IS_CHUNK_DEMUCS_HELP = translate(
    '? Enables \"Chunks\".\n? We recommend you not enable this option with \"Split Mode\" enabled or with the Demucs v4 Models.')
IS_CHUNK_MDX_NET_HELP = translate(
    '? Enables \"Chunks\".\n? Using this option for MDX-Net no longer effects RAM usage.\n? Having this enabled will effect output quality, for better or worse depending on the set value.')
IS_SPLIT_MODE_HELP = translate(
    '? Enables \"Segments\". \n? We recommend you not enable this option with \"Enable Chunks\".\n') + \
                     translate(
                         '? Deselecting this option is only recommended for those with powerful PCs or if using \"Chunk\" mode instead.')
IS_DEMUCS_COMBINE_STEMS_HELP = translate(
    'The application will create the secondary stem by combining the remaining stems \ninstead of inverting the primary stem with the mixture.')
COMPENSATE_HELP = translate('Compensates the audio of the primary stems to allow for a better secondary stem.')
IS_DENOISE_HELP = translate(
    '? This option removes a majority of the noise generated by the MDX-Net models.\n? The conversion will take nearly twice as long with this enabled.')
CLEAR_CACHE_HELP = translate('Clears any user selected model settings for previously unrecognized models.')
IS_SAVE_ALL_OUTPUTS_ENSEMBLE_HELP = translate(
    'Enabling this option will keep all indivudual outputs generated by an ensemble.')
IS_APPEND_ENSEMBLE_NAME_HELP = translate(
    'The application will append the ensemble name to the final output \nwhen this option is enabled.')
DONATE_HELP = translate('Takes the user to an external web-site to donate to this project!')
IS_INVERT_SPEC_HELP = translate(
    '? This option may produce a better secondary stem.\n? Inverts primary stem with mixture using spectragrams instead of wavforms.\n? This inversion method is slightly slower.')
IS_MIXER_MODE_HELP = translate(
    '? This option may improve separations for outputs from 4-stem models.\n? Might produce more noise.\n? This option might slow down separation time.')
IS_TESTING_AUDIO_HELP = translate(
    'Appends a unique 10 digit number to output files so the user \ncan compare results with different settings.')
IS_MODEL_TESTING_AUDIO_HELP = translate(
    'Appends the model name to output files so the user \ncan compare results with different settings.')
IS_ACCEPT_ANY_INPUT_HELP = translate(
    'The application will accept any input when enabled, even if it does not have an audio format extension.\n\nThis is for experimental purposes, and having it enabled is not recommended.')
IS_TASK_COMPLETE_HELP = translate('When enabled, chimes will be heard when a process completes or fails.')
IS_CREATE_MODEL_FOLDER_HELP = translate(
    'Two new directories will be generated for the outputs in \nthe export directory after each conversion.\n\n') + \
                              translate('? First directory - Named after the model.\n') + \
                              translate('? Second directory - Named after the track.\n\n') + \
                              translate('? Example: \n\n') + \
                              translate('─ Export Directory\n') + \
                              translate(')   └── First Directory\n') + \
                              translate(')           └── Second Directory\n') + \
                              translate(')                    └── Output File(s)')
DELETE_YOUR_SETTINGS_HELP = translate(
    'This menu contains your saved settings. You will be asked to \nconfirm if you wish to delete the selected setting.')
SET_STEM_NAME_HELP = translate('Choose the primary stem for the selected model.')
MDX_DIM_T_SET_HELP = INTERNAL_MODEL_ATT
MDX_DIM_F_SET_HELP = INTERNAL_MODEL_ATT
MDX_N_FFT_SCALE_SET_HELP = translate('Set the N_FFT size the model was trained with.')
POPUP_COMPENSATE_HELP = translate(
    f'Choose the appropriate voluem compensattion for the selected model\n\nReminder: {COMPENSATE_HELP}')
VR_MODEL_PARAM_HELP = translate('Choose the parameters needed to run the selected model.')
CHOSEN_ENSEMBLE_HELP = translate(
    'Select saved enselble or save current ensemble.\n\nDefault Selections:\n\n? Save the current ensemble.\n? Clears all current model selections.')
CHOSEN_PROCESS_METHOD_HELP = translate(
    'Here, you choose between different Al networks and algorithms to process your track.\n\n') + \
                             translate('There are five options:\n\n') + \
                             translate(
                                 '? VR Architecture - These models use magnitude spectrograms for Source Separation.\n') + \
                             translate(
                                 '? MDX-Net - These models use Hybrid Spectrogram/Waveform for Source Separation.\n') + \
                             translate(
                                 '? Demucs v3 - These models use Hybrid Spectrogram/Waveform for Source Separation.\n') + \
                             translate(
                                 '? Ensemble Mode - Here, you can get the best results from multiple models and networks.\n') + \
                             translate('? Audio Tools - These are additional tools for added convenience.')
INPUT_FOLDER_ENTRY_HELP = translate('Select Input:\n\nHere is where you select the audio files(s) you wish to process.')
INPUT_FOLDER_ENTRY_HELP_2 = translate('Input Option Menu:\n\nClick here to access the input option menu.')
OUTPUT_FOLDER_ENTRY_HELP = translate(
    'Select Output:\n\nHere is where you select the directory where your processed files are to be saved.')
INPUT_FOLDER_BUTTON_HELP = translate(
    'Open Input Folder Button: \n\nOpens the directory containing the selected input audio file(s).')
OUTPUT_FOLDER_BUTTON_HELP = translate('Open Output Folder Button: \n\nOpens the selected output folder.')
CHOOSE_MODEL_HELP = translate(
    'Each process method comes with its own set of options and models.\n\nHere is where you choose the model associated with the selected process method.')
FORMAT_SETTING_HELP = translate('Save outputs as ')
SECONDARY_MODEL_ACTIVATE_HELP = translate(
    'When enabled, the application will run an additional inference with the selected model(s) above.')
SECONDARY_MODEL_HELP = translate(
    'Choose the secondary model associated with this stem you wish to run with the current process method.')
SECONDARY_MODEL_SCALE_HELP = translate(
    'The scale determines how the final audio outputs will be averaged between the primary and secondary models.\n\nFor example:\n\n') + \
                             translate(
                                 '? 10% - 10 percent of the main model result will be factored into the final result.\n') + \
                             translate(
                                 '? 50% - The results from the main and secondary models will be averaged evenly.\n') + \
                             translate(
                                 '? 90% - 90 percent of the main model result will be factored into the final result.')
PRE_PROC_MODEL_ACTIVATE_HELP = translate(
    'The application will run an inference with the selected model above, pulling only the instrumental stem when enabled. \nFrom there, all of the non-vocal stems will be pulled from the generated instrumental.\n\nNotes:\n\n') + \
                               translate(
                                   '? This option can significantly reduce vocal bleed within the non-vocal stems.\n') + \
                               translate('? It is only available in Demucs.\n') + \
                               translate(
                                   '? It is only compatible with non-vocal and non-instrumental stem outputs.\n') + \
                               translate('? This will increase thetotal processing time.\n') + \
                               translate('? Only VR and MDX-Net Vocal or Instrumental models are selectable above.')

AUDIO_TOOLS_HELP = translate('Here, you choose between different audio tools to process your track.\n\n') + \
                   translate(
                       '? Manual Ensemble - You must have 2 or more files selected as your inputs. Allows the user to run their tracks through \nthe same algorithms used in Ensemble Mode.\n') + \
                   translate(
                       '? Align Inputs - You must have exactly 2 files selected as your inputs. The second input will be aligned with the first input.\n') + \
                   translate('? Time Stretch - The user can speed up or slow down the selected inputs.\n') + \
                   translate('? Change Pitch - The user can change the pitch for the selected inputs.\n')
PRE_PROC_MODEL_INST_MIX_HELP = translate(
    'When enabled, the application will generate a third output without the selected stem and vocals.')
MODEL_SAMPLE_MODE_HELP = translate(
    'Allows the user to process only part of a track to sample settings or a model without \nrunning a full conversion.\n\nNotes:\n\n') + \
                         translate(
                             '? The number in the parentheses is the current number of seconds the generated sample will be.\n') + \
                         translate(
                             '? You can choose the number of seconds to extract from the track in the \"Additional Settings\" menu.')

POST_PROCESS_THREASHOLD_HELP = translate(
    'Allows the user to control the intensity of the Post_process option.\n\nNotes:\n\n') + \
                               translate(translate(
                                   '? Higher values potentially remove more artifacts. However, bleed might increase.\n') + \
                                         '? Lower values limit artifact removal.')

BATCH_SIZE_HELP = translate('Specify the number of batches to be processed at a time.\n\nNotes:\n\n') + \
                  translate('? Higher values mean more RAM usage but slightly faster processing times.\n') + \
                  translate('? Lower values mean less RAM usage but slightly longer processing times.\n') + \
                  translate('? Batch size value has no effect on output quality.')

# Warning Messages

STORAGE_ERROR = translate('Insufficient Storage'),translate('There is not enough storage on main drive to continue. Your main drive must have at least 3 GB\'s of storage in order for this application function properly. \n\nPlease ensure your main drive has at least 3 GB\'s of storage and try again.\n\n')
STORAGE_WARNING = translate('Available Storage Low'),translate('Your main drive is running low on storage. Your main drive must have at least 3 GB\'s of storage in order for this application function properly.\n\n')
CONFIRM_WARNING = translate('\nAre you sure you wish to continue?')
PROCESS_FAILED = translate('Process failed, please see error log\n')
EXIT_PROCESS_ERROR = translate('Active Process'),translate('Please stop the active process or wait for it to complete before you exit.')
EXIT_HALTED_PROCESS_ERROR = translate('Halting Process'),translate('Please wait for the application to finish halting the process before exiting.')
EXIT_DOWNLOAD_ERROR = translate('Active Download'),translate('Please stop the download or wait for it to complete before you exit.')
SET_TO_DEFAULT_PROCESS_ERROR = translate('Active Process'),translate('You cannot reset all of the application settings during an active process.')
SET_TO_ANY_PROCESS_ERROR = translate('Active Process'),translate('You cannot reset the application settings during an active process.')
RESET_ALL_TO_DEFAULT_WARNING = translate('Reset Settings Confirmation'),translate('All application settings will be set to factory default.\n\nAre you sure you wish to continue?')
AUDIO_VERIFICATION_CHECK = lambda i, e: translate(f'++++++++++++++++++++++++++++++++++++++++++++++++++++\n\nBroken File Removed: \n\n{i}\n\nError Details:\n\n{e}\n++++++++++++++++++++++++++++++++++++++++++++++++++++')
INVALID_ONNX_MODEL_ERROR = translate('Invalid Model'),translate('The file selected is not a valid MDX-Net model. Please see the error log for more information.')

# Separation Text

LOADING_MODEL = translate('Loading model...')
INFERENCE_STEP_1 = translate('Running inference...')
INFERENCE_STEP_1_SEC = translate('Running inference (secondary model)...')
INFERENCE_STEP_1_4_STEM = lambda stem: translate(f'Running inference (secondary model for {stem})...')
INFERENCE_STEP_1_PRE = translate('Running inference (pre-process model)...')
INFERENCE_STEP_2_PRE = lambda pm, m: translate(f'Loading pre-process model ({pm}: {m})...')
INFERENCE_STEP_2_SEC = lambda pm, m: translate(f'Loading secondary model ({pm}: {m})...')
INFERENCE_STEP_2_SEC_CACHED_MODOEL = lambda pm, m: translate(f'Secondary model ({pm}: {m}) cache loaded.\n')
INFERENCE_STEP_2_PRE_CACHED_MODOEL = lambda pm, m: translate(f'Pre-process model ({pm}: {m}) cache loaded.\n')
INFERENCE_STEP_2_SEC_CACHED = translate('Loading cached secondary model source(s)... Done!\n')
INFERENCE_STEP_2_PRIMARY_CACHED = translate('Model cache loaded.\n')
INFERENCE_STEP_2 = translate('Inference complete.')
SAVING_STEM = translate('Saving stem...')
SAVING_ALL_STEMS = translate('Saving all stems...')
ENSEMBLING_OUTPUTS = translate('Ensembling outputs...')
DONE = translate('Done!\n')
ENSEMBLES_SAVED = translate('Ensembled outputs saved!\n\n')
DONE = translate(' Done!\n')
ENSEMBLES_SAVED = translate('Ensembled outputs saved!\n\n')
NEW_LINES = "\n\n"
NEW_LINE = "\n"
NO_LINE = ''

# Widget Placements

MAIN_ROW_Y = -15, -17
MAIN_ROW_X = -4, 21
MAIN_ROW_WIDTH = -53
MAIN_ROW_2_Y = -15, -17
MAIN_ROW_2_X = -28, 1
CHECK_BOX_Y = 0
CHECK_BOX_X = 20
CHECK_BOX_WIDTH = -50
CHECK_BOX_HEIGHT = 2
LEFT_ROW_WIDTH = -10
LABEL_HEIGHT = -5
OPTION_HEIGHT = 7
LOW_MENU_Y = 18, 16
FFMPEG_EXT = (".aac", ".aiff", ".alac" ,".flac", ".FLAC", ".mov", ".mp4", ".MP4", 
              ".m4a", ".M4A", ".mp2", ".mp3", "MP3", ".mpc", ".mpc8", 
              ".mpeg", ".ogg", ".OGG", ".tta", ".wav", ".wave", ".WAV", ".WAVE", ".wma", ".webm", ".eac3", ".mkv")

FFMPEG_MORE_EXT = (".aa", ".aac", ".ac3", ".aiff", ".alac", ".avi", ".f4v",".flac", ".flic", ".flv",
              ".m4v",".mlv", ".mov", ".mp4", ".m4a", ".mp2", ".mp3", ".mp4", ".mpc", ".mpc8", 
              ".mpeg", ".ogg", ".tta", ".tty", ".vcd", ".wav", ".wma")
ANY_EXT = ""

# Secondary Menu Constants

VOCAL_PAIR_PLACEMENT = 1, 2, 3, 4
OTHER_PAIR_PLACEMENT = 5, 6, 7, 8
BASS_PAIR_PLACEMENT = 9, 10, 11, 12
DRUMS_PAIR_PLACEMENT = 13, 14, 15, 16

# Drag n Drop String Checks

DOUBLE_BRACKET = "} {"
RIGHT_BRACKET = "}"
LEFT_BRACKET = "{"

# Manual Downloads

VR_PLACEMENT_TEXT = 'Place models in \"models/VR_Models\" directory.'
MDX_PLACEMENT_TEXT = 'Place models in \"models/MDX_Net_Models\" directory.'
DEMUCS_PLACEMENT_TEXT = 'Place models in \"models/Demucs_Models\" directory.'
DEMUCS_V3_V4_PLACEMENT_TEXT = 'Place items in \"models/Demucs_Models/v3_v4_repo\" directory.'

FULL_DOWNLOAD_LIST_VR = {
                    "VR Arch Single Model v5: 1_HP-UVR": "1_HP-UVR.pth",
                    "VR Arch Single Model v5: 2_HP-UVR": "2_HP-UVR.pth",
                    "VR Arch Single Model v5: 3_HP-Vocal-UVR": "3_HP-Vocal-UVR.pth",
                    "VR Arch Single Model v5: 4_HP-Vocal-UVR": "4_HP-Vocal-UVR.pth",
                    "VR Arch Single Model v5: 5_HP-Karaoke-UVR": "5_HP-Karaoke-UVR.pth",
                    "VR Arch Single Model v5: 6_HP-Karaoke-UVR": "6_HP-Karaoke-UVR.pth",
                    "VR Arch Single Model v5: 7_HP2-UVR": "7_HP2-UVR.pth",
                    "VR Arch Single Model v5: 8_HP2-UVR": "8_HP2-UVR.pth",
                    "VR Arch Single Model v5: 9_HP2-UVR": "9_HP2-UVR.pth",
                    "VR Arch Single Model v5: 10_SP-UVR-2B-32000-1": "10_SP-UVR-2B-32000-1.pth",
                    "VR Arch Single Model v5: 11_SP-UVR-2B-32000-2": "11_SP-UVR-2B-32000-2.pth",
                    "VR Arch Single Model v5: 12_SP-UVR-3B-44100": "12_SP-UVR-3B-44100.pth",
                    "VR Arch Single Model v5: 13_SP-UVR-4B-44100-1": "13_SP-UVR-4B-44100-1.pth",
                    "VR Arch Single Model v5: 14_SP-UVR-4B-44100-2": "14_SP-UVR-4B-44100-2.pth",
                    "VR Arch Single Model v5: 15_SP-UVR-MID-44100-1": "15_SP-UVR-MID-44100-1.pth",
                    "VR Arch Single Model v5: 16_SP-UVR-MID-44100-2": "16_SP-UVR-MID-44100-2.pth",
                    "VR Arch Single Model v4: MGM_HIGHEND_v4": "MGM_HIGHEND_v4.pth",
                    "VR Arch Single Model v4: MGM_LOWEND_A_v4": "MGM_LOWEND_A_v4.pth",
                    "VR Arch Single Model v4: MGM_LOWEND_B_v4": "MGM_LOWEND_B_v4.pth",
                    "VR Arch Single Model v4: MGM_MAIN_v4": "MGM_MAIN_v4.pth"
                  }

FULL_DOWNLOAD_LIST_MDX = {
                    "MDX-Net Model: UVR-MDX-NET Main": "UVR_MDXNET_Main.onnx",
                    "MDX-Net Model: UVR-MDX-NET Inst Main": "UVR-MDX-NET-Inst_Main.onnx",
                    "MDX-Net Model: UVR-MDX-NET 1": "UVR_MDXNET_1_9703.onnx",
                    "MDX-Net Model: UVR-MDX-NET 2": "UVR_MDXNET_2_9682.onnx",
                    "MDX-Net Model: UVR-MDX-NET 3": "UVR_MDXNET_3_9662.onnx",
                    "MDX-Net Model: UVR-MDX-NET Inst 1": "UVR-MDX-NET-Inst_1.onnx",
                    "MDX-Net Model: UVR-MDX-NET Inst 2": "UVR-MDX-NET-Inst_2.onnx",
                    "MDX-Net Model: UVR-MDX-NET Inst 3": "UVR-MDX-NET-Inst_3.onnx",
                    "MDX-Net Model: UVR-MDX-NET Karaoke": "UVR_MDXNET_KARA.onnx",
                    "MDX-Net Model: UVR_MDXNET_9482": "UVR_MDXNET_9482.onnx",
                    "MDX-Net Model: Kim_Vocal_1": "Kim_Vocal_1.onnx",
                    "MDX-Net Model: kuielab_a_vocals": "kuielab_a_vocals.onnx",
                    "MDX-Net Model: kuielab_a_other": "kuielab_a_other.onnx",
                    "MDX-Net Model: kuielab_a_bass": "kuielab_a_bass.onnx",
                    "MDX-Net Model: kuielab_a_drums": "kuielab_a_drums.onnx",
                    "MDX-Net Model: kuielab_b_vocals": "kuielab_b_vocals.onnx",
                    "MDX-Net Model: kuielab_b_other": "kuielab_b_other.onnx",
                    "MDX-Net Model: kuielab_b_bass": "kuielab_b_bass.onnx",
                    "MDX-Net Model: kuielab_b_drums": "kuielab_b_drums.onnx"}
                    
FULL_DOWNLOAD_LIST_DEMUCS = {
                    
	                "Demucs v4: htdemucs_ft":{
	                                "f7e0c4bc-ba3fe64a.th":"https://dl.fbaipublicfiles.com/demucs/hybrid_transformer/f7e0c4bc-ba3fe64a.th",
	                                "d12395a8-e57c48e6.th":"https://dl.fbaipublicfiles.com/demucs/hybrid_transformer/d12395a8-e57c48e6.th",
	                                "92cfc3b6-ef3bcb9c.th":"https://dl.fbaipublicfiles.com/demucs/hybrid_transformer/92cfc3b6-ef3bcb9c.th",
	                                "04573f0d-f3cf25b2.th":"https://dl.fbaipublicfiles.com/demucs/hybrid_transformer/04573f0d-f3cf25b2.th",
	                                "htdemucs_ft.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/htdemucs_ft.yaml"
	                                },

	                "Demucs v4: htdemucs":{
	                                "955717e8-8726e21a.th": "https://dl.fbaipublicfiles.com/demucs/hybrid_transformer/955717e8-8726e21a.th",
	                                "htdemucs.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/htdemucs.yaml"
	                                },

	                "Demucs v4: hdemucs_mmi":{
	                                "75fc33f5-1941ce65.th": "https://dl.fbaipublicfiles.com/demucs/hybrid_transformer/75fc33f5-1941ce65.th",
	                                "hdemucs_mmi.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/hdemucs_mmi.yaml"
	                                },
	                "Demucs v4: htdemucs_6s":{
	                                "5c90dfd2-34c22ccb.th": "https://dl.fbaipublicfiles.com/demucs/hybrid_transformer/5c90dfd2-34c22ccb.th",
	                                "htdemucs_6s.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/htdemucs_6s.yaml"
	                                },
	                "Demucs v3: mdx":{
	                                "0d19c1c6-0f06f20e.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/0d19c1c6-0f06f20e.th", 
	                                "7ecf8ec1-70f50cc9.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/7ecf8ec1-70f50cc9.th",
	                                "c511e2ab-fe698775.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/c511e2ab-fe698775.th",
	                                "7d865c68-3d5dd56b.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/7d865c68-3d5dd56b.th",
	                                "mdx.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/mdx.yaml"
	                                },
	                
	                "Demucs v3: mdx_q":{
	                                "6b9c2ca1-3fd82607.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/6b9c2ca1-3fd82607.th",
	                                "b72baf4e-8778635e.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/b72baf4e-8778635e.th",
	                                "42e558d4-196e0e1b.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/42e558d4-196e0e1b.th",
	                                "305bc58f-18378783.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/305bc58f-18378783.th",
	                                "mdx_q.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/mdx_q.yaml"
	                                },
	                
	                "Demucs v3: mdx_extra":{
	                                "e51eebcc-c1b80bdd.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/e51eebcc-c1b80bdd.th",
	                                "a1d90b5c-ae9d2452.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/a1d90b5c-ae9d2452.th",
	                                "5d2d6c55-db83574e.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/5d2d6c55-db83574e.th",
	                                "cfa93e08-61801ae1.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/cfa93e08-61801ae1.th",
	                                "mdx_extra.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/mdx_extra.yaml"
	                                },
	                
	                "Demucs v3: mdx_extra_q": {
	                                "83fc094f-4a16d450.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/83fc094f-4a16d450.th",
	                                "464b36d7-e5a9386e.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/464b36d7-e5a9386e.th",
	                                "14fc6a69-a89dd0ee.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/14fc6a69-a89dd0ee.th",
	                                "7fd6ef75-a905dd85.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/7fd6ef75-a905dd85.th",
	                                "mdx_extra_q.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/mdx_extra_q.yaml"
	                                },
	                
	                "Demucs v3: UVR Model":{
	                                "ebf34a2db.th": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/ebf34a2db.th",
	                                "UVR_Demucs_Model_1.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/UVR_Demucs_Model_1.yaml"
	                                },

	                "Demucs v3: repro_mdx_a":{
	                                "9a6b4851-03af0aa6.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/9a6b4851-03af0aa6.th", 
	                                "1ef250f1-592467ce.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/1ef250f1-592467ce.th",
	                                "fa0cb7f9-100d8bf4.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/fa0cb7f9-100d8bf4.th",
	                                "902315c2-b39ce9c9.th": "https://dl.fbaipublicfiles.com/demucs/mdx_final/902315c2-b39ce9c9.th",
	                                "repro_mdx_a.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/repro_mdx_a.yaml"
	                                },

	                "Demucs v3: repro_mdx_a_time_only":{
	                                "9a6b4851-03af0aa6.th":"https://dl.fbaipublicfiles.com/demucs/mdx_final/9a6b4851-03af0aa6.th",
	                                "1ef250f1-592467ce.th":"https://dl.fbaipublicfiles.com/demucs/mdx_final/1ef250f1-592467ce.th",
	                                "repro_mdx_a_time_only.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/repro_mdx_a_time_only.yaml"
	                                },

	                "Demucs v3: repro_mdx_a_hybrid_only":{
	                                "fa0cb7f9-100d8bf4.th":"https://dl.fbaipublicfiles.com/demucs/mdx_final/fa0cb7f9-100d8bf4.th",
	                                "902315c2-b39ce9c9.th":"https://dl.fbaipublicfiles.com/demucs/mdx_final/902315c2-b39ce9c9.th",
	                                "repro_mdx_a_hybrid_only.yaml": "https://github.com/TRvlvr/model_repo/releases/download/all_public_uvr_models/repro_mdx_a_hybrid_only.yaml"
	                                },

	                "Demucs v2: demucs": {
	                                "demucs-e07c671f.th": "https://dl.fbaipublicfiles.com/demucs/v3.0/demucs-e07c671f.th"
	                                },

	                "Demucs v2: demucs_extra": {
	                                "demucs_extra-3646af93.th":"https://dl.fbaipublicfiles.com/demucs/v3.0/demucs_extra-3646af93.th"
	                                },

	                "Demucs v2: demucs48_hq": {
	                                "demucs48_hq-28a1282c.th":"https://dl.fbaipublicfiles.com/demucs/v3.0/demucs48_hq-28a1282c.th"
	                                },

	                "Demucs v2: tasnet": {
	                                "tasnet-beb46fac.th":"https://dl.fbaipublicfiles.com/demucs/v3.0/tasnet-beb46fac.th"
	                                },

	                "Demucs v2: tasnet_extra": {
	                                "tasnet_extra-df3777b2.th":"https://dl.fbaipublicfiles.com/demucs/v3.0/tasnet_extra-df3777b2.th"
	                                },
	                                
	                "Demucs v2: demucs_unittest": {
	                                "demucs_unittest-09ebc15f.th":"https://dl.fbaipublicfiles.com/demucs/v3.0/demucs_unittest-09ebc15f.th"
	                                },

	                "Demucs v1: demucs": {
	                                "demucs.th":"https://dl.fbaipublicfiles.com/demucs/v2.0/demucs.th"
	                                },

	                "Demucs v1: demucs_extra": {
	                                "demucs_extra.th":"https://dl.fbaipublicfiles.com/demucs/v2.0/demucs_extra.th"
	                                },

	                "Demucs v1: light": {
	                                "light.th":"https://dl.fbaipublicfiles.com/demucs/v2.0/light.th"
	                                },

	                "Demucs v1: light_extra": {
	                                "light_extra.th":"https://dl.fbaipublicfiles.com/demucs/v2.0/light_extra.th"
	                                },

	                "Demucs v1: tasnet": {
	                                "tasnet.th":"https://dl.fbaipublicfiles.com/demucs/v2.0/tasnet.th"
	                                },
	                                
	                "Demucs v1: tasnet_extra": {
	                                "tasnet_extra.th":"https://dl.fbaipublicfiles.com/demucs/v2.0/tasnet_extra.th"
	                                }
                }

# Main Menu Labels

CHOOSE_PROC_METHOD_MAIN_LABEL = translate('CHOOSE PROCESS METHOD')
SELECT_SAVED_SETTINGS_MAIN_LABEL = translate('SELECT SAVED SETTINGS')
CHOOSE_MDX_MODEL_MAIN_LABEL = translate('CHOOSE MDX-NET MODEL')
BATCHES_MDX_MAIN_LABEL = translate('BATCH SIZE')
VOL_COMP_MDX_MAIN_LABEL = translate('VOLUME COMPENSATION')
SELECT_VR_MODEL_MAIN_LABEL = translate('CHOOSE VR MODEL')
AGGRESSION_SETTING_MAIN_LABEL = translate('AGGRESSION SETTING')
WINDOW_SIZE_MAIN_LABEL = translate('WINDOW SIZE')
CHOOSE_DEMUCS_MODEL_MAIN_LABEL = translate('CHOOSE DEMUCS MODEL')
CHOOSE_DEMUCS_STEMS_MAIN_LABEL = translate('CHOOSE STEM(S)')
CHOOSE_SEGMENT_MAIN_LABEL =translate( 'SEGMENT')
ENSEMBLE_OPTIONS_MAIN_LABEL = translate('ENSEMBLE OPTIONS')
CHOOSE_MAIN_PAIR_MAIN_LABEL = translate('MAIN STEM PAIR')
CHOOSE_ENSEMBLE_ALGORITHM_MAIN_LABEL =translate( 'ENSEMBLE ALGORITHM')
AVAILABLE_MODELS_MAIN_LABEL = translate('AVAILABLE MODELS')
CHOOSE_AUDIO_TOOLS_MAIN_LABEL =translate( 'CHOOSE AUDIO TOOL')
CHOOSE_MANUAL_ALGORITHM_MAIN_LABEL = translate('CHOOSE ALGORITHM')
CHOOSE_RATE_MAIN_LABEL = translate('RATE')
CHOOSE_SEMITONES_MAIN_LABEL = translate('SEMITONES')
GPU_CONVERSION_MAIN_LABEL =translate( 'GPU Conversion')

if OPERATING_SYSTEM=="Darwin":
   LICENSE_OS_SPECIFIC_TEXT = translate('• This application is intended for those running macOS Catalina and above.\n') +\
                              translate('• Application functionality for systems running macOS Mojave or lower is not guaranteed.\n') +\
                              translate('• Application functionality for older or budget Mac systems is not guaranteed.\n\n')
   FONT_SIZE_F1 = 13
   FONT_SIZE_F2 = 11
   FONT_SIZE_F3 = 12
   FONT_SIZE_0 = 9
   FONT_SIZE_1 = 11
   FONT_SIZE_2 = 12
   FONT_SIZE_3 = 13
   FONT_SIZE_4 = 14
   FONT_SIZE_5 = 15
   FONT_SIZE_6 = 17
   HELP_HINT_CHECKBOX_WIDTH = 13
   MDX_CHECKBOXS_WIDTH = 14
   VR_CHECKBOXS_WIDTH = 14
   ENSEMBLE_CHECKBOXS_WIDTH = 18
   DEMUCS_CHECKBOXS_WIDTH = 14
   DEMUCS_PRE_CHECKBOXS_WIDTH = 20
   GEN_SETTINGS_WIDTH = 17
   MENU_COMBOBOX_WIDTH = 16

elif OPERATING_SYSTEM=="Linux":
   LICENSE_OS_SPECIFIC_TEXT = translate('• This application is intended for those running Linux Ubuntu 18.04+.\n') +\
                              translate('• Application functionality for systems running other Linux platforms is not guaranteed.\n' )+\
                              translate('• Application functionality for older or budget systems is not guaranteed.\n\n')
   FONT_SIZE_F1 = 10
   FONT_SIZE_F2 = 8
   FONT_SIZE_F3 = 9
   FONT_SIZE_0 = 7
   FONT_SIZE_1 = 8
   FONT_SIZE_2 = 9
   FONT_SIZE_3 = 10
   FONT_SIZE_4 = 11
   FONT_SIZE_5 = 12
   FONT_SIZE_6 = 15
   HELP_HINT_CHECKBOX_WIDTH = 13
   MDX_CHECKBOXS_WIDTH = 14
   VR_CHECKBOXS_WIDTH = 16
   ENSEMBLE_CHECKBOXS_WIDTH = 25
   DEMUCS_CHECKBOXS_WIDTH = 18
   DEMUCS_PRE_CHECKBOXS_WIDTH = 27
   GEN_SETTINGS_WIDTH = 17
   MENU_COMBOBOX_WIDTH = 19
    
elif OPERATING_SYSTEM=="Windows":
   LICENSE_OS_SPECIFIC_TEXT = translate('• This application is intended for those running Windows 10 or higher.\n') +\
                              translate('• Application functionality for systems running Windows 7 or lower is not guaranteed.\n') +\
                              translate('• Application functionality for Intel Pentium & Celeron CPUs systems is not guaranteed.\n\n')
   FONT_SIZE_F1 = 10
   FONT_SIZE_F2 = 8
   FONT_SIZE_F3 = 9
   FONT_SIZE_0 = 7
   FONT_SIZE_1 = 8
   FONT_SIZE_2 = 9
   FONT_SIZE_3 = 10
   FONT_SIZE_4 = 11
   FONT_SIZE_5 = 12
   FONT_SIZE_6 = 15
   HELP_HINT_CHECKBOX_WIDTH = 16
   MDX_CHECKBOXS_WIDTH = 16
   VR_CHECKBOXS_WIDTH = 16
   ENSEMBLE_CHECKBOXS_WIDTH = 25
   DEMUCS_CHECKBOXS_WIDTH = 18
   DEMUCS_PRE_CHECKBOXS_WIDTH = 27
   GEN_SETTINGS_WIDTH = 23
   MENU_COMBOBOX_WIDTH = 19


LICENSE_TEXT = lambda a, p:translate(f'Current Application Version: Ultimate Vocal Remover {a}\n' )+\
               translate(f'Current Patch Version: {p}\n\n') +\
               translate('Copyright (c) 2022 Ultimate Vocal Remover\n\n') +\
               translate('UVR is free and open-source, but MIT licensed. Please credit us if you use our\n') +\
               translate(f'models or code for projects unrelated to UVR.\n\n{LICENSE_OS_SPECIFIC_TEXT}') +\
               translate('This bundle contains the UVR interface, Python, PyTorch, and other\n' )+\
               translate('dependencies needed to run the application effectively.\n\n') +\
               translate('Website Links: This application, System or Service(s) may contain links to\n' )+\
               translate('other websites and downloads, and they are solely provided to you as an\n') +\
               translate('additional convenience. You understand and acknowledge that by clicking\n' )+\
               translate('or activating such links you are accessing a site or service outside of\n' )+\
               translate('this application, and that we do not screen, review, approve, or otherwise\n') +\
               translate('endorse any content or information contained in these linked websites.\n') +\
               translate('You acknowledge and agree that we, our affiliates and partners are not\n' )+\
               translate('responsible for the contents of any of these linked websites, including\n' )+\
               translate('the accuracy or availability of information provided by the linked websites,\n') +\
               translate('and we make no representations or warranties regarding your use of\n' )+\
               translate('the linked websites.\n\n' )+\
               translate('This application is MIT Licensed\n\n' )+\
               translate('Permission is hereby granted, free of charge, to any person obtaining a copy\n') +\
               translate('of this software and associated documentation files (the "Software"), to deal\n' )+\
               translate('in the Software without restriction, including without limitation the rights\n' )+\
               translate('to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n') +\
               translate('copies of the Software, and to permit persons to whom the Software is\n') +\
               translate('furnished to do so, subject to the following conditions:\n\n') +\
               translate('The above copyright notice and this permission notice shall be included in all\n' )+\
               translate('copies or substantial portions of the Software.\n\n') +\
               translate('THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n' )+\
               translate('IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n') +\
               translate('FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n') +\
               translate('AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n' )+\
               translate('LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n' )+\
               translate('OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n' )+\
               translate('SOFTWARE.')

CHANGE_LOG_HEADER = lambda patch:translate(f"Patch Version:\n\n{patch}")

#DND CONSTS

MAC_DND_CHECK = ('/Users/',
                 '/Applications/',
                 '/Library/',
                 '/System/')
LINUX_DND_CHECK = ('/home/',
                   '/usr/')
WINDOWS_DND_CHECK = ('A:', 'B:', 'C:', 'D:', 'E:', 'F:', 'G:', 'H:', 'I:', 'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:', 'V:', 'W:', 'X:', 'Y:', 'Z:')

WOOD_INST_MODEL_HASH = '0ec76fd9e65f81d8b4fbd13af4826ed8'
WOOD_INST_PARAMS = {
    "vr_model_param": "4band_v3",
    "primary_stem": NO_WIND_INST_STEM
                     }
