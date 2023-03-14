function bookShelf(input) {
    let shelfIdGenreMap = {};
    let shelfGenreBooksMap = {};

    for (const line of input) {
        if (line.includes('->')) {
            let [shelfId, genre] = line.split(' -> ');
            if (!shelfIdGenreMap.hasOwnProperty(shelfId)) {
                shelfIdGenreMap[shelfId] = genre;
                shelfGenreBooksMap[genre] = [];
            }
        } else {
            let [bookTitle, other] = line.split(': ');
            let [bookAuthor, bookGenre] = other.split(', ');
            if (shelfGenreBooksMap.hasOwnProperty(bookGenre)) {
                shelfGenreBooksMap[bookGenre].push({bookTitle, bookAuthor});
            }
        }
    }

    let sortedGenres = Object.entries(shelfGenreBooksMap)
        .sort((bookA, bookB) => {
            let booksACount = bookA[1].length;
            let booksBCount = bookB[1].length;

            return booksBCount - booksACount;
        })
    for (const [genre, books] of sortedGenres) {
        let shelfId = Object.entries(shelfIdGenreMap)
            .find(([id, g]) => g === genre)[0];
        console.log(`${shelfId} ${genre}: ${books.length}`);
        let sortedBooks = books.sort((bookA, bookB) => bookA.bookTitle.localeCompare(bookB.bookTitle));
        for (const {bookTitle, bookAuthor} of sortedBooks) {
            console.log(`--> ${bookTitle}: ${bookAuthor}`)
        }
    }
    
}


bookShelf(['1 -> history', '1 -> action',
    'Death in Time: Criss Bell, mystery',
    '2 -> mystery', '3 -> sci-fi',
    'Child of Silver: Bruce Rich, mystery',
    'Hurting Secrets: Dustin Bolt, action',
    'Future of Dawn: Aiden Rose, sci-fi',
    'Lions and Rats: Gabe Roads, history',
    '2 -> romance', 'Effect of the Void: Shay B, romance',
    'Losing Dreams: Gail Starr, sci-fi',
    'Name of Earth: Jo Bell, sci-fi',
    'Pilots of Stone: Brook Jay, history']
)