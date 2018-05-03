from django.db import models
from mongoengine import *
import json

class ActionType(Document):
    action_name = StringField(unique=True)

    def __unicode__(self):
        return json.dumps({
            'id': str(self.id),
            'action_name': str(self.action_name),
        })

class Action(Document):
    url = StringField()
    action = ReferenceField('ActionType')
    time = DateTimeField()
    title = StringField()
    ip = StringField()
    agent = StringField()
    referer = StringField()

    meta = {'allow_inheritance': True}

class DealAction(Action):
    deal_id = StringField()


class BrandAction(Action):
    brand_id = StringField()


class CouponAction(Action):
    coupon_id = StringField()

