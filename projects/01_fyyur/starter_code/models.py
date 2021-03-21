from app import db
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
### Muath TODO: Implement a genre model ((Done))
class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'<Genre {self.id}: {self.name}>'

### Muath TODO: Implement an association table venue_themes ((Done))
venue_themes = db.Table('venue_themes',
db.Column('venue_id', db.Integer, db.ForeignKey('venue.id'), primary_key=True),
db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True))

class Venue(db.Model):
### Muath TODO: changing table name to lower case i.e:venue (it's annoying to put the name in double qoutes when using psql to inspect the database!) ((Done))
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String)
    genres = db.relationship('Genre', secondary=venue_themes, backref=db.backref('venues', lazy=True))
    shows = db.relationship('Show', backref='venue', lazy=True)

    def __repr__(self):
        return f'<Venue {self.id}: {self.name}>'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate ((Done))

### Muath TODO: Implement an association table artist_themes ((Done))
artist_themes = db.Table('artist_themes',
db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True),
db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True))

class Artist(db.Model):
    ### Muath TODO: changing table names to lower case i.e:artist (it's annoying to put the name in double qoutes when using psql to inspect the database!) ((Done))
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    ### Muath TODO: removing the genres column and have it in seprate table ((Done))
    ### genres = db.Column(db.String(120)) ###
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String)
    genres = db.relationship('Genre', secondary=artist_themes, backref=db.backref('artists', lazy=True))
    shows = db.relationship('Show', backref='artist', lazy=True)

    def __repr__(self):
        return f'<Artist {self.id}: {self.name}>'
    
    # TODO: implement any missing fields, as a database migration using Flask-Migrate ((Done))

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration. ((Done))

### Muath TODO: Implement a show model ((Done))
class Show(db.Model):
    __tablename__ = 'show'

    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    start_time = db.Column(db.DateTime(timezone=True))

    def __repr__(self):
        return f'<Show {self.id}: Artist {self.artist_id} at Venue {self.venue_id}>'
