C, D = 1, 0

prisonersDilemma = {
(D, D): (+0, +0),
(D, C): (+4, -1),
(C, D): (-1, +4),
(C, C): (+3, +3) }

deadlock = {
(D, D): (+1, +1),
(D, C): (+2, -1),
(C, D): (-1, +2),
(C, C): (+0, +0) }

chicken = {
(D, D): (-4, -4),
(D, C): (+2, +0),
(C, D): (+0, +2),
(C, C): (+1, +1) }

stagHunt = {
(D, D): (-1, -1),
(D, C): (+2, -2),
(C, D): (-2, +2),
(C, C): (+3, +3) }

coordination = {
(D, D): (+1, +1),
(D, C): (-1, -1),
(C, D): (-1, -1),
(C, C): (+1, +1) }

matchingPennies = {
(D, D): (+1, -1),
(D, C): (-1, +1),
(C, D): (-1, +1),
(C, C): (+1, -1) }

battleOfTheSexes = {
(D, D): (-2, -2),
(D, C): (+4, +0),
(C, D): (+0, +4),
(C, C): (-1, -1) }  # chicken variant

hawkDove = {
(D, D): (-2, -2),
(D, C): (+3, -1),
(C, D): (-1, +3),
(C, C): (+1, +1) }  # chicken variant

assuranceGame = {
(D, D): (-1, -1),
(D, C): (+0, -2),
(C, D): (-2, +0),
(C, C): (+3, +3) }  # stagHunt variant

friendOrFoe = {
(D, D): (-1, -1),
(D, C): (+1, -1),
(C, D): (-1, +1),
(C, C): (+0, +0) }  # deadlock variant