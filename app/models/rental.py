from app import db
from app.models.video import Video

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
    due_date = db.Column(db.DateTime)
    is_checked_in = db.Column(db.Boolean, default=False)

    def to_dict(self):
        video = Video.query.get(self.video_id)
        checked_out = Rental.query.filter_by(video_id = self.video_id, is_checked_in=False).all()
        return {
            "video_id": self.video_id,
            "customer_id": self.customer_id,
            "videos_checked_out_count": len(checked_out),
            "available_inventory": video.total_inventory - len(checked_out)
        }