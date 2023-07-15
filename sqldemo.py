import sqlalchemy as sa

class User:

    id = sa.Column(sa.Integer)
    usernam = sa.Column(sa.String)
    password = sa.Column(sa.String)
    email = sa.Column(sa.String)