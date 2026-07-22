class GameVars: # Singleton class for game-related variables
    def __init__():
        raise NotImplementedError("GameVars Class is for holding Game-related variables only -- objects of this class should not be instantiated")
    
    # Frame Timers -- Maximum and Current

    are = 0 # Piece entry delay in frames
    line_are = 2 # Time for next piece to appear after line clear animation is complete
    das = 1 # Delayed Auto-Shift in frames
    lock_delay = 30 # Lock Delay in frames -- time a piece can remain on the ground before it locks into place
    line_clear = 2 # Time in frames it takes for the line clear animation to complete

    invis_mode = False # Invisible Mode
    bone_blocks = False # TODO: Implement custom block texture images 

