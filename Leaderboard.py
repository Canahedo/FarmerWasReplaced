import Utils
import Data

speedup = 99999999999999999999
run_type = Leaderboards.Pumpkins_Single

files = {
Leaderboards.Fastest_Reset : "Fastest_Reset",
Leaderboards.Maze : "Maze",
Leaderboards.Dinosaur : "Dinosaur",
Leaderboards.Cactus : "Cactus",
Leaderboards.Sunflowers : "Sunflowers",
Leaderboards.Pumpkins : "Pumpkins",
Leaderboards.Wood : "Wood",
Leaderboards.Carrots : "Carrots",
Leaderboards.Hay : "Hay",
Leaderboards.Maze_Single : "Maze_Single",
Leaderboards.Cactus_Single : "Cactus_Single",
Leaderboards.Sunflowers_Single : "Sunflowers_Single",
Leaderboards.Pumpkins_Single : "Pumpkins_Single-7_27",
Leaderboards.Wood_Single : "Wood_Single",
Leaderboards.Carrots_Single : "Carrots_Single",
Leaderboards.Hay_Single : "Hay_Single",
}

leaderboard_run(run_type, files[run_type], speedup)