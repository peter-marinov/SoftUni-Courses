function movies(input){
    let movieDB = [];
    for (const line of input) {
        if (line.includes('addMovie')) {
            let [unusedData, movieName] = line.split('addMovie ');
            movieDB.push({
                name: movieName,
            })
        } else if (line.includes('directedBy')) {
            let [movieName, directorName] = line.split(' directedBy ');
            for (const movie of movieDB) {
                if (movie.name === movieName) {
                    movie['director'] = directorName;
                    break;
                }
            }
        } else if (line.includes('onDate')) {
            let [movieName, date] = line.split(' onDate ');
            for (const movie of movieDB) {
                if (movie.name === movieName) {
                    movie['date'] = date;
                    break;
                }
            }
        }
    }

    for (const movie of movieDB) {
        if (movie.hasOwnProperty('director') && movie.hasOwnProperty('date')) {
            console.log(JSON.stringify(movie));
        }
    }
}

movies([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
    ])