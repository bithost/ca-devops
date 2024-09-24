
https://ui.lanlab.xyz/browseCollection

// Query the Books collection
db.Books.find({})

// Query the Authors collection
db.Authors.find({})

// Query the Patrons collection
db.Patrons.find({})


// Query the Authors collection
db.Authors.find({}, {_id: 1})

// Query the Patrons collection
db.Patrons.find({}, {_id: 1})



// Insert an author
db.Authors.insert({
  _id: ObjectId(),
  name: "John Doe"
})

// Insert a patron
db.Patrons.insert({
  _id: ObjectId(),
  name: "Jane Smith"
})

// Insert a book linked to the author and patron
db.Books.insert({
  _id: ObjectId(),
  title: "The Great Book",
  author_id: ObjectId("656c661e31a9263367609130"),  // Replace with actual author_id
  patron_id: ObjectId("656c661e31a9263367609130")  // Replace with actual patron_id
})