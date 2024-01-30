import dijkstraLogic
'''
weights = {(1, 2): 10, (2, 1): 10, (1, 3): 20, (3, 1): 20, (1, 4): 50, (4, 1): 50, (2, 6): 60, (6, 2): 60, (3, 6): 40, (6, 3): 40, (4, 5): 1, (5, 4): 1, (5, 6): 5, (6, 5): 5}

distances, parents = dijkstraLogic.dijkstra(weights, start=1)
print(distances, parents)
assert distances == {1: 0, 2: 10, 3: 20, 4: 50, 5: 51, 6: 56}
assert parents == {1: None, 2: 1, 3: 1, 4: 1, 5: 4, 6: 5}'''

weights = {(0, 1): 60, (1, 0): 60, (0, 2): 90, (2, 0): 90, (0, 4): 40, (4, 0): 40, (1, 6): 50, (6, 1): 50, (2, 3): 30, (3, 2): 30, (3, 5): 20, (5, 3): 20, (3, 6): 15, (6, 3): 15, (4, 5): 100, (5, 4): 100}
distances, parents = dijkstraLogic.dijkstra(weights, start=0)
print(distances, parents)
assert distances == {0: 0, 4: 40, 1: 60, 2: 90, 6: 110, 3: 120, 5: 140}
assert parents == {0: None, 4: 0, 1: 0, 2: 0, 6: 1, 3: 2, 5: 3}


