from time import gmtime, sleep

# PARAMETERS

frame_input = 'ETH' # the string to use as input

frame_repeats_per_line = 7  # number of times the frame is printed per line

lines_printed_per_second = 5  # number of lines printed per second

# /PARAMETERS

####################################################################################################

# CODE

length_of_frame_input = len(frame_input)
last_char = frame_input[-1]
frame_input = frame_input[:-1]

def per_second_output():
    seconds = gmtime().tm_sec

    frame_index = seconds % length_of_frame_input
    
    last_char_position = length_of_frame_input - frame_index - 1
    
    line = ''.join((
        frame_input[:last_char_position],
        
        last_char,
        
        frame_input[last_char_position:]
        
    )) * frame_repeats_per_line
    
    print(
        '\n'.join(
            (line,) * lines_printed_per_second
        )
    )

        
if __name__ == '__main__':
    while True:
        per_second_output()
        sleep(1)

# /CODE
    
    
    
