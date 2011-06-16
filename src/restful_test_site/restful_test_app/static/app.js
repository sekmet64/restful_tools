var selectedBookshelf;
var selectedBook;
var selectedBookObject;
var booksSelect;
var bookshelvesSelect;

function updateBooks() {
	booksSelect = $('#books').empty();
	
	$.ajax({
		type: 'GET',
		url: '/restful_test/books/',
		dataType: 'json',
		success: function(books) {
			var addBookSelect = $('#all-books').empty();
			$.each(books, function() {
				addBookSelect.append($('<option />').val(this.pk).text(this.fields.title));
			});
		}
	});
}

function updateBookshelves() {
	bookshelvesSelect = $('#bookshelves').empty();
	
	$.ajax({
		type: 'GET',
		url: '/restful_test/bookshelves/',
		dataType: 'json',
		success: function(bookshelves) {

			$.each(bookshelves, function() {
				bookshelvesSelect.append($('<option />').val(this.pk).text(this.pk));
			});
		}
	});
}

function updateSelectedBooks() {
	selectedBookshelf = $('#bookshelves option:selected')[0];
	booksSelect.empty();
	
	$.ajax({
		type: 'GET',
		url: '/restful_test/bookshelves/' + selectedBookshelf.value + '/',
		dataType: 'json',
		success: function(books) {
			$.each(books, function() {
				booksSelect.append($('<option />').val(this.pk).text(this.fields.title));
			});
		}
	});
}

function updateDetails() {
	$.ajax({
			type: 'GET',
			url: '/restful_test/bookshelves/' + selectedBookshelf.value + '/' + $('#books option:selected')[0].value,
			dataType: 'json',
			success: function(books) {
				book = books[0];
				selectedBookObject = book;
				
				var details = $('#details').empty();
				details.append('<span class="bold">Title: </span>' + book.fields.title + '<br />');
				details.append('<span class="bold">ISBN: </span>' + book.pk + '<br />');
				details.append('<span class="bold">Published: </span>' + book.fields.published + '<br />');
				details.append('<br />');
				details.append(book.fields.description);
				
				$('#u-title').val(book.fields.title);
				$('#u-isbn').val(book.pk);
				$('#u-published').val(book.fields.published);
				$('#u-description').val(book.fields.description);
			}
		});	
}

$(document).ready(function() {
	
	booksSelect = $('#books');
	
	updateBookshelves();
	
	bookshelvesSelect.change(function() {
		updateSelectedBooks();
	});
	
	booksSelect.change(function() {
		selectedBook = $('#books option:selected')[0];
		
		updateDetails();
	});
	
	
	updateBooks();
	
	$('#create-book-button').click(function() {
		var title = $('#a-title').val();
		var isbn = $('#a-isbn').val();
		var published = $('#a-published').val();
		var description = $('#a-description').val();
		
		var newBook = new Object();
		
		newBook.pk = isbn;
		newBook.model = 'restful_test_app.book';
		newBook.fields = new Object();
		newBook.fields.published = published;
		newBook.fields.description = description;
		newBook.fields.title = title;
		
		books = [newBook];
		
		$.post('/restful_test/books/', JSON.stringify(books));
		updateBooks();
	});
	
	
	$('#create-bookshelf-button').click(function() {
		newBookshelf = new Object();
		newBookshelf.pk = $('#create-bookshelf-text').val();
		newBookshelf.model = 'restful_test_app.bookshelf';
		newBookshelf.fields = new Object();
		newBookshelf.fields.books = [];
		bookshelves = [newBookshelf];
		
		$.post('/restful_test/bookshelves/', JSON.stringify(bookshelves));
		
		updateBookshelves();
	});
	
	$('#add-book').click(function() {
		bookid = $('#all-books option:selected')[0].value;
		
		$.ajax({
			type: 'PUT',
			url: '/restful_test/bookshelves/' + selectedBookshelf.value + '/' + bookid, 
			success: function() {
				updateSelectedBooks();
			}
		});
	});
	
	
	$('#remove-book').click(function() {
		$.ajax({
			type: 'DELETE',
			url: '/restful_test/bookshelves/' + selectedBookshelf.value + '/' + selectedBook.value,
			success: function() {
				updateSelectedBooks();
			}			
		});
	});
	
	$('#update-book-button').click(function() {
		
		var newBook = new Object();
		newBook.pk = $('#u-isbn').val();
		newBook.model = 'restful_test_app.book';
		newBook.fields = new Object();
		newBook.fields.published = $('#u-published').val();
		newBook.fields.description = $('#u-description').val();
		newBook.fields.title = $('#u-title').val();
		
		books = [newBook];
		
		$.ajax({
			type: 'PUT',
			url: '/restful_test/books/' + selectedBook.value,
			data: JSON.stringify(books),
			success: function() {
				updateDetails();
			}
		});
			
	});
	
});