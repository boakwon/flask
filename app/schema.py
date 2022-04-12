from app import ma, db
from app.models import Post, User, Role


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_fk = True
        include_relationships =  True
        sql_session = db.session


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk =  True
        include_relationships =  True
        sql_session = db.session


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        include_fk = True
        include_relationships = True
        sql_session = db.session



role_schema = RoleSchema(many=True)
user_schema = UserSchema(many=True)
post_schema = PostSchema(many=True)




