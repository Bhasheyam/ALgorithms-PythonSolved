def searchInsert(A, B):
    n = len(A) // 2
   
    if ( A[ n ] > B):
        while( n > 0 ):
            if A[n - 1] == B:
                return n-1
            elif(A[n - 1] < B):
                return n
            n -= 1
        return 0
                
    else:
        while( n < len(A) ):
            if A[n] == B:
                return n
            elif(A[n] > B):
                return n
            n += 1
        return len(A)

    

print searchInsert([ 2, 4, 5, 21, 26, 28, 29, 35, 38, 42, 46, 47, 48, 56, 57, 59, 60, 68, 72, 78, 81, 84, 85, 86, 95, 99, 103, 107, 108, 113, 115, 118, 122, 127, 135, 136, 137, 143, 144, 148, 149, 150, 156, 157, 169, 171, 173, 175, 177, 178, 185, 187, 191, 193, 195, 196, 197, 202, 205, 206, 208, 209, 210, 211, 215, 217, 220, 222, 229, 234, 236, 243, 246, 251, 252, 253, 255, 256, 257, 262, 263, 266, 267, 268, 269, 273, 289, 296, 297, 299, 303, 312, 314, 317, 319, 324, 327, 329, 330, 332, 336, 349, 351, 352, 353, 355, 363, 365, 369, 373, 375, 377, 381, 382, 383, 384, 388, 390, 392, 395, 397, 400, 403, 408, 413, 414, 417, 418, 428, 437, 438, 440, 448, 451, 452, 454, 455, 457, 458, 459, 460, 467, 470, 475, 477, 482, 486, 489, 490, 495, 497, 498, 499, 504, 506, 508, 509, 516, 517, 519, 522, 526, 531, 532, 538, 553, 566, 567, 576, 578, 581, 583, 587, 588, 589, 591, 604, 609, 613, 614, 616, 619, 621, 624, 627, 630, 631, 634, 637, 640, 642, 654, 657, 661, 662, 664, 665, 668, 670, 671, 677, 681, 683, 684, 685, 688, 693, 694, 699, 701, 702, 705, 708, 712, 714, 720, 722, 723, 725, 727, 752, 754, 757, 761, 763, 764, 771, 772, 776, 777, 782, 784, 789, 793, 794, 795, 801, 806, 815, 817, 824, 831, 840, 842, 844, 846, 847, 850, 863, 864, 874, 875, 878, 879, 883, 887, 889, 893, 896, 898, 901, 902, 903, 904, 912, 917, 919, 920, 923, 925, 931, 933, 936, 940, 943, 945, 946, 947, 950, 953, 957, 958, 961, 964, 966, 970, 973, 974, 975, 976, 983, 985, 988, 994, 997, 999, 1001 ], 40)