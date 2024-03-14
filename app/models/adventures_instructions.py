from .db import db, environment, SCHEMA, add_prefix_for_prod

adventureActivitiesTable = db.Table(
    "adventuresActivities",
    db.Column("activityId", db.Integer, db.ForeignKey(add_prefix_for_prod('activities.id')), primary_key=True),
    db.Column("adventureId", db.Integer, db.ForeignKey(add_prefix_for_prod('adventures.id')), primary_key=True),
)

if environment == "production":
    adventureActivitiesTable.schema = SCHEMA