'''
weights = {(0, 1): 497, (0, 20): 171, (1, 2): 57, (1, 21): 595, (2, 3): 378, (2, 22): 593, (3, 4): 211, (3, 23): 418, (4, 5): 110, (4, 24): 538, (5, 6): 527, (5, 25): 564, (6, 7): 436, (6, 26): 401, (7, 8): 25, (7, 27): 200, (8, 9): 539, (8, 28): 585, (9, 10): 105, (9, 29): 308, (10, 11): 24, (10, 30): 205, (11, 12): 154, (11, 31): 479, (12, 13): 111, (12, 32): 36, (13, 14): 180, (13, 33): 421, (14, 15): 263, (14, 34): 297, (15, 16): 279, (15, 35): 0, (16, 17): 294, (16, 36): 150, (17, 18): 336, (17, 37): 571, (18, 19): 474, (18, 38): 410, (19, 39): 426, (20, 21): 373, (20, 40): 380, (21, 22): 313, (21, 41): 194, (22, 23): 99, (22, 42): 13, (23, 24): 241, (23, 43): 123, (24, 25): 550, (24, 44): 188, (25, 26): 520, (25, 45): 334, (26, 27): 571, (26, 46): 88, (27, 28): 163, (27, 47): 434, (28, 29): 215, (28, 48): 449, (29, 30): 464, (29, 49): 304, (30, 31): 418, (30, 50): 450, (31, 32): 415, (31, 51): 495, (32, 33): 311, (32, 52): 432, (33, 34): 279, (33, 53): 442, (34, 35): 211, (34, 54): 580, (35, 36): 440, (35, 55): 461, (36, 37): 22, (36, 56): 396, (37, 38): 450, (37, 57): 118, (38, 39): 229, (38, 58): 369, (39, 59): 554, (40, 41): 568, (40, 60): 64, (41, 42): 557, (41, 61): 576, (42, 43): 179, (42, 62): 537, (43, 44): 226, (43, 63): 162, (44, 45): 122, (44, 64): 510, (45, 46): 29, (45, 65): 122, (46, 47): 537, (46, 66): 210, (47, 48): 398, (47, 67): 295, (48, 49): 519, (48, 68): 208, (49, 50): 244, (49, 69): 24, (50, 51): 298, (50, 70): 226, (51, 52): 280, (51, 71): 434, (52, 53): 295, (52, 72): 126, (53, 54): 274, (53, 73): 144, (54, 55): 455, (54, 74): 192, (55, 56): 386, (55, 75): 113, (56, 57): 69, (56, 76): 597, (57, 58): 433, (57, 77): 458, (58, 59): 124, (58, 78): 288, (59, 79): 194, (60, 61): 27, (60, 80): 326, (61, 62): 487, (61, 81): 341, (62, 63): 589, (62, 82): 8, (63, 64): 271, (63, 83): 450, (64, 65): 133, (64, 84): 219, (65, 66): 462, (65, 85): 288, (66, 67): 107, (66, 86): 105, (67, 68): 140, (67, 87): 494, (68, 69): 498, (68, 88): 586, (69, 70): 447, (69, 89): 50, (70, 71): 268, (70, 90): 550, (71, 72): 553, (71, 91): 403, (72, 73): 386, (72, 92): 492, (73, 74): 464, (73, 93): 500, (74, 75): 516, (74, 94): 259, (75, 76): 126, (75, 95): 398, (76, 77): 575, (76, 96): 427, (77, 78): 42, (77, 97): 46, (78, 79): 256, (78, 98): 324, (79, 99): 154, (80, 81): 334, (80, 100): 509, (81, 82): 432, (81, 101): 583, (82, 83): 118, (82, 102): 86, (83, 84): 272, (83, 103): 444, (84, 85): 314, (84, 104): 145, (85, 86): 548, (85, 105): 224, (86, 87): 7, (86, 106): 413, (87, 88): 568, (87, 107): 425, (88, 89): 551, (88, 108): 366, (89, 90): 64, (89, 109): 46, (90, 91): 564, (90, 110): 278, (91, 92): 222, (91, 111): 421, (92, 93): 36, (92, 112): 276, (93, 94): 31, (93, 113): 65, (94, 95): 586, (94, 114): 513, (95, 96): 200, (95, 115): 110, (96, 97): 409, (96, 116): 504, (97, 98): 443, (97, 117): 203, (98, 99): 490, (98, 118): 536, (99, 119): 68, (100, 101): 347, (100, 120): 386, (101, 102): 44, (101, 121): 27, (102, 103): 271, (102, 122): 394, (103, 104): 589, (103, 123): 207, (104, 105): 248, (104, 124): 313, (105, 106): 107, (105, 125): 65, (106, 107): 357, (106, 126): 136, (107, 108): 474, (107, 127): 67, (108, 109): 434, (108, 128): 194, (109, 110): 431, (109, 129): 528, (110, 111): 439, (110, 130): 206, (111, 112): 441, (111, 131): 348, (112, 113): 127, (112, 132): 537, (113, 114): 448, (113, 133): 168, (114, 115): 112, (114, 134): 161, (115, 116): 0, (115, 135): 344, (116, 117): 321, (116, 136): 105, (117, 118): 143, (117, 137): 578, (118, 119): 32, (118, 138): 273, (119, 139): 66, (120, 121): 221, (120, 140): 282, (121, 122): 484, (121, 141): 117, (122, 123): 541, (122, 142): 3, (123, 124): 257, (123, 143): 452, (124, 125): 84, (124, 144): 160, (125, 126): 543, (125, 145): 380, (126, 127): 252, (126, 146): 66, (127, 128): 103, (127, 147): 315, (128, 129): 337, (128, 148): 303, (129, 130): 159, (129, 149): 278, (130, 131): 16, (130, 150): 89, (131, 132): 72, (131, 151): 590, (132, 133): 466, (132, 152): 134, (133, 134): 413, (133, 153): 0, (134, 135): 241, (134, 154): 177, (135, 136): 231, (135, 155): 451, (136, 137): 68, (136, 156): 5, (137, 138): 355, (137, 157): 562, (138, 139): 154, (138, 158): 38, (139, 159): 458, (140, 141): 350, (140, 160): 502, (141, 142): 424, (141, 161): 528, (142, 143): 301, (142, 162): 430, (143, 144): 3, (143, 163): 416, (144, 145): 59, (144, 164): 329, (145, 146): 307, (145, 165): 435, (146, 147): 438, (146, 166): 541, (147, 148): 425, (147, 167): 545, (148, 149): 369, (148, 168): 281, (149, 150): 47, (149, 169): 448, (150, 151): 56, (150, 170): 500, (151, 152): 149, (151, 171): 2, (152, 153): 459, (152, 172): 360, (153, 154): 232, (153, 173): 141, (154, 155): 283, (154, 174): 42, (155, 156): 62, (155, 175): 445, (156, 157): 97, (156, 176): 375, (157, 158): 481, (157, 177): 223, (158, 159): 221, (158, 178): 223, (159, 179): 570, (160, 161): 577, (160, 180): 90, (161, 162): 366, (161, 181): 111, (162, 163): 401, (162, 182): 359, (163, 164): 215, (163, 183): 239, (164, 165): 506, (164, 184): 160, (165, 166): 13, (165, 185): 368, (166, 167): 556, (166, 186): 169, (167, 168): 280, (167, 187): 130, (168, 169): 170, (168, 188): 548, (169, 170): 43, (169, 189): 316, (170, 171): 123, (170, 190): 168, (171, 172): 483, (171, 191): 406, (172, 173): 581, (172, 192): 439, (173, 174): 4, (173, 193): 285, (174, 175): 417, (174, 194): 302, (175, 176): 153, (175, 195): 271, (176, 177): 371, (176, 196): 389, (177, 178): 481, (177, 197): 139, (178, 179): 536, (178, 198): 459, (179, 199): 77, (180, 181): 48, (180, 200): 523, (181, 182): 67, (181, 201): 57, (182, 183): 493, (182, 202): 79, (183, 184): 357, (183, 203): 371, (184, 185): 463, (184, 204): 231, (185, 186): 285, (185, 205): 226, (186, 187): 193, (186, 206): 104, (187, 188): 584, (187, 207): 75, (188, 189): 233, (188, 208): 406, (189, 190): 80, (189, 209): 39, (190, 191): 466, (190, 210): 449, (191, 192): 142, (191, 211): 237, (192, 193): 17, (192, 212): 198, (193, 194): 24, (193, 213): 194, (194, 195): 552, (194, 214): 344, (195, 196): 308, (195, 215): 119, (196, 197): 326, (196, 216): 502, (197, 198): 519, (197, 217): 65, (198, 199): 219, (198, 218): 540, (199, 219): 136, (200, 201): 229, (200, 220): 394, (201, 202): 281, (201, 221): 496, (202, 203): 299, (202, 222): 256, (203, 204): 339, (203, 223): 315, (204, 205): 467, (204, 224): 165, (205, 206): 328, (205, 225): 4, (206, 207): 44, (206, 226): 88, (207, 208): 187, (207, 227): 257, (208, 209): 451, (208, 228): 342, (209, 210): 206, (209, 229): 234, (210, 211): 432, (210, 230): 538, (211, 212): 230, (211, 231): 209, (212, 213): 271, (212, 232): 174, (213, 214): 474, (213, 233): 283, (214, 215): 369, (214, 234): 62, (215, 216): 103, (215, 235): 379, (216, 217): 114, (216, 236): 66, (217, 218): 446, (217, 237): 296, (218, 219): 413, (218, 238): 468, (219, 239): 472, (220, 221): 408, (220, 240): 358, (221, 222): 88, (221, 241): 387, (222, 223): 468, (222, 242): 48, (223, 224): 203, (223, 243): 163, (224, 225): 346, (224, 244): 35, (225, 226): 120, (225, 245): 497, (226, 227): 369, (226, 246): 11, (227, 228): 454, (227, 247): 593, (228, 229): 462, (228, 248): 391, (229, 230): 138, (229, 249): 389, (230, 231): 317, (230, 250): 527, (231, 232): 488, (231, 251): 218, (232, 233): 504, (232, 252): 269, (233, 234): 468, (233, 253): 259, (234, 235): 230, (234, 254): 563, (235, 236): 457, (235, 255): 231, (236, 237): 461, (236, 256): 135, (237, 238): 486, (237, 257): 551, (238, 239): 593, (238, 258): 570, (239, 259): 116, (240, 241): 467, (240, 260): 395, (241, 242): 435, (241, 261): 123, (242, 243): 77, (242, 262): 325, (243, 244): 551, (243, 263): 112, (244, 245): 5, (244, 264): 144, (245, 246): 264, (245, 265): 204, (246, 247): 87, (246, 266): 396, (247, 248): 244, (247, 267): 389, (248, 249): 495, (248, 268): 511, (249, 250): 267, (249, 269): 577, (250, 251): 504, (250, 270): 453, (251, 252): 400, (251, 271): 104, (252, 253): 137, (252, 272): 304, (253, 254): 129, (253, 273): 215, (254, 255): 530, (254, 274): 456, (255, 256): 177, (255, 275): 78, (256, 257): 396, (256, 276): 596, (257, 258): 324, (257, 277): 149, (258, 259): 57, (258, 278): 570, (259, 279): 21, (260, 261): 208, (260, 280): 484, (261, 262): 294, (261, 281): 418, (262, 263): 452, (262, 282): 372, (263, 264): 171, (263, 283): 316, (264, 265): 293, (264, 284): 482, (265, 266): 406, (265, 285): 524, (266, 267): 39, (266, 286): 233, (267, 268): 170, (267, 287): 383, (268, 269): 129, (268, 288): 417, (269, 270): 506, (269, 289): 239, (270, 271): 19, (270, 290): 350, (271, 272): 134, (271, 291): 157, (272, 273): 129, (272, 292): 210, (273, 274): 166, (273, 293): 414, (274, 275): 354, (274, 294): 598, (275, 276): 164, (275, 295): 352, (276, 277): 465, (276, 296): 62, (277, 278): 194, (277, 297): 66, (278, 279): 243, (278, 298): 575, (279, 299): 28, (280, 281): 25, (281, 282): 187, (282, 283): 8, (283, 284): 319, (284, 285): 249, (285, 286): 169, (286, 287): 220, (287, 288): 530, (288, 289): 589, (289, 290): 582, (290, 291): 115, (291, 292): 150, (292, 293): 58, (293, 294): 16, (294, 295): 471, (295, 296): 449, (296, 297): 69, (297, 298): 286, (298, 299): 478, (1, 0): 497, (20, 0): 171, (2, 1): 57, (21, 1): 595, (3, 2): 378, (22, 2): 593, (4, 3): 211, (23, 3): 418, (5, 4): 110, (24, 4): 538, (6, 5): 527, (25, 5): 564, (7, 6): 436, (26, 6): 401, (8, 7): 25, (27, 7): 200, (9, 8): 539, (28, 8): 585, (10, 9): 105, (29, 9): 308, (11, 10): 24, (30, 10): 205, (12, 11): 154, (31, 11): 479, (13, 12): 111, (32, 12): 36, (14, 13): 180, (33, 13): 421, (15, 14): 263, (34, 14): 297, (16, 15): 279, (35, 15): 0, (17, 16): 294, (36, 16): 150, (18, 17): 336, (37, 17): 571, (19, 18): 474, (38, 18): 410, (39, 19): 426, (21, 20): 373, (40, 20): 380, (22, 21): 313, (41, 21): 194, (23, 22): 99, (42, 22): 13, (24, 23): 241, (43, 23): 123, (25, 24): 550, (44, 24): 188, (26, 25): 520, (45, 25): 334, (27, 26): 571, (46, 26): 88, (28, 27): 163, (47, 27): 434, (29, 28): 215, (48, 28): 449, (30, 29): 464, (49, 29): 304, (31, 30): 418, (50, 30): 450, (32, 31): 415, (51, 31): 495, (33, 32): 311, (52, 32): 432, (34, 33): 279, (53, 33): 442, (35, 34): 211, (54, 34): 580, (36, 35): 440, (55, 35): 461, (37, 36): 22, (56, 36): 396, (38, 37): 450, (57, 37): 118, (39, 38): 229, (58, 38): 369, (59, 39): 554, (41, 40): 568, (60, 40): 64, (42, 41): 557, (61, 41): 576, (43, 42): 179, (62, 42): 537, (44, 43): 226, (63, 43): 162, (45, 44): 122, (64, 44): 510, (46, 45): 29, (65, 45): 122, (47, 46): 537, (66, 46): 210, (48, 47): 398, (67, 47): 295, (49, 48): 519, (68, 48): 208, (50, 49): 244, (69, 49): 24, (51, 50): 298, (70, 50): 226, (52, 51): 280, (71, 51): 434, (53, 52): 295, (72, 52): 126, (54, 53): 274, (73, 53): 144, (55, 54): 455, (74, 54): 192, (56, 55): 386, (75, 55): 113, (57, 56): 69, (76, 56): 597, (58, 57): 433, (77, 57): 458, (59, 58): 124, (78, 58): 288, (79, 59): 194, (61, 60): 27, (80, 60): 326, (62, 61): 487, (81, 61): 341, (63, 62): 589, (82, 62): 8, (64, 63): 271, (83, 63): 450, (65, 64): 133, (84, 64): 219, (66, 65): 462, (85, 65): 288, (67, 66): 107, (86, 66): 105, (68, 67): 140, (87, 67): 494, (69, 68): 498, (88, 68): 586, (70, 69): 447, (89, 69): 50, (71, 70): 268, (90, 70): 550, (72, 71): 553, (91, 71): 403, (73, 72): 386, (92, 72): 492, (74, 73): 464, (93, 73): 500, (75, 74): 516, (94, 74): 259, (76, 75): 126, (95, 75): 398, (77, 76): 575, (96, 76): 427, (78, 77): 42, (97, 77): 46, (79, 78): 256, (98, 78): 324, (99, 79): 154, (81, 80): 334, (100, 80): 509, (82, 81): 432, (101, 81): 583, (83, 82): 118, (102, 82): 86, (84, 83): 272, (103, 83): 444, (85, 84): 314, (104, 84): 145, (86, 85): 548, (105, 85): 224, (87, 86): 7, (106, 86): 413, (88, 87): 568, (107, 87): 425, (89, 88): 551, (108, 88): 366, (90, 89): 64, (109, 89): 46, (91, 90): 564, (110, 90): 278, (92, 91): 222, (111, 91): 421, (93, 92): 36, (112, 92): 276, (94, 93): 31, (113, 93): 65, (95, 94): 586, (114, 94): 513, (96, 95): 200, (115, 95): 110, (97, 96): 409, (116, 96): 504, (98, 97): 443, (117, 97): 203, (99, 98): 490, (118, 98): 536, (119, 99): 68, (101, 100): 347, (120, 100): 386, (102, 101): 44, (121, 101): 27, (103, 102): 271, (122, 102): 394, (104, 103): 589, (123, 103): 207, (105, 104): 248, (124, 104): 313, (106, 105): 107, (125, 105): 65, (107, 106): 357, (126, 106): 136, (108, 107): 474, (127, 107): 67, (109, 108): 434, (128, 108): 194, (110, 109): 431, (129, 109): 528, (111, 110): 439, (130, 110): 206, (112, 111): 441, (131, 111): 348, (113, 112): 127, (132, 112): 537, (114, 113): 448, (133, 113): 168, (115, 114): 112, (134, 114): 161, (116, 115): 0, (135, 115): 344, (117, 116): 321, (136, 116): 105, (118, 117): 143, (137, 117): 578, (119, 118): 32, (138, 118): 273, (139, 119): 66, (121, 120): 221, (140, 120): 282, (122, 121): 484, (141, 121): 117, (123, 122): 541, (142, 122): 3, (124, 123): 257, (143, 123): 452, (125, 124): 84, (144, 124): 160, (126, 125): 543, (145, 125): 380, (127, 126): 252, (146, 126): 66, (128, 127): 103, (147, 127): 315, (129, 128): 337, (148, 128): 303, (130, 129): 159, (149, 129): 278, (131, 130): 16, (150, 130): 89, (132, 131): 72, (151, 131): 590, (133, 132): 466, (152, 132): 134, (134, 133): 413, (153, 133): 0, (135, 134): 241, (154, 134): 177, (136, 135): 231, (155, 135): 451, (137, 136): 68, (156, 136): 5, (138, 137): 355, (157, 137): 562, (139, 138): 154, (158, 138): 38, (159, 139): 458, (141, 140): 350, (160, 140): 502, (142, 141): 424, (161, 141): 528, (143, 142): 301, (162, 142): 430, (144, 143): 3, (163, 143): 416, (145, 144): 59, (164, 144): 329, (146, 145): 307, (165, 145): 435, (147, 146): 438, (166, 146): 541, (148, 147): 425, (167, 147): 545, (149, 148): 369, (168, 148): 281, (150, 149): 47, (169, 149): 448, (151, 150): 56, (170, 150): 500, (152, 151): 149, (171, 151): 2, (153, 152): 459, (172, 152): 360, (154, 153): 232, (173, 153): 141, (155, 154): 283, (174, 154): 42, (156, 155): 62, (175, 155): 445, (157, 156): 97, (176, 156): 375, (158, 157): 481, (177, 157): 223, (159, 158): 221, (178, 158): 223, (179, 159): 570, (161, 160): 577, (180, 160): 90, (162, 161): 366, (181, 161): 111, (163, 162): 401, (182, 162): 359, (164, 163): 215, (183, 163): 239, (165, 164): 506, (184, 164): 160, (166, 165): 13, (185, 165): 368, (167, 166): 556, (186, 166): 169, (168, 167): 280, (187, 167): 130, (169, 168): 170, (188, 168): 548, (170, 169): 43, (189, 169): 316, (171, 170): 123, (190, 170): 168, (172, 171): 483, (191, 171): 406, (173, 172): 581, (192, 172): 439, (174, 173): 4, (193, 173): 285, (175, 174): 417, (194, 174): 302, (176, 175): 153, (195, 175): 271, (177, 176): 371, (196, 176): 389, (178, 177): 481, (197, 177): 139, (179, 178): 536, (198, 178): 459, (199, 179): 77, (181, 180): 48, (200, 180): 523, (182, 181): 67, (201, 181): 57, (183, 182): 493, (202, 182): 79, (184, 183): 357, (203, 183): 371, (185, 184): 463, (204, 184): 231, (186, 185): 285, (205, 185): 226, (187, 186): 193, (206, 186): 104, (188, 187): 584, (207, 187): 75, (189, 188): 233, (208, 188): 406, (190, 189): 80, (209, 189): 39, (191, 190): 466, (210, 190): 449, (192, 191): 142, (211, 191): 237, (193, 192): 17, (212, 192): 198, (194, 193): 24, (213, 193): 194, (195, 194): 552, (214, 194): 344, (196, 195): 308, (215, 195): 119, (197, 196): 326, (216, 196): 502, (198, 197): 519, (217, 197): 65, (199, 198): 219, (218, 198): 540, (219, 199): 136, (201, 200): 229, (220, 200): 394, (202, 201): 281, (221, 201): 496, (203, 202): 299, (222, 202): 256, (204, 203): 339, (223, 203): 315, (205, 204): 467, (224, 204): 165, (206, 205): 328, (225, 205): 4, (207, 206): 44, (226, 206): 88, (208, 207): 187, (227, 207): 257, (209, 208): 451, (228, 208): 342, (210, 209): 206, (229, 209): 234, (211, 210): 432, (230, 210): 538, (212, 211): 230, (231, 211): 209, (213, 212): 271, (232, 212): 174, (214, 213): 474, (233, 213): 283, (215, 214): 369, (234, 214): 62, (216, 215): 103, (235, 215): 379, (217, 216): 114, (236, 216): 66, (218, 217): 446, (237, 217): 296, (219, 218): 413, (238, 218): 468, (239, 219): 472, (221, 220): 408, (240, 220): 358, (222, 221): 88, (241, 221): 387, (223, 222): 468, (242, 222): 48, (224, 223): 203, (243, 223): 163, (225, 224): 346, (244, 224): 35, (226, 225): 120, (245, 225): 497, (227, 226): 369, (246, 226): 11, (228, 227): 454, (247, 227): 593, (229, 228): 462, (248, 228): 391, (230, 229): 138, (249, 229): 389, (231, 230): 317, (250, 230): 527, (232, 231): 488, (251, 231): 218, (233, 232): 504, (252, 232): 269, (234, 233): 468, (253, 233): 259, (235, 234): 230, (254, 234): 563, (236, 235): 457, (255, 235): 231, (237, 236): 461, (256, 236): 135, (238, 237): 486, (257, 237): 551, (239, 238): 593, (258, 238): 570, (259, 239): 116, (241, 240): 467, (260, 240): 395, (242, 241): 435, (261, 241): 123, (243, 242): 77, (262, 242): 325, (244, 243): 551, (263, 243): 112, (245, 244): 5, (264, 244): 144, (246, 245): 264, (265, 245): 204, (247, 246): 87, (266, 246): 396, (248, 247): 244, (267, 247): 389, (249, 248): 495, (268, 248): 511, (250, 249): 267, (269, 249): 577, (251, 250): 504, (270, 250): 453, (252, 251): 400, (271, 251): 104, (253, 252): 137, (272, 252): 304, (254, 253): 129, (273, 253): 215, (255, 254): 530, (274, 254): 456, (256, 255): 177, (275, 255): 78, (257, 256): 396, (276, 256): 596, (258, 257): 324, (277, 257): 149, (259, 258): 57, (278, 258): 570, (279, 259): 21, (261, 260): 208, (280, 260): 484, (262, 261): 294, (281, 261): 418, (263, 262): 452, (282, 262): 372, (264, 263): 171, (283, 263): 316, (265, 264): 293, (284, 264): 482, (266, 265): 406, (285, 265): 524, (267, 266): 39, (286, 266): 233, (268, 267): 170, (287, 267): 383, (269, 268): 129, (288, 268): 417, (270, 269): 506, (289, 269): 239, (271, 270): 19, (290, 270): 350, (272, 271): 134, (291, 271): 157, (273, 272): 129, (292, 272): 210, (274, 273): 166, (293, 273): 414, (275, 274): 354, (294, 274): 598, (276, 275): 164, (295, 275): 352, (277, 276): 465, (296, 276): 62, (278, 277): 194, (297, 277): 66, (279, 278): 243, (298, 278): 575, (299, 279): 28, (281, 280): 25, (282, 281): 187, (283, 282): 8, (284, 283): 319, (285, 284): 249, (286, 285): 169, (287, 286): 220, (288, 287): 530, (289, 288): 589, (290, 289): 582, (291, 290): 115, (292, 291): 150, (293, 292): 58, (294, 293): 16, (295, 294): 471, (296, 295): 449, (297, 296): 69, (298, 297): 286, (299, 298): 478}
start = 224
correct_distances = {224: 0, 244: 35, 245: 40, 204: 165, 264: 179, 223: 203, 265: 244, 246: 304, 226: 315, 225: 346, 205: 350, 263: 350, 243: 366, 247: 391, 184: 396, 206: 403, 242: 443, 207: 447, 222: 491, 203: 504, 186: 507, 187: 522, 164: 556, 185: 576, 221: 579, 208: 634, 248: 635, 266: 650, 167: 652, 284: 661, 283: 666, 282: 674, 166: 676, 227: 684, 165: 689, 267: 689, 202: 747, 183: 753, 262: 768, 285: 768, 163: 771, 182: 826, 268: 859, 281: 861, 241: 878, 286: 883, 144: 885, 280: 886, 143: 888, 181: 893, 168: 932, 180: 941, 145: 944, 201: 950, 228: 976, 220: 987, 269: 988, 261: 1001, 161: 1004, 160: 1031, 188: 1040, 124: 1045, 287: 1072, 209: 1085, 169: 1102, 189: 1124, 125: 1129, 249: 1130, 170: 1145, 162: 1172, 200: 1179, 142: 1189, 122: 1192, 105: 1194, 147: 1197, 190: 1204, 260: 1209, 148: 1213, 146: 1217, 289: 1227, 171: 1268, 151: 1270, 288: 1276, 126: 1283, 210: 1291, 106: 1301, 123: 1302, 229: 1319, 150: 1326, 240: 1345, 104: 1358, 149: 1373, 250: 1397, 130: 1415, 85: 1418, 152: 1419, 131: 1431, 230: 1457, 270: 1494, 84: 1503, 132: 1503, 103: 1509, 127: 1512, 271: 1513, 128: 1516, 141: 1532, 140: 1533, 129: 1574, 107: 1579, 102: 1586, 251: 1617, 110: 1621, 101: 1630, 272: 1647, 121: 1649, 191: 1670, 291: 1670, 82: 1672, 62: 1680, 65: 1706, 108: 1710, 86: 1714, 87: 1721, 64: 1722, 211: 1723, 172: 1751, 231: 1774, 83: 1775, 273: 1776, 111: 1779, 290: 1785, 192: 1812, 120: 1815, 66: 1819, 292: 1820, 45: 1828, 193: 1829, 194: 1853, 46: 1857, 153: 1878, 133: 1878, 293: 1878, 294: 1894, 90: 1899, 67: 1926, 274: 1942, 26: 1945, 44: 1950, 252: 1951, 212: 1953, 89: 1963, 100: 1977, 253: 1991, 63: 1993, 109: 2009, 69: 2013, 173: 2019, 174: 2023, 213: 2023, 49: 2037, 112: 2040, 113: 2046, 154: 2065, 68: 2066, 88: 2076, 81: 2104, 93: 2111, 254: 2120, 232: 2127, 24: 2138, 94: 2142, 92: 2147, 43: 2155, 25: 2162, 61: 2167, 60: 2194, 214: 2197, 91: 2200, 42: 2217, 47: 2221, 22: 2230, 134: 2242, 233: 2250, 40: 2258, 234: 2259, 48: 2274, 23: 2278, 50: 2281, 275: 2296, 29: 2341, 6: 2346, 155: 2348, 295: 2365, 255: 2374, 74: 2401, 114: 2403, 195: 2405, 156: 2410, 136: 2415, 80: 2438, 175: 2440, 70: 2449, 276: 2460, 135: 2483, 137: 2483, 235: 2489, 157: 2507, 115: 2515, 116: 2515, 27: 2516, 296: 2522, 215: 2524, 21: 2543, 256: 2551, 28: 2556, 51: 2579, 297: 2591, 54: 2593, 176: 2593, 71: 2603, 73: 2611, 95: 2625, 216: 2627, 20: 2638, 72: 2639, 9: 2649, 277: 2657, 4: 2676, 236: 2686, 3: 2696, 196: 2713, 7: 2716, 5: 2726, 177: 2730, 30: 2731, 41: 2737, 8: 2741, 217: 2741, 10: 2754, 53: 2755, 52: 2765, 11: 2778, 197: 2806, 257: 2806, 0: 2809, 2: 2823, 96: 2825, 117: 2836, 138: 2838, 278: 2851, 158: 2876, 298: 2877, 1: 2880, 75: 2917, 12: 2932, 32: 2968, 118: 2979, 139: 2992, 119: 3011, 55: 3030, 237: 3037, 97: 3039, 13: 3043, 76: 3043, 31: 3074, 99: 3079, 77: 3085, 279: 3094, 159: 3097, 178: 3099, 259: 3115, 299: 3122, 78: 3127, 258: 3130, 34: 3173, 218: 3187, 33: 3197, 14: 3223, 239: 3231, 79: 3233, 198: 3325, 35: 3384, 15: 3384, 58: 3415, 56: 3416, 59: 3427, 98: 3451, 57: 3485, 238: 3523, 199: 3544, 219: 3600, 37: 3603, 179: 3621, 36: 3625, 16: 3663, 38: 3784, 17: 3957, 39: 3981, 18: 4194, 19: 4407}
correct_parents = {224: None, 244: 224, 245: 244, 204: 224, 264: 244, 223: 224, 265: 245, 246: 245, 226: 246, 225: 224, 205: 225, 263: 264, 243: 223, 247: 246, 184: 204, 206: 226, 242: 243, 207: 206, 222: 242, 203: 204, 186: 206, 187: 207, 164: 184, 185: 205, 221: 222, 208: 207, 248: 247, 266: 265, 167: 187, 284: 264, 283: 263, 282: 283, 166: 186, 227: 226, 165: 166, 267: 266, 202: 222, 183: 184, 262: 242, 285: 265, 163: 164, 182: 202, 268: 267, 281: 282, 241: 242, 286: 266, 144: 164, 280: 281, 143: 144, 181: 182, 168: 167, 180: 181, 145: 144, 201: 181, 228: 208, 220: 221, 269: 268, 261: 241, 161: 181, 160: 180, 188: 208, 124: 144, 287: 267, 209: 208, 169: 168, 189: 209, 125: 124, 249: 248, 170: 169, 162: 163, 200: 201, 142: 143, 122: 142, 105: 125, 147: 167, 190: 189, 260: 261, 148: 168, 146: 166, 289: 269, 171: 170, 151: 171, 288: 268, 126: 146, 210: 209, 106: 105, 123: 124, 229: 209, 150: 151, 240: 220, 104: 124, 149: 150, 250: 249, 130: 150, 85: 105, 152: 151, 131: 130, 230: 229, 270: 269, 84: 104, 132: 131, 103: 123, 127: 147, 271: 270, 128: 148, 141: 161, 140: 160, 129: 130, 107: 127, 102: 122, 251: 271, 110: 130, 101: 102, 272: 271, 121: 141, 191: 190, 291: 271, 82: 102, 62: 82, 65: 85, 108: 128, 86: 106, 87: 86, 64: 84, 211: 210, 172: 171, 231: 230, 83: 84, 273: 272, 111: 131, 290: 291, 192: 191, 120: 140, 66: 86, 292: 291, 45: 65, 193: 192, 194: 193, 46: 45, 153: 152, 133: 153, 293: 292, 294: 293, 90: 110, 67: 66, 274: 273, 26: 46, 44: 45, 252: 272, 212: 211, 89: 90, 100: 101, 253: 273, 63: 64, 109: 89, 69: 89, 173: 153, 174: 173, 213: 193, 49: 69, 112: 132, 113: 133, 154: 174, 68: 67, 88: 108, 81: 82, 93: 113, 254: 253, 232: 212, 24: 44, 94: 93, 92: 93, 43: 63, 25: 45, 61: 62, 60: 61, 214: 194, 91: 111, 42: 62, 47: 67, 22: 42, 134: 154, 233: 253, 40: 60, 234: 214, 48: 68, 23: 43, 50: 49, 275: 274, 29: 49, 6: 26, 155: 154, 295: 294, 255: 275, 74: 94, 114: 134, 195: 194, 156: 155, 136: 156, 80: 81, 175: 174, 70: 90, 276: 275, 135: 134, 137: 136, 235: 234, 157: 156, 115: 114, 116: 115, 27: 26, 296: 276, 215: 195, 21: 22, 256: 255, 28: 29, 51: 50, 297: 296, 54: 74, 176: 175, 71: 91, 73: 93, 95: 115, 216: 215, 20: 40, 72: 92, 9: 29, 277: 297, 4: 24, 236: 256, 3: 23, 196: 195, 7: 27, 5: 25, 177: 157, 30: 50, 41: 21, 8: 7, 217: 216, 10: 9, 53: 73, 52: 72, 11: 10, 197: 217, 257: 277, 0: 20, 2: 22, 96: 95, 117: 116, 138: 137, 278: 277, 158: 138, 298: 297, 1: 2, 75: 74, 12: 11, 32: 12, 118: 117, 139: 138, 119: 118, 55: 75, 237: 217, 97: 117, 13: 12, 76: 75, 31: 51, 99: 119, 77: 97, 279: 278, 159: 158, 178: 158, 259: 279, 299: 279, 78: 77, 258: 257, 34: 54, 218: 217, 33: 53, 14: 13, 239: 259, 79: 99, 198: 197, 35: 34, 15: 35, 58: 78, 56: 55, 59: 79, 98: 78, 57: 56, 238: 237, 199: 198, 219: 218, 37: 57, 179: 199, 36: 37, 16: 15, 38: 58, 17: 16, 39: 59, 18: 38, 19: 39}

def t():
    distances, parents = dijkstraLogic.dijkstra(weights, start=start)
    print(distances, parents)
    assert distances == correct_distances
    assert parents == correct_parents
t()'''