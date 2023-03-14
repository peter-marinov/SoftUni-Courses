function solve(input) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    let numberOfSongs = input[0];
    let songs = [];
    let neededSongs = input.slice(-1)[0];
    for (const line of input.slice(1,input.length - 1)) {
        let [type, name, time] = line.split('_');
        songs.push(new Song(type, name, time));
    }

    if (neededSongs === 'all') {
        for (const song of songs) {
            console.log(song.name);
        }
    } else {
        for (const song of songs) {
            if (neededSongs === song.typeList) {
                console.log(song.name);
            } 
        }
    }
        
}

solve(
    [3, 
    'favourite_DownTown_3:14', 
    'favourite_Kiss_4:16', 
    'favourite_Smooth Criminal_4:01', 
    'favourite'])